# Documentation SofEduc

Bienvenue sur la documentation officielle de **SofEduc**, plateforme EdTech
française pour générer, distribuer et corriger des devoirs en ligne ou
sur feuille.

## 🎯 Pour qui ?

| Rôle | Ce que SofEduc apporte |
|------|------------------------|
| 🧑‍🏫 **Professeurs** | Composer un devoir en quelques clics, faire générer 30 sujets paramétrés différents par élève, récupérer les copies corrigées automatiquement |
| 🎓 **Élèves** | Passer un devoir en ligne avec correction immédiate, saisir des formules avec un clavier mathématique, voir leur progression |
| 🏫 **Établissements** | Importer ses classes via ENT/SIECLE en une étape, configurer un SMTP partagé, suivre les statistiques d'usage |
| 👨‍👩‍👧 **Parents** | Suivre les devoirs en cours et les résultats de leur enfant |

## 🗺️ Naviguer dans la documentation

- **[Bilan fonctionnel par rôle](roles.md)** — ce que chaque rôle peut
  faire, URL par URL.
- **[Architecture technique](architecture.md)** — stack, apps Django,
  modèle d'exercice unifié, sécurité multi-tenant.
- **[Guide d'authoring d'exercices](authoring.md)** — créer des
  exercices paramétriques avec variables aléatoires et placeholders
  `{{n}}`.
- **[Format JSON des exercices](donnees-json.md)** — référence rapide
  des structures par sous-type (QCM, V/F, Trous, Calcul…).

## 🚀 Démo en ligne

L'instance de démonstration tourne en continu :
**[nauka-academy.org/se](https://nauka-academy.org/se/){:target="_blank"}**

!!! warning "Données de test uniquement"
    Cette instance est utilisée pour des tests réels. Ne pas y stocker
    de données sensibles.

## ⚖️ Licence et usage commercial

SofEduc est sous **licence propriétaire**.

- ✅ Évaluation et étude personnelles non-commerciales : autorisées
- ❌ Production, déploiement institutionnel, intégration commerciale :
  **interdits sans accord écrit**
- 💼 Licence commerciale disponible avec royalties

📧 **Contact** : [jeanroberthumbert@gmail.com](mailto:jeanroberthumbert@gmail.com)

---

<small>SofEduc / GenExoV2 — Construit en France 🇫🇷 par Jean-Robert Humbert.</small>
