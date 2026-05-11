# Parcours IA ATOS — Squelettes & mini-cours techniques

> Formation **« Concevoir et implémenter une solution d'IA »** — certification CISIA / OPCO ATLAS.
> Parcours 2 — Professionnels IT (devs, DBAs, archis, intégrateurs).
> Promo ATOS · démarrage 19 mai 2026 · ~14 semaines · 156 h.

Ce repo Git **complète Simplonline** : il contient les **squelettes de code à
cloner** et les **mini-cours techniques synthétiques** auxquels chaque brief fait
référence. Les briefs eux-mêmes (énoncés, consignes, livrables, critères de
performance) sont **diffusés sur Simplonline**, pas ici.

---

## 📁 Structure

```
parcours-public/
├── README.md                                ← (ce fichier)
├── .gitignore
│
├── briefs/                                  ← un dossier par brief
│   ├── P0/                                  ← pré-démarrage (asynchrone)
│   │   ├── ressources/                      ← mini-cours synthétiques + README d'accueil
│   │   │   ├── README.md                    ← page d'accueil pédagogique du brief
│   │   │   ├── 01_*_essentiel.md            ← 1 mini-cours par techno principale
│   │   │   ├── 02_*_essentiel.md
│   │   │   ├── …
│   │   │   └── liens_officiels.md           ← URLs externes datées
│   │   └── squelette/                       ← repo de départ à cloner
│   └── M0-B1/                               ← Module 0, Brief 1
│       └── (idem)
│
└── scripts/                                 ← utilitaires apprenants
    └── merge_for_certif.py                  ← fusion notebook + journal en fin de parcours (M9)
```

Le **canevas du notebook certif** et le **journal de bord** sont dans un repo
séparé : <https://github.com/Formation-SIMPLON-IA/ia-atos-ressources>.

---

## 🚀 Démarrage rapide apprenants

### Pré-démarrage (avant le 19 mai)

1. Consulte le brief **P0** sur Simplonline (énoncé + 6 liens utiles).
2. Suis l'ordre de lecture donné dans
   [`briefs/P0/ressources/README.md`](./briefs/P0/ressources/README.md).
3. Clone le squelette `briefs/P0/squelette/` dans ton repo perso.
4. Produis ton notebook de présentation et envoie-le avant le **18/05 — 18 h**.

### Pendant la formation

À chaque nouveau brief :

1. Tu lis le brief sur **Simplonline** (énoncé + situation pro + livrables).
2. Tu suis les liens vers ce repo pour les **mini-cours** et le **squelette**.
3. Tu clones / `git pull` ce repo pour récupérer les nouveautés.

### Convention de nommage de tes repos perso

```
github.com/<ton-compte>/ia-atos-<contexte>-<prenom>
```

Exemples : `ia-atos-onboarding-julien`, `ia-atos-m0-b1-julien`.

---

## 🛠️ Utilitaire fin de parcours

Un seul script t'est utile dans ce repo, à mobiliser en **M9** quand tu prépareras
ton rendu certif (fusion du notebook principal et du journal de bord en un seul
fichier) :

```bash
python scripts/merge_for_certif.py <main.ipynb> <journal.ipynb> <output.ipynb>
```

Aucune dépendance externe : stdlib Python 3.11+ uniquement.

---

## 📐 Convention des mini-cours

Chaque mini-cours technique suit la même structure (lisibilité garantie) :

1. **Pourquoi cette techno ?** — problème résolu, alternatives, contexte
2. **Concepts clés** — 3 à 5 notions, pas plus
3. **Exemple minimal qui tourne** — bloc de code copy-paste qui marche
4. **Exercice guidé** — variante à faire, avec solution attendue
5. **Pour aller plus loin** — doc officielle, ressources approfondies
6. **Vérification** — checklist apprenant (« je sais expliquer en 2 min… »)

Volume cible : 8-12 pages markdown. Pas de cours fleuve, on vise dense et moderne.

---

## 📜 Statut & licence

Repo de travail pédagogique, usage interne formation ATOS Atlas IA — promo
démarrant le 19 mai 2026. Pour toute réutilisation extérieure, contacter la
formatrice.
