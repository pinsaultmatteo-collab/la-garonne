# Site vitrine SA LA GARONNE — notes de livraison

Site statique (HTML / CSS / JavaScript vanilla, aucune dépendance ni framework), conçu par PMC Marketing
sur la base de la charte graphique V2.0 (09.2026).

## Langues

Le site existe en trois langues, chacune dans son propre dossier, avec des URL distinctes et indexables :

| Langue | URL | Dossier |
|---|---|---|
| Français (source) | `/` | racine de `site-internet/` |
| Anglais | `/en/` | `site-internet/en/` |
| Chinois simplifié | `/zh/` | `site-internet/zh/` |

Chaque page porte ses balises `hreflang` (fr, en, zh-Hans, x-default) et son `canonical`. Le `sitemap.xml`
liste les 27 URL avec leurs alternates. Le sélecteur à drapeaux de l'en-tête pointe vers la même page dans
l'autre langue. Le chinois utilise la pile de polices système (PingFang SC, Microsoft YaHei, Noto Sans CJK) :
une police chinoise auto-hébergée pèserait plusieurs centaines de kilo-octets par page.

**Le français est la seule source à modifier.** Pour répercuter un changement :

```bash
python3 outils-site/build.py      # régénère les 9 pages internes françaises depuis index.html
python3 outils-site/translate.py  # régénère en/ et zh/ depuis les pages françaises
python3 outils-site/lqip.py       # réinjecte les vignettes floutées dans les 30 pages
```

Les trois commandes s'enchaînent toujours dans cet ordre.

`outils-site/i18n.py` contient le dictionnaire de traduction (668 entrées, français → anglais → chinois).
Toute phrase française absente du dictionnaire est signalée en fin d'exécution de `translate.py` : le site
ne peut pas partir en ligne avec du texte non traduit sans que l'outil le dise.

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
| `en/` · `zh/` | Versions anglaise et chinoise, générées par `outils-site/translate.py` (ne pas éditer à la main) |
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
(contenus des pages internes), puis lancer `python3 ../outils-site/build.py`, et enfin
`python3 ../outils-site/translate.py` pour répercuter en anglais et en chinois.

## Changer la police de titrage

La charte V2.0 utilise Archivo Narrow 700 pour les titres. Pour revenir à Inter Display (charte V1.0), modifier
uniquement la variable `--font-display` en tête de `css/main.css` et adapter le `<link>` Google Fonts.

## Sources d'information

- Fiche contexte (PDF) et charte graphique V2.0 (`Design.pdf`).
- « Introduction au DA - 2026.docx » (dossier de candidature transmis par le client) : trois générations Pascual (1956 Eloy, 1987 Michel, 2017 Nicolas), 35 salariés en 4 équipes + atelier + bureau d'études (géomètre-dessinateur et chargé d'études), répartition d'activité (assainissement 75 %, eau potable 15 %, sans tranchée 10 %) — le montant de CA cité dans le document n'est pas repris sur le site à la demande de Mattéo, identifications FNTP 5118 / 5141 / 5161 / 5221, labels Canalisateur, RSE TP, Engagé RSE AFNOR (2023), Qualibat, NF, Amiante SS3, robot RIC breveté en 2018 (4K, 360°, + de 120 km inspectés), démarche RSE et objectifs 2026. Les photos et logos de ce document sont intégrés dans `assets/img/` et `assets/labels/`.

## Chargement des images

Trois mécanismes se combinent pour qu'aucun bloc n'apparaisse vide :

1. **Vignette floutée intégrée au HTML.** `outils-site/lqip.py` encode une miniature de 16 px
   (environ 400 octets) dans l'attribut `style` de chaque conteneur d'image. Le bloc affiche les
   couleurs de la photo dès le premier rendu, sans requête supplémentaire.
2. **Chargement anticipé.** `loading="lazy"` ne déclenche le téléchargement qu'à l'approche
   immédiate du bloc, ce qui est trop tard sur une page longue avec sections épinglées. Le script
   repasse les images en chargement immédiat dès qu'elles sont à 1400 px du viewport.
3. **Variantes dimensionnées.** Chaque photo existe en plusieurs largeurs, et l'attribut `sizes`
   déclare la largeur réelle d'affichage pour que le navigateur choisisse le bon fichier.

Le préchargement de l'image du hero utilise `imagesrcset` et `imagesizes` identiques à ceux de la
balise `img` : sans cela le navigateur télécharge deux variantes de la même photo.

## Éléments à valider avec le client

- Coordonnées : téléphone +33 5 62 13 07 80, email contact@lagaronnetp.org (issus de la charte et de l'annuaire Guide de l'eau), domaine `sa-la-garonne.fr`.
- Chiffres : 35 collaborateurs, 3 générations et répartition par activité (dossier de candidature), tranchées jusqu'à 6–7 m et conduites jusqu'à Ø 2000 mm (annuaire Guide de l'eau).
- Photos issues du dossier de candidature (RIC, collecteur visitable, tranchée blindée devant le monument aux morts, raccordement AEP, pelle) : définition moyenne (530 à 1024 px), à remplacer par les originaux si le client les possède.
- Légendes des photos de chantier (rédigées d'après ce que montrent les images, à ajuster avec les vrais noms de chantiers si le client le souhaite).
- Liste des prestations, matériaux (fonte ductile, PEHD…) et moyens matériels sur les pages expertises et entreprise.
- Traductions anglaise et chinoise : terminologie métier posée dans l'en-tête de `outils-site/i18n.py`. À faire relire par le client s'il a des interlocuteurs anglophones ou sinophones.
- Frise historique (accueil et page entreprise) : dates issues du dossier de candidature (1956, 1987, 2017, 2018, 2022/2023, 2026).
- Directeur de la publication : Nicolas Pascual.
