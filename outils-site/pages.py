# -*- coding: utf-8 -*-
# Contenus des pages internes — SA LA GARONNE
import os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "site-internet")
index = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()

def section_head(eyebrow, title, lead=None, light=False):
    l = f'<p class="lead" data-reveal>{lead}</p>' if lead else ""
    return f'<div class="section-head"><div><p class="eyebrow{" eyebrow--light" if light else ""}" data-reveal>{eyebrow}</p><h2 class="h2" data-split>{title}</h2></div>{l}</div>'

def intro(eyebrow, title, paras):
    ps = "".join(f"<p>{p}</p>" for p in paras)
    return f'<section class="section"><div class="container"><div class="intro"><div><p class="eyebrow" data-reveal>{eyebrow}</p><h2 class="h2" style="margin-top:20px" data-split>{title}</h2></div><div class="intro__text stagger">{ps}</div></div></div></section>'

def chips_specs(eyebrow, title, lead, chips, specs):
    ch = "".join(f'<span class="chip"><i></i>{c}</span>' for c in chips)
    sp = "".join(f'<div class="spec"><span>{k}</span><b>{v}</b></div>' for k, v in specs)
    return f'''<section class="section"><div class="container"><div class="grid grid-5-7"><div><p class="eyebrow" data-reveal>{eyebrow}</p><h2 class="h2" style="margin-top:20px" data-split>{title}</h2><p class="lead" style="margin-top:24px" data-reveal>{lead}</p><div class="chips stagger" style="margin-top:32px">{ch}</div></div><div data-reveal><p class="mono" style="color:var(--steel);margin-bottom:12px">Repères techniques</p>{sp}</div></div></div></section>'''

# ---------------------------------------------------------------- ASSAINISSEMENT
body = hero(
    ['<a href="assainissement.html">Expertises</a>', "Assainissement"],
    "Expertise 01 / Assainissement",
    "Assainis&shy;sement",
    "Construire, renouveler et réhabiliter les réseaux d'eaux usées et pluviales, leurs branchements et leurs ouvrages — en milieu urbain dense et sur des réseaux en service.",
    [("Part d'activité", "75 % de l'activité"), ("Réseaux", "Unitaires · EU · EP"), ("Diamètres", "jusqu'à Ø 2000 mm"), ("Profondeur", "jusqu'à 7 m"), ("Qualifications", "FNTP 5141 · 5161 · 5221")],
    bg="collecteur-visitable-profondeur", bgalt="Canalisateur SA LA GARONNE dans un collecteur visitable en grande profondeur"
)
body += intro("Notre approche", "Un réseau qui fonctionne en continu, et qui ne doit jamais s'arrêter.",
    ["Les réseaux d'assainissement collectent chaque jour les eaux usées et pluviales d'une agglomération entière. Ils sont enterrés, souvent anciens, et rarement visibles — jusqu'au jour où ils défaillent.",
     "Depuis 1956, SA LA GARONNE construit, renouvelle et réhabilite ces réseaux pour les collectivités et les exploitants de Toulouse et de son agglomération : collecteurs, branchements particuliers, regards et ouvrages annexes. Nous intervenons sur des réseaux en service, à grande profondeur et sur des canalisations de grand diamètre, avec une exigence constante : maintenir l'écoulement pendant les travaux.",
     "Notre connaissance du sous-sol toulousain et de ses réseaux, souvent depuis leur construction, est un atout décisif pour anticiper les contraintes et sécuriser chaque phase."])
body += f'''<section class="section section--tight bg-white"><div class="container">{section_head("Prestations", "Ce que nous réalisons.", "De la pose d'un collecteur neuf à la réhabilitation d'un ouvrage existant, nous couvrons l'ensemble des travaux d'assainissement.")}{services([
 ("assainissement", "Construction et renouvellement de collecteurs", "Réseaux unitaires, eaux usées et eaux pluviales : terrassement, blindage, pose et raccordement, tous diamètres jusqu'à Ø 2000 mm."),
 ("reseau", "Branchements particuliers", "Création et renouvellement de branchements d'assainissement en centre-ville, y compris en secteur piéton ou à forte fréquentation."),
 ("regard", "Regards et ouvrages annexes", "Regards de visite, chambres, déversoirs et ouvrages spéciaux : construction, mise à niveau et réhabilitation."),
 ("continuite", "Interventions sur réseaux en service", "Maintien de l'écoulement pendant les travaux : pompage, dérivation provisoire et phasage adapté à l'exploitation."),
 ("chemisage", "Réhabilitation d'ouvrages existants", "Réhabilitation de collecteurs et de regards, par tranchée ouverte ou par techniques sans tranchée selon le diagnostic."),
 ("controle", "Contrôles et remise en état", "Essais d'étanchéité, inspection télévisée, remblaiement contrôlé et réfection de voirie à l'identique."),
])}</div></section>'''
body += band("chantier-tranchee-centre-ville", "Tranchée d'assainissement en centre-ville de Toulouse", [768,1280,1920], "Toulouse · centre-ville", "Renouvellement de réseau en secteur piéton")
body += f'''<section class="section bg-navy"><div class="container">{section_head("Méthode", "Quatre étapes, aucune approximation.", "Chaque chantier d'assainissement suit une méthode éprouvée, du diagnostic à la remise en état de la voirie.", light=True)}{process([
 ("inspection", "Diagnostic et préparation", "Inspection de l'existant, repérage des réseaux, déclarations réglementaires (DT-DICT), phasage et plan de circulation."),
 ("securite", "Sécurisation de l'emprise", "Balisage, blindage de tranchée, gestion des flux piétons et véhicules, protection des riverains et des équipes."),
 ("chantier", "Travaux", "Terrassement, pose ou réhabilitation, raccordements et branchements — en maintenant l'écoulement du réseau."),
 ("controle", "Contrôles et réception", "Essais d'étanchéité, inspection télévisée, remblaiement contrôlé, réfection de voirie et dossier de récolement."),
])}</div></section>'''
body += chips_specs("Contraintes maîtrisées", "Le terrain, tel qu'il est.", "Nous intervenons là où les conditions sont les plus exigeantes : hypercentre historique, réseaux anciens, nappes, trafic, riverains.",
    ["Réseaux en service", "Tranchées profondes", "Grand diamètre", "Hypercentre historique", "Secteurs piétons", "Coordination multi-réseaux", "Présence de nappe", "Travaux de nuit possibles"],
    [("Diamètre maximal posé", "Ø 2000 mm"), ("Profondeur de tranchée", "6 à 7 m"), ("Types de réseaux", "Unitaire · EU · EP"), ("Identifications FNTP", "5141 · 5161 · 5221"), ("Inspection", "Robot RIC 4K 360° (brevet)"), ("Bureau d'études", "Intégré · géomètre & chargé d'études"), ("Zone d'intervention", "Toulouse Métropole & agglomération")])
