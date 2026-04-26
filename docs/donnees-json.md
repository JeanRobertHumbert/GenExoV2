# Format des données d'exercice

Référence rapide des structures JSON acceptées pour `donnees_json` selon
le sous-type. La validation se fait via JSON Schema, voir
[exercises/schemas.py](https://github.com/JeanRobertHumbert/GenExoV2/blob/fusion/main/exercises/schemas.py) pour la définition stricte.

Tous les sous-types acceptent en option `"shuffle_choix": true`
(qcm_unique, qcm_multiple uniquement) qui permute les choix à chaque
tirage.

## qcm_unique

```json
{
  "type": "qcm_unique",
  "consigne": "...",
  "choix": ["A", "B", "C", "D"],
  "reponse_index": 0,
  "explication": "(optionnel)",
  "shuffle_choix": true
}
```

## qcm_multiple

```json
{
  "type": "qcm_multiple",
  "consigne": "...",
  "choix": ["A", "B", "C", "D"],
  "reponses_index": [0, 2],
  "explication": "(optionnel)",
  "shuffle_choix": true
}
```

Scoring : `(bonnes - fausses) / total_attendu`, clampé à 0.

## vrai_faux

```json
{
  "type": "vrai_faux",
  "consigne": "...",
  "affirmations": [
    {"texte": "...", "vrai": true},
    {"texte": "...", "vrai": false}
  ]
}
```

Scoring : `corrects / total`.

## trous

```json
{
  "type": "trous",
  "texte_avec_trous": "Paris est [TROU:1] et Rome [TROU:2].",
  "reponses": ["la capitale de la France", "celle de l'Italie"],
  "casse_sensible": false
}
```

Marqueur `[TROU:N]` à partir de 1. Comparaison textuelle normalisée.

## calcul

```json
{
  "type": "calcul",
  "consigne": "Calcule ...",
  "reponse": 42,
  "tolerance": 0.001,
  "unite": "m"
}
```

`reponse` accepte int, float, ou string numérique. `tolerance` permet
les approximations (utile pour les fractions). L'élève peut saisir
`5/2`, `2,5`, `2.5` — tous parseés vers `2.5`.

## reponse_libre

```json
{
  "type": "reponse_libre",
  "consigne": "Explique pourquoi ...",
  "correction_modele": "(modèle de réponse)",
  "mots_cles": ["loi", "constitution"]
}
```

Correction manuelle par le prof (pas auto-corrigible).

## drag_drop

```json
{
  "type": "drag_drop",
  "consigne": "Place chaque item dans la bonne zone :",
  "items": ["item1", "item2", "item3"],
  "zones": ["zone A", "zone B"],
  "associations_correctes": [0, 1, 0]
}
```

`associations_correctes[i]` = index de la zone dans laquelle item `i`
doit être placé.

## association

```json
{
  "type": "association",
  "consigne": "Associe chaque pays à sa capitale :",
  "paires": [
    {"gauche": "France", "droite": "Paris"},
    {"gauche": "Italie", "droite": "Rome"}
  ]
}
```

## redaction, upload_fichier, schema_annote

Voir [`exercises/schemas.py`](https://github.com/JeanRobertHumbert/GenExoV2/blob/fusion/main/exercises/schemas.py) pour le détail.
Ces types nécessitent une correction manuelle.

## Variables paramétriques

Tous les champs string acceptent les placeholders `{{var}}` ou
`{{expr}}`. Si une string entière est `{{expr}}`, elle est convertie
en valeur typée (int / float / Fraction). Voir
[guide d'authoring](authoring.md) pour le détail.
