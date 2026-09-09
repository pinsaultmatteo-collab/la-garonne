# -*- coding: utf-8 -*-
"""Générateur hebdomadaire d'article de blog — SA LA GARONNE.

Chaque mardi matin (GitHub Actions), ce script :
  1. prend le prochain sujet dans contenu-blog/sujets.json (ou demande à Claude d'en proposer si la liste est vide) ;
  2. rédige l'article avec Claude (claude-opus-5), en suivant contenu-blog/BRIEF.md ;
  3. vérifie le résultat (frontmatter, longueur, structure, slug unique) ;
  4. écrit contenu-blog/AAAA-MM-JJ-<slug>.md.
La chaîne de publication (outils-site/publier.sh) régénère ensuite le site.

Usage :
  python3 outils-site/generer_article.py            # sujet suivant de la liste
  python3 outils-site/generer_article.py --sujet "…" # sujet imposé
  python3 outils-site/generer_article.py --dry-run   # prépare le prompt sans appeler l'API
  python3 outils-site/generer_article.py --stub      # article factice sans API (test de la chaîne)
Variables : ANTHROPIC_API_KEY (obligatoire hors --dry-run / --stub).
"""
import os, re, sys, json, glob, datetime, argparse, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
BLOG = os.path.join(HERE, "..", "contenu-blog")
MODEL = "claude-opus-5"
CATEGORIES = ["Assainissement", "Eau potable", "Réhabilitation sans tranchée", "Travaux complexes", "Entreprise"]

def slugify(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:80].rstrip("-")

def existing():
    out = []
    for f in sorted(glob.glob(os.path.join(BLOG, "[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]-*.md"))):
        raw = open(f, encoding="utf-8").read()
        m = re.search(r"^title:\s*(.+)$", raw, re.M); s = re.search(r"^slug:\s*(.+)$", raw, re.M)
        if m and s: out.append({"title": m.group(1).strip(), "slug": s.group(1).strip()})
    return out

def covers():
    root = os.path.join(HERE, "..", "site-internet", "assets", "img")
    names = ["chantier-capitole-engins", "chantier-tranchee-centre-ville", "chantier-hydrocurage-equipe", "equipe-reunion-inspection",
             "ric-robot-inspection", "aep-raccordement-fonte", "camion-rehabilitation-sans-tranchee", "parc-engins"]
    names += ["realisations/" + os.path.basename(f)[:-9] for f in sorted(glob.glob(os.path.join(root, "realisations", "*-01-1200.jpg")))]
    return names

def build_prompt(sujet, brief, done, covs):
    today = datetime.date.today().isoformat()
    titres = "\n".join(f"- {a['title']} (blog/{a['slug']}.html)" for a in done) or "- (aucun)"
    system = f"""Vous êtes le rédacteur du blog de SA LA GARONNE, entreprise de travaux publics spécialisée dans les réseaux d'eau et d'assainissement à Toulouse. Vous écrivez en français, pour le web, avec un souci de référencement naturel : un sujet par article, un mot-clé principal placé dans le titre, la description, l'introduction et au moins un intertitre, des intertitres informatifs, des paragraphes courts, des listes quand elles aident, des réponses précises aux questions que se posent les lecteurs. Vous respectez strictement le brief ci-dessous.

{brief}
"""
    user = f"""Rédigez l'article de blog de cette semaine.

Sujet : {sujet['sujet']}
Mot-clé principal : {sujet['mot_cle']}
Catégorie : {sujet['categorie']}
Photo de couverture (valeur du champ cover) : {sujet['cover']}
Date de publication (champ date) : {today}

Articles déjà publiés (ne pas les réécrire ; vous pouvez y faire un lien quand c'est pertinent) :
{titres}

Couvertures possibles si celle proposée ne convient pas : {", ".join(covs)}

Répondez uniquement par le contenu du fichier Markdown, en commençant par la ligne `---` du frontmatter et sans aucun commentaire avant ou après. Le slug doit être en minuscules, sans accent, mots séparés par des tirets, dérivé du titre."""
    return system, user