body += related("assainissement.html") + CTA
page("assainissement.html", "Assainissement à Toulouse — construction, renouvellement et réhabilitation de réseaux | SA LA GARONNE",
     "Travaux d'assainissement à Toulouse : collecteurs, branchements, regards et ouvrages, réseaux en service, grande profondeur et grand diamètre. SA LA GARONNE, depuis 1956.", body, "chantier-hydrocurage-equipe-1280.jpg")

# ---------------------------------------------------------------- EAU POTABLE
body = hero(
    ['<a href="assainissement.html">Expertises</a>', "Adduction d'eau potable"],
    "Expertise 02 / Eau potable",
    "Adduction d'eau potable",
    "Poser, renouveler et raccorder les conduites qui acheminent l'eau potable — avec un objectif simple : un service continu et une eau préservée.",
    [("Part d'activité", "15 % de l'activité"), ("Réseaux", "Adduction · distribution"), ("Ouvrages", "Chambres · vannes · comptage"), ("Qualification", "FNTP 5118 · AEP zone urbaine"), ("Zone", "Toulouse & agglomération")],
    bg="aep-raccordement-fonte", bgalt="Raccordement de conduites d'eau potable en fonte dans une tranchée"
)
body += intro("Notre approche", "L'eau doit arriver. Chaque jour, à chaque robinet.",
    ["Un réseau d'eau potable se juge à sa fiabilité. Renouveler une conduite ancienne, créer un branchement ou raccorder un nouveau quartier doit se faire sans dégrader la qualité de l'eau ni interrompre durablement le service.",
     "SA LA GARONNE réalise la pose et le renouvellement de conduites d'adduction et de distribution, les branchements particuliers et les ouvrages hydrauliques associés. Nos équipes travaillent sur des réseaux exploités, en coordination étroite avec les exploitants, pour limiter les coupures et sécuriser chaque remise en eau.",
     "Désinfection, essais de pression, contrôles de qualité : la mise en service est une étape à part entière, que nous traitons avec la même rigueur que la pose."])
body += f'''<section class="section section--tight bg-white"><div class="container">{section_head("Prestations", "Ce que nous réalisons.", "De la conduite structurante au branchement individuel, nous intervenons sur l'ensemble du réseau d'eau potable.")}{services([
 ("eau", "Pose et renouvellement de conduites", "Conduites d'adduction et de distribution, tous matériaux courants (fonte ductile, PEHD…), en tranchée ouverte ou par techniques adaptées."),
 ("reseau", "Branchements particuliers", "Création, renouvellement et reprise de branchements d'eau potable, en centre-ville comme en zone périurbaine."),
 ("vanne", "Ouvrages hydrauliques", "Chambres de vannes, regards de comptage, dispositifs de sectorisation, ventouses et vidanges."),
 ("continuite", "Raccordements sur réseaux exploités", "Interventions planifiées avec l'exploitant pour réduire au strict nécessaire la durée et le périmètre des coupures."),
 ("controle", "Essais et désinfection", "Essais de pression, rinçage, désinfection et analyses avant remise en service."),
 ("chantier", "Réfection et remise en état", "Remblaiement contrôlé, réfection de voirie et de trottoirs à l'identique, dossier de récolement."),
])}</div></section>'''
body += band("chantier-capitole-engins", "Engins SA LA GARONNE en intervention en hypercentre de Toulouse", [768,1280,1920], "Toulouse · hypercentre", "Intervenir sans interrompre la ville")
body += f'''<section class="section bg-navy"><div class="container">{section_head("Méthode", "Une remise en eau préparée dès le premier jour.", "La qualité de l'eau et la continuité du service guident chaque phase du chantier.", light=True)}{process([
 ("phasage", "Préparation et coordination", "Repérage des réseaux, déclarations réglementaires, phasage des coupures avec l'exploitant, information des riverains."),
 ("securite", "Sécurisation", "Balisage, blindage, gestion des accès et des flux, protection des conduites voisines et des équipes."),
 ("eau", "Pose et raccordement", "Terrassement, lit de pose, assemblage des conduites, raccordement des branchements et des ouvrages."),
 ("controle", "Essais et mise en service", "Essais de pression, désinfection, analyses, remise en eau progressive et réfection de voirie."),
])}</div></section>'''
body += chips_specs("Contraintes maîtrisées", "Un réseau sous pression, une ville en activité.", "Nous concilions les exigences sanitaires de l'eau potable et celles d'un chantier urbain.",
    ["Réseaux exploités", "Coupures minimisées", "Coordination exploitant", "Centre-ville", "Multi-réseaux", "Qualité sanitaire", "Réfection à l'identique"],
    [("Conduites", "Adduction · distribution"), ("Matériaux", "Fonte ductile · PEHD · acier"), ("Ouvrages", "Chambres · vannes · comptage"), ("Identification FNTP", "5118 · réseaux AEP en zone urbaine"), ("Mise en service", "Essais · désinfection · analyses"), ("Bureau d'études", "Intégré · plans d'exécution & récolement"), ("Zone d'intervention", "Toulouse Métropole & agglomération")])
body += related("eau-potable.html") + CTA
page("eau-potable.html", "Adduction d'eau potable à Toulouse — pose, renouvellement et branchements | SA LA GARONNE",
     "Travaux d'adduction d'eau potable à Toulouse : pose et renouvellement de conduites, branchements, ouvrages hydrauliques, raccordements sur réseaux exploités. SA LA GARONNE, depuis 1956.", body, "chantier-tranchee-centre-ville-1280.jpg")

