# 📘 Guide d’utilisation du fichier JSON — GenExoV2

Ce document décrit la structure et l’usage du fichier JSON utilisé par **GenExoV2** pour configurer la génération d’un examen.

---

## 🎯 Objectif

Le fichier JSON permet de **décrire intégralement un sujet d’examen** sans modifier le code Python.  
Il contient deux sections principales :

- `meta` : les métadonnées générales de l’examen (titre, durée, classe, etc.)  
- `exercices` : la liste ordonnée des exercices qui composent le sujet

---

## 🧩 Structure générale

```json
{
    "meta": { ... },
    "exercices": [ ... ]
}
```

---

## 🧠 Section `meta`

Cette section regroupe les **informations descriptives** de l’examen.

| Clé | Type | Description | Exemple |
|-----|------|--------------|--------|
| `title` | string | Titre complet du sujet | "Devoir Commun N°1 TSTMG" |
| `source` | string | Nom du générateur ou de la version de GenExoV2 | |
| `dateOfExam` | string | Date de l’évaluation au format `DD/MM/YYYY` | |
| `points` | number | Total des points du devoir | 40 |
| `bonus` | number | Points Bonus (rédaction, soin, etc.) | 5 |
| `duree` | string | Durée de l’épreuve | "2 heures" |
| `consignes` | array(string) | Liste des consignes à afficher sur le sujet | [
|             |               |                                             |   "La calculatrice n'est pas autorisée",
|             |               |                                             |   "Le téléphone n’est pas autorisé, même comme calculatrice",
|             |               |                                             |   "Le bonus est accordé selon la qualité de la rédaction et du soin"
|             |               |                                             | ], |
| `classe` | string \| null | Nom de la classe concernée (ou `null` si examen générique) | "TSTMG1" |
| `CSVfile` | string \| null | Fichier CSV des élèves à utiliser (ou `null` si aucun) | "TSTMG1.csv" dans le sous-répertoire /csv|
| `nbAnonymous` | integer | Nombre de copies anonymes à générer | 4 |

### Exemple : (pas de lecture de fichier csv et 1 seule copie Anonyme)

```json
"meta": {
    "title": "Devoir Commun N°1 TSTMG",
    "source": "GenExoV2",
    "dateOfExam": "03/11/2025",
    "points": 43,
    "bonus": 2,
    "duree": "1 heure",
    "consignes": [
        "La calculatrice n'est pas autorisée",
        "Le téléphone n’est pas autorisé, même comme calculatrice",
        "Le bonus est accordé selon la qualité de la rédaction et du soin"
    ],
    "classe": "TSTMG1",
    "CSVfile": null,
    "nbAnonymous": 1
}
```

---

## 🧮 Section `exercices`

Cette section définit **l’ordre et la composition du sujet**.  
Elle est constituée d’une **liste ordonnée** d’objets, chacun décrivant un exercice.

Chaque objet contient au minimum :

| Clé | Type | Description |
|-----|------|--------------|
| `name` | string | Nom de la fonction Python correspondant à l’exercice |
| `repeat` | integer | Nombre de répétitions de cet exercice |

Exemple :
```json
"exercices": [
    { "name": "exoTableauEvolution", "repeat": 1 },
    { "name": "addClearPage", "repeat": 1 },
    { "name": "evolSchema2", "repeat": 1 },
    { "name": "addClearPage", "repeat": 1 },
    { "name": "exoP1Type4", "repeat": 1 },
    { "name": "exoP1Type5", "repeat": 1 },
    { "name": "exoP1Type6", "repeat": 1 },
    { "name": "exoP1Type7", "repeat": 1 },
    { "name": "exoP1Type8", "repeat": 1 },
    { "name": "exoP1Type9", "repeat": 1 },
    { "name": "exoP1Type10", "repeat": 1 },
    { "name": "exoProportion", "repeat": 1 }
]
```

### ➕ Extensions possibles

Chaque entrée peut contenir d’autres champs, par exemple :

```json
{ 
    "name": "exoP1Type9",
    "repeat": 1
}
```

---

## 🚀 Bonnes pratiques

- 🔒 **Respecter l’ordre** des exercices (liste, pas dictionnaire)
- 🧱 **Toujours valider le JSON** avant exécution :  
  ```bash
  python -m json.tool exam_TSTMG1.json
  ```
- 🧠 **Utiliser `null`** au lieu de `None` pour les valeurs absentes
- 🏷️ **Conserver un `_comment`** facultatif pour annoter ton JSON :
  ```json
  "_comment": "Sujet de test – version de novembre 2025"
  ```

---

## ✅ Exemple complet

```json
{
    "meta"  : {
        "title"       : "Devoir Commun N°1 TSTMG",
        "source"      : "GenExoV2",
        "dateOfExam"  : "03/11/2025",
        "points"      : 43,
        "bonus"       : 2,
        "duree"       : "1 heure",
        "consignes"   : [
            "La calculatrice n'est pas autorisée",
            "Le téléphone n’est pas autorisé, même comme calculatrice",
            "Le bonus est accordé selon la qualité de la rédaction et du soin"
        ],
        "classe"      : "TSTMG1",
        "CSVfile"     : null,
        "nbAnonymous" : 1
    },

    "exercices": [
        { "name": "exoTableauEvolution", "repeat": 1 },
        { "name": "addClearPage", "repeat": 1 },
        { "name": "evolSchema2", "repeat": 1 },
        { "name": "addClearPage", "repeat": 1 },
        { "name": "exoP1Type4", "repeat": 1 },
        { "name": "exoP1Type5", "repeat": 1 },
        { "name": "exoP1Type6", "repeat": 1 },
        { "name": "exoP1Type7", "repeat": 1 },
        { "name": "exoP1Type8", "repeat": 1 },
        { "name": "exoP1Type9", "repeat": 1 },
        { "name": "exoP1Type10", "repeat": 1 },
        { "name": "exoProportion", "repeat": 1 }
    ]
}
```

---

© 2025 — **Jean-Robert Humbert**  
Documentation du format JSON pour **GenExoV2**
