# -*- coding: utf-8 -*-
"""Dictionnaire de traduction du site SA LA GARONNE — français (source) → anglais, chinois simplifié.

Terminologie métier retenue :
  assainissement            → sewerage / wastewater networks   → 排水管网
  adduction d'eau potable   → drinking water supply            → 给水管网
  réhabilitation sans tranchée → trenchless rehabilitation     → 非开挖修复
  chemisage                 → CIPP lining                      → 原位固化内衬 (CIPP)
  collecteur                → sewer main                       → 排水干管
  branchement               → service connection               → 接户管
  regard                    → manhole                          → 检查井
  récolement                → as-built survey                  → 竣工测量
  bureau d'études           → in-house design office           → 技术设计部
Le nom de l'entreprise (SA LA GARONNE, La Garonne) n'est pas traduit.
"""

T = {}

def add(d):
    T.update(d)

# ---------------------------------------------------------------- Interface, navigation, pied de page
add({
"Aller au contenu": ("Skip to content", "跳转到主要内容"),
"SA LA GARONNE · Toulouse · Depuis 1956": ("SA LA GARONNE · Toulouse · Since 1956", "SA LA GARONNE · 图卢兹 · 始于 1956 年"),
"Navigation principale": ("Main navigation", "主导航"),
"Expertises": ("Expertise", "专业领域"),
"Assainissement": ("Sewerage", "排水管网"),
"Réseaux d'eaux usées et pluviales": ("Wastewater and stormwater networks", "污水与雨水管网"),
"Adduction d'eau potable": ("Drinking water supply", "饮用水输配"),
"Conduites, branchements, ouvrages": ("Mains, service connections, structures", "管道、接户管、构筑物"),
"Réhabilitation sans tranchée": ("Trenchless rehabilitation", "非开挖修复"),
"Chemisage, gainage, robotique": ("CIPP lining, sleeving, robotics", "原位固化内衬、内衬修复、机器人作业"),
"Travaux complexes": ("Complex works", "复杂工程"),
"Réseaux en service, grande profondeur": ("Live networks, deep excavation", "在役管网、深基坑"),
"Réalisations": ("Projects", "工程案例"),
"L'entreprise": ("The company", "关于我们"),
"Contact": ("Contact", "联系我们"),
"Appeler": ("Call us", "致电"),
"Nous contacter": ("Get in touch", "联系我们"),
"Ouvrir le menu": ("Open menu", "打开菜单"),
"Menu": ("Menu", "菜单"),
"Accueil": ("Home", "首页"),
"Eau potable": ("Drinking water", "饮用水"),
"Sans tranchée": ("Trenchless", "非开挖"),
"Téléphone": ("Phone", "电话"),
"Email": ("Email", "电子邮箱"),
"Siège": ("Head office", "总部"),
"63 chemin de Guilhermy, 31100 Toulouse": ("63 chemin de Guilhermy, 31100 Toulouse, France", "法国图卢兹 31100，63 chemin de Guilhermy"),
"63 chemin de Guilhermy": ("63 chemin de Guilhermy", "63 chemin de Guilhermy"),
"31100 Toulouse": ("31100 Toulouse, France", "31100 图卢兹，法国"),
"SA LA GARONNE — Travaux Publics": ("SA LA GARONNE — Civil Engineering", "SA LA GARONNE — 市政工程"),
"Expert des réseaux d'eau et d'assainissement depuis 1956. PME familiale de travaux publics, Toulouse.":
  ("Water and wastewater network specialists since 1956. Family-owned civil engineering company, Toulouse, France.",
   "自 1956 年起专注给排水管网工程。法国图卢兹家族企业，市政工程承包商。"),
"Entreprise": ("Company", "公司"),
"Mentions légales": ("Legal notice", "法律声明"),
"SA LA GARONNE · SIREN 560 800 583 · Tous droits réservés": ("SA LA GARONNE · Company no. 560 800 583 · All rights reserved", "SA LA GARONNE · 企业注册号 560 800 583 · 版权所有"),
"Site créé par PMC Marketing — ouvrir le site de l'agence": ("Site built by PMC Marketing — visit the agency website", "网站由 PMC Marketing 制作 — 访问代理机构网站"),
"Site créé par": ("Site built by", "网站制作"),
"PMC Marketing — agence digitale, Toulouse": ("PMC Marketing — digital agency, Toulouse", "PMC Marketing — 数字代理机构，图卢兹"),
"Fil d'Ariane": ("Breadcrumb", "面包屑导航"),
"Travaux Publics": ("Civil Engineering", "市政工程"),
"La Garonne": ("La Garonne", "La Garonne"),
"SA LA GARONNE": ("SA LA GARONNE", "SA LA GARONNE"),
"contact@lagaronnetp.org": ("contact@lagaronnetp.org", "contact@lagaronnetp.org"),
"PMC Marketing": ("PMC Marketing", "PMC Marketing"),
})

# ---------------------------------------------------------------- Page 404
add({
"Page introuvable — SA LA GARONNE": ("Page not found — SA LA GARONNE", "页面未找到 — SA LA GARONNE"),
"La page demandée n'existe pas. Retrouvez les expertises, réalisations et coordonnées de SA LA GARONNE.":
  ("The page you asked for does not exist. Browse SA LA GARONNE's expertise, projects and contact details.",
   "您访问的页面不存在。请浏览 SA LA GARONNE 的专业领域、工程案例与联系方式。"),
"Erreur 404": ("Error 404", "错误 404"),
"Cette page n'existe pas.": ("This page does not exist.", "该页面不存在。"),
"Le lien est peut-être ancien ou l'adresse contient une erreur. Nos expertises, nos réalisations et nos coordonnées restent accessibles ci-dessous.":
  ("The link may be outdated or the address may contain a mistake. Our expertise, projects and contact details are all available below.",
   "该链接可能已失效，或网址有误。我们的专业领域、工程案例与联系方式仍可在下方查看。"),
"Retour à l'accueil": ("Back to home", "返回首页"),
})

# ---------------------------------------------------------------- Accueil
add({
"SA LA GARONNE — Réseaux d'eau et assainissement, Toulouse": ("SA LA GARONNE — Water and sewer networks, Toulouse", "SA LA GARONNE — 给排水管网工程，图卢兹"),
"PME familiale de travaux publics à Toulouse depuis 1956 : assainissement, eau potable, réhabilitation sans tranchée et chantiers urbains complexes.":
  ("Family-owned civil engineering company in Toulouse since 1956: sewerage, drinking water, trenchless rehabilitation and complex urban worksites.",
   "自 1956 年扎根图卢兹的家族市政工程企业：排水管网、饮用水管网、非开挖修复及复杂城市工程。"),
"Assainissement, adduction d'eau potable, réhabilitation sans tranchée et travaux complexes. Toulouse et son agglomération.":
  ("Sewerage, drinking water supply, trenchless rehabilitation and complex works. Toulouse and its metropolitan area.",
   "排水管网、饮用水输配、非开挖修复与复杂工程。服务图卢兹及周边地区。"),
"Canalisateur SA LA GARONNE réglant le lit de pose d'une tranchée en centre-ville de Toulouse, pelle mécanique en arrière-plan":
  ("SA LA GARONNE pipelayer levelling the bedding of a trench in central Toulouse, excavator in the background",
   "SA LA GARONNE 管道工在图卢兹市中心整平沟槽垫层，背景为挖掘机"),
"SA La Garonne · Travaux publics · Toulouse": ("SA La Garonne · Civil engineering · Toulouse", "SA La Garonne · 市政工程 · 图卢兹"),
"PME familiale toulousaine, nous construisons, entretenons et réhabilitons les réseaux d'assainissement et d'eau potable — y compris sur les chantiers urbains les plus contraints.":
  ("A family-owned company from Toulouse, we build, maintain and rehabilitate sewer and drinking water networks — including on the most constrained urban worksites.",
   "作为图卢兹本地家族企业，我们建设、维护并修复排水与饮用水管网，包括条件最苛刻的城市工程。"),
"Nos expertises": ("Our expertise", "专业领域"),
"Défiler": ("Scroll", "向下滚动"),
"Depuis": ("Since", "创立于"),
"Depuis 1956": ("Since 1956", "始于 1956 年"),
"Effectif": ("Team", "员工人数"),
"35 collaborateurs": ("35 employees", "35 名员工"),
"Tranchées": ("Trenches", "沟槽深度"),
"jusqu'à 7 m": ("up to 7 m", "最深 7 米"),
"Conduites": ("Pipes", "管径"),
"Ø 2000 mm": ("Ø 2000 mm", "Ø 2000 毫米"),
"Zone": ("Area", "服务区域"),
"Toulouse & agglomération": ("Toulouse & metropolitan area", "图卢兹及周边地区"),
"Grande profondeur": ("Deep excavation", "深基坑作业"),
"Chemisage": ("CIPP lining", "原位固化内衬"),
"Fraisage robotisé": ("Robotic milling", "机器人铣削"),
"Bureau d'études intégré": ("In-house design office", "内设技术设计部"),
"Réseaux en service": ("Live networks", "在役管网"),
"01 / L'essentiel": ("01 / The essentials", "01 / 核心"),
"Sous la ville, l'essentiel.": ("Beneath the city, the essentials.", "城市之下，至关重要。"),
"Les réseaux d'eau ne se voient pas. Ils doivent pourtant fonctionner chaque jour, sans interruption.":
  ("Water networks are invisible. Yet they have to work every single day, without interruption.",
   "给排水管网深埋地下，却必须日复一日不间断地运行。"),
"Depuis 1956, SA LA GARONNE construit, entretient et réhabilite les réseaux d'assainissement et d'adduction d'eau potable de Toulouse et de son agglomération. Une PME familiale de 35 collaborateurs — quatre équipes de chantier, un atelier et un bureau d'études intégré — dirigée par la troisième génération de la famille Pascual et reconnue pour sa maîtrise des chantiers urbains complexes : réseaux en service, grande profondeur, canalisations de grand diamètre.":
  ("Since 1956, SA LA GARONNE has been building, maintaining and rehabilitating the sewer and drinking water networks of Toulouse and its metropolitan area. A family-owned company of 35 employees — four site crews, a workshop and an in-house design office — led by the third generation of the Pascual family and recognised for its command of complex urban worksites: live networks, deep excavation, large-diameter pipes.",
   "自 1956 年以来，SA LA GARONNE 一直负责图卢兹及周边地区排水与饮用水管网的建设、维护与修复。公司为家族企业，现有 35 名员工，下设四支施工班组、一个机修车间和一个内部技术设计部，由帕斯夸尔（Pascual）家族第三代执掌，以驾驭复杂城市工程见长：在役管网作业、深基坑施工、大口径管道敷设。"),
"Notre engagement tient en trois mots : technicité, sécurité, continuité de service.":
  ("Our commitment comes down to three words: technical skill, safety, continuity of service.",
   "我们的承诺可归结为三点：技术实力、施工安全、供水排水不中断。"),
"Découvrir l'entreprise": ("Discover the company", "了解公司"),
"Année de création": ("Year founded", "创立年份"),
"ans": ("years", "年"),
"d'expérience terrain": ("of hands-on experience", "现场施工经验"),
"Collaborateurs qualifiés": ("Skilled employees", "专业员工"),
"générations": ("generations", "代传承"),
"À la tête de l'entreprise familiale": ("At the head of the family business", "家族企业掌门人"),
"02 / Expertises": ("02 / Expertise", "02 / 专业领域"),
"Quatre métiers, un seul niveau d'exigence.": ("Four disciplines, one standard.", "四大业务，同一标准。"),
"Nous concentrons notre savoir-faire sur les réseaux d'eau. C'est ce que nous faisons de mieux — et ce que nous faisons depuis 70 ans.":
  ("We focus our know-how on water networks. It is what we do best — and what we have been doing for 70 years.",
   "我们专注于给排水管网，这是我们最擅长的领域，也是我们坚持了 70 年的事业。"),
"Construction, renouvellement et réhabilitation des réseaux d'eaux usées et pluviales, branchements et ouvrages.":
  ("Construction, renewal and rehabilitation of wastewater and stormwater networks, service connections and structures.",
   "污水与雨水管网、接户管及构筑物的新建、更新与修复。"),
"Découvrir": ("Learn more", "了解详情"),
"Pose et renouvellement de conduites d'adduction et de distribution, branchements, ouvrages hydrauliques.":
  ("Laying and renewal of supply and distribution mains, service connections and hydraulic structures.",
   "输水与配水管道敷设更新、接户管及水工构筑物。"),
"Chemisage, gainage, fraisage et interventions robotisées : rénover les réseaux sans ouvrir la voirie.":
  ("CIPP lining, sleeving, milling and robotic operations: renovating networks without opening the road.",
   "原位固化内衬、内衬修复、铣削与机器人作业：无需开挖路面即可修复管网。"),
"Réseaux en service, grande profondeur, grand diamètre, secteurs très fréquentés : des chantiers maîtrisés.":
  ("Live networks, deep excavation, large diameters, busy areas: worksites under control.",
   "在役管网、深基坑、大口径、人流密集区域：全程可控的施工。"),
"03 / Savoir-faire signature": ("03 / Signature know-how", "03 / 核心技术"),
"Réhabiliter sans ouvrir la voirie.": ("Rehabilitation without opening the road.", "无需开挖路面的管网修复。"),
"La réhabilitation sans tranchée rénove les réseaux existants depuis l'intérieur. Moins d'ouverture de chaussée, des délais plus courts, moins de nuisances pour les riverains.":
  ("Trenchless rehabilitation renovates existing networks from the inside. Less road opening, shorter schedules, less disruption for residents.",
   "非开挖修复从管道内部对既有管网进行更新：路面开挖更少、工期更短、对周边居民的影响更小。"),
"Inspection caméra": ("CCTV inspection", "闭路电视检测"),
"Diagnostic précis de l'état de la conduite avant toute intervention.": ("Precise assessment of the pipe's condition before any work begins.", "施工前对管道状况进行精确诊断。"),
"Préparation robotisée": ("Robotic preparation", "机器人预处理"),
"Hydrocurage, fraisage des obstacles et des dépôts, préparation des branchements.":
  ("High-pressure jetting, milling of obstructions and deposits, preparation of service connections.",
   "高压水射流清洗、铣除障碍物与结垢、接户管口预处理。"),
"Chemisage / gainage": ("CIPP lining / sleeving", "原位固化内衬 / 内衬修复"),
"Mise en place d'une gaine polymérisée en place : une conduite neuve dans l'ancienne.":
  ("Installation of a cured-in-place liner: a new pipe inside the old one.",
   "植入原位固化内衬：在旧管内形成一条新管。"),
"Remise en service": ("Return to service", "恢复通水"),
"Réouverture des branchements, contrôles, remise en eau. La rue n'a pas été ouverte.":
  ("Service connections reopened, checks completed, flow restored. The street was never opened.",
   "重新开通接户管、完成检验、恢复通水。全程未开挖路面。"),
"Découvrir la réhabilitation sans tranchée": ("Discover trenchless rehabilitation", "了解非开挖修复"),
"Unité mobile · sans tranchée": ("Mobile unit · trenchless", "移动作业车 · 非开挖"),
"Regard": ("Manhole", "检查井"),
"0 m": ("0 m", "0 米"),
"−3 m": ("−3 m", "−3 米"),
"−6 m": ("−6 m", "−6 米"),
"Conduite existante · Ø 800 mm": ("Existing pipe · Ø 800 mm", "既有管道 · Ø 800 毫米"),
"Réseau en service": ("Network in service", "管网运行中"),
"Défilez pour piloter l'intervention": ("Scroll to run the operation", "滚动页面以推进施工流程"),
"Camions et équipes SA LA GARONNE en intervention sous les arcades de la place du Capitole, à Toulouse":
  ("SA LA GARONNE trucks and crews at work under the arcades of Place du Capitole in Toulouse",
   "SA LA GARONNE 的车辆与班组在图卢兹市政厅广场拱廊下作业"),
"Toulouse · place du Capitole": ("Toulouse · Place du Capitole", "图卢兹 · 市政厅广场"),
"04 / Chantiers contraints": ("04 / Constrained worksites", "04 / 受限工况"),
"Là où le chantier se complique, nous intervenons.": ("Where the job gets complicated, we step in.", "工况越复杂，越是我们的舞台。"),
"Hypercentre, réseaux en service, tranchées profondes, canalisations de grand diamètre : nos équipes sont dimensionnées pour les chantiers qui n'admettent pas l'approximation.":
  ("City centre, live networks, deep trenches, large-diameter pipes: our crews are sized for worksites that leave no room for approximation.",
   "老城核心区、在役管网、深沟槽、大口径管道：我们的团队专为不容差错的工程而组建。"),
"Maintien de la continuité de service pendant toute la durée des travaux.": ("Continuity of service maintained throughout the works.", "施工全程保持供水与排水不中断。"),
"Tranchées jusqu'à 6 à 7 mètres, blindage et sécurisation systématiques.": ("Trenches 6 to 7 metres deep, with systematic shoring and safety measures.", "沟槽深度达 6 至 7 米，全程支护并落实安全措施。"),
"Pose de canalisations jusqu'à Ø 2000 mm.": ("Pipes laid up to Ø 2000 mm.", "可敷设管径达 Ø 2000 毫米的管道。"),
"Secteurs très fréquentés": ("Busy areas", "人流密集区域"),
"Phasage précis, emprises réduites, gestion des flux piétons et véhicules.": ("Precise phasing, reduced footprint, management of pedestrian and vehicle flows.", "精细分阶段施工、缩小占地范围、组织人车通行。"),
"Nos travaux complexes": ("Our complex works", "复杂工程业务"),
"Grand diamètre": ("Large diameter", "大口径"),
"05 / Ingénierie intégrée": ("05 / In-house engineering", "05 / 内部工程能力"),
"06 / Réalisations": ("06 / Projects", "06 / 工程案例"),
"Sur le terrain.": ("On site.", "施工现场。"),
"Toutes nos réalisations": ("All our projects", "全部工程案例"),
"07 / Engagements": ("07 / Commitments", "07 / 我们的承诺"),
"08 / L'entreprise": ("08 / The company", "08 / 关于我们"),
"09 / Donneurs d'ordre": ("09 / Clients", "09 / 客户群体"),
"10 / Contact": ("10 / Contact", "10 / 联系我们"),
})

