<div align="center">

# 🎓 SofEduc

### Plateforme EdTech française pour générer, distribuer et corriger des devoirs en ligne ou sur feuille.

[![Statut](https://img.shields.io/badge/statut-prod-success)](https://nauka-academy.org/se/)
[![Licence](https://img.shields.io/badge/licence-Propri%C3%A9taire-red)](LICENSE)
[![Tests](https://img.shields.io/badge/tests-82%20verts-brightgreen)](#-tests)
[![Python](https://img.shields.io/badge/Python-3.12-3776ab?logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.x-092e20?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-336791?logo=postgresql&logoColor=white)](https://www.postgresql.org/)

[**Démo en ligne**](https://nauka-academy.org/se/) · [**Documentation**](https://jeanroberthumbert.github.io/GenExoV2/) · [Licence commerciale](#%EF%B8%8F-licence)

</div>

---

## 🎯 À qui s'adresse SofEduc ?

| Rôle | Ce que SofEduc apporte |
|------|------------------------|
| 🧑‍🏫 **Professeurs** | Composer un devoir en quelques clics, faire générer 30 sujets paramétrés différents par élève, récupérer les copies corrigées automatiquement |
| 🎓 **Élèves** | Passer un devoir en ligne avec correction immédiate, saisir des formules avec un clavier mathématique, voir leur progression |
| 🏫 **Établissements** | Importer ses classes via ENT/SIECLE en une étape, configurer un SMTP partagé, suivre les statistiques d'usage |
| 👨‍👩‍👧 **Parents** | Suivre les devoirs en cours et les résultats de leur enfant |

## ✨ Fonctionnalités

### 📐 Authoring d'exercices
- **454+ exercices** prêts à l'emploi (Maths, Droit, Économie, Management, SES…)
- **Variables aléatoires** : chaque tentative tire un jeu de valeurs unique
  ```python
  # Script de variables
  a = randint(1, 6)
  b = randint(1, 6)

  # Données JSON
  {"type": "qcm_unique", "shuffle_choix": true,
   "consigne": "$({{a}}x+{{b}})^2 =$",
   "choix": ["${{a**2}}x^2 + {{2*a*b}}x + {{b**2}}$", ...]}
  ```
- **Shuffle** des choix QCM pour chaque élève
- **Multi-niveaux** et **multi-chapitres** par exercice
- **Assistant de paramétrisation** dans l'UI

### 💻 Devoirs en ligne (interactifs)
- 8 types : QCM, V/F, Trous, Calcul, Réponse libre, Drag-Drop, Association, Rédaction
- Rendu **KaTeX** des formules en temps réel
- **Clavier mathématique** virtuel (MathLive) pour les fractions, racines, intégrales
- **Calculatrice** popup conditionnelle (selon `calculatrice_autorisee`)
- Correction **automatique** avec barème, tolérance, fractions acceptées (`1/9`)
- **Mode simulation** prof : tester un devoir sans polluer les statistiques

### 📄 Devoirs sur feuille (LaTeX → PDF)
- Génération paramétrique via `lualatex` + TikZ + Fourier
- 3 sujets différents par classe en une commande
- Correction PDF générée en parallèle
- 144+ fonctions Python paramétriques (catalogue national)

### 🔐 Multi-tenant & sécurité
- Isolation stricte par établissement (filtrage queryset systématique)
- Rôles : Élève · Professeur · Parent · Admin Étab · Staff
- Authentification email (django-allauth)
- Tests de permissions automatisés sur les vues critiques

### 📨 Communication
- **Annonces** ciblées par classe (élèves et/ou parents)
- Stats de lecture en temps réel
- Badge non-lu dans la sidebar
- Notification email de première connexion personnalisée par établissement (UAI dans le sujet)

### 📊 Pilotage
- Tableau de bord admin étab : nb users par rôle, taux d'activation, devoirs publiés, moyenne globale, tentatives 30j
- Top matières par nb de devoirs
- Stats par enfant pour les parents

## 🚀 Démo

L'instance de démonstration tourne en continu : **[nauka-academy.org/se](https://nauka-academy.org/se/)**

> ⚠️ Cette instance est utilisée pour des tests réels. Ne stocker aucune donnée sensible.

## 📚 Documentation

| Document | Pour qui ? |
|----------|-----------|
| [Bilan fonctionnel par rôle](docs/roles.md) | Comprendre ce que chaque rôle peut faire |
| [Architecture technique](docs/architecture.md) | Développeurs, intégrateurs |
| [Guide d'authoring d'exercices](docs/authoring.md) | Profs qui créent leurs propres exos |
| [Format des données d'exercice](docs/donnees-json.md) | Authoring avancé (JSON brut) |
| [Décisions techniques (ADR)](https://github.com/JeanRobertHumbert/GenExoV2/tree/fusion/main/memory) | Historique des choix |

## 🛠️ Stack

```
┌─ Frontend ─────────────────┬─ Backend ──────────┬─ Infra ─────────────┐
│ Bootstrap 5                │ Python 3.12        │ Ubuntu / systemd    │
│ KaTeX (rendu LaTeX inline) │ Django 5.x         │ PostgreSQL 16       │
│ MathLive (clavier maths)   │ django-allauth     │ Gunicorn            │
│ HTMX (interactions légères)│ jsonschema         │ Nginx (reverse proxy)│
└─ — ────────────────────────┴─ — ────────────────┴─ — ─────────────────┘
                              ┌─ PDF ──────────────┐
                              │ LuaLaTeX           │
                              │ TikZ + Fourier     │
                              │ ImageMagick        │
                              └─ — ────────────────┘
```

## 🧪 Tests

```bash
python manage.py test
# → 82 tests verts, 5 skipped (modèles refactorés)
```

Couvre : permissions par rôle, multi-tenant, import ENT, correction automatique, messagerie, dashboard.

## ⚖️ Licence

**SofEduc est sous licence propriétaire**. Voir [LICENSE](LICENSE).

- ✅ Évaluation et étude **personnelles non-commerciales** : autorisées
- ❌ Production, déploiement institutionnel, intégration commerciale : **interdits sans accord écrit**
- 💼 **Licence commerciale** disponible avec royalties — l'auteur peut adapter les conditions à votre contexte (école, université, organisme de formation, SaaS tiers)

📧 **Contact** : [jeanroberthumbert@gmail.com](mailto:jeanroberthumbert@gmail.com)

## 👤 Auteur

**Jean-Robert Humbert** — professeur de mathématiques, auteur de SofEduc.

---

<div align="center">
  <sub>Construit en France 🇫🇷 pour les profs qui veulent reprendre la main sur leurs outils.</sub>
</div>