# ---------------------------------------------------------------- SANS TRANCHÉE
coupe = index[index.index("<!-- ============ COUPE SOUS LA VILLE"):index.index("<!-- ============ CHANTIERS COMPLEXES")]
coupe = coupe.replace("03 / Savoir-faire signature", "Le procédé, étape par étape").replace('<p style="margin-top:32px"><a class="link-arrow" href="rehabilitation-sans-tranchee.html" style="color:#0A94F2"><span>Découvrir la réhabilitation sans tranchée</span>', '<p style="margin-top:32px"><a class="link-arrow" href="contact.html" style="color:#0A94F2"><span>Étudier votre réseau avec nous</span>')
body = hero(
    ['<a href="assainissement.html">Expertises</a>', "Réhabilitation sans tranchée"],
    "Expertise 03 / Sans tranchée",
    "Réhabilitation sans tranchée",
    "Rénover les réseaux existants depuis l'intérieur : chemisage, gainage, fraisage et interventions robotisées. Moins d'ouverture de voirie, des délais réduits, des nuisances limitées.",
    [("Part d'activité", "10 % de l'activité"), ("Procédés", "Chemisage · gainage · fraisage"), ("Robotique", "RIC 4K 360° · brevet 2018"), ("Qualification", "FNTP 5221 · réseaux visitables"), ("Voirie", "Non ouverte")],
    bg="chantier-capitole-engins", bgalt="Unités mobiles SA LA GARONNE en intervention en hypercentre"
)
body += intro("Notre approche", "Une conduite neuve dans l'ancienne. Sans ouvrir la rue.",
    ["Renouveler un réseau enterré en tranchée ouverte signifie ouvrir la chaussée, dévier la circulation, immobiliser un quartier pendant des semaines. La réhabilitation sans tranchée apporte une alternative : rénover la conduite depuis l'intérieur, à partir des regards existants.",
     "SA LA GARONNE a fait de ces techniques un axe différenciant de son savoir-faire. Chemisage continu, gainage, fraisage robotisé, réparations ponctuelles : nos équipes et nos unités mobiles interviennent sur des réseaux en service, en centre-ville dense comme en zone périurbaine.",
     "Le résultat : une conduite structurellement neuve, une durée de vie prolongée de plusieurs décennies, un chantier plus court et une voirie préservée."])
body += coupe
body += f'''<section class="section section--tight bg-white"><div class="container">{section_head("Techniques", "Les procédés que nous mettons en œuvre.", "Chaque réseau est différent : le diagnostic détermine la technique la plus adaptée à l'état de la conduite et aux contraintes du site.")}{services([
 ("inspection", "Inspection télévisée et diagnostic", "Passage caméra — dont le RIC, robot de télé-visualisation 4K à 360° breveté par La Garonne — relevé des défauts, mesure des ovalisations et des contre-pentes."),
 ("pompage", "Hydrocurage et préparation", "Nettoyage haute pression de la conduite, élimination des dépôts, préparation de la surface avant chemisage."),
 ("chantier", "Fraisage robotisé", "Suppression des obstacles (racines, concrétions, branchements pénétrants) par robot fraiseur piloté depuis la surface."),
 ("chemisage", "Chemisage continu", "Gaine imprégnée de résine, mise en place et polymérisée en place : une conduite neuve, continue et étanche, dans l'existante."),
 ("regard", "Gainage partiel et manchettes", "Réparation localisée d'un tronçon ou d'un raccord par manchette ou chemisage court, sans intervention sur l'ensemble du linéaire."),
 ("reseau", "Réouverture des branchements", "Réouverture robotisée des branchements après chemisage, reprise des raccords et contrôle d'étanchéité."),
])}</div></section>'''
body += f'''<section class="section bg-navy"><div class="container"><div class="grid grid-5-7"><div><p class="eyebrow eyebrow--light" data-reveal>Bénéfices</p><h2 class="h2" style="margin-top:20px" data-split>Ce que la ville y gagne.</h2></div><ul class="checks stagger" style="margin-top:0"><li>{picto("ville")}<div><strong>Voirie préservée</strong><span>Pas de tranchée sur le linéaire : la chaussée, les trottoirs et les réseaux voisins restent intacts.</span></div></li><li>{picto("continuite")}<div><strong>Délais réduits</strong><span>Des interventions à l'échelle de la journée ou de la semaine, là où une tranchée ouverte se compte en mois.</span></div></li><li>{picto("securite")}<div><strong>Nuisances limitées</strong><span>Moins de bruit, de poussière et de déviations pour les riverains, les commerces et la circulation.</span></div></li><li>{picto("durabilite")}<div><strong>Durabilité</strong><span>Une conduite structurellement renforcée, étanche, pour plusieurs décennies de service supplémentaires.</span></div></li><li>{picto("controle")}<div><strong>Coût global maîtrisé</strong><span>Moins de terrassement, de remblais et de réfection : un budget optimisé pour la collectivité.</span></div></li></ul></div></div></section>'''
body += chips_specs("Champ d'intervention", "Des réseaux de toutes tailles, dans tous les contextes.", "Collecteurs, branchements, ouvrages : nous adaptons la technique au diamètre, au matériau et à l'état de la conduite.",
    ["Réseaux en service", "Centre-ville dense", "Collecteurs visitables", "Conduites non visitables", "Branchements", "Regards et ouvrages", "Interventions robotisées"],
    [("Diagnostic", "Inspection télévisée · robot RIC 4K 360°"), ("Réseaux inspectés", "+ de 120 km à Toulouse"), ("Procédés", "Chemisage · gainage · manchettes"), ("Préparation", "Hydrocurage · fraisage robotisé"), ("Identification FNTP", "5221 · réhabilitation de réseaux visitables"), ("Voirie", "Non ouverte sur le linéaire"), ("Zone d'intervention", "Toulouse Métropole & agglomération")])
body += related("rehabilitation-sans-tranchee.html") + CTA
page("rehabilitation-sans-tranchee.html", "Réhabilitation sans tranchée à Toulouse — chemisage, gainage, fraisage robotisé | SA LA GARONNE",
     "Réhabilitation de canalisations sans tranchée à Toulouse : inspection, hydrocurage, fraisage robotisé, chemisage et gainage. Rénover les réseaux sans ouvrir la voirie. SA LA GARONNE, depuis 1956.", body, "chantier-capitole-engins-1280.jpg")

# ---------------------------------------------------------------- TRAVAUX COMPLEXES
body = hero(
    ['<a href="assainissement.html">Expertises</a>', "Travaux complexes"],
    "Expertise 04 / Travaux & interventions complexes",
    "Travaux complexes",
    "Réseaux en service, tranchées à grande profondeur, canalisations de grand diamètre, secteurs très fréquentés : des chantiers où la méthode fait la différence.",
    [("Profondeur", "jusqu'à 7 m"), ("Diamètre", "jusqu'à Ø 2000 mm"), ("Qualifications", "FNTP 5141 · 5161"), ("Contexte", "Hypercentre · secteurs sensibles")],
    bg="tranchee-blindee-monument", bgalt="Tranchée blindée SA LA GARONNE devant le monument aux morts de Toulouse"
)
body += intro("Notre approche", "Plus le chantier est contraint, plus la préparation compte.",
    ["Un collecteur à sept mètres de profondeur sous une rue commerçante. Une canalisation de deux mètres de diamètre à renouveler sans interrompre le réseau. Une intervention au pied d'un monument, sous les yeux des riverains et des touristes. Ce sont les chantiers pour lesquels SA LA GARONNE est sollicitée.",
     "Notre valeur ajoutée tient dans la préparation : études d'exécution, phasage précis, blindages adaptés, logistique urbaine, coordination avec les exploitants et les services de la ville. Sur le terrain, des équipes expérimentées et un matériel dimensionné pour ces conditions.",
     "Sécurité des équipes, continuité de service, respect des délais : sur un chantier complexe, ces trois exigences ne se négocient jamais."])