# ---------------------------------------------------------------- Page Assainissement
add({
"Assainissement à Toulouse — SA LA GARONNE": ("Sewerage works in Toulouse — SA LA GARONNE", "图卢兹排水管网工程 — SA LA GARONNE"),
"Construction, renouvellement et réhabilitation de réseaux d'assainissement à Toulouse : collecteurs, branchements, réseaux en service, grande profondeur.":
  ("Construction, renewal and rehabilitation of sewer networks in Toulouse: mains, service connections, live networks, deep excavation.",
   "图卢兹排水管网的新建、更新与修复：排水干管、接户管、在役管网作业、深基坑施工。"),
"Canalisateur SA LA GARONNE dans un collecteur visitable en grande profondeur": ("SA LA GARONNE pipelayer inside a deep man-entry sewer", "SA LA GARONNE 管道工在深埋可通行排水干管内作业"),
"Expertise 01 / Assainissement": ("Expertise 01 / Sewerage", "专业领域 01 / 排水管网"),
"Assainis\xadsement": ("Sewerage", "排水管网"),
"Construire, renouveler et réhabiliter les réseaux d'eaux usées et pluviales, leurs branchements et leurs ouvrages — en milieu urbain dense et sur des réseaux en service.":
  ("Building, renewing and rehabilitating wastewater and stormwater networks, their service connections and structures — in dense urban settings and on live networks.",
   "在密集城区及在役管网条件下，新建、更新并修复污水与雨水管网及其接户管和构筑物。"),
"Part d'activité": ("Share of business", "业务占比"),
"75 % de l'activité": ("75% of business", "占业务量 75%"),
"Réseaux": ("Networks", "管网类型"),
"Unitaires · EU · EP": ("Combined · foul · storm", "合流 · 污水 · 雨水"),
"Diamètres": ("Diameters", "管径范围"),
"jusqu'à Ø 2000 mm": ("up to Ø 2000 mm", "最大 Ø 2000 毫米"),
"Profondeur": ("Depth", "施工深度"),
"Qualifications": ("Qualifications", "资质认证"),
"FNTP 5141 · 5161 · 5221": ("FNTP 5141 · 5161 · 5221", "FNTP 5141 · 5161 · 5221"),
"Notre approche": ("Our approach", "我们的理念"),
"Un réseau qui fonctionne en continu, et qui ne doit jamais s'arrêter.": ("A network that runs continuously, and must never stop.", "持续运行、不容中断的管网系统。"),
"Les réseaux d'assainissement collectent chaque jour les eaux usées et pluviales d'une agglomération entière. Ils sont enterrés, souvent anciens, et rarement visibles — jusqu'au jour où ils défaillent.":
  ("Sewer networks collect the wastewater and stormwater of an entire metropolitan area every day. They are buried, often old, and rarely visible — until the day they fail.",
   "排水管网每天承担整个城市片区的污水与雨水收集。它们深埋地下、往往年代久远，平时无人察觉，直到出现故障的那一天。"),
"Depuis 1956, SA LA GARONNE construit, renouvelle et réhabilite ces réseaux pour les collectivités et les exploitants de Toulouse et de son agglomération : collecteurs, branchements particuliers, regards et ouvrages annexes. Nous intervenons sur des réseaux en service, à grande profondeur et sur des canalisations de grand diamètre, avec une exigence constante : maintenir l'écoulement pendant les travaux.":
  ("Since 1956, SA LA GARONNE has been building, renewing and rehabilitating these networks for local authorities and operators in Toulouse and its metropolitan area: sewer mains, individual service connections, manholes and ancillary structures. We work on live networks, at great depth and on large-diameter pipes, with one constant requirement: keeping the flow running throughout the works.",
   "自 1956 年起，SA LA GARONNE 为图卢兹及周边地区的地方政府与管网运营商新建、更新并修复这些管网，涵盖排水干管、住户接户管、检查井及附属构筑物。我们在在役管网、深基坑和大口径管道条件下施工，并始终坚持一条要求：施工期间保持管道通畅。"),
"Notre connaissance du sous-sol toulousain et de ses réseaux, souvent depuis leur construction, est un atout décisif pour anticiper les contraintes et sécuriser chaque phase.":
  ("Our knowledge of the Toulouse subsoil and its networks, often since they were first built, is a decisive advantage in anticipating constraints and securing every phase.",
   "我们对图卢兹地下环境及其管网的了解，往往可追溯至管网建成之初，这使我们能够预判制约因素并保障每个施工阶段的安全。"),
"Prestations": ("Services", "服务内容"),
"Ce que nous réalisons.": ("What we deliver.", "我们的施工能力。"),
"De la pose d'un collecteur neuf à la réhabilitation d'un ouvrage existant, nous couvrons l'ensemble des travaux d'assainissement.":
  ("From laying a new sewer main to rehabilitating an existing structure, we cover the full range of sewerage works.",
   "从新建排水干管到既有构筑物修复，我们覆盖排水工程的全部环节。"),
"Construction et renouvellement de collecteurs": ("Construction and renewal of sewer mains", "排水干管新建与更新"),
"Réseaux unitaires, eaux usées et eaux pluviales : terrassement, blindage, pose et raccordement, tous diamètres jusqu'à Ø 2000 mm.":
  ("Combined, foul and stormwater networks: earthworks, shoring, laying and connection, all diameters up to Ø 2000 mm.",
   "合流、污水与雨水管网：土方开挖、沟槽支护、管道敷设与连接，管径最大可达 Ø 2000 毫米。"),
"Branchements particuliers": ("Individual service connections", "住户接户管"),
"Création et renouvellement de branchements d'assainissement en centre-ville, y compris en secteur piéton ou à forte fréquentation.":
  ("Creation and renewal of sewer service connections in the city centre, including pedestrian and high-footfall areas.",
   "在市中心（含步行区及人流密集地段）新建与更新排水接户管。"),
"Regards et ouvrages annexes": ("Manholes and ancillary structures", "检查井与附属构筑物"),
"Regards de visite, chambres, déversoirs et ouvrages spéciaux : construction, mise à niveau et réhabilitation.":
  ("Inspection manholes, chambers, overflow structures and special works: construction, level adjustment and rehabilitation.",
   "检查井、井室、溢流构筑物及特殊构筑物的新建、调平与修复。"),
"Interventions sur réseaux en service": ("Work on live networks", "在役管网作业"),
"Maintien de l'écoulement pendant les travaux : pompage, dérivation provisoire et phasage adapté à l'exploitation.":
  ("Keeping the flow running during the works: pumping, temporary bypass and phasing tailored to operations.",
   "施工期间保持管道通畅：抽排、临时导流以及配合运营要求的分阶段施工。"),
"Réhabilitation d'ouvrages existants": ("Rehabilitation of existing structures", "既有构筑物修复"),
"Réhabilitation de collecteurs et de regards, par tranchée ouverte ou par techniques sans tranchée selon le diagnostic.":
  ("Rehabilitation of sewer mains and manholes, by open trench or trenchless techniques depending on the survey.",
   "根据检测结果，采用开挖或非开挖工艺修复排水干管与检查井。"),
"Contrôles et remise en état": ("Testing and reinstatement", "检验与路面恢复"),
"Essais d'étanchéité, inspection télévisée, remblaiement contrôlé et réfection de voirie à l'identique.":
  ("Tightness testing, CCTV inspection, controlled backfilling and like-for-like road reinstatement.",
   "密闭性试验、闭路电视检测、回填压实控制以及路面原样恢复。"),
"Tranchée d'assainissement en centre-ville de Toulouse": ("Sewer trench in central Toulouse", "图卢兹市中心排水沟槽施工"),
"Toulouse · centre-ville": ("Toulouse · city centre", "图卢兹 · 市中心"),
"Renouvellement de réseau en secteur piéton": ("Network renewal in a pedestrian area", "步行区管网更新"),
"Méthode": ("Method", "施工方法"),
"Quatre étapes, aucune approximation.": ("Four stages, no guesswork.", "四个阶段，毫不含糊。"),
"Chaque chantier d'assainissement suit une méthode éprouvée, du diagnostic à la remise en état de la voirie.":
  ("Every sewerage worksite follows a proven method, from survey to road reinstatement.",
   "每一个排水工程都遵循成熟的作业流程，从前期检测到路面恢复。"),
"Étape 01": ("Stage 01", "第 01 步"),
"Étape 02": ("Stage 02", "第 02 步"),
"Étape 03": ("Stage 03", "第 03 步"),
"Étape 04": ("Stage 04", "第 04 步"),
"Diagnostic et préparation": ("Survey and preparation", "检测与准备"),
"Inspection de l'existant, repérage des réseaux, déclarations réglementaires (DT-DICT), phasage et plan de circulation.":
  ("Inspection of existing works, utility locating, statutory notifications, phasing and traffic management plan.",
   "既有设施检查、地下管线探测、法定申报手续、分阶段方案与交通组织方案。"),
"Sécurisation de l'emprise": ("Securing the work area", "作业区安全布置"),
"Balisage, blindage de tranchée, gestion des flux piétons et véhicules, protection des riverains et des équipes.":
  ("Signage, trench shoring, management of pedestrian and vehicle flows, protection of residents and crews.",
   "警示围挡、沟槽支护、人车通行组织，保障周边居民与施工人员安全。"),
"Travaux": ("Works", "施工作业"),
"Terrassement, pose ou réhabilitation, raccordements et branchements — en maintenant l'écoulement du réseau.":
  ("Earthworks, laying or rehabilitation, connections and service laterals — while keeping the network flowing.",
   "土方开挖、管道敷设或修复、管道连接与接户管施工，全程保持管网通畅。"),
"Contrôles et réception": ("Testing and handover", "检验与验收"),
"Essais d'étanchéité, inspection télévisée, remblaiement contrôlé, réfection de voirie et dossier de récolement.":
  ("Tightness testing, CCTV inspection, controlled backfilling, road reinstatement and as-built documentation.",
   "密闭性试验、闭路电视检测、回填压实控制、路面恢复及竣工资料移交。"),
"Contraintes maîtrisées": ("Constraints under control", "可控的施工约束"),
"Le terrain, tel qu'il est.": ("The ground, as we find it.", "直面真实工况。"),
"Nous intervenons là où les conditions sont les plus exigeantes : hypercentre historique, réseaux anciens, nappes, trafic, riverains.":
  ("We work where conditions are most demanding: historic city centre, old networks, groundwater, traffic, residents.",
   "我们在最严苛的条件下作业：历史老城区、老旧管网、地下水、交通流量与周边居民。"),
"Tranchées profondes": ("Deep trenches", "深沟槽"),
"Hypercentre historique": ("Historic city centre", "历史老城核心区"),
"Secteurs piétons": ("Pedestrian areas", "步行区"),
"Coordination multi-réseaux": ("Multi-utility coordination", "多管线协调"),
"Présence de nappe": ("Groundwater present", "地下水位高"),
"Travaux de nuit possibles": ("Night work possible", "可夜间施工"),
"Repères techniques": ("Technical data", "技术参数"),
"Diamètre maximal posé": ("Maximum diameter laid", "最大敷设管径"),
"Profondeur de tranchée": ("Trench depth", "沟槽深度"),
"6 à 7 m": ("6 to 7 m", "6 至 7 米"),
"Types de réseaux": ("Network types", "管网类型"),
"Unitaire · EU · EP": ("Combined · foul · storm", "合流 · 污水 · 雨水"),
"Identifications FNTP": ("FNTP qualifications", "FNTP 资质"),
"Inspection": ("Inspection", "检测手段"),
"Robot RIC 4K 360° (brevet)": ("RIC robot, 4K 360° (patented)", "RIC 机器人 4K 360°（专利）"),
"Bureau d'études": ("Design office", "技术设计部"),
"Intégré · géomètre & chargé d'études": ("In-house · surveyor & design engineer", "内设 · 测量绘图员与技术工程师"),
"Zone d'intervention": ("Area of operation", "服务区域"),
"Toulouse Métropole & agglomération": ("Toulouse Métropole & surrounding area", "图卢兹都市区及周边"),
"Autres expertises": ("Other expertise", "其他专业领域"),
"Un savoir-faire complet sur les réseaux d'eau.": ("Complete know-how across water networks.", "覆盖给排水管网的完整能力。"),
"Un réseau à construire, entretenir ou réhabiliter ?": ("A network to build, maintain or rehabilitate?", "需要新建、维护或修复管网？"),
"Parlons de votre projet. Nos équipes vous répondent avec précision, sur la base de 70 ans de chantiers.":
  ("Let's talk about your project. Our teams give you precise answers, drawing on 70 years of worksites.",
   "欢迎与我们探讨您的项目。凭借 70 年的施工积累，我们的团队将给出精准答复。"),
})