def validate(text, done):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text.strip(), re.S)
    if not m: return None, "frontmatter introuvable"
    meta = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1); meta[k.strip()] = v.strip().strip('"').strip("'")
    body = m.group(2).strip()
    for k in ("title", "slug", "date", "description", "category", "tags", "keywords", "cover"):
        if not meta.get(k): return None, f"champ « {k} » manquant"
    if meta["category"] not in CATEGORIES: return None, f"catégorie invalide : {meta['category']}"
    if not (40 <= len(meta["title"]) <= 80): return None, f"titre de {len(meta['title'])} caractères (attendu 50-70)"
    if not (100 <= len(meta["description"]) <= 175): return None, f"description de {len(meta['description'])} caractères (attendu 120-160)"
    try: datetime.date.fromisoformat(meta["date"])
    except ValueError: return None, "date invalide"
    meta["slug"] = slugify(meta["slug"]) or slugify(meta["title"])
    if meta["slug"] in {a["slug"] for a in done}: meta["slug"] += "-" + meta["date"].replace("-", "")
    words = len(re.findall(r"\w+", body))
    if words < 750: return None, f"article trop court ({words} mots)"
    if len(re.findall(r"^## ", body, re.M)) < 4: return None, "moins de 4 sections ##"
    if not re.search(r"^## (Questions fréquentes|FAQ)", body, re.M): return None, "section « Questions fréquentes » absente"
    if re.search(r"^```", body, re.M): return None, "bloc de code inattendu"
    front = "\n".join(f"{k}: {meta[k]}" for k in ("title", "slug", "date", "description", "category", "tags", "keywords", "cover"))
    return (meta, f"---\n{front}\n---\n\n{body}\n"), None

def ask_claude(system, user):
    import anthropic
    client = anthropic.Anthropic()
    common = dict(model=MODEL, max_tokens=16000, thinking={"type": "adaptive"}, output_config={"effort": "high"},
                  system=[{"type": "text", "text": system, "cache_control": {"type": "ephemeral"}}],
                  messages=[{"role": "user", "content": user}])
    try:
        # repli serveur automatique en cas de refus (recommandé sur claude-opus-5)
        with client.beta.messages.stream(betas=["server-side-fallback-2026-07-01"], fallbacks="default", **common) as stream:
            msg = stream.get_final_message()
    except TypeError:
        with client.messages.stream(**common) as stream:
            msg = stream.get_final_message()
    if msg.stop_reason == "refusal":
        raise SystemExit(f"réponse refusée par le modèle ({getattr(msg.stop_details, 'category', '?')})")
    if msg.stop_reason == "max_tokens":
        raise SystemExit("réponse tronquée (max_tokens)")
    text = "".join(b.text for b in msg.content if b.type == "text")
    print(f"  tokens : {msg.usage.input_tokens} entrée, {msg.usage.output_tokens} sortie", file=sys.stderr)
    return text

def propose_topics(brief, done):
    import anthropic
    client = anthropic.Anthropic()
    titres = "\n".join(f"- {a['title']}" for a in done)
    with client.messages.stream(model=MODEL, max_tokens=4000, thinking={"type": "adaptive"}, output_config={"effort": "medium"},
        system="Vous êtes le responsable éditorial du blog de SA LA GARONNE. Répondez uniquement en JSON.",
        messages=[{"role": "user", "content": f"{brief}\n\nArticles déjà publiés :\n{titres}\n\nProposez 8 nouveaux sujets d'articles, utiles pour le référencement et non traités. Répondez par un tableau JSON d'objets avec les clés sujet, mot_cle, categorie (parmi {CATEGORIES}) et cover (parmi {covers()})."}]) as stream:
        msg = stream.get_final_message()
    text = "".join(b.text for b in msg.content if b.type == "text")
    data = json.loads(re.search(r"\[.*\]", text, re.S).group(0))
    return [d for d in data if d.get("sujet") and d.get("categorie") in CATEGORIES]

