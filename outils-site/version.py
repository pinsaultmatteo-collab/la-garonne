# -*- coding: utf-8 -*-
"""Ajoute un numéro de version (empreinte du contenu) aux liens vers main.css et main.js
dans toutes les pages, pour que chaque déploiement invalide le cache des navigateurs."""
import os, re, glob, hashlib
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, "..", "site-internet")
def h(path): return hashlib.md5(open(path, "rb").read()).hexdigest()[:8]
css, js = h(os.path.join(ROOT, "css", "main.css")), h(os.path.join(ROOT, "js", "main.js"))
n = 0
for f in glob.glob(os.path.join(ROOT, "*.html")) + glob.glob(os.path.join(ROOT, "*", "*.html")):
    s = open(f, encoding="utf-8").read()
    t = re.sub(r'((?:\.\./)*css/main\.css)(\?v=[0-9a-f]+)?"', lambda m: f'{m.group(1)}?v={css}"', s)
    t = re.sub(r'((?:\.\./)*js/main\.js)(\?v=[0-9a-f]+)?"', lambda m: f'{m.group(1)}?v={js}"', t)
    if t != s: open(f, "w", encoding="utf-8").write(t); n += 1
print(f"version : css {css}, js {js}, {n} pages mises à jour")