# ---------------------------------------------------------------- Page Eau potable
add({
"Adduction d'eau potable à Toulouse — SA LA GARONNE": ("Drinking water supply in Toulouse — SA LA GARONNE", "图卢兹饮用水输配工程 — SA LA GARONNE"),
"Pose et renouvellement de conduites d'eau potable, branchements et ouvrages hydrauliques à Toulouse, avec coupures limitées. SA LA GARONNE, depuis 1956.":
  ("Laying and renewal of drinking water mains, service connections and hydraulic structures in Toulouse, with minimal shutdowns. SA LA GARONNE, since 1956.",
   "图卢兹饮用水管道敷设更新、接户管及水工构筑物施工，尽量减少停水。SA LA GARONNE，始于 1956 年。"),
"Raccordement de conduites d'eau potable en fonte dans une tranchée": ("Ductile iron drinking water mains being connected in a trench", "沟槽内球墨铸铁给水管道连接作业"),
"Expertise 02 / Eau potable": ("Expertise 02 / Drinking water", "专业领域 02 / 饮用水"),
"Poser, renouveler et raccorder les conduites qui acheminent l'eau potable — avec un objectif simple : un service continu et une eau préservée.":
  ("Laying, renewing and connecting the mains that carry drinking water — with one simple goal: uninterrupted service and water quality preserved.",
   "敷设、更新并连接输送饮用水的管道，目标简单明确：供水不中断，水质有保障。"),
"15 % de l'activité": ("15% of business", "占业务量 15%"),
"Adduction · distribution": ("Supply · distribution", "输水 · 配水"),
"Ouvrages": ("Structures", "构筑物"),
"Chambres · vannes · comptage": ("Chambers · valves · metering", "井室 · 阀门 · 计量"),
"Qualification": ("Qualification", "资质"),
"FNTP 5118 · AEP zone urbaine": ("FNTP 5118 · urban drinking water networks", "FNTP 5118 · 城区给水管网"),
"L'eau doit arriver. Chaque jour, à chaque robinet.": ("The water has to arrive. Every day, at every tap.", "水必须送达，每一天，每一个水龙头。"),
"Un réseau d'eau potable se juge à sa fiabilité. Renouveler une conduite ancienne, créer un branchement ou raccorder un nouveau quartier doit se faire sans dégrader la qualité de l'eau ni interrompre durablement le service.":
  ("A drinking water network is judged on its reliability. Renewing an old main, creating a service connection or connecting a new neighbourhood must be done without degrading water quality or interrupting service for long.",
   "饮用水管网的价值在于可靠性。更新旧管、新增接户管或接入新建小区，都必须在不影响水质、不长时间停水的前提下完成。"),
"SA LA GARONNE réalise la pose et le renouvellement de conduites d'adduction et de distribution, les branchements particuliers et les ouvrages hydrauliques associés. Nos équipes travaillent sur des réseaux exploités, en coordination étroite avec les exploitants, pour limiter les coupures et sécuriser chaque remise en eau.":
  ("SA LA GARONNE lays and renews supply and distribution mains, individual service connections and the associated hydraulic structures. Our crews work on networks in operation, in close coordination with the operators, to limit shutdowns and secure every return to service.",
   "SA LA GARONNE 承担输水与配水管道的敷设更新、住户接户管以及配套水工构筑物施工。我们的班组在管网运行状态下作业，与运营方紧密配合，尽量减少停水并确保每一次恢复通水安全可靠。"),
"Désinfection, essais de pression, contrôles de qualité : la mise en service est une étape à part entière, que nous traitons avec la même rigueur que la pose.":
  ("Disinfection, pressure testing, quality checks: commissioning is a stage in its own right, which we treat with the same rigour as the laying itself.",
   "消毒、压力试验、水质检测：通水验收本身就是一道独立工序，我们以与管道敷设同等的严谨对待。"),
"De la conduite structurante au branchement individuel, nous intervenons sur l'ensemble du réseau d'eau potable.":
  ("From trunk mains to individual service connections, we work across the whole drinking water network.",
   "从主干管道到住户接户管，我们覆盖饮用水管网的各个环节。"),
"Pose et renouvellement de conduites": ("Laying and renewal of mains", "管道敷设与更新"),
"Conduites d'adduction et de distribution, tous matériaux courants (fonte ductile, PEHD…), en tranchée ouverte ou par techniques adaptées.":
  ("Supply and distribution mains, in all common materials (ductile iron, HDPE and others), by open trench or suitable techniques.",
   "输水与配水管道，适配各类常用材质（球墨铸铁、高密度聚乙烯等），可采用开挖或其他适配工艺。"),
"Création, renouvellement et reprise de branchements d'eau potable, en centre-ville comme en zone périurbaine.":
  ("Creation, renewal and repair of drinking water service connections, in the city centre and in outlying areas.",
   "在市中心及城郊新建、更新与改造饮用水接户管。"),
"Ouvrages hydrauliques": ("Hydraulic structures", "水工构筑物"),
"Chambres de vannes, regards de comptage, dispositifs de sectorisation, ventouses et vidanges.":
  ("Valve chambers, metering manholes, district metering equipment, air valves and washouts.",
   "阀门井、计量井、分区计量装置、排气阀与排泥阀。"),
"Raccordements sur réseaux exploités": ("Connections on networks in operation", "运行管网上的接驳"),
"Interventions planifiées avec l'exploitant pour réduire au strict nécessaire la durée et le périmètre des coupures.":
  ("Operations planned with the network operator to keep the duration and scope of shutdowns to a strict minimum.",
   "与运营方共同排定作业计划，将停水时间与影响范围压缩到最低限度。"),
"Essais et désinfection": ("Testing and disinfection", "试验与消毒"),
"Essais de pression, rinçage, désinfection et analyses avant remise en service.":
  ("Pressure testing, flushing, disinfection and analysis before returning to service.",
   "通水前进行压力试验、冲洗、消毒与水质化验。"),
"Réfection et remise en état": ("Reinstatement", "路面与场地恢复"),
"Remblaiement contrôlé, réfection de voirie et de trottoirs à l'identique, dossier de récolement.":
  ("Controlled backfilling, like-for-like reinstatement of roads and pavements, as-built documentation.",
   "回填压实控制、车行道与人行道原样恢复、竣工资料移交。"),
"Engins SA LA GARONNE en intervention en hypercentre de Toulouse": ("SA LA GARONNE plant at work in central Toulouse", "SA LA GARONNE 施工机械在图卢兹核心城区作业"),
"Toulouse · hypercentre": ("Toulouse · city centre", "图卢兹 · 核心城区"),
"Intervenir sans interrompre la ville": ("Working without bringing the city to a halt", "施工不打断城市运转"),
"Une remise en eau préparée dès le premier jour.": ("A return to service prepared from day one.", "从开工第一天就为通水做准备。"),
"La qualité de l'eau et la continuité du service guident chaque phase du chantier.":
  ("Water quality and continuity of service guide every phase of the worksite.",
   "水质与供水连续性贯穿施工的每个阶段。"),
"Préparation et coordination": ("Preparation and coordination", "准备与协调"),
"Repérage des réseaux, déclarations réglementaires, phasage des coupures avec l'exploitant, information des riverains.":
  ("Utility locating, statutory notifications, shutdown phasing agreed with the operator, resident information.",
   "地下管线探测、法定申报、与运营方商定停水安排、向周边居民发布通知。"),
"Sécurisation": ("Safety measures", "安全防护"),
"Balisage, blindage, gestion des accès et des flux, protection des conduites voisines et des équipes.":
  ("Signage, shoring, access and flow management, protection of neighbouring mains and crews.",
   "警示围挡、沟槽支护、出入与通行组织、保护邻近管道与施工人员。"),
"Pose et raccordement": ("Laying and connection", "敷设与接驳"),
"Terrassement, lit de pose, assemblage des conduites, raccordement des branchements et des ouvrages.":
  ("Earthworks, pipe bedding, pipe assembly, connection of service laterals and structures.",
   "土方开挖、管道垫层、管节组装、接户管与构筑物接驳。"),
"Essais et mise en service": ("Testing and commissioning", "试验与通水"),
"Essais de pression, désinfection, analyses, remise en eau progressive et réfection de voirie.":
  ("Pressure testing, disinfection, analysis, gradual return to service and road reinstatement.",
   "压力试验、消毒、水质化验、逐步恢复通水以及路面恢复。"),
"Un réseau sous pression, une ville en activité.": ("A pressurised network, a city going about its business.", "带压运行的管网，正常运转的城市。"),
"Nous concilions les exigences sanitaires de l'eau potable et celles d'un chantier urbain.":
  ("We reconcile drinking water health requirements with the demands of an urban worksite.",
   "我们兼顾饮用水的卫生要求与城市施工的现实约束。"),
"Réseaux exploités": ("Networks in operation", "运行中的管网"),
"Coupures minimisées": ("Shutdowns minimised", "停水最小化"),
"Coordination exploitant": ("Coordination with operator", "与运营方协同"),
"Centre-ville": ("City centre", "市中心"),
"Multi-réseaux": ("Multi-utility", "多管线并存"),
"Qualité sanitaire": ("Health and water quality", "卫生与水质"),
"Réfection à l'identique": ("Like-for-like reinstatement", "原样恢复"),
"Matériaux": ("Materials", "管材"),
"Fonte ductile · PEHD · acier": ("Ductile iron · HDPE · steel", "球墨铸铁 · 高密度聚乙烯 · 钢管"),
"Identification FNTP": ("FNTP qualification", "FNTP 资质"),
"5118 · réseaux AEP en zone urbaine": ("5118 · urban drinking water networks", "5118 · 城区给水管网"),
"Mise en service": ("Commissioning", "通水验收"),
"Essais · désinfection · analyses": ("Testing · disinfection · analysis", "试验 · 消毒 · 化验"),
"Intégré · plans d'exécution & récolement": ("In-house · construction & as-built drawings", "内设 · 施工图与竣工图"),
})

