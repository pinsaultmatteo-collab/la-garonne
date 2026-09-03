# -*- coding: utf-8 -*-
"""Génère les versions anglaise (site-internet/en/) et chinoise (site-internet/zh/)
à partir des pages françaises, via le dictionnaire outils-site/i18n.py.

Usage : python3 outils-site/translate.py
Signale en fin d'exécution toute chaîne française non traduite.
"""
import os, re, json, shutil, importlib.util, sys, html as htmlmod

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..", "site-internet")
SITE = "https://www.sa-la-garonne.fr/"

spec = importlib.util.spec_from_file_location("i18n", os.path.join(HERE, "i18n.py"))
i18n = importlib.util.module_from_spec(spec); spec.loader.exec_module(i18n)
T, SPECIAL, LANGS = i18n.T, i18n.SPECIAL, i18n.LANGS

PAGES = ["index.html", "assainissement.html", "eau-potable.html", "rehabilitation-sans-tranchee.html",
         "travaux-complexes.html", "entreprise.html", "realisations.html", "contact.html",
         "mentions-legales.html", "404.html"]
ATTRS = ("alt", "placeholder", "aria-label", "title", "data-cursor")
missing = {}

def tr(text, lang, page):
    """Traduit une chaîne ; mémorise les manques."""
    key = re.sub(r"\s+", " ", text).strip()
    if not key or not re.search(r"[A-Za-zÀ-ÿ]", key):
        return text
    if key in T:
        val = T[key][0 if lang == "en" else 1]
        return text.replace(key, val) if text.strip() == key else val
    # pas de lettre accentuée ni de mot français courant → sans doute un sigle ou un nom propre
    missing.setdefault(key, set()).add(f"{page}")
    return text

def translate_jsonld(obj, lang, page):
    if isinstance(obj, dict):
        return {k: (tr(v, lang, page) if k in ("name", "description", "slogan", "serviceType", "alternateName") and isinstance(v, str) else translate_jsonld(v, lang, page)) for k, v in obj.items()}
    if isinstance(obj, list):
        return [translate_jsonld(v, lang, page) for v in obj]
    return obj