def stub_text(sujet):
    today = datetime.date.today().isoformat()
    paras = " ".join(["Ce paragraphe de test vérifie que la chaîne de publication fonctionne de bout en bout, sans appel à l'API."] * 6)
    sections = "\n\n".join(f"## Section de test {i}\n\n{paras}" for i in range(1, 5))
    return f"""---
title: Article de test automatique : {sujet['sujet'][:40]}
slug: test-automatique-{today}
date: {today}
description: Article factice généré par l'option --stub pour vérifier la chaîne de publication du blog SA LA GARONNE, sans appel à l'API. À supprimer.
category: {sujet['categorie']}
tags: test, chaîne de publication
keywords: test
cover: {sujet['cover']}
---

Introduction de test. {paras}

{sections}

## Questions fréquentes

### Ceci est-il un vrai article ?

Non, c'est un article de test généré sans intelligence artificielle.

### Faut-il le supprimer ?

Oui, dès que la chaîne de publication est validée.

## En résumé

{paras} [Contactez-nous](contact.html).
"""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sujet", default="", help="sujet imposé (sinon : prochain de sujets.json)")
    ap.add_argument("--dry-run", action="store_true"); ap.add_argument("--stub", action="store_true")
    args = ap.parse_args()
    brief = open(os.path.join(BLOG, "BRIEF.md"), encoding="utf-8").read()
    sujets_path = os.path.join(BLOG, "sujets.json")
    sujets = json.load(open(sujets_path, encoding="utf-8"))
    done = existing(); covs = covers()

    if args.sujet.strip():
        sujet = {"sujet": args.sujet.strip(), "mot_cle": args.sujet.strip(), "categorie": "Assainissement", "cover": "chantier-hydrocurage-equipe"}
        from_list = False
    else:
        if not sujets["a_faire"]:
            if args.dry_run or args.stub: raise SystemExit("liste de sujets vide")
            print("liste de sujets vide : demande de nouvelles propositions", file=sys.stderr)
            sujets["a_faire"] = propose_topics(brief, done)
            if not sujets["a_faire"]: raise SystemExit("aucun sujet proposé")
        sujet = sujets["a_faire"][0]; from_list = True
    if sujet.get("cover") not in covs: sujet["cover"] = "chantier-hydrocurage-equipe"
    print(f"sujet : {sujet['sujet']}", file=sys.stderr)

    system, user = build_prompt(sujet, brief, done, covs)
    if args.dry_run:
        print(system); print("\n=====\n"); print(user); return
    text = stub_text(sujet) if args.stub else ask_claude(system, user)
    result, err = validate(text, done)
    if err and not args.stub:
        print(f"première version rejetée ({err}) : nouvelle tentative", file=sys.stderr)
        text = ask_claude(system, user + f"\n\nVotre précédente version a été rejetée pour la raison suivante : {err}. Corrigez ce point en respectant toutes les consignes.")
        result, err = validate(text, done)
    if err: raise SystemExit(f"article rejeté : {err}")
    meta, content = result
    path = os.path.join(BLOG, f"{meta['date']}-{meta['slug']}.md")
    open(path, "w", encoding="utf-8").write(content)
    if from_list:
        sujets["faits"].append({**sujet, "date": meta["date"], "slug": meta["slug"]}); sujets["a_faire"].pop(0)
        json.dump(sujets, open(sujets_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"article écrit : {os.path.relpath(path, os.path.join(HERE, '..'))}")
    print(f"titre : {meta['title']}")
    open(os.path.join(HERE, "..", ".dernier-article.txt"), "w", encoding="utf-8").write(meta["title"])

if __name__ == "__main__":
    main()
