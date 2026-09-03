# -*- coding: utf-8 -*-
"""Injecte une miniature floutée (LQIP) dans les conteneurs d'images de toutes les pages.

La vignette pèse quelques centaines d'octets et voyage dans le HTML : le bloc affiche
immédiatement les couleurs de la photo au lieu d'une zone vide pendant le téléchargement.
À lancer en dernier, après build.py et translate.py :  python3 outils-site/lqip.py
"""
import os, re, io, base64, glob
from PIL import Image, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..", "site-internet")
CONTAINERS = ("mask", "work", "scan", "hq__img", "hero-page__bg", "hero__media", "band")
cache = {}

def lqip(path):
    """Renvoie une data-URI JPEG de 16 px de large, floutée."""
    if path in cache:
        return cache[path]
    if not os.path.exists(path):
        cache[path] = None; return None
    im = Image.open(path).convert("RGB")
    w = 16; h = max(1, round(im.height * w / im.width))
    im = im.resize((w, h), Image.LANCZOS).filter(ImageFilter.GaussianBlur(0.6))
    buf = io.BytesIO(); im.save(buf, "JPEG", quality=40, optimize=True)
    cache[path] = "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()
    return cache[path]

TAG = re.compile(r'<(?:div|article|a|span|picture)\b[^>]*class="[^"]*\b(?:' + "|".join(CONTAINERS) + r')\b[^"]*"[^>]*>')
SRC = re.compile(r'src="([^"]*assets/img/[^"]+\.(?:jpg|png))"')

def process(page):
    s = open(page, encoding="utf-8").read()
    base = os.path.dirname(page)
    out, pos, added = [], 0, 0
    for m in TAG.finditer(s):
        tag = m.group(0)
        if "--lqip" in tag:
            continue
        nxt = SRC.search(s, m.end(), m.end() + 1600)
        if not nxt:
            continue
        data = lqip(os.path.normpath(os.path.join(base, nxt.group(1))))
        if not data:
            continue
        if 'style="' in tag:
            new = tag.replace('style="', f'style="--lqip:url({data});', 1)
        else:
            new = tag[:-1] + f' style="--lqip:url({data})">'
        out.append(s[pos:m.start()]); out.append(new); pos = m.end(); added += 1
    out.append(s[pos:])
    open(page, "w", encoding="utf-8").write("".join(out))
    return added

if __name__ == "__main__":
    total = 0
    for page in sorted(glob.glob(os.path.join(ROOT, "*.html")) + glob.glob(os.path.join(ROOT, "*", "*.html"))):
        if os.path.basename(os.path.dirname(page)) not in ("site-internet", "en", "zh"):
            continue
        n = process(page); total += n
        print(f"  {os.path.relpath(page, ROOT)} : {n} vignettes")
    print(f"total : {total} vignettes injectées, {len([v for v in cache.values() if v])} images distinctes")
    if cache:
        big = max((len(v) for v in cache.values() if v), default=0)
        print(f"vignette la plus lourde : {big} caractères (~{big*3//4} octets)")