body += f'''<section class="section section--tight bg-white"><div class="container">{section_head("Situations", "Ce que nous savons faire.", "Les configurations pour lesquelles nos équipes sont spécifiquement équipées et formées.")}{services([
 ("continuite", "Réseaux en service", "Intervenir sur un réseau exploité sans interrompre l'écoulement ou la distribution : pompage, dérivation, phasage par tronçon."),
 ("profondeur", "Grande profondeur", "Tranchées de 6 à 7 mètres avec blindage adapté, gestion des venues d'eau et sécurisation des abords."),
 ("diametre", "Grand diamètre", "Pose et renouvellement de canalisations jusqu'à Ø 2000 mm : levage, calage, assemblage et contrôles spécifiques."),
 ("ville", "Secteurs très fréquentés", "Hypercentre, zones piétonnes, abords d'équipements publics : emprises réduites, phasage fin, information des riverains."),
 ("reseau", "Coordination multi-réseaux", "Chantiers en présence de réseaux concessionnaires denses : repérage, protection, dévoiements et coordination des intervenants."),
 ("phasage", "Chantiers à fortes contraintes de délai", "Travaux de nuit, phases courtes, interventions planifiées autour d'événements ou de contraintes d'exploitation."),
])}</div></section>'''
body += band("chantier-hydrocurage-equipe", "Équipe SA LA GARONNE en intervention sur réseau en service en centre-ville", [768,1280,1920], "Toulouse · réseau en service", "Continuité de service, quelles que soient les conditions")
body += f'''<section class="section bg-navy"><div class="container">{section_head("Méthode", "Préparer, sécuriser, exécuter, contrôler.", "Une méthode unique appliquée à chaque chantier complexe, quelle que soit sa taille.", light=True)}{process([
 ("phasage", "Études et phasage", "Analyse des contraintes, études d'exécution, phasage détaillé, plan de circulation et plan de prévention."),
 ("securite", "Sécurisation", "Blindages dimensionnés, balisage, gestion des accès et des flux, protection des ouvrages voisins et des équipes."),
 ("chantier", "Exécution", "Équipes expérimentées et matériel adapté : terrassement profond, levage, pose grand diamètre, réseaux en service."),
 ("controle", "Contrôles et réception", "Essais, inspections, remblaiement contrôlé, réfection à l'identique et dossier de récolement complet."),
])}</div></section>'''
body += chips_specs("Moyens", "Des équipes et un matériel dimensionnés.", "35 collaborateurs, un parc matériel dédié et 70 ans de chantiers sur l'agglomération toulousaine.",
    ["4 équipes de chantier", "Encadrement expérimenté", "Bureau d'études intégré", "Géomètre-dessinateur", "Blindages de tranchée", "Engins de terrassement", "Unités d'hydrocurage", "Robot d'inspection RIC", "Matériel de réhabilitation robotisée", "Atelier intégré"],
    [("Profondeur de tranchée", "6 à 7 m"), ("Diamètre maximal", "Ø 2000 mm"), ("Identifications FNTP", "5141 · 5161 · 5118 · 5221"), ("Organisation", "4 équipes · atelier · bureau d'études"), ("Effectif", "35 collaborateurs"), ("Expérience", "Depuis 1956")])
body += related("travaux-complexes.html") + CTA
page("travaux-complexes.html", "Travaux complexes de réseaux à Toulouse — réseaux en service, grande profondeur, grand diamètre | SA LA GARONNE",
     "Chantiers de réseaux complexes à Toulouse : réseaux en service, tranchées jusqu'à 7 m, canalisations jusqu'à Ø 2000 mm, secteurs très fréquentés. SA LA GARONNE, depuis 1956.", body, "chantier-capitole-engins-1280.jpg")

# ---------------------------------------------------------------- ENTREPRISE
body = hero(
    ["L'entreprise"],
    "L'entreprise",
    "Une entreprise familiale toulousaine, depuis 1956.",
    "Trois générations de la famille Pascual, près de 70 ans de chantiers sur l'agglomération toulousaine, 35 collaborateurs et une conviction : les réseaux d'eau méritent des spécialistes.",
    [("Création", "1956"), ("Direction", "Nicolas Pascual · 3e génération"), ("Effectif", "35 collaborateurs"), ("Organisation", "4 équipes · atelier · bureau d'études")],
    bg="equipe-reunion-inspection", bgalt="Équipe SA LA GARONNE réunie autour d'une inspection vidéo de réseau"
)
body += intro("Qui nous sommes", "Le métier de l'eau, et rien d'autre.",
    ["SA LA GARONNE est une PME familiale de travaux publics fondée à Toulouse le 13 janvier 1956 par Eloy Pascual. Michel Pascual lui succède en 1987, puis Nicolas Pascual en 2017 : trois générations à la tête d'une entreprise concentrée, depuis l'origine, sur un seul domaine — les réseaux d'eau et d'assainissement.",
     "Cette spécialisation nous a permis de développer une expertise reconnue sur les chantiers urbains les plus contraints, d'investir tôt dans la réhabilitation sans tranchée et de concevoir nos propres outils, comme le RIC, robot d'inspection breveté en 2018.",
     "Aujourd'hui, 35 collaborateurs répartis en quatre équipes de chantier, un atelier et un bureau d'études portent cette exigence au quotidien, pour les collectivités, les exploitants et les acteurs du cycle de l'eau. L'activité se répartit entre assainissement (75 %), eau potable (15 %) et réhabilitation sans tranchée (10 %)."])
