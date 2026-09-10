#!/usr/bin/env bash
# Chaîne complète de génération du site SA LA GARONNE (à lancer depuis la racine du dépôt ou n'importe où).
set -euo pipefail
cd "$(dirname "$0")/.."
python3 outils-site/build.py      >/dev/null   # pages internes françaises
python3 outils-site/translate.py               # versions anglaise et chinoise
python3 outils-site/blog.py                    # articles, index, RSS, copies Markdown
python3 outils-site/lqip.py       >/dev/null   # vignettes floutées
python3 outils-site/sitemap.py                 # plan du site
python3 outils-site/llms.py                    # llms.txt, llms-full.txt, md/, robots.txt
python3 outils-site/version.py                 # empreinte anti-cache sur main.css et main.js
python3 outils-site/urls.py                    # liens internes sans .html (cleanUrls Vercel)
echo "site régénéré"