# ---------------------------------------------------------------- Page Réhabilitation sans tranchée
add({
"Réhabilitation sans tranchée à Toulouse — SA LA GARONNE": ("Trenchless rehabilitation in Toulouse — SA LA GARONNE", "图卢兹非开挖修复工程 — SA LA GARONNE"),
"Chemisage, gainage, fraisage robotisé et inspection par robot RIC : rénover les canalisations sans ouvrir la voirie. SA LA GARONNE, Toulouse.":
  ("CIPP lining, sleeving, robotic milling and RIC robot inspection: renovating pipes without opening the road. SA LA GARONNE, Toulouse.",
   "原位固化内衬、内衬修复、机器人铣削与 RIC 机器人检测：无需开挖路面即可修复管道。SA LA GARONNE，图卢兹。"),
"Unités mobiles SA LA GARONNE en intervention en hypercentre": ("SA LA GARONNE mobile units at work in the city centre", "SA LA GARONNE 移动作业车在核心城区施工"),
"Expertise 03 / Sans tranchée": ("Expertise 03 / Trenchless", "专业领域 03 / 非开挖"),
"Rénover les réseaux existants depuis l'intérieur : chemisage, gainage, fraisage et interventions robotisées. Moins d'ouverture de voirie, des délais réduits, des nuisances limitées.":
  ("Renovating existing networks from the inside: CIPP lining, sleeving, milling and robotic operations. Less road opening, shorter schedules, limited disruption.",
   "从管道内部修复既有管网：原位固化内衬、内衬修复、铣削与机器人作业。开挖更少、工期更短、干扰更小。"),
"10 % de l'activité": ("10% of business", "占业务量 10%"),
"Procédés": ("Processes", "工艺"),
"Chemisage · gainage · fraisage": ("CIPP lining · sleeving · milling", "原位固化内衬 · 内衬修复 · 铣削"),
"Robotique": ("Robotics", "机器人技术"),
"RIC 4K 360° · brevet 2018": ("RIC 4K 360° · patented 2018", "RIC 4K 360° · 2018 年专利"),
"FNTP 5221 · réseaux visitables": ("FNTP 5221 · man-entry networks", "FNTP 5221 · 可通行管道"),
"Voirie": ("Roadway", "路面"),
"Non ouverte": ("Not opened", "无需开挖"),
"Une conduite neuve dans l'ancienne. Sans ouvrir la rue.": ("A new pipe inside the old one. Without opening the street.", "在旧管中形成新管，无需开挖街道。"),
"Renouveler un réseau enterré en tranchée ouverte signifie ouvrir la chaussée, dévier la circulation, immobiliser un quartier pendant des semaines. La réhabilitation sans tranchée apporte une alternative : rénover la conduite depuis l'intérieur, à partir des regards existants.":
  ("Renewing a buried network by open trench means opening the road, diverting traffic and immobilising a neighbourhood for weeks. Trenchless rehabilitation offers an alternative: renovating the pipe from the inside, working from the existing manholes.",
   "采用开挖方式更新地下管网，意味着破除路面、改道交通，让整个街区停摆数周。非开挖修复提供了另一条路径：从既有检查井进入，在管道内部完成修复。"),
"SA LA GARONNE a fait de ces techniques un axe différenciant de son savoir-faire. Chemisage continu, gainage, fraisage robotisé, réparations ponctuelles : nos équipes et nos unités mobiles interviennent sur des réseaux en service, en centre-ville dense comme en zone périurbaine.":
  ("SA LA GARONNE has made these techniques a distinctive part of its know-how. Continuous CIPP lining, sleeving, robotic milling, spot repairs: our crews and mobile units work on live networks, in the dense city centre as well as in outlying areas.",
   "SA LA GARONNE 将这些技术打造为自身的差异化优势。连续原位固化内衬、内衬修复、机器人铣削、局部修补：我们的班组与移动作业车可在在役管网上施工，既适用于密集市中心，也适用于城郊区域。"),
"Le résultat : une conduite structurellement neuve, une durée de vie prolongée de plusieurs décennies, un chantier plus court et une voirie préservée.":
  ("The result: a structurally new pipe, a service life extended by several decades, a shorter worksite and a road left intact.",
   "最终成效：结构上焕然一新的管道、延长数十年的使用寿命、更短的工期以及完好无损的路面。"),
"Le procédé, étape par étape": ("The process, step by step", "工艺流程详解"),
"Étudier votre réseau avec nous": ("Assess your network with us", "与我们一同评估您的管网"),
"Techniques": ("Techniques", "技术工艺"),
"Les procédés que nous mettons en œuvre.": ("The processes we deploy.", "我们采用的工艺。"),
"Chaque réseau est différent : le diagnostic détermine la technique la plus adaptée à l'état de la conduite et aux contraintes du site.":
  ("Every network is different: the survey determines the technique best suited to the pipe's condition and the site constraints.",
   "每条管网各不相同：检测结果决定最适合管道状况与现场条件的工艺。"),
"Inspection télévisée et diagnostic": ("CCTV inspection and survey", "闭路电视检测与诊断"),
"Passage caméra — dont le RIC, robot de télé-visualisation 4K à 360° breveté par La Garonne — relevé des défauts, mesure des ovalisations et des contre-pentes.":
  ("Camera survey — including the RIC, La Garonne's patented 4K 360° inspection robot — recording defects and measuring ovalisation and adverse gradients.",
   "摄像检测（含 La Garonne 自主研发并获专利的 RIC 4K 360° 检测机器人），记录缺陷并测量管道变形与倒坡。"),
"Hydrocurage et préparation": ("High-pressure jetting and preparation", "高压水射流清洗与预处理"),
"Nettoyage haute pression de la conduite, élimination des dépôts, préparation de la surface avant chemisage.":
  ("High-pressure cleaning of the pipe, removal of deposits, surface preparation before lining.",
   "高压清洗管道内壁、清除沉积物，为内衬施工做好基面处理。"),
"Suppression des obstacles (racines, concrétions, branchements pénétrants) par robot fraiseur piloté depuis la surface.":
  ("Removal of obstructions (roots, encrustation, intruding connections) by a milling robot operated from the surface.",
   "由地面遥控铣削机器人清除障碍物（树根、结垢、伸入管内的接户管）。"),
"Chemisage continu": ("Continuous CIPP lining", "连续原位固化内衬"),
"Gaine imprégnée de résine, mise en place et polymérisée en place : une conduite neuve, continue et étanche, dans l'existante.":
  ("A resin-impregnated liner, installed and cured in place: a new, continuous and watertight pipe inside the existing one.",
   "树脂浸渍软管就位后原位固化：在既有管道内形成一条连续、密闭的新管。"),
"Gainage partiel et manchettes": ("Partial lining and sleeves", "局部内衬与套管修补"),
"Réparation localisée d'un tronçon ou d'un raccord par manchette ou chemisage court, sans intervention sur l'ensemble du linéaire.":
  ("Localised repair of a section or joint using a sleeve or short liner, without treating the whole length.",
   "采用套管或短管内衬对局部管段或接口进行修补，无需处理整条管线。"),
"Réouverture des branchements": ("Reopening of service connections", "接户管重新开孔"),
"Réouverture robotisée des branchements après chemisage, reprise des raccords et contrôle d'étanchéité.":
  ("Robotic reopening of service connections after lining, reworking of joints and tightness testing.",
   "内衬完成后由机器人重新开通接户管口、处理接口并进行密闭性检验。"),
"Bénéfices": ("Benefits", "工艺优势"),
"Ce que la ville y gagne.": ("What the city gains.", "城市从中受益。"),
"Voirie préservée": ("Road left intact", "路面完好"),
"Pas de tranchée sur le linéaire : la chaussée, les trottoirs et les réseaux voisins restent intacts.":
  ("No trench along the route: the road, the pavements and the neighbouring utilities stay intact.",
   "管线沿线无需开挖：车行道、人行道与邻近管线均保持完好。"),
"Délais réduits": ("Shorter schedules", "工期缩短"),
"Des interventions à l'échelle de la journée ou de la semaine, là où une tranchée ouverte se compte en mois.":
  ("Operations measured in days or weeks, where an open trench would be measured in months.",
   "作业以天或周计，而开挖施工往往需要数月。"),
"Nuisances limitées": ("Limited disruption", "干扰有限"),
"Moins de bruit, de poussière et de déviations pour les riverains, les commerces et la circulation.":
  ("Less noise, dust and traffic diversion for residents, businesses and road users.",
   "对周边居民、商户与交通的噪声、扬尘和改道影响更小。"),
"Une conduite structurellement renforcée, étanche, pour plusieurs décennies de service supplémentaires.":
  ("A structurally reinforced, watertight pipe, good for several more decades of service.",
   "结构得到加固且密闭的管道，可再服役数十年。"),
"Coût global maîtrisé": ("Controlled overall cost", "综合成本可控"),
"Moins de terrassement, de remblais et de réfection : un budget optimisé pour la collectivité.":
  ("Less excavation, backfilling and reinstatement: an optimised budget for the local authority.",
   "土方、回填与路面恢复量大幅减少，为地方政府优化预算。"),
"Champ d'intervention": ("Scope of work", "适用范围"),
"Des réseaux de toutes tailles, dans tous les contextes.": ("Networks of every size, in every setting.", "适配各种口径与各类工况的管网。"),
"Collecteurs, branchements, ouvrages : nous adaptons la technique au diamètre, au matériau et à l'état de la conduite.":
  ("Sewer mains, service connections, structures: we match the technique to the diameter, the material and the condition of the pipe.",
   "排水干管、接户管、构筑物：我们根据管径、管材与管道状况选择相应工艺。"),
"Centre-ville dense": ("Dense city centre", "密集市中心"),
"Collecteurs visitables": ("Man-entry sewers", "可通行排水干管"),
"Conduites non visitables": ("Non man-entry pipes", "不可通行管道"),
"Branchements": ("Service connections", "接户管"),
"Regards et ouvrages": ("Manholes and structures", "检查井与构筑物"),
"Interventions robotisées": ("Robotic operations", "机器人作业"),
"Diagnostic": ("Survey", "检测"),
"Inspection télévisée · robot RIC 4K 360°": ("CCTV inspection · RIC 4K 360° robot", "闭路电视检测 · RIC 4K 360° 机器人"),
"Réseaux inspectés": ("Networks inspected", "已检测管网"),
"+ de 120 km à Toulouse": ("over 120 km in Toulouse", "图卢兹超 120 公里"),
"Chemisage · gainage · manchettes": ("CIPP lining · sleeving · sleeves", "原位固化内衬 · 内衬修复 · 套管修补"),
"Préparation": ("Preparation", "预处理"),
"Hydrocurage · fraisage robotisé": ("High-pressure jetting · robotic milling", "高压清洗 · 机器人铣削"),
"5221 · réhabilitation de réseaux visitables": ("5221 · rehabilitation of man-entry networks", "5221 · 可通行管道修复"),
"Non ouverte sur le linéaire": ("Not opened along the route", "沿线无需开挖"),
})

# ---------------------------------------------------------------- Page Travaux complexes
add({
"Travaux de réseaux complexes à Toulouse — SA LA GARONNE": ("Complex network works in Toulouse — SA LA GARONNE", "图卢兹复杂管网工程 — SA LA GARONNE"),
"Réseaux en service, tranchées jusqu'à 7 m, canalisations Ø 2000 mm, hypercentre : des chantiers contraints maîtrisés par SA LA GARONNE à Toulouse.":
  ("Live networks, trenches up to 7 m, Ø 2000 mm pipes, city centre: constrained worksites mastered by SA LA GARONNE in Toulouse.",
   "在役管网、7 米深沟槽、Ø 2000 毫米管道、核心城区：SA LA GARONNE 在图卢兹驾驭各类受限工程。"),
"Tranchée blindée SA LA GARONNE devant le monument aux morts de Toulouse": ("SA LA GARONNE shored trench in front of the Toulouse war memorial", "SA LA GARONNE 在图卢兹阵亡将士纪念碑前的支护沟槽"),
"Expertise 04 / Travaux & interventions complexes": ("Expertise 04 / Complex works and operations", "专业领域 04 / 复杂工程与作业"),
"Réseaux en service, tranchées à grande profondeur, canalisations de grand diamètre, secteurs très fréquentés : des chantiers où la méthode fait la différence.":
  ("Live networks, deep trenches, large-diameter pipes, busy areas: worksites where method makes the difference.",
   "在役管网、深沟槽、大口径管道、人流密集区域：施工方法决定成败的工程。"),
"Diamètre": ("Diameter", "管径"),
"FNTP 5141 · 5161": ("FNTP 5141 · 5161", "FNTP 5141 · 5161"),
"Contexte": ("Setting", "施工环境"),
"Hypercentre · secteurs sensibles": ("City centre · sensitive areas", "核心城区 · 敏感区域"),
"Plus le chantier est contraint, plus la préparation compte.": ("The tighter the constraints, the more preparation counts.", "工况越受限，前期准备越关键。"),
"Un collecteur à sept mètres de profondeur sous une rue commerçante. Une canalisation de deux mètres de diamètre à renouveler sans interrompre le réseau. Une intervention au pied d'un monument, sous les yeux des riverains et des touristes. Ce sont les chantiers pour lesquels SA LA GARONNE est sollicitée.":
  ("A sewer seven metres down beneath a shopping street. A two-metre-diameter pipe to be renewed without interrupting the network. An operation at the foot of a monument, under the eyes of residents and tourists. These are the worksites SA LA GARONNE is called in for.",
   "商业街下方七米深的排水干管；需要在不中断管网的情况下更新的两米口径管道；在纪念碑脚下、居民与游客注视下的施工作业。这些正是客户找到 SA LA GARONNE 的原因。"),
"Notre valeur ajoutée tient dans la préparation : études d'exécution, phasage précis, blindages adaptés, logistique urbaine, coordination avec les exploitants et les services de la ville. Sur le terrain, des équipes expérimentées et un matériel dimensionné pour ces conditions.":
  ("Our added value lies in preparation: construction studies, precise phasing, suitable shoring, urban logistics, coordination with operators and city departments. On site, experienced crews and plant sized for these conditions.",
   "我们的价值体现在准备工作上：施工深化设计、精细分阶段方案、适配的支护体系、城市物流组织，以及与运营方和市政部门的协调。在现场，则是经验丰富的班组与匹配工况的装备。"),
"Sécurité des équipes, continuité de service, respect des délais : sur un chantier complexe, ces trois exigences ne se négocient jamais.":
  ("Crew safety, continuity of service, schedule compliance: on a complex worksite, these three requirements are never negotiable.",
   "人员安全、服务不中断、按期交付：在复杂工程中，这三项要求没有商量余地。"),
"Situations": ("Situations", "典型工况"),
"Ce que nous savons faire.": ("What we know how to do.", "我们的专长。"),
"Les configurations pour lesquelles nos équipes sont spécifiquement équipées et formées.":
  ("The configurations our crews are specifically equipped and trained for.",
   "我们的团队针对这些工况配备了专门装备并接受过专项培训。"),
"Intervenir sur un réseau exploité sans interrompre l'écoulement ou la distribution : pompage, dérivation, phasage par tronçon.":
  ("Working on a network in operation without interrupting flow or distribution: pumping, bypass, section-by-section phasing.",
   "在管网运行状态下作业而不中断排水或供水：抽排、导流、按管段分阶段推进。"),
"Tranchées de 6 à 7 mètres avec blindage adapté, gestion des venues d'eau et sécurisation des abords.":
  ("Trenches 6 to 7 metres deep with suitable shoring, management of water ingress and securing of the surroundings.",
   "6 至 7 米深沟槽配备适配支护，处理涌水并做好周边安全防护。"),
"Pose et renouvellement de canalisations jusqu'à Ø 2000 mm : levage, calage, assemblage et contrôles spécifiques.":
  ("Laying and renewal of pipes up to Ø 2000 mm: lifting, bedding, assembly and dedicated checks.",
   "敷设与更新管径达 Ø 2000 毫米的管道：吊装、找平、组装及专项检验。"),
"Hypercentre, zones piétonnes, abords d'équipements publics : emprises réduites, phasage fin, information des riverains.":
  ("City centre, pedestrian zones, around public facilities: reduced footprint, fine phasing, resident information.",
   "核心城区、步行区、公共设施周边：缩小占地、精细分期、及时向居民通报。"),
"Coordination multi-réseaux": ("Multi-utility coordination", "多管线协调"),
"Chantiers en présence de réseaux concessionnaires denses : repérage, protection, dévoiements et coordination des intervenants.":
  ("Worksites amid dense utility networks: locating, protection, diversions and coordination of all parties.",
   "在管线密集区域施工：探测定位、保护、改迁以及各参建方协调。"),
"Chantiers à fortes contraintes de délai": ("Worksites under tight deadlines", "工期高度受限的工程"),
"Travaux de nuit, phases courtes, interventions planifiées autour d'événements ou de contraintes d'exploitation.":
  ("Night work, short phases, operations planned around events or operating constraints.",
   "夜间施工、短周期分期、围绕活动安排或运营要求排定作业。"),
"Équipe SA LA GARONNE en intervention sur réseau en service en centre-ville": ("SA LA GARONNE crew working on a live network in the city centre", "SA LA GARONNE 班组在市中心对在役管网作业"),
"Toulouse · réseau en service": ("Toulouse · live network", "图卢兹 · 在役管网"),
"Continuité de service, quelles que soient les conditions": ("Continuity of service, whatever the conditions", "无论工况如何，服务不中断"),
"Préparer, sécuriser, exécuter, contrôler.": ("Prepare, secure, execute, verify.", "准备、防护、施工、检验。"),
"Une méthode unique appliquée à chaque chantier complexe, quelle que soit sa taille.":
  ("A single method applied to every complex worksite, whatever its size.",
   "无论规模大小，每个复杂工程都遵循同一套方法。"),
"Études et phasage": ("Studies and phasing", "深化设计与分期"),
"Analyse des contraintes, études d'exécution, phasage détaillé, plan de circulation et plan de prévention.":
  ("Constraint analysis, construction studies, detailed phasing, traffic management plan and safety plan.",
   "约束条件分析、施工深化设计、详细分期方案、交通组织方案与安全防护方案。"),
"Blindages dimensionnés, balisage, gestion des accès et des flux, protection des ouvrages voisins et des équipes.":
  ("Engineered shoring, signage, access and flow management, protection of neighbouring structures and crews.",
   "经计算的支护体系、警示围挡、出入与通行组织、保护邻近构筑物与施工人员。"),
"Exécution": ("Execution", "施工实施"),
"Équipes expérimentées et matériel adapté : terrassement profond, levage, pose grand diamètre, réseaux en service.":
  ("Experienced crews and suitable plant: deep excavation, lifting, large-diameter laying, live networks.",
   "经验丰富的班组与适配装备：深基坑开挖、吊装、大口径敷设、在役管网作业。"),
"Essais, inspections, remblaiement contrôlé, réfection à l'identique et dossier de récolement complet.":
  ("Testing, inspections, controlled backfilling, like-for-like reinstatement and complete as-built documentation.",
   "试验、检测、回填压实控制、原样恢复以及完整的竣工资料。"),
"Moyens": ("Resources", "资源配置"),
"Des équipes et un matériel dimensionnés.": ("Crews and plant sized for the job.", "与工程相匹配的团队与装备。"),
"35 collaborateurs, un parc matériel dédié et 70 ans de chantiers sur l'agglomération toulousaine.":
  ("35 employees, a dedicated plant fleet and 70 years of worksites across the Toulouse metropolitan area.",
   "35 名员工、专属设备机队，以及在图卢兹地区 70 年的施工积累。"),
"4 équipes de chantier": ("4 site crews", "4 支施工班组"),
"Encadrement expérimenté": ("Experienced supervision", "经验丰富的管理层"),
"Géomètre-dessinateur": ("Surveyor-draughtsman", "测量绘图员"),
"Blindages de tranchée": ("Trench shoring", "沟槽支护体系"),
"Engins de terrassement": ("Earthmoving plant", "土方机械"),
"Unités d'hydrocurage": ("Jetting units", "高压清洗车"),
"Robot d'inspection RIC": ("RIC inspection robot", "RIC 检测机器人"),
"Matériel de réhabilitation robotisée": ("Robotic rehabilitation equipment", "机器人修复设备"),
"Atelier intégré": ("In-house workshop", "内设机修车间"),
"Diamètre maximal": ("Maximum diameter", "最大管径"),
})

