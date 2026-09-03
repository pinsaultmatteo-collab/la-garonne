# SA LA GARONNE — site vitrine

Site statique (HTML / CSS / JavaScript vanilla) conçu par PMC Marketing pour SA LA GARONNE, entreprise de travaux publics spécialisée dans les réseaux d'eau et d'assainissement à Toulouse depuis 1956.

- `site-internet/` : le site prêt à héberger (dossier à publier tel quel, `index.html` à la racine). Notes de livraison détaillées dans [site-internet/README.md](site-internet/README.md).
- `outils-site/` : assembleur des pages internes (`python3 outils-site/build.py`) à relancer après modification de l'en-tête, du pied de page ou de `pages.py`.

Hébergement : définir `site-internet` comme dossier de publication (Netlify, Vercel, Cloudflare Pages), ou copier son contenu à la racine du serveur.

## Déploiement Vercel

Le site se trouve dans `site-internet/`, pas à la racine. Le fichier `vercel.json` indique ce dossier
à Vercel (`outputDirectory`), aucune commande de build n'est nécessaire. Même principe sur Netlify ou
Cloudflare Pages : définir `site-internet` comme dossier de publication.

## Langues

Le site est trilingue : français (racine), anglais (`/en/`), chinois simplifié (`/zh/`).
Le français est la seule source à modifier ; `python3 outils-site/build.py` puis
`python3 outils-site/translate.py` régénèrent les deux autres langues à partir du dictionnaire
`outils-site/i18n.py`.
