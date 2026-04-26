# Architecture technique

## Stack

| Couche | Choix | Raison |
|--------|-------|--------|
| Langage | Python 3.12 | Stack Django / écosystème scientifique |
| Framework | Django 5.x | Multi-tenant, admin gratuit, ORM mature |
| DB prod | PostgreSQL 16 | JSONField indexé, fiabilité, support FR (encodage) |
| DB dev | SQLite | Setup zéro |
| Frontend | Templates Django + Bootstrap 5 | Pas de SPA, time-to-fix court |
| Rendu math | KaTeX + MathLive | Rapide, sans MathJax, clavier virtuel intégré |
| PDF | LuaLaTeX + TikZ + Fourier | Qualité typographique, paramétrique via Python |
| Auth | django-allauth (email-only) | Pas de username, gestion par email |
| Web server | Gunicorn + Nginx | Reverse proxy + statiques par WhiteNoise |
| Process manager | systemd | Restart auto, logs centralisés |

## Apps Django

```
genexo/                — Settings, URLs racine, dashboard
├── accounts/          — User custom (email login), AdminEtablissement,
│                        LienParentEleve, ProfesseurMatiere/Classe
├── assignments/       — Devoir, DevoirExercice, ResultatDevoir
│                        (devoirs en ligne)
├── exams/             — ExamTemplate, ExamRun, ExamExercise
│                        (devoirs sur feuille / PDF)
├── exercises/         — Exercice (modèle unifié, cf. ADR-002)
│                        + correction.py (correction automatique)
│                        + interpolation.py (variables paramétriques)
│                        + schemas.py (validation JSON par sous-type)
├── authoring/         — UserExercise (exos LaTeX paramétriques perso)
│                        + variables.py (DSL randint/sample/choice/…)
├── catalog/           — Catalogue national d'exercices Python
├── competences/       — Référentiels, domaines, compétences
├── core/              — Etablissement, Classe, Matiere, AcademieX
├── messagerie/        — Annonces unidirectionnelles (cf. ADR-003)
├── programmes/        — Niveau, Programme, Chapitre (BO)
└── students/          — Classes locales miroir (perso prof)
```

## Modèle Exercice unifié (ADR-002)

Un seul modèle `Exercice` couvre 4 types via `source_type` :

| `source_type` | Rendu | Champ porteur |
|---------------|-------|---------------|
| `catalog_python` | LaTeX (PDF) | `catalog_function_name` |
| `latex_statique` | LaTeX (PDF) | `latex_exo` + `latex_correction` |
| `interactif_json` | HTML/JS | `donnees_json` validé contre `schemas.py` |
| `parametrique_examtrainer` | HTML/JS | `generateur_code` + `generateur_params` |

Sous-types `interactif_json` (champ `donnees_json["type"]`) :
`qcm_unique`, `qcm_multiple`, `vrai_faux`, `trous`, `calcul`,
`reponse_libre`, `drag_drop`, `association`, `redaction`,
`upload_fichier`, `schema_annote`.

Chaque sous-type a un JSON Schema strict (`exercises/schemas.py`) qui
empêche l'introduction de structures aberrantes.

## Variables paramétriques (`exercises/interpolation.py`)

Le DSL est déclaré dans `authoring/variables.py` :

```python
n = randint(1, 6)
a = sample(range(1, 11), 3)
op = choice("+", "-", "×")
f = frac(1, 5)
```

Au rendu d'un exo (`PasserDevoirView.get` ou `DevoirSimulerView.get`) :

1. **Tirage** : `parse_and_tire(variables_script)` → `{n: 3}`
2. **Interpolation** : `interpoler_donnees(donnees_json, variables)`
   - Substitue `{{n}}`, `{{n*n - 9}}` dans toutes les chaînes du JSON.
   - Cas spécial : si une string entière est `{{expr}}`, retourne la
     valeur typée (`int`, `Fraction`, etc.) — utile pour la `reponse`.
3. **Shuffle** : si `donnees_json.shuffle_choix == True`, permute les
   choix QCM et ajuste `reponse_index` / `reponses_index`.
4. **Snapshot** : stocké en session (`passer_snapshot_<pk>` ou
   `simu_snapshot_<pk>`) pour que la correction utilise les **mêmes**
   valeurs que celles vues par l'élève.

## Sécurité multi-tenant

- Mixins centralisés dans `accounts/mixins.py` :
  `ProfesseurRequiredMixin`, `AdminEtablissementRequiredMixin`,
  `ParentRequiredMixin`, `ProfesseurOuAdminEtabRequiredMixin`.
- Toutes les vues sensibles (création de devoir, suppression d'utilisateur,
  configuration SMTP étab) appliquent un mixin.
- Filtrage queryset systématique : `Devoir.objects.filter(professeur=user)`.
- Pour les actions destructives en masse (`devoir_bulk_delete`,
  `utilisateurs_bulk_delete`) : intersection avec le queryset autorisé
  AVANT le `.delete()`, jamais une suppression sur PKs reçus bruts.
- Tests automatisés des permissions : `tests/test_permissions.py`,
  `tests/test_module_parent.py`.

## Sécurité des données élève

- Les CSV ENT importés sont stockés en `mediafiles/ent_tmp/user_<pk>_etab_<pk>.csv`
  pour la durée de la session d'import, puis supprimés.
- Mots de passe hashés (PBKDF2 par défaut Django).
- Imports ENT créent les comptes avec `set_unusable_password()` ; le
  flux d'invitation envoie un lien d'activation à durée limitée.

## Déploiement

```
[Internet] → [Nginx :443] → [Gunicorn :8003] → [Django] → [PostgreSQL]
                                                       └ [Lua-LaTeX] (PDF on demand)
```

Gunicorn lancé par systemd via `deploy/sofeduc.service` :
3 workers, timeout 90s, capture-output.

NOPASSWD configuré dans `/etc/sudoers.d/sofeduc` pour les commandes
`systemctl restart/reload/status/start/stop/daemon-reload sofeduc`,
permettant un redéploiement automatique sans interaction.

## Tests

```bash
python manage.py test
# 82 tests verts, 5 skipped (modèles refactorés depuis l'import)
```

Couverture :
- Permissions par rôle (élève, prof, parent, admin étab, staff)
- Module parent (cloisonnement, redirect home)
- Dashboard admin étab (KPI, taux d'activation)
- Messagerie (modèles + vues auteur + vues lecteur)
- Compétences (CRUD permissions)
- Programmes (seed, copie de référentiel)

## Contact

Pour les choix d'architecture détaillés et leurs conséquences, voir les
ADR (Architecture Decision Records) dans `memory/decisions.md`.