def build(page, lang):
    src = open(os.path.join(ROOT, page), encoding="utf-8").read()
    L = LANGS[lang]
    out = src

    # 1. mise à l'écart de ce qui ne doit pas passer par la traduction automatique :
    #    scripts, styles, sélecteur de langue, puis fragments HTML déjà traduits à la main.
    blocks = []
    def stash(m):
        blocks.append(m.group(0)); return f"\x00{len(blocks)-1}\x00"
    out = re.sub(r"<script\b[^>]*>.*?</script>|<style\b[^>]*>.*?</style>|<div class=\"langs[^\"]*\"[^>]*>.*?</div>", stash, out, flags=re.S)
    for frag, tradu in SPECIAL.items():
        if frag in out:
            blocks.append(tradu[lang])
            out = out.replace(frag, f"\x00{len(blocks)-1}\x00")

    # 2. nœuds de texte
    def text_node(m):
        return ">" + tr(m.group(1), lang, page) + "<"
    out = re.sub(r">([^<>\x00]+)<", text_node, out)

    # 3. attributs traduisibles
    for attr in ATTRS:
        out = re.sub(rf'{attr}="([^"]+)"', lambda m, a=attr: f'{a}="{htmlmod.escape(tr(htmlmod.unescape(m.group(1)), lang, page), quote=True)}"', out)
    out = re.sub(r'<option value="([^"]+)"', lambda m: f'<option value="{htmlmod.escape(tr(m.group(1), lang, page), quote=True)}"', out)
    for name in ("description",):
        out = re.sub(rf'(<meta name="{name}" content=")([^"]+)(")', lambda m: m.group(1) + htmlmod.escape(tr(htmlmod.unescape(m.group(2)), lang, page), quote=True) + m.group(3), out)
    for prop in ("og:title", "og:description"):
        out = re.sub(rf'(<meta property="{prop}" content=")([^"]+)(")', lambda m: m.group(1) + htmlmod.escape(tr(htmlmod.unescape(m.group(2)), lang, page), quote=True) + m.group(3), out)

    # 4. en-tête du document
    out = out.replace('<html lang="fr">', f'<html lang="{L["html"]}">')
    out = out.replace('<meta property="og:locale" content="fr_FR">', f'<meta property="og:locale" content="{L["locale"]}">')
    out = re.sub(r'(<link rel="canonical" href=")([^"]+)(">)', lambda m: m.group(1) + SITE + L["dir"] + page + m.group(3), out)
    out = re.sub(r'(<meta property="og:url" content=")([^"]+)(">)', lambda m: m.group(1) + SITE + L["dir"] + page + m.group(3), out)

    # 5. balises hreflang (identiques dans les trois langues, x-default = français)
    alt = (f'  <link rel="alternate" hreflang="fr" href="{SITE}{page}">\n'
           f'  <link rel="alternate" hreflang="en" href="{SITE}en/{page}">\n'
           f'  <link rel="alternate" hreflang="zh-Hans" href="{SITE}zh/{page}">\n'
           f'  <link rel="alternate" hreflang="x-default" href="{SITE}{page}">\n')
    out = re.sub(r'(  <link rel="alternate" hreflang="[^"]+" href="[^"]+">\n)+', alt, out)
    if 'hreflang="x-default"' not in out:
        out = re.sub(r'(<link rel="canonical"[^>]*>\n)', r"\1" + alt, out)

    # 6. restitution des blocs protégés, avec traduction du JSON-LD
    def unstash(m):
        blk = blocks[int(m.group(1))]
        if 'application/ld+json' in blk:
            body = re.search(r'>(.*)</script>', blk, re.S).group(1)
            try:
                data = translate_jsonld(json.loads(body), lang, page)
                for k in ("url", "@id"):
                    if isinstance(data, dict) and k in data and isinstance(data[k], str) and data[k].startswith(SITE):
                        data[k] = data[k].replace(SITE, SITE + L["dir"], 1)
                if isinstance(data, dict) and data.get("@type") == "BreadcrumbList":
                    for it in data.get("itemListElement", []):
                        if "item" in it and it["item"].startswith(SITE):
                            it["item"] = it["item"].replace(SITE, SITE + L["dir"], 1)
                blk = re.sub(r'>(.*)</script>', lambda _: ">" + json.dumps(data, ensure_ascii=False) + "</script>", blk, flags=re.S)
            except Exception as e:
                print("  JSON-LD non traduit :", e)
        blk = re.sub(r'(href|src)="(css/|js/|assets/)', r'\1="../\2', blk)
        return blk
    out = re.sub(r"\x00(\d+)\x00", unstash, out)

    # 7. liens du sélecteur de langue (depuis un sous-dossier)
    def fix_langs(m):
        blk = m.group(0)
        tgt = {"fr": f"../{page}", "en": (page if lang == "en" else f"../en/{page}"), "zh": (page if lang == "zh" else f"../zh/{page}")}
        blk = re.sub(r'href="(?:\.\./)*index\.html"|href="[^"]*\.html"(?=[^>]*hreflang="fr")', f'href="{tgt["fr"]}"', blk, count=1)
        blk = re.sub(r'href="(?:\.\./)*en/[^"]*"|href="[^"]*"(?=[^>]*hreflang="en")', f'href="{tgt["en"]}"', blk, count=1)
        blk = re.sub(r'href="(?:\.\./)*zh/[^"]*"|href="[^"]*"(?=[^>]*hreflang="zh-Hans")', f'href="{tgt["zh"]}"', blk, count=1)
        blk = blk.replace('aria-current="true"', '')
        blk = re.sub(r'class="lang is-active"', 'class="lang"', blk)
        blk = re.sub(rf'(<a class="lang)(" href="[^"]*" hreflang="{ {"fr":"fr","en":"en","zh":"zh-Hans"}[lang] }")', r'\1 is-active\2 aria-current="true"', blk)
        return blk
    out = re.sub(r'<div class="langs[^"]*"[^>]*>.*?</div>', fix_langs, out, flags=re.S)

    # 8. chemins des ressources (les pages vivent dans un sous-dossier)
    out = re.sub(r'(href|src)="(css/|js/|assets/|favicon|apple-touch-icon|site\.webmanifest|sitemap\.xml|robots\.txt)', r'\1="../\2', out)
    out = re.sub(r'srcset="([^"]+)"', lambda m: 'srcset="' + re.sub(r'(^|,\s*)assets/', r'\1../assets/', m.group(1)) + '"', out)

    return out

def main():
    for lang in ("en", "zh"):
        d = os.path.join(ROOT, lang)
        os.makedirs(d, exist_ok=True)
        for page in PAGES:
            open(os.path.join(d, page), "w", encoding="utf-8").write(build(page, lang))
        print(f"{lang} : {len(PAGES)} pages écrites")
    if missing:
        print(f"\n⚠ {len(missing)} chaînes non traduites :")
        for k, v in sorted(missing.items())[:40]:
            print(f"   [{','.join(sorted(v))}] {k[:110]}")
    else:
        print("\n✓ Toutes les chaînes sont traduites.")

if __name__ == "__main__":
    main()