# ---------------------------------------------------------------- Page Entreprise
add({
"L'entreprise — SA LA GARONNE, Toulouse depuis 1956": ("The company — SA LA GARONNE, Toulouse since 1956", "关于我们 — SA LA GARONNE，图卢兹，始于 1956 年"),
"Trois générations Pascual, 35 collaborateurs, bureau d'études intégré et robot d'inspection breveté : l'histoire et les valeurs de SA LA GARONNE.":
  ("Three Pascual generations, 35 employees, an in-house design office and a patented inspection robot: the story and values of SA LA GARONNE.",
   "帕斯夸尔家族三代传承、35 名员工、内设技术设计部与获专利的检测机器人：SA LA GARONNE 的历史与价值观。"),
"Équipe SA LA GARONNE réunie autour d'une inspection vidéo de réseau": ("SA LA GARONNE team gathered around a network video inspection", "SA LA GARONNE 团队围绕管网视频检测开展讨论"),
"Une entreprise familiale toulousaine, depuis 1956.": ("A family business from Toulouse, since 1956.", "扎根图卢兹的家族企业，始于 1956 年。"),
"Trois générations de la famille Pascual, près de 70 ans de chantiers sur l'agglomération toulousaine, 35 collaborateurs et une conviction : les réseaux d'eau méritent des spécialistes.":
  ("Three generations of the Pascual family, nearly 70 years of worksites across the Toulouse area, 35 employees and one conviction: water networks deserve specialists.",
   "帕斯夸尔家族三代人、近 70 年扎根图卢兹地区的施工历程、35 名员工，以及一个信念：给排水管网值得交给专业的人。"),
"Création": ("Founded", "创立"),
"Direction": ("Management", "管理层"),
"Nicolas Pascual · 3e génération": ("Nicolas Pascual · 3rd generation", "Nicolas Pascual · 第三代"),
"4 équipes · atelier · bureau d'études": ("4 crews · workshop · design office", "4 支班组 · 机修车间 · 技术设计部"),
"Qui nous sommes": ("Who we are", "我们是谁"),
"Le métier de l'eau, et rien d'autre.": ("The water trade, and nothing else.", "专注水务，别无其他。"),
"SA LA GARONNE est une PME familiale de travaux publics fondée à Toulouse le 13 janvier 1956 par Eloy Pascual. Michel Pascual lui succède en 1987, puis Nicolas Pascual en 2017 : trois générations à la tête d'une entreprise concentrée, depuis l'origine, sur un seul domaine — les réseaux d'eau et d'assainissement.":
  ("SA LA GARONNE is a family-owned civil engineering company founded in Toulouse on 13 January 1956 by Eloy Pascual. Michel Pascual took over in 1987, then Nicolas Pascual in 2017: three generations at the head of a company focused, from the outset, on a single field — water and sewer networks.",
   "SA LA GARONNE 是一家家族市政工程企业，由 Eloy Pascual 于 1956 年 1 月 13 日在图卢兹创立。1987 年 Michel Pascual 接掌公司，2017 年 Nicolas Pascual 继任：三代人执掌的企业，自创立之初便专注于同一个领域——给排水管网。"),
"Cette spécialisation nous a permis de développer une expertise reconnue sur les chantiers urbains les plus contraints, d'investir tôt dans la réhabilitation sans tranchée et de concevoir nos propres outils, comme le RIC, robot d'inspection breveté en 2018.":
  ("This specialisation has allowed us to build recognised expertise on the most constrained urban worksites, to invest early in trenchless rehabilitation and to design our own tools, such as the RIC inspection robot, patented in 2018.",
   "这种专注让我们在最受限的城市工程中积累了公认的专业能力，较早投入非开挖修复技术，并自主研发装备，例如 2018 年获专利的 RIC 检测机器人。"),
"Aujourd'hui, 35 collaborateurs répartis en quatre équipes de chantier, un atelier et un bureau d'études portent cette exigence au quotidien, pour les collectivités, les exploitants et les acteurs du cycle de l'eau. L'activité se répartit entre assainissement (75 %), eau potable (15 %) et réhabilitation sans tranchée (10 %).":
  ("Today, 35 employees split across four site crews, a workshop and a design office uphold that standard every day for local authorities, network operators and water sector players. Activity breaks down into sewerage (75%), drinking water (15%) and trenchless rehabilitation (10%).",
   "如今，35 名员工分布于四支施工班组、一个机修车间和一个技术设计部，每天为地方政府、管网运营商及水务行业各方践行这一标准。业务构成为：排水管网 75%、饮用水 15%、非开挖修复 10%。"),
"Repères": ("Milestones", "发展历程"),
"70 ans d'histoire, une trajectoire cohérente.": ("70 years of history, one consistent path.", "70 年历史，一条清晰的发展主线。"),
"Fondation": ("Founding", "公司创立"),
"Eloy Pascual crée La Garonne": ("Eloy Pascual founds La Garonne", "Eloy Pascual 创立 La Garonne"),
"La société est constituée à Toulouse le 13 janvier 1956, sous forme de SARL, pour répondre aux besoins de la ville en réseaux d'eau et d'assainissement.":
  ("The company is incorporated in Toulouse on 13 January 1956 to meet the city's needs in water and sewer networks.",
   "公司于 1956 年 1 月 13 日在图卢兹注册成立，以满足城市对给排水管网建设的需求。"),
"Deuxième génération": ("Second generation", "第二代"),
"Michel Pascual prend la direction": ("Michel Pascual takes over", "Michel Pascual 接掌公司"),
"Le fils du fondateur reprend l'entreprise et consolide son ancrage sur l'agglomération toulousaine : chantiers urbains, grande profondeur, grand diamètre.":
  ("The founder's son takes over the company and strengthens its footing across the Toulouse area: urban worksites, deep excavation, large diameters.",
   "创始人之子接手企业，进一步巩固其在图卢兹地区的根基：城市工程、深基坑、大口径管道。"),
"Troisième génération": ("Third generation", "第三代"),
"Nicolas Pascual succède à son père": ("Nicolas Pascual succeeds his father", "Nicolas Pascual 接替其父"),
"Troisième génération à la tête de l'entreprise familiale. Cette longévité nourrit une relation de confiance avec les acteurs de l'eau du secteur toulousain.":
  ("Third generation at the head of the family business. That continuity sustains a relationship of trust with water sector players in the Toulouse area.",
   "家族企业迎来第三代掌门人。长期的延续性使公司与图卢兹地区水务各方建立了牢固的信任关系。"),
"Innovation": ("Innovation", "技术创新"),
"Le RIC, robot d'inspection breveté": ("The RIC, a patented inspection robot", "RIC，获专利的检测机器人"),
"La Garonne développe et brevète le RIC, robot de télé-visualisation des ouvrages d'assainissement en 4K et à 360°. Plus de 120 km de réseaux inspectés depuis sur la commune de Toulouse.":
  ("La Garonne develops and patents the RIC, a 4K 360° remote inspection robot for sewer structures. Over 120 km of networks have been inspected with it in Toulouse since.",
   "La Garonne 自主研发并申请专利的 RIC，是一款用于排水构筑物的 4K 360° 远程视像检测机器人。此后已在图卢兹检测管网超过 120 公里。"),
"Responsabilité": ("Responsibility", "社会责任"),
"Certification RSE, puis label Engagé RSE d'AFNOR": ("CSR certification, then AFNOR's Engagé RSE label", "企业社会责任认证，随后获 AFNOR「Engagé RSE」标识"),
"Portée par la responsable QHSE, la démarche RSE est certifiée en juin 2022 et labellisée Engagé RSE par AFNOR en mai 2023. Un comité RSE fixe et évalue des objectifs chaque année.":
  ("Led by the QHSE manager, the CSR programme was certified in June 2022 and awarded AFNOR's Engagé RSE label in May 2023. A CSR committee sets and reviews objectives each year.",
   "在质量健康安全环境（QHSE）负责人的推动下，企业社会责任体系于 2022 年 6 月通过认证，并于 2023 年 5 月获得 AFNOR「Engagé RSE」标识。企业社会责任委员会每年制定并评估目标。"),
"70 ans": ("70 years", "70 周年"),
"Une marque technique, fiable et en mouvement": ("A technical brand, reliable and moving forward", "技术过硬、值得信赖、持续前行的品牌"),
"35 collaborateurs, quatre équipes de chantier, un atelier, un bureau d'études intégré et une identité renouvelée : l'entreprise aborde ses 70 ans en référence des réseaux d'eau sur son territoire.":
  ("35 employees, four site crews, a workshop, an in-house design office and a refreshed identity: the company approaches its 70th year as the local benchmark in water networks.",
   "35 名员工、四支施工班组、一个机修车间、内设技术设计部以及全新的品牌形象：公司以本地给排水管网标杆的姿态迎接 70 周年。"),
"Ingénierie intégrée": ("In-house engineering", "内部工程能力"),
"Un bureau d'études dans l'entreprise.": ("A design office within the company.", "企业内部设有技术设计部。"),
"Géomètre-dessinateur et chargé d'études travaillent en interne, de la réponse aux appels d'offres jusqu'au récolement. Une plus-value rare pour une entreprise de 35 personnes.":
  ("A surveyor-draughtsman and a design engineer work in-house, from tender response through to as-built records. A rare asset for a 35-strong company.",
   "测量绘图员与技术工程师均为内部编制，从投标响应一直负责到竣工资料。对一家 35 人的企业而言，这是难得的优势。"),
"Étudier, lever, dessiner, contrôler.": ("Study, survey, draw, verify.", "研究、测量、绘图、复核。"),
"Études de prix et mémoires techniques": ("Cost studies and technical bids", "报价测算与技术标书"),
"Une réponse précise aux consultations : variantes, phasages et méthodes argumentés.":
  ("A precise response to tenders: reasoned alternatives, phasing and methods.",
   "对招标作出精准响应：论证充分的替代方案、分期安排与施工方法。"),
"Une réponse précise aux appels d'offres : variantes, phasages et méthodes argumentés.":
  ("A precise response to tenders: reasoned alternatives, phasing and methods.",
   "对招标作出精准响应：论证充分的替代方案、分期安排与施工方法。"),
"Levés hebdomadaires des travaux": ("Weekly site surveys", "每周现场测量"),
"Un géomètre-dessinateur pour quatre équipes de chantier : les ouvrages réalisés sont levés chaque semaine.":
  ("One surveyor-draughtsman for four site crews: completed works are surveyed every week.",
   "一名测量绘图员服务四支施工班组：已完成的工程每周测量一次。"),
"Plans d'exécution et de récolement": ("Construction and as-built drawings", "施工图与竣工图"),
"Une réactivité réelle dans la production des plans, pour le chantier comme pour l'exploitant.":
  ("Genuine responsiveness in producing drawings, for the site as much as for the operator.",
   "图纸出具高效及时，兼顾施工现场与运营方需求。"),
"Appui technique aux équipes": ("Technical support for the crews", "为班组提供技术支持"),
"Le chargé d'études suit le chantier, anticipe les points durs et sécurise les choix d'exécution.":
  ("The design engineer follows the site, anticipates critical points and secures construction choices.",
   "技术工程师跟踪现场、预判难点并确保施工方案可靠。"),
"Innovation · brevet 2018": ("Innovation · patented 2018", "技术创新 · 2018 年专利"),
"RIC, le robot d'inspection conçu par La Garonne.": ("RIC, the inspection robot designed by La Garonne.", "RIC，由 La Garonne 自主研发的检测机器人。"),
"Robot de télé-visualisation des ouvrages d'assainissement en 4K et à 360°, développé et breveté par l'entreprise. Plus de 120 km de réseaux inspectés sur la commune de Toulouse.":
  ("A 4K 360° remote inspection robot for sewer structures, developed and patented by the company. Over 120 km of networks inspected in Toulouse.",
   "用于排水构筑物的 4K 360° 远程视像检测机器人，由公司自主研发并获专利。已在图卢兹检测管网超过 120 公里。"),
"Robot de télé-visualisation des ouvrages d'assainissement en 4K et à 360°, développé et breveté par l'entreprise en 2018.":
  ("A 4K 360° remote inspection robot for sewer structures, developed and patented by the company in 2018.",
   "用于排水构筑物的 4K 360° 远程视像检测机器人，由公司于 2018 年自主研发并获专利。"),
"Le RIC, robot d'inspection conçu par SA LA GARONNE": ("The RIC, inspection robot designed by SA LA GARONNE", "RIC，由 SA LA GARONNE 研发的检测机器人"),
"Le RIC, robot d'inspection des réseaux d'assainissement conçu par SA LA GARONNE": ("The RIC, sewer network inspection robot designed by SA LA GARONNE", "RIC，由 SA LA GARONNE 研发的排水管网检测机器人"),
"RIC · télé-visualisation 4K · 360°": ("RIC · 4K remote inspection · 360°", "RIC · 4K 远程视像 · 360°"),
"km": ("km", "公里"),
"de réseaux inspectés": ("of networks inspected", "已检测管网"),
"de réseaux inspectés à Toulouse": ("of networks inspected in Toulouse", "图卢兹已检测管网"),
"4K": ("4K", "4K"),
"Qualité d'image": ("Image quality", "图像质量"),
"Brevet déposé": ("Patent filed", "已申请专利"),
"géomètre": ("surveyor", "测量绘图员"),
"pour 4 équipes de chantier": ("for 4 site crews", "服务 4 支施工班组"),
"Hebdo": ("Weekly", "每周"),
"Levé des travaux réalisés": ("Survey of completed works", "已完工工程测量"),
"Étudier, lever, dessiner, contrôler : nous internalisons l'ingénierie de nos chantiers, de la réponse à l'appel d'offres jusqu'au dossier de récolement. Un atout rare pour une entreprise de notre taille.":
  ("Study, survey, draw, verify: we keep the engineering of our worksites in-house, from tender response to as-built file. A rare asset for a company of our size.",
   "研究、测量、绘图、复核：从投标响应到竣工资料，工程技术工作全部由内部完成。对我们这样规模的企业而言，这是难得的优势。"),
"Géomètre-dessinateur et chargé d'études, en interne.": ("Surveyor-draughtsman and design engineer, in-house.", "内设测量绘图员与技术工程师。"),
"Un bureau d'études intégré accompagne chaque projet, en phase de consultation comme en phase d'exécution.":
  ("An in-house design office supports every project, at tender stage and during construction.",
   "内部技术设计部全程参与每个项目，覆盖投标阶段与施工阶段。"),
"Qualifications & labels": ("Qualifications & labels", "资质与认证"),
"Identifications professionnelles FNTP, labels métier et engagements certifiés.":
  ("FNTP professional qualifications, industry labels and certified commitments.",
   "FNTP 专业资质、行业认证及经认证的承诺。"),
"Des compétences reconnues par la profession et des engagements certifiés.":
  ("Skills recognised by the industry and certified commitments.",
   "获行业认可的专业能力与经认证的承诺。"),
"FNTP": ("FNTP", "FNTP"),
"5118 · AEP zone urbaine": ("5118 · urban drinking water networks", "5118 · 城区给水管网"),
"5141 · Tranchées fortes profondeurs": ("5141 · deep trenches", "5141 · 深沟槽施工"),
"5161 · Grand diamètre": ("5161 · large diameter", "5161 · 大口径管道"),
"5221 · Réhabilitation réseaux visitables": ("5221 · rehabilitation of man-entry networks", "5221 · 可通行管道修复"),
"Label Canalisateur": ("Canalisateur label", "Canalisateur 管道施工认证"),
"Label RSE TP": ("RSE TP label", "RSE TP 社会责任认证"),
"Engagé RSE · AFNOR": ("Engagé RSE · AFNOR", "Engagé RSE · AFNOR"),
"Amiante SS3": ("Asbestos SS3", "石棉作业 SS3 资质"),
"AIPR · CATEC · SST · H0B0": ("AIPR · CATEC · first aid · H0B0", "AIPR · CATEC · 急救员 · H0B0"),
"Qualibat": ("Qualibat", "Qualibat"),
"NF · AFNOR": ("NF · AFNOR", "NF · AFNOR"),
"Fédération Nationale des Travaux Publics": ("French National Federation of Public Works", "法国全国市政工程联合会"),
"Label Canalisateur — assainissement": ("Canalisateur label — sewerage", "Canalisateur 认证 — 排水管网"),
"Label Engagé RSE — AFNOR Certification": ("Engagé RSE label — AFNOR Certification", "Engagé RSE 标识 — AFNOR 认证"),
"Valeurs": ("Values", "价值观"),
"Ce qui guide nos équipes.": ("What guides our crews.", "指引我们团队的原则。"),
"Six principes, hérités de 70 ans de terrain, appliqués à chaque intervention.":
  ("Six principles, inherited from 70 years in the field, applied to every operation.",
   "源自 70 年现场经验的六项原则，落实到每一次作业。"),
"Technicité": ("Technical skill", "技术实力"),
"Des compétences pointues sur les réseaux, les matériaux, les procédés et les contraintes du sous-sol urbain.":
  ("Sharp skills in networks, materials, processes and the constraints of the urban subsoil.",
   "在管网、管材、工艺以及城市地下环境约束方面拥有精深能力。"),
"Expérience": ("Experience", "经验积淀"),
"Près de 70 ans de chantiers sur le même territoire : nous connaissons les réseaux, souvent depuis leur construction.":
  ("Nearly 70 years of worksites in the same area: we know the networks, often since they were built.",
   "在同一片区域施工近 70 年：我们熟悉这些管网，往往从它们建成之日起就是如此。"),
"Sécurité": ("Safety", "安全"),
"Une responsable QHSE dédiée, des formations AIPR, CATEC, SST et H0B0, des EPI contrôlés : la sécurité des équipes et des riverains est la première condition de tout chantier.":
  ("A dedicated QHSE manager, AIPR, CATEC, first aid and H0B0 training, checked PPE: the safety of crews and residents is the first condition of every worksite.",
   "配备专职 QHSE 负责人，开展 AIPR、CATEC、急救员与 H0B0 培训，个人防护装备定期查验：施工人员与周边居民的安全是一切工程的首要前提。"),
"Un responsable QHSE dédié, des équipes formées (AIPR, CATEC, SST), des EPI systématiques et des chantiers balisés — pour nos collaborateurs comme pour les riverains.":
  ("A dedicated QHSE manager, trained crews (AIPR, CATEC, first aid), systematic PPE and signposted worksites — for our staff as much as for residents.",
   "配备专职 QHSE 负责人、接受过 AIPR、CATEC 与急救培训的班组、全员个人防护装备以及规范围挡的工地——既为员工，也为周边居民。"),
"Fiabilité opérationnelle": ("Operational reliability", "履约可靠"),
"Des engagements tenus sur les délais, la qualité d'exécution et la continuité de service.":
  ("Commitments kept on schedule, quality of execution and continuity of service.",
   "在工期、施工质量与服务连续性上说到做到。"),
"Limitation des nuisances": ("Limiting disruption", "减少干扰"),
"Techniques sans tranchée, phasage, emprises réduites : nous respectons la vie du quartier pendant les travaux.":
  ("Trenchless techniques, phasing, reduced footprint: we respect neighbourhood life during the works.",
   "非开挖工艺、分期施工、缩小占地：施工期间尊重街区的正常生活。"),
"Techniques sans tranchée, phasage précis, emprises réduites : nous limitons l'impact sur la vie du quartier.":
  ("Trenchless techniques, precise phasing, reduced footprint: we limit the impact on neighbourhood life.",
   "非开挖工艺、精细分期、缩小占地：将对街区生活的影响降到最低。"),
"Durabilité": ("Sustainability", "可持续性"),
"Démarche RSE labellisée, tri et réemploi des déblais, test de chantiers bas carbone : des infrastructures et des pratiques conçues pour durer.":
  ("A labelled CSR programme, sorting and reuse of excavated spoil, low-carbon worksite trials: infrastructure and practices built to last.",
   "获认证的社会责任体系、弃土分类与再利用、低碳工地试点：为长期使用而设计的基础设施与作业方式。"),
"Démarche RSE labellisée, tri et réemploi des déblais, expérimentation de chantiers bas carbone : des infrastructures et des pratiques conçues pour durer.":
  ("A labelled CSR programme, sorting and reuse of excavated spoil, low-carbon worksite trials: infrastructure and practices built to last.",
   "获认证的社会责任体系、弃土分类与再利用、低碳工地试点：为长期使用而设计的基础设施与作业方式。"),
"Démarche RSE": ("CSR programme", "社会责任体系"),
"Certifiée en 2022, labellisée Engagé RSE par AFNOR en 2023. Objectifs 2026 :":
  ("Certified in 2022, awarded AFNOR's Engagé RSE label in 2023. 2026 objectives:",
   "2022 年通过认证，2023 年获 AFNOR「Engagé RSE」标识。2026 年目标："),
"Tendre vers le zéro accident": ("Towards zero accidents", "力争零事故"),
"Comité RSE trimestriel": ("Quarterly CSR committee", "每季度召开社会责任委员会"),
"Partenariats locaux": ("Local partnerships", "本地合作伙伴"),
"Réemploi des déblais": ("Reuse of excavated spoil", "弃土再利用"),
"Chantier bas carbone · biocarburant": ("Low-carbon worksite · biofuel", "低碳工地 · 生物燃料"),
"Réunion d'équipe SA LA GARONNE devant une inspection vidéo de canalisation": ("SA LA GARONNE team meeting in front of a pipe video inspection", "SA LA GARONNE 团队在管道视频检测前召开会议"),
"Collaboratrices de SA LA GARONNE lors d'un événement d'entreprise": ("SA LA GARONNE staff at a company event", "SA LA GARONNE 员工参加公司活动"),
"Pelle mécanique SA LA GARONNE sur chantier": ("SA LA GARONNE excavator on site", "SA LA GARONNE 挖掘机在施工现场"),
"Équipe & moyens": ("Team & resources", "团队与装备"),
"35 collaborateurs, quatre équipes, un bureau d'études.": ("35 employees, four crews, one design office.", "35 名员工、四支班组、一个技术设计部。"),
"Chefs de chantier, canalisateurs, conducteurs d'engins, opérateurs de réhabilitation, encadrement technique : une équipe stable, formée et attachée à son métier.":
  ("Site managers, pipelayers, plant operators, rehabilitation technicians, technical supervision: a stable team, trained and committed to its trade.",
   "工地负责人、管道工、机械操作手、修复作业技师、技术管理人员：一支稳定、受过训练且热爱本职的队伍。"),
"Quatre équipes de chantier": ("Four site crews", "四支施工班组"),
"Des équipes qualifiées et fidèles, une transmission du savoir-faire entre générations de canalisateurs et de chefs de chantier.":
  ("Skilled, long-serving crews and know-how passed down between generations of pipelayers and site managers.",
   "队伍专业且稳定，技艺在几代管道工与工地负责人之间传承。"),
"Un bureau d'études intégré": ("An in-house design office", "内设技术设计部"),
"Géomètre-dessinateur et chargé d'études : levés hebdomadaires, plans d'exécution et de récolement, études de prix.":
  ("Surveyor-draughtsman and design engineer: weekly surveys, construction and as-built drawings, cost studies.",
   "测量绘图员与技术工程师：每周测量、施工图与竣工图、报价测算。"),
"Un atelier et un parc matériel adaptés": ("A workshop and a suitable plant fleet", "机修车间与适配设备机队"),
"Engins de terrassement, unités d'hydrocurage et d'inspection, robot RIC, matériel de réhabilitation robotisée, pompage.":
  ("Earthmoving plant, jetting and inspection units, the RIC robot, robotic rehabilitation equipment, pumping.",
   "土方机械、高压清洗与检测车辆、RIC 机器人、机器人修复设备、抽排装置。"),
"Une culture sécurité": ("A safety culture", "安全文化"),
"Formations régulières, EPI systématiques, plans de prévention et analyse des risques sur chaque chantier.":
  ("Regular training, systematic PPE, prevention plans and risk assessment on every worksite.",
   "定期培训、全员个人防护装备、每个工地均编制安全防护方案并开展风险评估。"),
"Un siège à Toulouse": ("A head office in Toulouse", "图卢兹总部"),
"63 chemin de Guilhermy : bureaux, atelier et parc matériel au cœur de notre zone d'intervention.":
  ("63 chemin de Guilhermy: offices, workshop and plant yard at the heart of our operating area.",
   "63 chemin de Guilhermy：办公场所、机修车间与设备停放场，位于我们服务区域的中心。"),
"Nous rejoindre": ("Join us", "加入我们"),
"Un métier utile, des chantiers qui comptent.": ("A useful trade, worksites that matter.", "有价值的职业，有分量的工程。"),
"Canalisateur, chef de chantier, conducteur d'engins, opérateur de réhabilitation : nous recrutons régulièrement des profils de terrain, débutants comme expérimentés.":
  ("Pipelayer, site manager, plant operator, rehabilitation technician: we regularly recruit field profiles, both entry-level and experienced.",
   "管道工、工地负责人、机械操作手、修复作业技师：我们长期招聘一线人才，欢迎新手与资深从业者。"),
"Envoyer une candidature": ("Send an application", "投递简历"),
"Fiche d'identité": ("Company details", "企业信息"),
"Dénomination": ("Registered name", "企业名称"),
"Forme juridique": ("Legal form", "企业类型"),
"SA à conseil d'administration": ("Public limited company with a board of directors", "设董事会的股份有限公司"),
"Capital social": ("Share capital", "注册资本"),
"génération": ("generation", "代"),
"35 salariés · 4 équipes de chantier · atelier · bureau d'études": ("35 employees · 4 site crews · workshop · design office", "35 名员工 · 4 支施工班组 · 机修车间 · 技术设计部"),
"Activité": ("Activity", "业务构成"),
"Assainissement 75 % · eau potable 15 % · sans tranchée 10 %": ("Sewerage 75% · drinking water 15% · trenchless 10%", "排水管网 75% · 饮用水 15% · 非开挖 10%"),
"SIREN": ("Company number", "企业注册号"),
"Code APE": ("Business code", "行业代码"),
"4221Z — Construction de réseaux pour fluides": ("4221Z — Construction of utility projects for fluids", "4221Z — 流体输送管网工程施工"),
"Une histoire familiale, une exigence d'aujourd'hui.": ("A family story, a present-day standard.", "家族传承的历史，与时俱进的标准。"),
"Fondée à Toulouse en 1956 par Eloy Pascual, SA LA GARONNE est aujourd'hui dirigée par Nicolas Pascual, troisième génération de la famille. Près de 70 ans plus tard, elle conjugue l'expérience de ses équipes et des procédés modernes — chemisage, gainage, fraisage, robotique.":
  ("Founded in Toulouse in 1956 by Eloy Pascual, SA LA GARONNE is today led by Nicolas Pascual, the family's third generation. Nearly 70 years on, it combines the experience of its crews with modern processes — CIPP lining, sleeving, milling, robotics.",
   "SA LA GARONNE 于 1956 年由 Eloy Pascual 在图卢兹创立，如今由家族第三代 Nicolas Pascual 执掌。近 70 年后的今天，公司将团队经验与现代工艺相结合：原位固化内衬、内衬修复、铣削与机器人技术。"),
"35 collaborateurs répartis en quatre équipes de chantier, un atelier, un bureau d'études et un siège à Toulouse : nous connaissons les réseaux sur lesquels nous intervenons, souvent depuis leur construction.":
  ("35 employees across four site crews, a workshop, a design office and a head office in Toulouse: we know the networks we work on, often since they were built.",
   "35 名员工分布于四支施工班组、一个机修车间、一个技术设计部和图卢兹总部：我们熟悉所施工的管网，往往从它们建成之日起就是如此。"),
"70 ans d'expérience, et l'exigence de chaque premier chantier.": ("70 years of experience, and the standards of a first worksite every time.", "70 年经验，始终保持初次施工般的严谨。"),
"SA La Garonne · Toulouse · trois générations": ("SA La Garonne · Toulouse · three generations", "SA La Garonne · 图卢兹 · 三代传承"),
"Société fondée à Toulouse le 13 janvier 1956, dédiée aux réseaux d'eau et d'assainissement.":
  ("Company founded in Toulouse on 13 January 1956, dedicated to water and sewer networks.",
   "公司于 1956 年 1 月 13 日在图卢兹成立，专注给排水管网。"),
"La deuxième génération poursuit le développement de l'entreprise sur l'agglomération toulousaine.":
  ("The second generation continues to grow the company across the Toulouse area.",
   "第二代继续推动公司在图卢兹地区的发展。"),
"Troisième génération à la tête de l'entreprise familiale.": ("Third generation at the head of the family business.", "家族企业第三代掌门人。"),
"Télé-visualisation 4K à 360° : plus de 120 km de réseaux inspectés à Toulouse.":
  ("4K 360° remote inspection: over 120 km of networks inspected in Toulouse.",
   "4K 360° 远程视像检测：在图卢兹检测管网超过 120 公里。"),
"Engagement": ("Commitment", "责任承诺"),
"Label Engagé RSE d'AFNOR": ("AFNOR's Engagé RSE label", "AFNOR「Engagé RSE」标识"),
"Après la certification RSE de 2022, un comité RSE pilote des objectifs annuels.":
  ("Following the 2022 CSR certification, a CSR committee steers annual objectives.",
   "继 2022 年通过社会责任认证后，由社会责任委员会推动年度目标落实。"),
"35 collaborateurs, 4 équipes, un bureau d'études": ("35 employees, 4 crews, one design office", "35 名员工、4 支班组、一个技术设计部"),
"Une identité renouvelée pour rester la référence des réseaux d'eau à Toulouse.":
  ("A refreshed identity to remain the benchmark for water networks in Toulouse.",
   "全新的品牌形象，继续担当图卢兹给排水管网的标杆。"),
"Ce qui ne se négocie pas.": ("What is not up for negotiation.", "没有商量余地的原则。"),
"Nos chantiers touchent à des infrastructures essentielles, au cœur de la vie des quartiers. Quatre engagements structurent chacune de nos interventions.":
  ("Our worksites touch essential infrastructure, at the heart of neighbourhood life. Four commitments shape every operation we carry out.",
   "我们的工程关乎城市核心基础设施，就在居民生活之中。四项承诺贯穿每一次作业。"),
"Continuité de service": ("Continuity of service", "服务不中断"),
"Nous intervenons sur des réseaux en service : l'eau continue de couler, les eaux usées continuent d'être évacuées.":
  ("We work on live networks: the water keeps flowing, the wastewater keeps draining.",
   "我们在在役管网上作业：供水不停，污水照排。"),
"Nous intervenons pour": ("We work for", "我们的客户"),
"Un environnement B2B et marchés publics, aux côtés des acteurs qui exploitent et font vivre les infrastructures de l'eau.":
  ("A B2B and public procurement environment, alongside the players who operate and sustain water infrastructure.",
   "面向企业客户与政府采购市场，与运营和维护水务基础设施的各方并肩合作。"),
"Collectivités & métropoles": ("Local authorities & metropolitan bodies", "地方政府与都市区管理机构"),
"Marchés publics": ("Public contracts", "政府采购"),
"Exploitants de réseaux": ("Network operators", "管网运营商"),
"Régies · délégataires": ("Municipal utilities · concession holders", "市政水务单位 · 特许经营方"),
"Acteurs publics & aménageurs": ("Public bodies & developers", "公共机构与开发商"),
"Infrastructures": ("Infrastructure", "基础设施"),
"Professionnels du cycle de l'eau": ("Water cycle professionals", "水务行业从业方"),
"Ingénierie · entreprises": ("Engineering · contractors", "工程咨询 · 承包企业"),
"Donneurs d'ordre": ("Clients", "客户群体"),
})

