# Site vitrine SA LA GARONNE — notes de livraison

Site statique (HTML / CSS / JavaScript vanilla, aucune dépendance ni framework), conçu par PMC Marketing
sur la base de la charte graphique V2.0 (09.2026).

## Arborescence

| Fichier | Rôle |
|---|---|
| `index.html` | Accueil : hero, chiffres clés, 4 expertises, coupe animée « sans tranchée » pilotée au scroll, chantiers contraints, réalisations en défilement horizontal, engagements, entreprise, donneurs d'ordre, CTA |
| `assainissement.html` · `eau-potable.html` · `rehabilitation-sans-tranchee.html` · `travaux-complexes.html` | Les 4 pages expertises (approche, prestations, bande photo, méthode, contraintes, expertises liées) |
| `entreprise.html` | Histoire (frise animée), valeurs, équipe & moyens, recrutement, fiche d'identité |
| `realisations.html` | Galerie filtrable des chantiers |
| `contact.html` | Coordonnées, formulaire, plan d'accès |
| `mentions-legales.html` | Mentions légales (hébergeur à compléter) |
| `css/main.css` | Feuille de style unique (tokens de la charte en tête de fichier) |
| `js/main.js` | Animations et interactions (préchargeur, révélations au scroll, sections épinglées, curseur, menu, formulaire) |
| `assets/img/` | Photos optimisées en WebP + JPEG, 3 tailles (768 / 1280 / 1920) |
| `assets/logo/` | Logos et monogrammes issus de la charte |
| `404.html` | Page d'erreur personnalisée (servie automatiquement par Vercel) |
| `sitemap.xml` · `robots.txt` · `site.webmanifest` · favicons | SEO et icônes |

## Mise en ligne

1. Déposer tout le contenu de `site-internet/` à la racine de l'hébergement (aucune compilation nécessaire).
2. Remplacer le domaine `https://www.sa-la-garonne.fr/` (balises `canonical`, `og:*`, JSON-LD, `sitemap.xml`, `robots.txt`) par le domaine définitif si différent.
3. Compléter l'hébergeur dans `mentions-legales.html`.
4. Les polices (Archivo Narrow, Inter, JetBrains Mono) sont auto-hébergées dans `assets/fonts/` et déclarées dans `css/fonts.css` : aucun appel à Google Fonts (RGPD, performance).

## Formulaire de contact

Sans configuration, l'envoi ouvre la messagerie du visiteur avec un message pré-rempli (`mailto:`).
Pour un envoi serveur (recommandé), ajouter avant `<script src="js/main.js">` dans `contact.html` :

```html
<script>window.SLG_CONFIG = { formEndpoint: "https://formspree.io/f/XXXXXXXX", email: "contact@lagaronnetp.org" };</script>
```

Le formulaire envoie alors un JSON (nom, organisation, email, telephone, objet, message, consentement) vers l'endpoint
(Formspree, Basin, Netlify Forms via fonction, ou un script PHP maison). Un champ anti-spam invisible `_gotcha` est inclus.

## Modifier l'en-tête ou le pied de page sur toutes les pages

L'en-tête, le menu mobile et le pied de page sont dupliqués dans chaque page. Le dossier `../outils-site/`
contient un assembleur : modifier `index.html` (source de vérité de l'en-tête / pied de page) et/ou `pages.py`
(contenus des pages internes), puis lancer `python3 ../outils-site/build.py` pour régénérer les 8 pages internes.

## Changer la police de titrage

La charte V2.0 utilise Archivo Narrow 700 pour les titres. Pour revenir à Inter Display (charte V1.0), modifier
uniquement la variable `--font-display` en tête de `css/main.css` et adapter le `<link>` Google Fonts.

## Sources d'information

- Fiche contexte (PDF) et charte graphique V2.0 (`Design.pdf`).
- « Introduction au DA - 2026.docx » (dossier de candidature transmis par le client) : trois générations Pascual (1956 Eloy, 1987 Michel, 2017 Nicolas), 35 salariés en 4 équipes + atelier + bureau d'études (géomètre-dessinateur et chargé d'études), répartition d'activité (assainissement 75 %, eau potable 15 %, sans tranchée 10 %) — le montant de CA cité dans le document n'est pas repris sur le site à la demande de Mattéo, identifications FNTP 5118 / 5141 / 5161 / 5221, labels Canalisateur, RSE TP, Engagé RSE AFNOR (2023), Qualibat, NF, Amiante SS3, robot RIC breveté en 2018 (4K, 360°, + de 120 km inspectés), démarche RSE et objectifs 2026. Les photos et logos de ce document sont intégrés dans `assets/img/` et `assets/labels/`.

## Éléments à valider avec le client

- Coordonnées : téléphone +33 5 62 13 07 80, email contact@lagaronnetp.org (issus de la charte et de l'annuaire Guide de l'eau), domaine `sa-la-garonne.fr`.
- Chiffres : 35 collaborateurs, 3 générations et répartition par activité (dossier de candidature), tranchées jusqu'à 6–7 m et conduites jusqu'à Ø 2000 mm (annuaire Guide de l'eau).
- Photos issues du dossier de candidature (RIC, collecteur visitable, tranchée blindée devant le monument aux morts, raccordement AEP, pelle) : définition moyenne (530 à 1024 px), à remplacer par les originaux si le client les possède.
- Légendes des photos de chantier (rédigées d'après ce que montrent les images, à ajuster avec les vrais noms de chantiers si le client le souhaite).
- Liste des prestations, matériaux (fonte ductile, PEHD…) et moyens matériels sur les pages expertises et entreprise.
- Frise historique (accueil et page entreprise) : dates issues du dossier de candidature (1956, 1987, 2017, 2018, 2022/2023, 2026).
- Directeur de la publication : Nicolas Pascual.
