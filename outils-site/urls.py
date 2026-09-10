# -*- coding: utf-8 -*-
"""URL sans extension : réécrit les liens internes (relatifs et absolus) dans tout le site.
Vercel sert contact.html à l'adresse /contact (option cleanUrls) et redirige l'ancienne adresse.
À lancer en dernier dans la chaîne de publication."""
import os, re, glob
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, "..", "site-internet")
SITE = "https://www.sa-la-garonne.fr/"
def clean_html(s):
    # liens relatifs : contact.html → contact ; index.html → ./ ; en/index.html → en/ ; ../blog/index.html → ../blog/
    s = re.sub(r'href="(?!https?:|//|mailto:|tel:)([^"#?]*?)\.html(?=[#?"])', r'href="\1', s)
    s = re.sub(r'href="((?:\.\./)*(?:[a-z0-9-]+/)*)index(?=[#?"])', lambda m: 'href="' + (m.group(1) or "./"), s)
    return s
def clean_abs(s):
    s = re.sub(r'(https://www\.sa-la-garonne\.fr/[^\s"\'<>)]*?)\.html(?=[\s"\'<>)#?]|$)', r'\1', s)
    s = re.sub(r'(https://www\.sa-la-garonne\.fr/(?:[a-z0-9-]+/)*)index(?=[\s"\'<>)#?]|$)', r'\1', s)
    return s
n = 0
for f in glob.glob(os.path.join(ROOT, "**", "*"), recursive=True):
    if not os.path.isfile(f) or "/assets/" in f: continue
    ext = os.path.splitext(f)[1]
    if ext not in (".html", ".xml", ".txt", ".md", ".webmanifest"): continue
    s = open(f, encoding="utf-8").read()
    t = clean_abs(clean_html(s) if ext == ".html" else s)
    if t != s: open(f, "w", encoding="utf-8").write(t); n += 1
print(f"urls : {n} fichiers réécrits sans .html")
