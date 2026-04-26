# Guide d'authoring d'exercices

Ce guide montre comment créer un exercice **interactif en ligne** dans
SofEduc. Pour les exercices LaTeX (devoir sur feuille), voir le
catalogue Python paramétrique dans `catalog/` et les modèles
`UserExercise` de l'app `authoring`.

## Concepts

Un exercice interactif contient deux champs essentiels :

- **Script de variables** (optionnel) — un mini-langage pour tirer des
  valeurs aléatoires à chaque tentative.
- **Données JSON** — le contenu de l'exercice (consigne, choix, réponse…).
  Le format dépend du sous-type (`qcm_unique`, `vrai_faux`, etc.).

Au moment où l'élève passe l'exercice, le script est exécuté, les
valeurs sont substituées dans le JSON via les placeholders
`{{nom}}` ou `{{expression}}`, et le résultat est rendu.

## Script de variables

Une assignation par ligne, syntaxe `nom = expression`.

| Fonction | Effet | Exemple |
|----------|-------|---------|
| `randint(low, high)` | entier aléatoire entre `low` et `high` inclus | `n = randint(1, 10)` |
| `randint(low, high, exclude=[…], not_null=True)` | avec exclusions | `n = randint(2, 8, exclude=[5])` |
| `sample(pool, k)` | `k` éléments distincts | `xs = sample(range(1, 11), 3)` |
| `choice(*options)` | un parmi plusieurs | `op = choice("+", "-", "×")` |
| `frac(low, high)` | fraction aléatoire | `f = frac(1, 5)` |
| `randints(count, low, high)` | liste de `count` entiers | `vs = randints(3, 1, 10)` |
| `range(a, b)` | liste `[a, …, b-1]` | utilisé dans `sample` |

Les fonctions `if`/`for`/`while` Python ne sont **pas** acceptées —
le DSL est volontairement restreint pour la sécurité.

## Placeholders dans le JSON

Dans n'importe quelle chaîne du JSON, écrire `{{expression}}` substitue
la valeur évaluée :

| Placeholder | Effet |
|-------------|-------|
| `{{n}}` | valeur de `n` |
| `{{n*n - 9}}` | expression arithmétique évaluée |
| `{{a**2}}` | puissance |
| `{{2*a*b}}` | combinaison de variables |

**Règle clé** : si une chaîne entière est `"{{expr}}"`, le système
retourne la valeur typée (`int`, `float`, `Fraction`). Pratique pour
la `reponse` : `"reponse": "{{n*n - 9}}"` devient un `int 16` quand
`n=5`, prêt pour la comparaison automatique avec la saisie élève.

## Exemple complet — QCM aléatoire avec shuffle

```json
{
  "type": "qcm_unique",
  "shuffle_choix": true,
  "consigne": "$({{a}}x+{{b}})^2 =$",
  "choix": [
    "${{a**2}}x^2 + {{2*a*b}}x + {{b**2}}$",
    "${{a**2}}x^2 + {{a*b}}x + {{b**2}}$",
    "${{a**2}}x^2 + {{2*a*b}}x + {{b}}$",
    "$x^2 + {{b**2}}$"
  ],
  "reponse_index": 0
}
```

Avec script :
```
a = randint(1, 6)
b = randint(1, 6)
```

À chaque tentative :
1. `a` et `b` sont tirés (par ex. `a=3`, `b=4`)
2. La consigne devient `(3x+4)^2 =`
3. Les 4 choix sont calculés (`9x^2+24x+16`, `9x^2+12x+16`, etc.)
4. `shuffle_choix: true` permute aléatoirement les 4 choix
5. `reponse_index` est ajusté pour pointer sur le bon nouveau choix
6. La correction utilise le snapshot stocké en session

## Exemple — Calcul

```json
{
  "type": "calcul",
  "consigne": "Calcule $({{a}})^2 + ({{b}})^2$.",
  "reponse": "{{a**2 + b**2}}",
  "tolerance": 0
}
```

Le système accepte les formes `25` (int), `25.0`, `25,0` (virgule FR),
`5/1` (fraction simple). Pour des réponses approchées (ex. `1/3`),
préciser `"tolerance": 0.001`.

## Exemple — Vrai/Faux multi-affirmations

```json
{
  "type": "vrai_faux",
  "consigne": "Coche Vrai ou Faux pour chaque affirmation :",
  "affirmations": [
    {"texte": "$5 > 3$", "vrai": true},
    {"texte": "$\\pi$ est un entier", "vrai": false},
    {"texte": "$2^3 = 8$", "vrai": true}
  ]
}
```

Les affirmations sont rendues côte à côte ; l'élève clique Vrai ou
Faux pour chacune ; le score est `corrects / total`.

## Exemple — Trous

```json
{
  "type": "trous",
  "texte_avec_trous": "La capitale de la France est [TROU:1] et celle de l'Italie est [TROU:2].",
  "reponses": ["Paris", "Rome"],
  "casse_sensible": false
}
```

Marqueur `[TROU:N]` (avec N le rang de la réponse, à partir de 1).
Comparaison textuelle, normalisation de la casse par défaut.

## Saisie de la réponse côté élève

Le rendu intègre :

- **Clavier mathématique** virtuel (MathLive) pour saisir fractions,
  racines, intégrales, puissances. Le résultat est inséré au curseur
  en notation ASCII-math (`1/2`, `sqrt(x)`, `x^2`).
- **Calculatrice** popup numérique si `donnees_json.calculatrice_autorisee`
  est `true` (par défaut).
- Saisie **directe au clavier** acceptée (l'élève peut taper `1/9` ou
  `0.5` sans utiliser MathLive).

## Aperçu et simulation

- **Aperçu individuel** (`/exercices/<pk>/apercu/`) : voir l'exo en
  mode élève. Les variables sont tirées à chaque rechargement (un
  nouveau jeu à chaque visite). Panneau dépliable « Voir la réponse
  attendue (mode prof) » qui affiche la réponse.
- **Simulation prof** (`/assignments/<pk>/simuler/`) : passer un
  devoir entier en mode élève sans rien enregistrer en base. Récap
  complet à la soumission avec score, feedback et bonne réponse pour
  chaque exo.

## Erreurs courantes

| Symptôme | Cause | Fix |
|----------|-------|-----|
| « Saisissez du contenu JSON valide » | `{{expr}}` non quoté | Le form auto-wrappe ; sinon écrire `"{{expr}}"` |
| « Erreur dans le script de variables » | syntaxe Python invalide (ex. `1..5`) | Utiliser `randint(1, 5)` ou `range(1, 6)` |
| Aperçu vide | `donnees_json["type"]` manquant ou inconnu | Vérifier que le type est dans `exercises/schemas.py` |
| Réponse refusée alors qu'elle semble correcte | comparaison stricte sur fraction | Ajouter `"tolerance": 0.001` |
| Choix QCM toujours dans le même ordre | `shuffle_choix` absent | Ajouter `"shuffle_choix": true` |

## Pour aller plus loin

- Schémas JSON par sous-type : `exercises/schemas.py`
- Logique de correction : `exercises/correction.py`
- Tirage et interpolation : `exercises/interpolation.py`
- DSL des variables : `authoring/variables.py`
