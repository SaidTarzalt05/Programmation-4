# Product Backlog 

## Projet 1

**Préprocesseur de documents Word vers Markdown**

## Objectif

Développer un préprocesseur en Python capable de lire un document Word (`.docx`), d’en extraire le contenu et la structure, puis de produire un Markdown propre et compatible avec CommonMark afin qu’il puisse ensuite être utilisé par Mistletoe pour générer du HTML.

## Product Backlog

### PB-01 — Structure du préprocesseur
**Priorité : Haute**
Créer la structure de base du préprocesseur en Python.


### PB-02 — Lecture d’un fichier Word
**Priorité : Haute**
Permettre au programme de recevoir et ouvrir un fichier `.docx`.

### PB-03 — Extraction du texte
**Priorité : Haute**
Extraire le texte contenu dans le document Word.

### PB-04 — Reconnaissance des paragraphes
**Priorité : Haute**
Reconnaître les paragraphes du document.

### PB-05 — Reconnaissance des titres
**Priorité : Haute**
Reconnaître les titres et leurs différents niveaux.

### PB-06 — Conversion des titres
**Priorité : Haute**
Convertir les titres Word en titres Markdown avec `#`, `##`, `###`, etc.

### PB-07 — Conversion des paragraphes
**Priorité : Haute**
Convertir les paragraphes du document en texte Markdown correctement structuré.

### PB-08 — Compatibilité CommonMark
**Priorité : Haute**
Générer un document Markdown compatible avec CommonMark.

### PB-09 — Compatibilité avec Mistletoe
**Priorité : Haute**
Vérifier que le Markdown généré peut être utilisé directement par Mistletoe.

### PB-10 — Markdown lisible
**Priorité : Haute**
Produire un Markdown lisible et bien structuré sans modifier le code source de Mistletoe.

### PB-11 — Texte en gras
**Priorité : Moyenne**
Ajouter le support du texte en gras.

### PB-12 — Texte en italique
**Priorité : Moyenne**
Ajouter le support du texte en italique.

### PB-13 — Listes à puces
**Priorité : Moyenne**
Ajouter le support des listes à puces.

### PB-14 — Listes numérotées
**Priorité : Moyenne**
Ajouter le support des listes numérotées.

### PB-15 — Hyperliens
**Priorité : Basse**
Ajouter le support des hyperliens.

### PB-16 — Tableaux
**Priorité : Basse**
Ajouter le support des tableaux présents dans les documents Word.

### PB-17 — Images
**Priorité : Basse**
Évaluer si les images présentes dans les documents Word doivent être supportées.


### PB-18 — Tests
**Priorité : Moyenne**
Tester le préprocesseur avec plusieurs documents Word ayant des structures différentes.

### PB-19 — Documents mal structurés
**Priorité : Moyenne**
Gérer autant que possible les documents Word mal structurés afin d’éviter un Markdown incorrect ou incomplet.