body += f'''<section class="section section--tight bg-white"><div class="container">{section_head("Repères", "70 ans d'histoire, une trajectoire cohérente.")}<div class="timeline" data-scrub-line><span class="timeline__line"></span>
<div class="tl"><div class="tl__year">1956<small>Fondation</small></div><div><h3>Eloy Pascual crée La Garonne</h3><p>La société est constituée à Toulouse le 13 janvier 1956, sous forme de SARL, pour répondre aux besoins de la ville en réseaux d'eau et d'assainissement.</p></div></div>
<div class="tl"><div class="tl__year">1987<small>Deuxième génération</small></div><div><h3>Michel Pascual prend la direction</h3><p>Le fils du fondateur reprend l'entreprise et consolide son ancrage sur l'agglomération toulousaine : chantiers urbains, grande profondeur, grand diamètre.</p></div></div>
<div class="tl"><div class="tl__year">2017<small>Troisième génération</small></div><div><h3>Nicolas Pascual succède à son père</h3><p>Troisième génération à la tête de l'entreprise familiale. Cette longévité nourrit une relation de confiance avec les acteurs de l'eau du secteur toulousain.</p></div></div>
<div class="tl"><div class="tl__year">2018<small>Innovation</small></div><div><h3>Le RIC, robot d'inspection breveté</h3><p>La Garonne développe et brevète le RIC, robot de télé-visualisation des ouvrages d'assainissement en 4K et à 360°. Plus de 120 km de réseaux inspectés depuis sur la commune de Toulouse.</p></div></div>
<div class="tl"><div class="tl__year">2022<small>Responsabilité</small></div><div><h3>Certification RSE, puis label Engagé RSE d'AFNOR</h3><p>Portée par la responsable QHSE, la démarche RSE est certifiée en juin 2022 et labellisée Engagé RSE par AFNOR en mai 2023. Un comité RSE fixe et évalue des objectifs chaque année.</p></div></div>
<div class="tl"><div class="tl__year">2026<small>70 ans</small></div><div><h3>Une marque technique, fiable et en mouvement</h3><p>35 collaborateurs, quatre équipes de chantier, un atelier, un bureau d'études intégré et une identité renouvelée : l'entreprise aborde ses 70 ans en référence des réseaux d'eau sur son territoire.</p></div></div>
</div></div></section>'''
body += f'''<section class="section bg-ice"><div class="container">{section_head("Ingénierie intégrée", "Un bureau d'études dans l'entreprise.", "Géomètre-dessinateur et chargé d'études travaillent en interne, de la réponse aux appels d'offres jusqu'au récolement. Une plus-value rare pour une entreprise de 35 personnes.")}<div class="duo stagger"><div class="panel panel--white"><p class="eyebrow">Bureau d'études</p><h3 class="panel__title">Étudier, lever, dessiner, contrôler.</h3><ul class="checks"><li>{picto("phasage")}<div><strong>Études de prix et mémoires techniques</strong><span>Une réponse précise aux consultations : variantes, phasages et méthodes argumentés.</span></div></li><li>{picto("reseau")}<div><strong>Levés hebdomadaires des travaux</strong><span>Un géomètre-dessinateur pour quatre équipes de chantier : les ouvrages réalisés sont levés chaque semaine.</span></div></li><li>{picto("controle")}<div><strong>Plans d'exécution et de récolement</strong><span>Une réactivité réelle dans la production des plans, pour le chantier comme pour l'exploitant.</span></div></li><li>{picto("equipe")}<div><strong>Appui technique aux équipes</strong><span>Le chargé d'études suit le chantier, anticipe les points durs et sécurise les choix d'exécution.</span></div></li></ul></div><div class="panel panel--navy"><p class="eyebrow eyebrow--light">Innovation · brevet 2018</p><h3 class="panel__title">RIC, le robot d'inspection conçu par La Garonne.</h3><p class="lead">Robot de télé-visualisation des ouvrages d'assainissement en 4K et à 360°, développé et breveté par l'entreprise. Plus de 120 km de réseaux inspectés sur la commune de Toulouse.</p><div class="scan">{pic("ric-robot-inspection", [768,1024], "Le RIC, robot d'inspection conçu par SA LA GARONNE", "(max-width: 1000px) 100vw, 40vw")}<span class="scan__tag"><i></i>RIC · télé-visualisation 4K · 360°</span></div><div class="panel__facts"><div class="fact"><b>+<span data-count="120">0</span><small>km</small></b><span>de réseaux inspectés</span></div><div class="fact"><b>4K<small>360°</small></b><span>Qualité d'image</span></div><div class="fact"><b>2018</b><span>Brevet déposé</span></div></div></div></div>
<div class="labels labels--light" data-reveal><div><p class="eyebrow">Qualifications & labels</p><p class="muted" style="margin-top:12px;font-size:.9rem;max-width:28ch">Identifications professionnelles FNTP, labels métier et engagements certifiés.</p></div><div class="labels__list"><span><b>FNTP</b> 5118 · AEP zone urbaine</span><span><b>FNTP</b> 5141 · Tranchées fortes profondeurs</span><span><b>FNTP</b> 5161 · Grand diamètre</span><span><b>FNTP</b> 5221 · Réhabilitation réseaux visitables</span><span>Label Canalisateur</span><span>Label RSE TP</span><span>Engagé RSE · AFNOR</span><span>Amiante SS3</span><span>AIPR · CATEC · SST · H0B0</span><span>Qualibat</span><span>NF · AFNOR</span></div><div class="labels__logos"><img src="assets/labels/fntp.png" alt="Fédération Nationale des Travaux Publics" loading="lazy"><img src="assets/labels/label-canalisateur.png" alt="Label Canalisateur — assainissement" loading="lazy"><img src="assets/labels/engage-rse-afnor.png" alt="Label Engagé RSE — AFNOR Certification" loading="lazy"></div></div></div></section>'''
body += f'''<section class="section bg-navy"><div class="container">{section_head("Valeurs", "Ce qui guide nos équipes.", "Six principes, hérités de 70 ans de terrain, appliqués à chaque intervention.", light=True)}<div class="values stagger" style="grid-template-columns:repeat(3,1fr)">
<div class="value"><span class="exp-card__num">01</span>{picto("chantier")}<strong>Technicité</strong><p>Des compétences pointues sur les réseaux, les matériaux, les procédés et les contraintes du sous-sol urbain.</p></div>
<div class="value"><span class="exp-card__num">02</span>{picto("continuite")}<strong>Expérience</strong><p>Près de 70 ans de chantiers sur le même territoire : nous connaissons les réseaux, souvent depuis leur construction.</p></div>
<div class="value"><span class="exp-card__num">03</span>{picto("securite")}<strong>Sécurité</strong><p>Une responsable QHSE dédiée, des formations AIPR, CATEC, SST et H0B0, des EPI contrôlés : la sécurité des équipes et des riverains est la première condition de tout chantier.</p></div>
<div class="value"><span class="exp-card__num">04</span>{picto("controle")}<strong>Fiabilité opérationnelle</strong><p>Des engagements tenus sur les délais, la qualité d'exécution et la continuité de service.</p></div>
<div class="value"><span class="exp-card__num">05</span>{picto("ville")}<strong>Limitation des nuisances</strong><p>Techniques sans tranchée, phasage, emprises réduites : nous respectons la vie du quartier pendant les travaux.</p></div>
<div class="value"><span class="exp-card__num">06</span>{picto("durabilite")}<strong>Durabilité</strong><p>Démarche RSE labellisée, tri et réemploi des déblais, test de chantiers bas carbone : des infrastructures et des pratiques conçues pour durer.</p></div>
</div><div class="labels" data-reveal><div><p class="eyebrow eyebrow--light">Démarche RSE</p><p class="muted" style="margin-top:12px;font-size:.9rem;max-width:26ch">Certifiée en 2022, labellisée Engagé RSE par AFNOR en 2023. Objectifs 2026 :</p></div><div class="labels__list"><span>Tendre vers le zéro accident</span><span>Comité RSE trimestriel</span><span>Partenariats locaux</span><span>Réemploi des déblais</span><span>Chantier bas carbone · biocarburant</span></div></div></div></section>'''
body += f'''<section class="section"><div class="container"><div class="feature"><div class="mosaic"><div class="mask" data-parallax="0.06">{pic("equipe-reunion-inspection", [768,1280,1600], "Réunion d'équipe SA LA GARONNE devant une inspection vidéo de canalisation", "(max-width: 960px) 100vw, 35vw")}</div><div class="mask" data-parallax="-0.05">{pic("equipe-partenariat-moto", [768,946], "Collaboratrices de SA LA GARONNE lors d'un événement d'entreprise", "(max-width: 960px) 100vw, 25vw")}</div></div><div class="feature__body"><p class="eyebrow" data-reveal>Équipe & moyens</p><h2 class="h2" data-split>35 collaborateurs, quatre équipes, un bureau d'études.</h2><p class="lead" data-reveal>Chefs de chantier, canalisateurs, conducteurs d'engins, opérateurs de réhabilitation, encadrement technique : une équipe stable, formée et attachée à son métier.</p><ul class="checks stagger"><li>{picto("equipe")}<div><strong>Quatre équipes de chantier</strong><span>Des équipes qualifiées et fidèles, une transmission du savoir-faire entre générations de canalisateurs et de chefs de chantier.</span></div></li><li>{picto("phasage")}<div><strong>Un bureau d'études intégré</strong><span>Géomètre-dessinateur et chargé d'études : levés hebdomadaires, plans d'exécution et de récolement, études de prix.</span></div></li><li>{picto("chantier")}<div><strong>Un atelier et un parc matériel adaptés</strong><span>Engins de terrassement, unités d'hydrocurage et d'inspection, robot RIC, matériel de réhabilitation robotisée, pompage.</span></div></li><li>{picto("securite")}<div><strong>Une culture sécurité</strong><span>Formations régulières, EPI systématiques, plans de prévention et analyse des risques sur chaque chantier.</span></div></li><li>{picto("ville")}<div><strong>Un siège à Toulouse</strong><span>63 chemin de Guilhermy : bureaux, atelier et parc matériel au cœur de notre zone d'intervention.</span></div></li></ul></div></div></div></section>'''
body += f'''<section class="section section--tight bg-white"><div class="container"><div class="grid grid-5-7"><div><p class="eyebrow" data-reveal>Nous rejoindre</p><h2 class="h2" style="margin-top:20px" data-split>Un métier utile, des chantiers qui comptent.</h2><p class="lead" style="margin-top:24px" data-reveal>Canalisateur, chef de chantier, conducteur d'engins, opérateur de réhabilitation : nous recrutons régulièrement des profils de terrain, débutants comme expérimentés.</p><a class="btn" href="mailto:contact@lagaronnetp.org?subject=Candidature%20spontan%C3%A9e" style="margin-top:32px" data-reveal>Envoyer une candidature {ARROW}</a></div><div data-reveal><p class="mono" style="color:var(--steel);margin-bottom:12px">Fiche d'identité</p><div class="id-card"><div class="spec"><span class="mono">Dénomination</span><b>SA LA GARONNE</b></div><div class="spec"><span class="mono">Forme juridique</span><b>SA à conseil d'administration</b></div><div class="spec"><span class="mono">Capital social</span><b>400 000 €</b></div><div class="spec"><span class="mono">Création</span><b>1956</b></div><div class="spec"><span class="mono">Direction</span><b>Nicolas Pascual — 3<sup>e</sup> génération</b></div><div class="spec"><span class="mono">Effectif</span><b>35 salariés · 4 équipes de chantier · atelier · bureau d'études</b></div><div class="spec"><span class="mono">Activité</span><b>Assainissement 75 % · eau potable 15 % · sans tranchée 10 %</b></div><div class="spec"><span class="mono">SIREN</span><b>560 800 583</b></div><div class="spec"><span class="mono">Code APE</span><b>4221Z — Construction de réseaux pour fluides</b></div><div class="spec"><span class="mono">Siège</span><b>63 chemin de Guilhermy, 31100 Toulouse</b></div></div></div></div></div></section>'''
body += CTA
page("entreprise.html", "L'entreprise — SA LA GARONNE, PME familiale de travaux publics à Toulouse depuis 1956",
     "SA LA GARONNE : entreprise familiale de travaux publics fondée à Toulouse en 1956, 35 collaborateurs spécialisés dans les réseaux d'eau et d'assainissement. Histoire, valeurs, équipe et moyens.", body, "equipe-reunion-inspection-1280.jpg")