# ---------------------------------------------------------------- Page Réalisations
add({
"Réalisations — chantiers SA LA GARONNE à Toulouse": ("Projects — SA LA GARONNE worksites in Toulouse", "工程案例 — SA LA GARONNE 在图卢兹的项目"),
"Nos chantiers d'assainissement, d'eau potable et de réhabilitation sans tranchée à Toulouse et dans son agglomération, en images.":
  ("Our sewerage, drinking water and trenchless rehabilitation worksites in Toulouse and its metropolitan area, in pictures.",
   "图片呈现我们在图卢兹及周边地区的排水、饮用水与非开挖修复工程。"),
"Chantier SA LA GARONNE en centre-ville de Toulouse": ("SA LA GARONNE worksite in central Toulouse", "SA LA GARONNE 在图卢兹市中心的工地"),
"Sur le terrain, à Toulouse et autour.": ("On site, in and around Toulouse.", "施工现场，遍及图卢兹及周边。"),
"Un aperçu de nos interventions sur les infrastructures essentielles de l'agglomération toulousaine : assainissement, eau potable, réhabilitation sans tranchée et chantiers complexes.":
  ("An overview of our work on the essential infrastructure of the Toulouse area: sewerage, drinking water, trenchless rehabilitation and complex worksites.",
   "我们在图卢兹地区核心基础设施上的工作概览：排水管网、饮用水、非开挖修复与复杂工程。"),
"Territoire": ("Territory", "服务地域"),
"Cadre": ("Framework", "合同类型"),
"Marchés publics & privés": ("Public & private contracts", "政府采购与商业合同"),
"Galerie": ("Gallery", "工程图集"),
"Nos chantiers en images.": ("Our worksites in pictures.", "图片中的施工现场。"),
"Tous": ("All", "全部"),
"Travaux complexes · Toulouse": ("Complex works · Toulouse", "复杂工程 · 图卢兹"),
"Intervention en hypercentre": ("Operation in the city centre", "核心城区施工"),
"Logistique lourde, emprise maîtrisée et coordination fine au cœur de Toulouse, sous les arcades du Capitole.":
  ("Heavy logistics, controlled footprint and fine coordination in the heart of Toulouse, under the Capitole arcades.",
   "在图卢兹市中心市政厅广场拱廊下：重型物流组织、占地严格控制、各方精细协同。"),
"Logistique lourde et emprise maîtrisée au cœur de Toulouse.": ("Heavy logistics and a controlled footprint in the heart of Toulouse.", "在图卢兹市中心实现重型物流组织与占地控制。"),
"Camions SA LA GARONNE sous les arcades de la place du Capitole": ("SA LA GARONNE trucks under the Place du Capitole arcades", "SA LA GARONNE 车辆停驻于市政厅广场拱廊下"),
"Intervention sur regard d'assainissement": ("Work on a sewer manhole", "排水检查井作业"),
"Intervention sur regard": ("Work on a manhole", "检查井作业"),
"Équipe et matériel dédiés en centre-ville : continuité de service assurée pendant l'intervention.":
  ("Dedicated crew and equipment in the city centre: continuity of service maintained throughout.",
   "市中心专属班组与设备：作业期间服务不中断。"),
"Équipe et matériel dédiés, continuité de service assurée.": ("Dedicated crew and equipment, continuity of service maintained.", "专属班组与设备，服务不中断。"),
"Équipe SA LA GARONNE intervenant sur un regard d'assainissement en ville": ("SA LA GARONNE crew working on a sewer manhole in the city", "SA LA GARONNE 班组在城区检查井作业"),
"Assainissement · centre-ville": ("Sewerage · city centre", "排水管网 · 市中心"),
"Renouvellement de réseau en centre-ville": ("Network renewal in the city centre", "市中心管网更新"),
"Tranchée, lit de pose et réfection de voirie à l'identique, dans un secteur commerçant très fréquenté.":
  ("Trench, pipe bedding and like-for-like road reinstatement, in a busy shopping area.",
   "在人流密集的商业区完成沟槽开挖、管道垫层与路面原样恢复。"),
"Tranchée, pose et réfection de voirie en secteur piéton.": ("Trench, laying and road reinstatement in a pedestrian area.", "步行区内的沟槽开挖、管道敷设与路面恢复。"),
"Tranchée ouverte en centre-ville, équipe au travail": ("Open trench in the city centre, crew at work", "市中心开挖沟槽，班组作业中"),
"Chemisage et interventions robotisées pilotées depuis la surface, sans ouverture de la chaussée.":
  ("CIPP lining and robotic operations run from the surface, with no road opening.",
   "由地面遥控的原位固化内衬与机器人作业，无需开挖路面。"),
"Chemisage et interventions robotisées depuis la surface.": ("CIPP lining and robotic operations from the surface.", "在地面完成原位固化内衬与机器人作业。"),
"Unité mobile de réhabilitation": ("Mobile rehabilitation unit", "移动修复作业车"),
"Camion SA LA GARONNE — réhabilitation de canalisations sans tranchée": ("SA LA GARONNE truck — trenchless pipe rehabilitation", "SA LA GARONNE 作业车 — 非开挖管道修复"),
"Inspection télévisée de collecteur": ("CCTV inspection of a sewer main", "排水干管闭路电视检测"),
"Diagnostic & inspection": ("Survey & inspection", "检测与诊断"),
"Analyse en équipe des relevés caméra avant intervention : la préparation est la première étape de tout chantier.":
  ("Team analysis of camera footage before work begins: preparation is the first stage of every worksite.",
   "施工前团队共同分析摄像检测记录：准备工作是所有工程的第一步。"),
"Collecteur visitable en fouille blindée": ("Man-entry sewer in a shored excavation", "支护基坑内的可通行排水干管"),
"Collecteur visitable": ("Man-entry sewer", "可通行排水干管"),
"Réhabilitation d'un ouvrage visitable : accès par fouille blindée, intervention en sécurité à grande profondeur.":
  ("Rehabilitation of a man-entry structure: access via a shored excavation, safe work at great depth.",
   "可通行构筑物修复：通过支护基坑进入，在深处安全作业。"),
"Réhabilitation d'un ouvrage visitable en fouille blindée.": ("Rehabilitation of a man-entry structure in a shored excavation.", "在支护基坑内修复可通行构筑物。"),
"Canalisateur SA LA GARONNE dans un collecteur visitable en grande profondeur, tranchée blindée":
  ("SA LA GARONNE pipelayer inside a deep man-entry sewer, shored trench", "SA LA GARONNE 管道工在深埋可通行排水干管内，沟槽已支护"),
"Fouille blindée devant un monument": ("Shored excavation in front of a monument", "纪念碑前的支护基坑"),
"Fouille blindée en hypercentre": ("Shored excavation in the city centre", "核心城区支护基坑"),
"Secteur sensible · Toulouse": ("Sensitive area · Toulouse", "敏感区域 · 图卢兹"),
"Secteur sensible": ("Sensitive area", "敏感区域"),
"Blindage lourd au pied du monument aux morts, dans un carrefour très fréquenté, circulation et cheminements maintenus.":
  ("Heavy shoring at the foot of the war memorial, on a busy junction, with traffic and pedestrian routes maintained.",
   "在交通繁忙的路口、阵亡将士纪念碑脚下实施重型支护，同时保持车辆通行与人行通道畅通。"),
"Blindage lourd au pied d'un monument, circulation maintenue.": ("Heavy shoring at the foot of a monument, traffic maintained.", "纪念碑脚下的重型支护，交通保持通畅。"),
"Raccordement de conduites en fonte": ("Ductile iron pipe connection", "球墨铸铁管道接驳"),
"Pose de pièces de raccord et de vannes sur une conduite d'adduction : précision d'assemblage et essais avant remise en eau.":
  ("Fitting couplings and valves on a supply main: precision assembly and testing before the return to service.",
   "在输水主管上安装接头与阀门：精确组装并在通水前完成试验。"),
"RIC, robot d'inspection breveté": ("RIC, patented inspection robot", "RIC，获专利的检测机器人"),
"Télé-visualisation 4K à 360° des ouvrages d'assainissement, conçue par La Garonne : plus de 120 km inspectés à Toulouse.":
  ("4K 360° remote inspection of sewer structures, designed by La Garonne: over 120 km inspected in Toulouse.",
   "由 La Garonne 研发的排水构筑物 4K 360° 远程视像检测：在图卢兹已检测超 120 公里。"),
"Références": ("References", "业绩参考"),
"Vous souhaitez consulter nos références détaillées ?": ("Would you like to see our detailed references?", "希望查阅我们的详细业绩资料？"),
"Votre projet": ("Your project", "您的项目"),
"Vos réseaux méritent une équipe qui connaît le terrain.": ("Your networks deserve a team that knows the ground.", "您的管网值得一支熟悉现场的团队。"),
"Parlons-en": ("Let's talk", "与我们联系"),
})

