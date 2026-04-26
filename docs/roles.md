# Bilan fonctionnel par rôle

SofEduc définit 5 rôles, chacun avec un périmètre fonctionnel propre.
Multi-tenant : un professeur ne voit que ses propres devoirs et ses
classes ; un admin étab ne voit que les utilisateurs de son
établissement.

## 🎓 Élève (`is_eleve`)

| Fonctionnalité | URL |
|----------------|-----|
| Tableau de bord (devoirs à faire, résultats récents, progression) | `/` |
| Liste des devoirs publiés à rendre | `/assignments/mes-devoirs/` |
| Historique des résultats notés | `/assignments/mes-resultats/` |
| Passer un devoir | `/assignments/<pk>/passer/` |
| Détail d'une copie corrigée | `/assignments/<pk>/mon-resultat/` |
| Catalogue des programmes officiels | `/programmes/` |
| Grille de compétences personnelle | `/competences/mes-competences/` |
| Mes annonces (avec badge non-lu) | `/messagerie/mes-annonces/` |
| Aide dédiée | `/comptes/aide/eleve/` |

## 🧑‍🏫 Professeur (`is_professeur`)

### Devoirs en ligne (apps `assignments`, `messagerie`)
- CRUD complet des devoirs (titre, classes, dates, type)
- Composer un devoir avec les exercices `interactif_json` de la banque
- Filtres par matière, niveau, chapitre, type, difficulté, recherche
- Total des points calculé en temps réel
- Aperçu mode élève + mode simulation (rien n'est enregistré)
- Statistiques de lecture des annonces

### Devoirs sur feuille (app `exams`)
- Templates d'examens paramétrés (LaTeX/Python)
- Génération PDF par lualatex + TikZ
- 3 sujets différents par classe
- Correction automatique générée en parallèle

### Authoring d'exercices
- CRUD exercices personnels (`Exercice` model unifié)
- Paramétrisation : variables aléatoires (`randint`, `sample`, `choice`…)
- Substitution `{{var}}` et `{{expr}}` dans la consigne, les choix, la réponse
- Shuffle des choix QCM
- Statuts : brouillon / publié / partagé (banque commune)

### Communication
- Annonces ciblées par classe (élèves, parents, ou les deux)
- Tests SMTP + envoi d'invitations à activer un compte

### Profil
- Configuration SMTP perso ou héritée de l'étab
- Matières et niveaux enseignés

## 👨‍👩‍👧 Parent (`is_parent`)

- Liste des enfants liés (via `LienParentEleve`, créé à l'import ENT)
- Pour chaque enfant : devoirs en cours, résultats, annonces ciblant les parents
- Cloisonnement strict : un parent ne peut pas accéder aux données d'un
  enfant qui ne lui est pas lié.
- Si un seul enfant : redirection automatique vers son tableau de bord.

## 🏫 Admin d'établissement (`is_admin_etablissement`)

- Hub `/comptes/etab/` avec KPI : utilisateurs par rôle, taux d'activation
  des comptes, classes actives, devoirs publiés, devoirs en cours,
  moyenne globale, top 5 matières, tentatives sur 30 jours.
- CRUD utilisateurs (création, édition, suppression, suppression en masse)
- Invitation par email (lien d'activation)
- Import ENT/SIECLE par CSV (avec dry-run, lien parent-enfant automatique)
- Modèles d'import réutilisables
- Configuration SMTP étab (partagée par tous les profs)
- Vue admin de tous les devoirs de l'établissement

## 🛠️ Staff Django (`is_staff`)

- Accès à `/admin/` (admin Django complet)
- Bypass des restrictions multi-tenant (peut tout voir)
- Tous les pouvoirs des rôles précédents