# ---------------------------------------------------------------- RÉALISATIONS
def work(cat, catlabel, title, text, img, sizes_w, span="", sizes="(max-width: 960px) 100vw, 50vw"):
    return f'<article class="work {span}" data-cat="{cat}" data-reveal>{pic(img, sizes_w, title, sizes)}<div class="work__cap"><span class="mono">{catlabel}</span><strong>{title}</strong><span>{text}</span></div></article>'
body = hero(
    ["Réalisations"],
    "Réalisations",
    "Sur le terrain, à Toulouse et autour.",
    "Un aperçu de nos interventions sur les infrastructures essentielles de l'agglomération toulousaine : assainissement, eau potable, réhabilitation sans tranchée et chantiers complexes.",
    [("Territoire", "Toulouse Métropole & agglomération"), ("Cadre", "Marchés publics & privés"), ("Depuis", "1956")],
    bg="chantier-tranchee-centre-ville", bgalt="Chantier SA LA GARONNE en centre-ville de Toulouse"
)
body += f'''<section class="section"><div class="container"><div class="section-head"><div><p class="eyebrow" data-reveal>Galerie</p><h2 class="h2" data-split>Nos chantiers en images.</h2></div><div class="filters" data-reveal><button class="is-active" data-filter="all">Tous</button><button data-filter="assainissement">Assainissement</button><button data-filter="eau-potable">Eau potable</button><button data-filter="sans-tranchee">Sans tranchée</button><button data-filter="complexes">Travaux complexes</button></div></div>
<div class="gallery">
{work("complexes", "Travaux complexes · Toulouse", "Intervention en hypercentre", "Logistique lourde, emprise maîtrisée et coordination fine au cœur de Toulouse, sous les arcades du Capitole.", "chantier-capitole-engins", [768,1280,1920], "span-8", "(max-width: 960px) 100vw, 66vw")}
{work("assainissement complexes", "Réseau en service", "Intervention sur regard d'assainissement", "Équipe et matériel dédiés en centre-ville : continuité de service assurée pendant l'intervention.", "chantier-hydrocurage-equipe", [768,1280,1920], "span-4", "(max-width: 960px) 100vw, 33vw")}
{work("assainissement", "Assainissement · centre-ville", "Renouvellement de réseau en secteur piéton", "Tranchée, lit de pose et réfection de voirie à l'identique, dans un secteur commerçant très fréquenté.", "chantier-tranchee-centre-ville", [768,1280,1920], "", "(max-width: 960px) 100vw, 50vw")}
{work("sans-tranchee", "Sans tranchée", "Unité mobile de réhabilitation", "Chemisage et interventions robotisées pilotées depuis la surface, sans ouverture de la chaussée.", "camion-rehabilitation-sans-tranchee", [800], "", "(max-width: 960px) 100vw, 50vw")}
{work("sans-tranchee complexes", "Diagnostic & inspection", "Inspection télévisée de collecteur", "Analyse en équipe des relevés caméra avant intervention : la préparation est la première étape de tout chantier.", "equipe-reunion-inspection", [768,1280,1600], "span-8", "(max-width: 960px) 100vw, 66vw")}
{work("assainissement complexes", "Grande profondeur", "Collecteur visitable en fouille blindée", "Réhabilitation d'un ouvrage visitable : accès par fouille blindée, intervention en sécurité à grande profondeur.", "collecteur-visitable-profondeur", [536], "span-4", "(max-width: 960px) 100vw, 33vw")}
{work("complexes", "Secteur sensible · Toulouse", "Fouille blindée devant un monument", "Blindage lourd au pied du monument aux morts, dans un carrefour très fréquenté, circulation et cheminements maintenus.", "tranchee-blindee-monument", [529], "span-4", "(max-width: 960px) 100vw, 33vw")}
{work("eau-potable", "Eau potable", "Raccordement de conduites en fonte", "Pose de pièces de raccord et de vannes sur une conduite d'adduction : précision d'assemblage et essais avant remise en eau.", "aep-raccordement-fonte", [768], "span-4", "(max-width: 960px) 100vw, 33vw")}
{work("sans-tranchee", "Innovation", "RIC, robot d'inspection breveté", "Télé-visualisation 4K à 360° des ouvrages d'assainissement, conçue par La Garonne : plus de 120 km inspectés à Toulouse.", "ric-robot-inspection", [768,1024], "span-8", "(max-width: 960px) 100vw, 66vw")}
<article class="work work--text span-4" data-reveal><span class="mono accent-blue">Références</span><span class="h3">Vous souhaitez consulter nos références détaillées ?</span><a class="link-arrow" href="contact.html"><span>Nous contacter</span>{LARROW}</a></article>
</div></div></section>'''
body += f'''<section class="section section--tight bg-white"><div class="container">{section_head("Donneurs d'ordre", "Nous intervenons pour", "Un environnement B2B et marchés publics, aux côtés des acteurs qui exploitent et font vivre les infrastructures de l'eau.")}<ul class="clients stagger"><li class="client"><span>Collectivités & métropoles</span><span class="mono">Marchés publics</span></li><li class="client"><span>Exploitants de réseaux</span><span class="mono">Régies · délégataires</span></li><li class="client"><span>Acteurs publics & aménageurs</span><span class="mono">Infrastructures</span></li><li class="client"><span>Professionnels du cycle de l'eau</span><span class="mono">Ingénierie · entreprises</span></li></ul></div></section>'''
body += CTA
page("realisations.html", "Réalisations — chantiers de réseaux d'eau et d'assainissement à Toulouse | SA LA GARONNE",
     "Découvrez les chantiers de SA LA GARONNE à Toulouse : assainissement, eau potable, réhabilitation sans tranchée et interventions complexes en hypercentre.", body, "chantier-tranchee-centre-ville-1280.jpg")