# ---------------------------------------------------------------- Page Contact
add({
"Contact — SA LA GARONNE, Toulouse": ("Contact — SA LA GARONNE, Toulouse", "联系我们 — SA LA GARONNE，图卢兹"),
"Contactez SA LA GARONNE : devis, consultation de marché public ou question technique. 63 chemin de Guilhermy, 31100 Toulouse. Tél. 05 62 13 07 80.":
  ("Contact SA LA GARONNE: quotation, public tender enquiry or technical question. 63 chemin de Guilhermy, 31100 Toulouse, France. Tel. +33 5 62 13 07 80.",
   "联系 SA LA GARONNE：报价、招标咨询或技术问题。地址：法国图卢兹 31100，63 chemin de Guilhermy。电话：+33 5 62 13 07 80。"),
"Équipe SA LA GARONNE sur chantier": ("SA LA GARONNE crew on site", "SA LA GARONNE 班组在施工现场"),
"Parlons de votre réseau.": ("Let's talk about your network.", "聊聊您的管网项目。"),
"Demande de devis, consultation dans le cadre d'un marché public, question technique ou candidature : nos équipes vous répondent rapidement et précisément.":
  ("Quotation request, public tender enquiry, technical question or job application: our teams reply quickly and precisely.",
   "无论是报价需求、政府采购咨询、技术问题还是求职申请，我们的团队都会快速、准确地回复。"),
"Toulouse · 31100": ("Toulouse · 31100, France", "图卢兹 · 31100，法国"),
"Coordonnées": ("Contact details", "联系方式"),
"Nous joindre.": ("Reach us.", "与我们取得联系。"),
"Adresse": ("Address", "地址"),
"Toulouse Métropole et agglomération toulousaine": ("Toulouse Métropole and the surrounding area", "图卢兹都市区及周边地区"),
"Marchés": ("Contracts", "承接类型"),
"Réponse aux consultations publiques et privées": ("We respond to public and private tenders", "承接政府与商业招标项目"),
"Vue aérienne du siège de SA LA GARONNE, chemin de Guilhermy à Toulouse": ("Aerial view of SA LA GARONNE's head office, chemin de Guilhermy, Toulouse", "SA LA GARONNE 总部航拍图，位于图卢兹 chemin de Guilhermy"),
"Siège & parc matériel · Toulouse": ("Head office & plant yard · Toulouse", "总部与设备停放场 · 图卢兹"),
"Formulaire": ("Form", "在线留言"),
"Nom et prénom *": ("Full name *", "姓名 *"),
"Organisation": ("Organisation", "单位名称"),
"Collectivité, exploitant, entreprise…": ("Local authority, operator, company…", "地方政府、运营商、企业……"),
"Email *": ("Email *", "电子邮箱 *"),
"Objet *": ("Subject *", "主题 *"),
"Demande de devis": ("Quotation request", "报价咨询"),
"Consultation / marché public": ("Tender / public contract", "招标 / 政府采购"),
"Question technique": ("Technical question", "技术问题"),
"Candidature": ("Job application", "求职申请"),
"Autre": ("Other", "其他"),
"Votre message *": ("Your message *", "留言内容 *"),
"Nature du réseau, localisation, contraintes particulières, délais…": ("Type of network, location, specific constraints, timescales…", "管网类型、项目地点、特殊要求、工期……"),
"J'accepte que les informations saisies soient utilisées pour traiter ma demande. Elles ne sont ni cédées ni utilisées à d'autres fins.":
  ("I agree that the information provided may be used to process my enquiry. It is neither shared nor used for any other purpose.",
   "我同意所填写的信息仅用于处理本次咨询。这些信息不会被转让，也不会用于其他用途。"),
"Envoyer le message": ("Send message", "发送留言"),
"* Champs obligatoires. Réponse sous 48 h ouvrées.": ("* Required fields. Reply within 48 working hours.", "* 为必填项。我们将在 48 个工作小时内回复。"),
"Accès": ("Getting here", "交通指引"),
"Le siège, chemin de Guilhermy.": ("The head office, chemin de Guilhermy.", "总部，chemin de Guilhermy。"),
"Au sud-ouest de Toulouse, à proximité immédiate du périphérique — au cœur de notre zone d'intervention.":
  ("South-west of Toulouse, right next to the ring road — at the heart of our operating area.",
   "位于图卢兹西南、紧邻环城公路，处在我们服务区域的中心。"),
"Plan d'accès — SA LA GARONNE, 63 chemin de Guilhermy, 31100 Toulouse": ("Location map — SA LA GARONNE, 63 chemin de Guilhermy, 31100 Toulouse", "位置地图 — SA LA GARONNE，63 chemin de Guilhermy，31100 图卢兹"),
})