# ---------------------------------------------------------------- CONTACT
body = hero(
    ["Contact"],
    "Contact",
    "Parlons de votre réseau.",
    "Demande de devis, consultation dans le cadre d'un marché public, question technique ou candidature : nos équipes vous répondent rapidement et précisément.",
    [("Téléphone", "+33 5 62 13 07 80"), ("Email", "contact@lagaronnetp.org"), ("Siège", "Toulouse · 31100")],
    bg="chantier-hydrocurage-equipe", bgalt="Équipe SA LA GARONNE sur chantier"
)
body += f'''<section class="section"><div class="container"><div class="contact-grid"><div><p class="eyebrow" data-reveal>Coordonnées</p><h2 class="h2" style="margin-top:20px" data-split>Nous joindre.</h2><ul class="contact-list stagger"><li><span class="mono">Téléphone</span><a href="tel:+33562130780">+33 5 62 13 07 80</a></li><li><span class="mono">Email</span><a href="mailto:contact@lagaronnetp.org">contact@lagaronnetp.org</a></li><li><span class="mono">Adresse</span><address style="font-style:normal">SA LA GARONNE<br>63 chemin de Guilhermy<br>31100 Toulouse</address></li><li><span class="mono">Zone</span><span>Toulouse Métropole et agglomération toulousaine</span></li><li><span class="mono">Marchés</span><span>Réponse aux consultations publiques et privées</span></li></ul><div class="hq" style="margin-top:32px" data-reveal><div class="hq__img">{pic("siege-vue-aerienne", [768,1128], "Vue aérienne du siège de SA LA GARONNE, chemin de Guilhermy à Toulouse", "(max-width: 960px) 100vw, 40vw")}</div><p class="mono" style="color:var(--steel)">Siège & parc matériel · Toulouse</p></div></div>
<form class="form" data-form novalidate data-reveal>
<p class="eyebrow">Formulaire</p>
<div class="form__row"><div class="field"><label for="f-nom">Nom et prénom *</label><input id="f-nom" name="nom" type="text" required autocomplete="name"></div><div class="field"><label for="f-org">Organisation</label><input id="f-org" name="organisation" type="text" autocomplete="organization" placeholder="Collectivité, exploitant, entreprise…"></div></div>
<div class="form__row"><div class="field"><label for="f-email">Email *</label><input id="f-email" name="email" type="email" required autocomplete="email"></div><div class="field"><label for="f-tel">Téléphone</label><input id="f-tel" name="telephone" type="tel" autocomplete="tel"></div></div>
<div class="field"><label for="f-objet">Objet *</label><select id="f-objet" name="objet" required><option value="Demande de devis">Demande de devis</option><option value="Consultation / marché public">Consultation / marché public</option><option value="Question technique">Question technique</option><option value="Candidature">Candidature</option><option value="Autre">Autre</option></select></div>
<div class="field"><label for="f-msg">Votre message *</label><textarea id="f-msg" name="message" required placeholder="Nature du réseau, localisation, contraintes particulières, délais…"></textarea></div>
<input type="text" name="_gotcha" tabindex="-1" autocomplete="off" style="position:absolute;left:-9999px" aria-hidden="true">
<div class="field" style="grid-template-columns:auto 1fr;display:grid;gap:12px;align-items:start"><input id="f-rgpd" name="consentement" type="checkbox" required style="width:18px;height:18px;margin-top:3px"><label for="f-rgpd" style="text-transform:none;letter-spacing:0;font-family:var(--font-body);font-size:.85rem;color:var(--navy)">J'accepte que les informations saisies soient utilisées pour traiter ma demande. Elles ne sont ni cédées ni utilisées à d'autres fins.</label></div>
<div class="form__foot"><button class="btn" type="submit">Envoyer le message {ARROW}</button><p class="form__note">* Champs obligatoires. Réponse sous 48 h ouvrées.</p></div>
<p class="form__status" role="status" aria-live="polite"></p>
</form></div></div></section>'''
body += f'''<section class="section section--tight bg-white"><div class="container">{section_head("Accès", "Le siège, chemin de Guilhermy.", "Au sud-ouest de Toulouse, à proximité immédiate du périphérique — au cœur de notre zone d'intervention.")}<div class="map" data-reveal><iframe title="Plan d'accès — SA LA GARONNE, 63 chemin de Guilhermy, 31100 Toulouse" src="https://www.google.com/maps?q=63+chemin+de+Guilhermy,+31100+Toulouse&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div></div></section>'''
page("contact.html", "Contact — SA LA GARONNE, travaux publics réseaux d'eau et d'assainissement à Toulouse",
     "Contactez SA LA GARONNE à Toulouse : demande de devis, consultation marché public, question technique. 63 chemin de Guilhermy, 31100 Toulouse — +33 5 62 13 07 80.", body, "chantier-hydrocurage-equipe-1280.jpg")

# ---------------------------------------------------------------- MENTIONS LÉGALES
body = f'''<section class="hero-page" style="padding-bottom:clamp(32px,4vw,56px)">{RINGS}<div class="container"><nav class="crumbs" aria-label="Fil d'Ariane"><a href="index.html">Accueil</a> <span>/</span> Mentions légales</nav><h1 class="h1" style="margin-top:28px" data-split>Mentions légales</h1></div></section>
<section class="section"><div class="container"><div class="prose" data-reveal>
<h2>Éditeur du site</h2>
<p>Le site <strong>sa-la-garonne.fr</strong> est édité par <strong>SA LA GARONNE</strong> (dénomination sociale : SOC LA GARONNE), société anonyme à conseil d'administration au capital de 400 000 €, immatriculée au RCS de Toulouse sous le numéro 560 800 583 — code APE 4221Z (construction de réseaux pour fluides).</p>
<p>Siège social : 63 chemin de Guilhermy, 31100 Toulouse, France.<br>Téléphone : +33 5 62 13 07 80 — Email : <a href="mailto:contact@lagaronnetp.org">contact@lagaronnetp.org</a><br>N° de TVA intracommunautaire : FR05 560 800 583.</p>
<p>Directeur de la publication : Nicolas Pascual.</p>
<h2>Hébergement</h2>
<p>[Nom de l'hébergeur — raison sociale, adresse, téléphone — à compléter lors de la mise en ligne.]</p>
<h2>Conception et réalisation</h2>
<p>Direction artistique, identité visuelle et développement : <a href="https://agence-pmc-marketing.com" target="_blank" rel="noopener">PMC Marketing</a>, agence digitale Performance & IA, Toulouse.<br>Photographies : SA LA GARONNE. Toute reproduction est interdite sans autorisation.</p>
<h2>Propriété intellectuelle</h2>
<p>L'ensemble des contenus de ce site (textes, photographies, illustrations, logotype, pictogrammes, structure) est protégé par le droit d'auteur et le droit des marques. Toute reproduction, représentation, modification ou adaptation, totale ou partielle, sans autorisation écrite préalable de SA LA GARONNE est interdite.</p>
<h2>Données personnelles</h2>
<p>Les informations transmises via le formulaire de contact (nom, organisation, email, téléphone, message) sont utilisées exclusivement pour répondre à votre demande. Elles sont destinées aux services concernés de SA LA GARONNE et ne sont ni cédées ni vendues à des tiers. Elles sont conservées pendant la durée nécessaire au traitement de la demande et, le cas échéant, de la relation commerciale qui en découle.</p>
<p>Conformément au Règlement général sur la protection des données (RGPD) et à la loi Informatique et Libertés, vous disposez d'un droit d'accès, de rectification, d'effacement, de limitation et d'opposition sur vos données. Vous pouvez l'exercer en écrivant à <a href="mailto:contact@lagaronnetp.org">contact@lagaronnetp.org</a> ou par courrier à l'adresse du siège.</p>
<h2>Cookies</h2>
<p>Ce site n'utilise aucun cookie publicitaire ni outil de suivi tiers. Seul un stockage technique de session, sans identification, est utilisé pour le confort de navigation (affichage unique de l'écran d'introduction). La carte d'accès de la page Contact est fournie par Google Maps et soumise à ses propres conditions d'utilisation.</p>
<h2>Responsabilité</h2>
<p>SA LA GARONNE s'efforce d'assurer l'exactitude des informations publiées sur ce site, sans pouvoir garantir l'absence d'erreur ou d'omission. Les informations présentées n'ont pas de valeur contractuelle. SA LA GARONNE se réserve le droit de modifier le contenu du site à tout moment.</p>
<h2>Droit applicable</h2>
<p>Le présent site est soumis au droit français. Tout litige relatif à son utilisation relève de la compétence des tribunaux de Toulouse.</p>
</div></div></section>'''
page("mentions-legales.html", "Mentions légales — SA LA GARONNE", "Mentions légales du site de SA LA GARONNE, société de travaux publics à Toulouse.", body)