# ---------------------------------------------------------------- Mentions légales
add({
"Mentions légales — SA LA GARONNE": ("Legal notice — SA LA GARONNE", "法律声明 — SA LA GARONNE"),
"Mentions légales du site de SA LA GARONNE, société de travaux publics à Toulouse : éditeur, hébergement, données personnelles.":
  ("Legal notice for the SA LA GARONNE website, a civil engineering company in Toulouse: publisher, hosting, personal data.",
   "SA LA GARONNE（图卢兹市政工程企业）网站法律声明：出版方、托管服务、个人数据。"),
"Éditeur du site": ("Website publisher", "网站出版方"),
"Le site": ("The website", "本网站"),
"sa-la-garonne.fr": ("sa-la-garonne.fr", "sa-la-garonne.fr"),
"est édité par": ("is published by", "由以下主体出版："),
"(dénomination sociale : SOC LA GARONNE), société anonyme à conseil d'administration au capital de 400 000 €, immatriculée au RCS de Toulouse sous le numéro 560 800 583 — code APE 4221Z (construction de réseaux pour fluides).":
  ("(registered name: SOC LA GARONNE), a public limited company with a board of directors and share capital of €400,000, registered with the Toulouse Trade and Companies Register under number 560 800 583 — business code 4221Z (construction of utility projects for fluids).",
   "（注册名称：SOC LA GARONNE），设董事会的股份有限公司，注册资本 400,000 欧元，在图卢兹商事法院登记，注册号 560 800 583，行业代码 4221Z（流体输送管网工程施工）。"),
"Siège social : 63 chemin de Guilhermy, 31100 Toulouse, France.": ("Registered office: 63 chemin de Guilhermy, 31100 Toulouse, France.", "注册地址：法国图卢兹 31100，63 chemin de Guilhermy。"),
"Téléphone : +33 5 62 13 07 80 — Email :": ("Phone: +33 5 62 13 07 80 — Email:", "电话：+33 5 62 13 07 80 — 电子邮箱："),
"N° de TVA intracommunautaire : FR05 560 800 583.": ("EU VAT number: FR05 560 800 583.", "欧盟增值税号：FR05 560 800 583。"),
"Directeur de la publication : Nicolas Pascual.": ("Publication director: Nicolas Pascual.", "出版负责人：Nicolas Pascual。"),
"Hébergement": ("Hosting", "网站托管"),
"[Nom de l'hébergeur — raison sociale, adresse, téléphone — à compléter lors de la mise en ligne.]":
  ("[Host name — company name, address, telephone — to be completed at go-live.]",
   "［托管服务商名称、地址与电话，将于网站上线时补充。］"),
"Conception et réalisation": ("Design and development", "设计与开发"),
"Direction artistique, identité visuelle et développement :": ("Art direction, visual identity and development:", "艺术指导、视觉识别与开发："),
", agence digitale Performance & IA, Toulouse.": (", a performance and AI digital agency, Toulouse.", "，绩效与人工智能数字代理机构，图卢兹。"),
"Photographies : SA LA GARONNE. Toute reproduction est interdite sans autorisation.":
  ("Photographs: SA LA GARONNE. Reproduction is prohibited without authorisation.",
   "图片版权：SA LA GARONNE。未经授权禁止转载。"),
"Propriété intellectuelle": ("Intellectual property", "知识产权"),
"L'ensemble des contenus de ce site (textes, photographies, illustrations, logotype, pictogrammes, structure) est protégé par le droit d'auteur et le droit des marques. Toute reproduction, représentation, modification ou adaptation, totale ou partielle, sans autorisation écrite préalable de SA LA GARONNE est interdite.":
  ("All content on this site (text, photographs, illustrations, logo, pictograms, structure) is protected by copyright and trademark law. Any reproduction, display, modification or adaptation, in whole or in part, without SA LA GARONNE's prior written authorisation is prohibited.",
   "本网站全部内容（文字、图片、插图、标识、图标及结构）均受著作权法与商标法保护。未经 SA LA GARONNE 事先书面许可，禁止对其进行全部或部分的复制、展示、修改或改编。"),
"Données personnelles": ("Personal data", "个人数据"),
"Les informations transmises via le formulaire de contact (nom, organisation, email, téléphone, message) sont utilisées exclusivement pour répondre à votre demande. Elles sont destinées aux services concernés de SA LA GARONNE et ne sont ni cédées ni vendues à des tiers. Elles sont conservées pendant la durée nécessaire au traitement de la demande et, le cas échéant, de la relation commerciale qui en découle.":
  ("The information submitted through the contact form (name, organisation, email, telephone, message) is used solely to respond to your enquiry. It is intended for the relevant SA LA GARONNE departments and is neither shared nor sold to third parties. It is retained for as long as needed to process the enquiry and, where applicable, the business relationship that follows.",
   "通过联系表单提交的信息（姓名、单位、电子邮箱、电话、留言内容）仅用于回复您的咨询。这些信息仅提供给 SA LA GARONNE 的相关部门，不会转让或出售给第三方，并仅在处理咨询及后续业务关系所需的期限内保存。"),
"Conformément au Règlement général sur la protection des données (RGPD) et à la loi Informatique et Libertés, vous disposez d'un droit d'accès, de rectification, d'effacement, de limitation et d'opposition sur vos données. Vous pouvez l'exercer en écrivant à":
  ("In accordance with the General Data Protection Regulation (GDPR) and French data protection law, you have the right to access, rectify, erase, restrict and object to the processing of your data. You may exercise those rights by writing to",
   "根据《通用数据保护条例》（GDPR）及法国相关数据保护法律，您有权访问、更正、删除、限制处理并反对处理您的个人数据。您可通过以下方式行使上述权利：发送邮件至"),
"ou par courrier à l'adresse du siège.": ("or by post to the registered office address.", "或寄信至公司注册地址。"),
"Cookies": ("Cookies", "Cookie 使用"),
"Ce site n'utilise aucun cookie publicitaire ni outil de suivi tiers. Seul un stockage technique de session, sans identification, est utilisé pour le confort de navigation (affichage unique de l'écran d'introduction). La carte d'accès de la page Contact est fournie par Google Maps et soumise à ses propres conditions d'utilisation.":
  ("This site uses no advertising cookies and no third-party tracking tools. Only anonymous technical session storage is used for browsing comfort (showing the intro screen once). The location map on the Contact page is provided by Google Maps and subject to its own terms of use.",
   "本网站不使用任何广告 Cookie，也不使用第三方追踪工具。仅使用不含身份识别的会话级技术存储以提升浏览体验（引导画面只显示一次）。联系页面的地图由 Google Maps 提供，适用其自身的使用条款。"),
"SA LA GARONNE s'efforce d'assurer l'exactitude des informations publiées sur ce site, sans pouvoir garantir l'absence d'erreur ou d'omission. Les informations présentées n'ont pas de valeur contractuelle. SA LA GARONNE se réserve le droit de modifier le contenu du site à tout moment.":
  ("SA LA GARONNE endeavours to ensure the accuracy of the information published on this site, without being able to guarantee that it is free of error or omission. The information presented is not contractually binding. SA LA GARONNE reserves the right to modify the site's content at any time.",
   "SA LA GARONNE 力求确保本网站所载信息准确，但无法保证完全没有错误或遗漏。所列信息不构成合同约定。SA LA GARONNE 保留随时修改网站内容的权利。"),
"Droit applicable": ("Governing law", "适用法律"),
"Le présent site est soumis au droit français. Tout litige relatif à son utilisation relève de la compétence des tribunaux de Toulouse.":
  ("This site is governed by French law. Any dispute relating to its use falls within the jurisdiction of the courts of Toulouse.",
   "本网站适用法国法律。与本网站使用相关的任何争议，均由图卢兹法院管辖。"),
})

# ---------------------------------------------------------------- Compléments (SVG, JSON-LD, curseur)
add({
"Coupe schématique d'une rue : réhabilitation d'une conduite enterrée sans tranchée":
  ("Schematic street cross-section: trenchless rehabilitation of a buried pipe",
   "街道剖面示意图：地下管道的非开挖修复"),
"Voir": ("View", "查看"),
"PME familiale de travaux publics spécialisée dans les réseaux d'eau et d'assainissement : construction, entretien et réhabilitation sans tranchée. Toulouse, depuis 1956.":
  ("Family-owned civil engineering company specialising in water and sewer networks: construction, maintenance and trenchless rehabilitation. Toulouse, since 1956.",
   "专注给排水管网的家族市政工程企业：新建、维护与非开挖修复。法国图卢兹，始于 1956 年。"),
"Expert des réseaux d'eau et d'assainissement depuis 1956":
  ("Water and wastewater network specialists since 1956", "自 1956 年起深耕给排水管网"),
"Travaux et interventions complexes sur réseaux":
  ("Complex network works and operations", "复杂管网工程与作业"),
# noms propres et repères conservés tels quels
"La Garonne Travaux Publics": ("La Garonne Travaux Publics", "La Garonne Travaux Publics"),
"Eloy Pascual": ("Eloy Pascual", "Eloy Pascual"),
"Toulouse": ("Toulouse", "Toulouse"),
})

# ---------------------------------------------------------------- Fragments HTML spécifiques (titres à retours de ligne, exposants)
SPECIAL = {
 # titre principal de l'accueil : quatre lignes maîtrisées par langue
 '<span class="nw">Expert des</span> <br><span class="nw">réseaux d\'eau et</span> <br>d\'assainissement <br><em class="nw">depuis 1956.</em>': {
   "en": '<span class="nw">Water and</span> <br><span class="nw">wastewater network</span> <br><span class="nw">specialists</span> <br><em class="nw">since 1956.</em>',
   "zh": '<span class="nw">给排水管网</span> <br><span class="nw">工程专家</span> <br><em class="nw">自 1956 年</em>',
 },
 'Nicolas Pascual — 3<sup>e</sup> génération': {
   "en": 'Nicolas Pascual — 3rd generation',
   "zh": 'Nicolas Pascual — 第三代',
 },
 '2<sup>e</sup> génération': {"en": '2nd generation', "zh": '第二代'},
 '3<sup>e</sup> génération': {"en": '3rd generation', "zh": '第三代'},
 'Assainis&shy;sement': {"en": 'Sewerage', "zh": '排水管网'},
}

# Chaînes générées par le JavaScript
JS = {
 "en": {"sending": "Sending…", "sent": "Thank you, your message has been sent. We will get back to you shortly.",
        "error": "Something went wrong. You can also write to us directly at ", "mail": "Your email client will open with the message pre-filled.",
        "subject": "[Website] ", "default_subject": "Contact enquiry",
        "l_name": "Name", "l_org": "Organisation", "l_email": "Email", "l_phone": "Phone", "l_subject": "Subject"},
 "zh": {"sending": "正在发送……", "sent": "感谢您的留言，我们已收到并将尽快回复。",
        "error": "发送失败。您也可以直接发送邮件至 ", "mail": "系统将打开您的邮件客户端，内容已自动填好。",
        "subject": "［网站留言］", "default_subject": "联系咨询",
        "l_name": "姓名", "l_org": "单位", "l_email": "电子邮箱", "l_phone": "电话", "l_subject": "主题"},
}

LANGS = {
 "fr": {"name": "Français", "locale": "fr_FR", "html": "fr", "dir": "", "hreflang": "fr"},
 "en": {"name": "English", "locale": "en_GB", "html": "en", "dir": "en/", "hreflang": "en"},
 "zh": {"name": "中文", "locale": "zh_CN", "html": "zh-Hans", "dir": "zh/", "hreflang": "zh-Hans"},
}
