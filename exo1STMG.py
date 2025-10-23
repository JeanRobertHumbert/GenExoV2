import os,sys
import random
import unicodedata
import numpy as np
from sympy import *
import matplotlib.pyplot as plt
from fractions import Fraction

from baseMaths import *
##--------------------------------- EXERCICES STMG - PARTIE 1 ---------------------------------##
""""""
def exoP1Type1(id=False):
    if id:
        identification = r"""exoP1Type1\\"""  
    else:
        identification = r""""""  

    # --- Données aléatoires ---
    prenom = random.choice([
        "Jean","Marie","Luc","Sophie","Paul","Laura","Pierre","Julie","Mohamed","Emma","Babou",
        "Chloé","Léa","Camille","Manon","Inès","Sarah","Anaïs","Clara","Juliette",
        "Ali","Youssef","Zinedine","Fatima","Aïcha","Hassan","Omar"
    ])
    propJournee = random.choice([20, 30, 40, 50])
    propExpose = random.choice([20, 25, 50, 75, 80])

    # --- Calcul de la bonne réponse ---
    bonne_valeur = round(propJournee * propExpose / 100, 0)

    # --- Génération de fausses réponses cohérentes ---
    erreurs = []
    while len(erreurs) < 3:
        delta = random.choice([-15,-10,-5,5,10,15])
        faux = bonne_valeur + delta
        if faux > 0 and faux not in erreurs and faux != bonne_valeur:
            erreurs.append(faux)

    # --- Mélange et placement aléatoire ---
    toutes_valeurs = erreurs + [bonne_valeur]
    random.shuffle(toutes_valeurs)
    lettres = ["A", "B", "C", "D"]

    # --- Trouver la position correcte ---
    index_bonne_reponse = toutes_valeurs.index(bonne_valeur)
    lettre_bonne_reponse = lettres[index_bonne_reponse]

    # --- Construction du tableau LaTeX pour la question ---
    lignes = []
    for i, val in enumerate(toutes_valeurs):
        lignes.append(rf"\textbf{{{lettres[i]}}} : ${val}\%$")
    tab_latex = r" & ".join(lignes) + r" \\ \hline"

    # --- Énoncé LaTeX ---
    exo = identification + rf"""
    \question[1] {prenom} consacre {propJournee}\% de sa journée de dimanche à faire ses devoirs. {propExpose}\% du temps consacré aux devoirs est consacré à faire un exposé. Le pourcentage du temps consacré à l’exposé par rapport à la journée de dimanche est égal à :
    \vspace{{-2em}}
    \begin{{center}}
        \begin{{tabular}}{{|
            >{{\centering\arraybackslash}}m{{3.5cm}}|
            >{{\centering\arraybackslash}}m{{3.5cm}}|
            >{{\centering\arraybackslash}}m{{3.5cm}}|
            >{{\centering\arraybackslash}}m{{3.5cm}}|}}
        \hline
        {tab_latex}
        \end{{tabular}}
    \end{{center}}
"""

    # --- Construction du tableau LaTeX pour la correction ---
    lignes_corr = []
    for i, val in enumerate(toutes_valeurs):
        if i == index_bonne_reponse:
            lignes_corr.append(
                rf"\textbf{{{lettres[i]}}} : \textcolor{{red}}{{${val}\%$}}"
            )
        else:
            lignes_corr.append(rf"\textbf{{{lettres[i]}}} : ${val}\%$")
    tab_corr = r" & ".join(lignes_corr) + r" \\ \hline"

    correction = identification + rf"""
    \question[1] {prenom} consacre {propJournee}\% de sa journée de dimanche à faire ses devoirs. {propExpose}\% du temps consacré aux devoirs est consacré à faire un exposé. Le pourcentage du temps consacré à l’exposé par rapport à la journée de dimanche est égal à :
    \vspace{{-2em}}
    \begin{{center}}
        \begin{{tabular}}{{|
            >{{\centering\arraybackslash}}m{{3.5cm}}|
            >{{\centering\arraybackslash}}m{{3.5cm}}|
            >{{\centering\arraybackslash}}m{{3.5cm}}|
            >{{\centering\arraybackslash}}m{{3.5cm}}|}}
        \hline
        {tab_corr}
        \end{{tabular}}
    \end{{center}}
"""

    return (exo, correction)

def exoP1Type2(id=False):
    """Generate a multiple-choice question about percentage changes."""
    if id:
        identification = r"""exoP1Type2\\"""  
    else:
        identification = r""""""  

    # --- Données aléatoires ---
    tauxEvolution = random.choice([-50, -20, 25])*sign(random.choice([-1,1])
)
    

    # --- Calcul de la bonne réponse ---
    bonne_valeur = round((1/(1+tauxEvolution/100)-1)*100, 0)

    # --- Génération de fausses réponses cohérentes ---
    erreurs = set()
    essais = 0
    while len(erreurs) < 3 and essais < 50:
        delta = random.choice([-15, -10, -5, 5, 10, 15])
        faux = bonne_valeur + delta
        essais += 1
        if faux != bonne_valeur and faux not in erreurs:
            erreurs.add(faux)

    # Sécurité : si on n’a pas 3 erreurs, on complète arbitrairement
    while len(erreurs) < 3:
        erreurs.add(bonne_valeur + random.randint(1, 20))

    erreurs = list(erreurs)

    # --- Mélange et placement aléatoire ---
    toutes_valeurs = erreurs + [bonne_valeur]
    random.shuffle(toutes_valeurs)
    lettres = ["A", "B", "C", "D"]

    # --- Trouver la position correcte ---
    index_bonne_reponse = toutes_valeurs.index(bonne_valeur)
    lettre_bonne_reponse = lettres[index_bonne_reponse]

    # --- Construction du tableau LaTeX pour la question ---
    lignes = []
    for i, val in enumerate(toutes_valeurs):
        lignes.append(rf"\textbf{{{lettres[i]}}} : ${val}\%$")
    tab_latex = r" & ".join(lignes) + r" \\ \hline"
    if tauxEvolution > 0:
        enonce = rf"""Un prix augmente de {abs(tauxEvolution)}\%. Pour retrouver le prix initial, il faut une diminution de :"""
    else:
        enonce = rf"""Un prix diminue de {abs(tauxEvolution)}\%. Pour retrouver le prix initial, il faut une augmentation de :"""
    # --- Énoncé LaTeX ---
    exo = identification + rf"""
        \question[1] {enonce}
            \vspace{{-2em}}
            \begin{{center}}
                \begin{{tabular}}{{|
                    >{{\centering\arraybackslash}}m{{3.5cm}}|
                    >{{\centering\arraybackslash}}m{{3.5cm}}|
                    >{{\centering\arraybackslash}}m{{3.5cm}}|
                    >{{\centering\arraybackslash}}m{{3.5cm}}|}}
                \hline
                {tab_latex}
                \end{{tabular}}
            \end{{center}}
"""

    # --- Construction du tableau LaTeX pour la correction ---
    lignes_corr = []
    for i, val in enumerate(toutes_valeurs):
        if i == index_bonne_reponse:
            lignes_corr.append(
                rf"\textbf{{{lettres[i]}}} : \textcolor{{red}}{{${val}\%$}}"
            )
        else:
            lignes_corr.append(rf"\textbf{{{lettres[i]}}} : ${val}\%$")
    tab_corr = r" & ".join(lignes_corr) + r" \\ \hline"

    correction = identification + rf"""
    \question[1] {enonce}
    \vspace{{-2em}}
    \begin{{center}}
        \begin{{tabular}}{{|
            >{{\centering\arraybackslash}}m{{3.5cm}}|
            >{{\centering\arraybackslash}}m{{3.5cm}}|
            >{{\centering\arraybackslash}}m{{3.5cm}}|
            >{{\centering\arraybackslash}}m{{3.5cm}}|}}
        \hline
        {tab_corr}
        \end{{tabular}}
    \end{{center}}
"""

    return (exo, correction)

def exoP1Type3(id=False):
    """Generate a multiple-choice question about multiplication factors."""
    if id:
        identification = r"""exoP1Type3\\"""  
    else:
        identification = r""""""  

    # --- Données aléatoires ---
    prix = random.choice([100, 150, 200, 250, 300, 350, 400])
    tauxEvolution = random.choice([10, 20, 25, 50, 75, 100])*sign(random.randint(-1,1))
    nouveauPrix = round(prix*(1+tauxEvolution/100), 0)  
    # --- Calcul de la bonne réponse ---
    bonne_valeur = round(1+tauxEvolution/100, 2)

    # --- Génération de fausses réponses cohérentes ---
    erreurs = []
    while len(erreurs) < 3:
        delta = random.choice([-15,-10,-5,5,10,15])
        faux = bonne_valeur + delta
        if faux > 0 and faux not in erreurs and faux != bonne_valeur:
            erreurs.append(faux)

    # --- Mélange et placement aléatoire ---
    toutes_valeurs = erreurs + [bonne_valeur]
    random.shuffle(toutes_valeurs)
    lettres = ["A", "B", "C", "D"]

    # --- Trouver la position correcte ---
    index_bonne_reponse = toutes_valeurs.index(bonne_valeur)
    lettre_bonne_reponse = lettres[index_bonne_reponse]

    # --- Construction du tableau LaTeX pour la question ---
    lignes = []
    for i, val in enumerate(toutes_valeurs):
        lignes.append(rf"\textbf{{{lettres[i]}}} : ${val}$")
    tab_latex = r" & ".join(lignes) + r" \\ \hline"
    if tauxEvolution > 0:
        enonce = rf"""Le prix d’une tablette a augmenté : il est passé de {prix} euros à {nouveauPrix} euros. Cela signifie que ce prix a été multiplié par :"""
    else:
        enonce = rf"""Le prix d’une tablette a diminué : il est passé de {prix} euros à {nouveauPrix} euros. Cela signifie que ce prix a été multiplié par :"""
    # --- Énoncé LaTeX ---
    exo = identification + rf"""
        \question[1] {enonce}
            \vspace{{-2em}}
            \begin{{center}}
                \begin{{tabular}}{{|
                    >{{\centering\arraybackslash}}m{{3.5cm}}|
                    >{{\centering\arraybackslash}}m{{3.5cm}}|
                    >{{\centering\arraybackslash}}m{{3.5cm}}|
                    >{{\centering\arraybackslash}}m{{3.5cm}}|}}
                \hline
                {tab_latex}
                \end{{tabular}}
            \end{{center}}
"""

    # --- Construction du tableau LaTeX pour la correction ---
    lignes_corr = []
    for i, val in enumerate(toutes_valeurs):
        if i == index_bonne_reponse:
            lignes_corr.append(
                rf"\textbf{{{lettres[i]}}} : \textcolor{{red}}{{${val}$}}"
            )
        else:
            lignes_corr.append(rf"\textbf{{{lettres[i]}}} : ${val}$")
    tab_corr = r" & ".join(lignes_corr) + r" \\ \hline"

    correction = identification + rf"""
    \question[1] {enonce}
    \vspace{{-2em}}
    \begin{{center}}
        \begin{{tabular}}{{|
            >{{\centering\arraybackslash}}m{{3.5cm}}|
            >{{\centering\arraybackslash}}m{{3.5cm}}|
            >{{\centering\arraybackslash}}m{{3.5cm}}|
            >{{\centering\arraybackslash}}m{{3.5cm}}|}}
        \hline
        {tab_corr}
        \end{{tabular}}
    \end{{center}}
"""

    return (exo, correction)

def exoP1Type4(id=False):
    """Generate a multiple-choice question about exponentiation rules."""
    if id:
        identification = r"""exoP1Type4\\"""  
    else:
        identification = r""""""  

    # --- Données aléatoires ---
    egalites_vraies = [
        r"$2^3 \times 2^4 = 2^7$",
        r"$5^2 \times 5^{-3} = 5^{-1}$",
        r"$10^{-2} \times 10^5 = 10^3$",
        r"$7^4 \div 7^2 = 7^2$",
        r"$3^{-5} \times 3^{2} = 3^{-3}$",
        r"$\dfrac{2^8}{2^3} = 2^5$",
        r"$\dfrac{10^{-5}}{10^2} = 10^{-7}$",
        r"$\dfrac{4^{-3}}{4^{-5}} = 4^{2}$",
        r"$5^{-2} \times 25 = 5^0$",
        r"$9^3 \div 9^4 = 9^{-1}$",
        r"$(2^{-3})^2 = 2^{-6}$",
        r"$(5^4)^2 = 5^8$",
        r"$\dfrac{10^7}{10^{10}} = 10^{-3}$",
        r"$6^{-2} \times 6^5 = 6^3$",
        r"$\dfrac{3^{-4}}{3^{-6}} = 3^{2}$",
        r"$\dfrac{2^5}{2^8} = 2^{-3}$",
        r"$4^2 \times 4^{-5} = 4^{-3}$",
        r"$(10^{-3})^2 = 10^{-6}$",
        r"$7^0 = 1$",
        r"$(-3)^2 = 9$",
        r"$\dfrac{5^{-7}}{5^{-4}} = 5^{-3}$",
        r"$\dfrac{8^5}{8^2} = 8^3$",
        r"$2^{-1} \times 2^{-1} = 2^{-2}$",
        r"$3^{-2} \times 3^{5} = 3^{3}$",
        r"$\dfrac{10^{-4}}{10^{-1}} = 10^{-3}$",
        r"$4^5 \div 4^5 = 4^0$",
        r"$(a^3)^2 = a^6$",
        r"$\dfrac{a^{-2}}{a^{-5}} = a^3$",
        r"$x^{-1} \times x^{-2} = x^{-3}$",
        r"$\dfrac{x^4}{x^9} = x^{-5}$"
    ]
    egalites_fausses = [
        r"$2^3 \times 2^4 = 2^{12}$",                  # Mauvaise addition d’exposants
        r"$5^2 \times 5^{-3} = 5^{5}$",                # Mauvais signe
        r"$10^{-2} \times 10^5 = 10^{-7}$",            # Mauvais calcul d’exposant
        r"$7^4 \div 7^2 = 7^6$",                       # Mauvais sens de la soustraction
        r"$3^{-5} \times 3^2 = 3^{-7}$",               # Mauvaise addition
        r"$\dfrac{2^8}{2^3} = 2^{11}$",                # Mauvais calcul (8-3 = 5)
        r"$\dfrac{10^{-5}}{10^2} = 10^{7}$",           # Mauvais signe
        r"$\dfrac{4^{-3}}{4^{-5}} = 4^{-8}$",          # Mauvaise soustraction
        r"$5^{-2} \times 25 = 5^3$",                   # Erreur de conversion
        r"$9^3 \div 9^4 = 9^7$",                       # Inversion des signes
        r"$(2^{-3})^2 = 2^{-1}$",                      # Mauvaise multiplication des exposants
        r"$(5^4)^2 = 5^6$",                            # 4×2 ≠ 6
        r"$\dfrac{10^7}{10^{10}} = 10^{3}$",           # Mauvais signe
        r"$6^{-2} \times 6^5 = 6^{-7}$",               # Mauvais calcul (devrait être 6^3)
        r"$\dfrac{3^{-4}}{3^{-6}} = 3^{-10}$",         # Erreur de soustraction
        r"$\dfrac{2^5}{2^8} = 2^{3}$",                 # Mauvais signe
        r"$4^2 \times 4^{-5} = 4^{7}$",                # Erreur sur addition
        r"$(10^{-3})^2 = 10^{-9}$",                    # Mauvais produit d’exposants
        r"$7^0 = 0$",                                  # Confusion avec zéro
        r"$(-3)^2 = -9$",                              # Oubli des parenthèses
        r"$\dfrac{5^{-7}}{5^{-4}} = 5^{3}$",           # Mauvais signe
        r"$\dfrac{8^5}{8^2} = 8^{-3}$",                # Mauvais signe
        r"$2^{-1} \times 2^{-1} = 2^{1}$",             # Erreur de somme d’exposants
        r"$3^{-2} \times 3^{5} = 3^{-3}$",             # Mauvais calcul
        r"$\dfrac{10^{-4}}{10^{-1}} = 10^{5}$",        # Mauvais signe
        r"$4^5 \div 4^5 = 4^{10}$",                    # Erreur conceptuelle
        r"$(a^3)^2 = a^5$",                            # Mauvais produit d’exposants
        r"$\dfrac{a^{-2}}{a^{-5}} = a^{-7}$",          # Erreur de signe
        r"$x^{-1} \times x^{-2} = x^{1}$",             # Mauvais calcul
        r"$\dfrac{x^4}{x^9} = x^{5}$"                  # Inversion du signe
    ]
    # --- Calcul de la bonne réponse ---
    bonne_valeur = random.choice(egalites_vraies)

    # --- Génération de fausses réponses cohérentes ---
    erreurs = []
    while len(erreurs) < 3:
        erreurs.append(random.choice(egalites_fausses))


    # --- Mélange et placement aléatoire ---
    toutes_valeurs = erreurs + [bonne_valeur]
    random.shuffle(toutes_valeurs)
    lettres = ["A", "B", "C", "D"]

    # --- Trouver la position correcte ---
    index_bonne_reponse = toutes_valeurs.index(bonne_valeur)
    lettre_bonne_reponse = lettres[index_bonne_reponse]

    # --- Construction du tableau LaTeX pour la question ---
    lignes = []
    for i, val in enumerate(toutes_valeurs):
        lignes.append(rf"\textbf{{{lettres[i]}}} : ${val}$")
    tab_latex = r" & ".join(lignes) + r" \\ \hline"
    
    enonce = rf"""La seule égalité vraie est :"""
    
    # --- Énoncé LaTeX ---
    exo = identification + rf"""
        \question[1] {enonce}
            \vspace{{-2em}}
            \begin{{center}}
                \begin{{tabular}}{{|
                    >{{\centering\arraybackslash}}m{{3.5cm}}|
                    >{{\centering\arraybackslash}}m{{3.5cm}}|
                    >{{\centering\arraybackslash}}m{{3.5cm}}|
                    >{{\centering\arraybackslash}}m{{3.5cm}}|}}
                \hline
                {tab_latex}
                \end{{tabular}}
            \end{{center}}
"""

    # --- Construction du tableau LaTeX pour la correction ---
    lignes_corr = []
    for i, val in enumerate(toutes_valeurs):
        if i == index_bonne_reponse:
            lignes_corr.append(
                rf"\textbf{{{lettres[i]}}} : \textcolor{{red}}{{${val}$}}"
            )
        else:
            lignes_corr.append(rf"\textbf{{{lettres[i]}}} : ${val}$")
    tab_corr = r" & ".join(lignes_corr) + r" \\ \hline"

    correction = identification + rf"""
    \question[1] {enonce}
    \vspace{{-2em}}
    \begin{{center}}
        \begin{{tabular}}{{|
            >{{\centering\arraybackslash}}m{{3.5cm}}|
            >{{\centering\arraybackslash}}m{{3.5cm}}|
            >{{\centering\arraybackslash}}m{{3.5cm}}|
            >{{\centering\arraybackslash}}m{{3.5cm}}|}}
        \hline
        {tab_corr}
        \end{{tabular}}
    \end{{center}}
"""

    return (exo, correction)

def exoP1Type5(id=False):
    """Generate a multiple-choice question about scientific notation."""
    if id:
        identification = r"""exoP1Type5\\"""  
    else:
        identification = r""""""  

    # --- Données aléatoires ---
    multiplicateur = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])*random.choice([100, 1000])
    unites = ["mm", "cm", "m"]  # liste des unités possibles

    # --- Calcul de la bonne réponse ---
    valeur_numerique = multiplicateur*(70e-3)
    bonne_valeur = round(multiplicateur*(70e-3), 2)

    # --- Conversion en écriture scientifique ---
    exposant = int(math.floor(math.log10(abs(valeur_numerique)))) if valeur_numerique != 0 else 0
    mantisse = valeur_numerique / (10**exposant)

    # --- Deux formats LaTeX possibles ---
    valeur_conventionnelle = f"{bonne_valeur}"
    valeur_puissance10 = rf"{mantisse:.2f} \times 10^{{{exposant}}}"
    aspectBonneValeur = [valeur_conventionnelle+" mm",
                         valeur_puissance10+" mm",
                         f"{bonne_valeur/10:.2f} cm",
                         rf"{mantisse/10:.2f} \times 10^{{{exposant+1}}} cm",]
    # --- Génération de fausses réponses cohérentes ---
    erreurs = []
    while len(erreurs) < 3:
        delta = random.choice([0.01, 0.1, 10, 100, 1000])
        faux = round(bonne_valeur * delta,2)
        if faux > 0 and faux not in erreurs and faux != bonne_valeur:
            erreurs.append(f"{faux} "+random.choice(unites))

    # --- Mélange et placement aléatoire ---
    bonne_valeur = random.choice(aspectBonneValeur)
    toutes_valeurs = erreurs + [bonne_valeur]
    random.shuffle(toutes_valeurs)
    lettres = ["A", "B", "C", "D"]

    # --- Trouver la position correcte ---
    index_bonne_reponse = toutes_valeurs.index(bonne_valeur)
    lettre_bonne_reponse = lettres[index_bonne_reponse]

    # --- Construction du tableau LaTeX pour la question ---
    lignes = []
    for i, val in enumerate(toutes_valeurs):
        lignes.append(rf"\textbf{{{lettres[i]}}} : ${val}$")
    tab_latex = r" & ".join(lignes) + r" \\ \hline"

    enonce = rf"""L’épaisseur d’une feuille de papier est égale à $70\times 10^{{-3}}$mm. L'épaisseur d’une pile de {multiplicateur: } feuilles est égale à :"""
    
    exo = identification + rf"""
        \question[1] {enonce}
            \vspace{{-2em}}
            \begin{{center}}
                \begin{{tabular}}{{|
                    >{{\centering\arraybackslash}}m{{3.5cm}}|
                    >{{\centering\arraybackslash}}m{{3.5cm}}|
                    >{{\centering\arraybackslash}}m{{3.5cm}}|
                    >{{\centering\arraybackslash}}m{{3.5cm}}|}}
                \hline
                {tab_latex}
                \end{{tabular}}
            \end{{center}}
"""

    # --- Construction du tableau LaTeX pour la correction ---
    lignes_corr = []
    for i, val in enumerate(toutes_valeurs):
        if i == index_bonne_reponse:
            lignes_corr.append(
                rf"\textbf{{{lettres[i]}}} : \textcolor{{red}}{{${val}$}}"
            )
        else:
            lignes_corr.append(rf"\textbf{{{lettres[i]}}} : ${val}$")
    tab_corr = r" & ".join(lignes_corr) + r" \\ \hline"

    correction = identification + rf"""
    \question[1] {enonce}
    \vspace{{-2em}}
    \begin{{center}}
        \begin{{tabular}}{{|
            >{{\centering\arraybackslash}}m{{3.5cm}}|
            >{{\centering\arraybackslash}}m{{3.5cm}}|
            >{{\centering\arraybackslash}}m{{3.5cm}}|
            >{{\centering\arraybackslash}}m{{3.5cm}}|}}
        \hline
        {tab_corr}
        \end{{tabular}}
    \end{{center}}
"""

    return (exo, correction)

def exoP1Type6(id=False):
    """Generate a multiple-choice question about algebraic expressions."""
    if id:
        identification = r"""exoP1Type6\\"""  
    else:
        identification = r""""""  

    # --- Données aléatoires ---
    expressions_algebriques = [
        {
            "enonce": r"On additionne un nombre réel $x$, avec son triple et son carré. Le résultat est égal à :",
            "bonne_reponse": r"$x + 3x + x^2$",
            "fausses_reponses": [r"$x + 3x^2$", r"$x^2 + 3$", r"$3x^2 + x$"]
        },
        {
            "enonce": r"On retranche au carré d’un nombre réel $x$ le double de ce nombre. Le résultat est égal à :",
            "bonne_reponse": r"$x^2 - 2x$",
            "fausses_reponses": [r"$x^2 + 2x$", r"$2x^2 - x$", r"$x - 2x^2$"]
        },
        {
            "enonce": r"On ajoute au produit de $x$ par 5 la moitié de ce nombre. Le résultat est égal à :",
            "bonne_reponse": r"$5x + \dfrac{x}{2}$",
            "fausses_reponses": [r"$\dfrac{5x}{2}$", r"$5 + \dfrac{x}{2}$", r"$5 + x^2$"]
        },
        {
            "enonce": r"On multiplie la somme d’un nombre réel $x$ et de 2 par 3. Le résultat est égal à :",
            "bonne_reponse": r"$3(x + 2)$",
            "fausses_reponses": [r"$3x + 2$", r"$x + 3 \times 2$", r"$3x + 6x$"]
        },
        {
            "enonce": r"On divise le cube d’un nombre réel $x$ par le double de ce nombre. Le résultat est égal à :",
            "bonne_reponse": r"$\dfrac{x^3}{2x}$",
            "fausses_reponses": [r"$\dfrac{2x}{x^3}$", r"$\dfrac{x^3}{2}$", r"$2x^3$"]
        },
        {
            "enonce": r"On retranche à la somme $3x + 4$ le nombre $2x - 1$. Le résultat est égal à :",
            "bonne_reponse": r"$(3x + 4) - (2x - 1)$",
            "fausses_reponses": [r"$3x + 4 - 2x + 1$", r"$3x - 2x - 4 - 1$", r"$3x + 4 - 2x - 1$"]
        },
        {
            "enonce": r"On multiplie la différence de $x$ et 5 par la somme de $x$ et 5. Le résultat est égal à :",
            "bonne_reponse": r"$(x - 5)(x + 5)$",
            "fausses_reponses": [r"$x^2 + 25$", r"$x^2 - 10$", r"$(x + 5)^2$"]
        },
        {
            "enonce": r"On calcule le double de la somme du carré d’un nombre $x$ et de 4. Le résultat est égal à :",
            "bonne_reponse": r"$2(x^2 + 4)$",
            "fausses_reponses": [r"$2x^2 + 4$", r"$2x + 4$", r"$2x(x + 4)$"]
        },
        {
            "enonce": r"On ajoute au carré d’un nombre $x$ la moitié de ce nombre et 7. Le résultat est égal à :",
            "bonne_reponse": r"$x^2 + \dfrac{x}{2} + 7$",
            "fausses_reponses": [r"$x^2 + \dfrac{1}{2x} + 7$", r"$x^2 + 7x + \dfrac{1}{2}$", r"$\dfrac{x^2}{2} + 7$"]
        },
        {
            "enonce": r"On divise la somme de $x$ et 3 par la différence de $x$ et 1. Le résultat est égal à :",
            "bonne_reponse": r"$\dfrac{x + 3}{x - 1}$",
            "fausses_reponses": [r"$\dfrac{x - 1}{x + 3}$", r"$x + \dfrac{3}{x - 1}$", r"$\dfrac{x}{x - 1} + 3$"]
        }
    ]

    # --- Calcul de la bonne réponse ---
    choix = random.choice(expressions_algebriques)
    enonce = choix["enonce"]
    bonne_valeur = choix["bonne_reponse"]
    erreurs = choix["fausses_reponses"]
    
    # --- Mélange et placement aléatoire ---
    toutes_valeurs = erreurs + [bonne_valeur]
    random.shuffle(toutes_valeurs)
    lettres = ["A", "B", "C", "D"]

    # --- Trouver la position correcte ---
    index_bonne_reponse = toutes_valeurs.index(bonne_valeur)
    lettre_bonne_reponse = lettres[index_bonne_reponse]

    # --- Construction du tableau LaTeX pour la question ---
    lignes = []
    for i, val in enumerate(toutes_valeurs):
        lignes.append(rf"\textbf{{{lettres[i]}}} : ${val}$")
    tab_latex = r" & ".join(lignes) + r" \\ \hline"

    # --- Énoncé LaTeX ---
    exo = identification + rf"""
        \question[1] {enonce}
            \vspace{{-2em}}
            \begin{{center}}
                \begin{{tabular}}{{|
                    >{{\centering\arraybackslash}}m{{3.5cm}}|
                    >{{\centering\arraybackslash}}m{{3.5cm}}|
                    >{{\centering\arraybackslash}}m{{3.5cm}}|
                    >{{\centering\arraybackslash}}m{{3.5cm}}|}}
                \hline
                {tab_latex}
                \end{{tabular}}
            \end{{center}}
"""

    # --- Construction du tableau LaTeX pour la correction ---
    lignes_corr = []
    for i, val in enumerate(toutes_valeurs):
        if i == index_bonne_reponse:
            lignes_corr.append(
                rf"\textbf{{{lettres[i]}}} : \textcolor{{red}}{{${val}$}}"
            )
        else:
            lignes_corr.append(rf"\textbf{{{lettres[i]}}} : ${val}$")
    tab_corr = r" & ".join(lignes_corr) + r" \\ \hline"

    correction = identification + rf"""
    \question[1] {enonce}
    \vspace{{-2em}}
    \begin{{center}}
        \begin{{tabular}}{{|
            >{{\centering\arraybackslash}}m{{3.5cm}}|
            >{{\centering\arraybackslash}}m{{3.5cm}}|
            >{{\centering\arraybackslash}}m{{3.5cm}}|
            >{{\centering\arraybackslash}}m{{3.5cm}}|}}
        \hline
        {tab_corr}
        \end{{tabular}}
    \end{{center}}
"""

    return (exo, correction)

def exoP1Type7(id=False):
    """Generate a multiple-choice question about function signs."""
    if id:
        identification = r"""exoP1Type7\\"""  
    else:
        identification = r""""""  

    # --- Données aléatoires ---
    x, a, b, a_i, b_i = sp.symbols('x a b a_i b_i')
    a,b = nonEqRandomValue(n=2, notNull=True, tier=False, quart=False)
    autres = []

    while len(autres) < 3:
        a_i, b_i = nonEqRandomValue(n=2, notNull=True, tier=False, quart=False)
        # On impose que la nouvelle fonction soit différente
        if (a_i, b_i) != (a, b) and all(a_i != a for a, _ in autres):
            autres.append((a_i, b_i))
    # --- Calcul de la bonne réponse ---
    bonne_valeur = rf"$f(x) = {Latex(a*x+b)}$"
    erreurs = [rf"$f(x) = {Latex(a_i*x+b_i)}$" for a_i, b_i in autres]
    enonce = rf"""On considère une fonction $f$ définie sur $\R$ dont le tableau de signes est donné ci-dessous."""
    # --- Mélange et placement aléatoire ---
    toutes_valeurs = erreurs + [bonne_valeur]
    random.shuffle(toutes_valeurs)
    lettres = ["A", "B", "C", "D"]

    # --- Trouver la position correcte ---
    index_bonne_reponse = toutes_valeurs.index(bonne_valeur)
    lettre_bonne_reponse = lettres[index_bonne_reponse]

    # --- Construction du tableau LaTeX pour la question ---
    lignes = []
    for i, val in enumerate(toutes_valeurs):
        lignes.append(rf"\textbf{{{lettres[i]}}} : ${val}$")
    tab_latex = r" & ".join(lignes) + r" \\ \hline"
    if a>0:
        signes = r"""\tkzTabLine{,-,z,+}"""
    else:
        signes = r"""\tkzTabLine{,+,z,-}"""
    tab_signes = rf"""
            \begin{{center}}
                \begin{{tikzpicture}}[scale=0.75]
                    \tkzTabInit[lgt=2, espcl=3]%
                    {{$x$ /2, $f(x)$ /2}}%
                    {{$-\infty$, ${Latex(-b/a)}$, $+\infty$}}
                    {signes}
                \end{{tikzpicture}}
            \end{{center}}
    """

    # --- Énoncé LaTeX ---
    exo = identification + rf"""
        \question[1] {enonce}
            \vspace{{-1em}}
            {tab_signes}
            \vspace{{-1em}}
            Parmi les quatre expressions proposées pour la fonction $f$, une seule est possible.
            \vspace{{-2em}}
            \begin{{center}}
                \begin{{tabular}}{{|
                    >{{\centering\arraybackslash}}m{{3.5cm}}|
                    >{{\centering\arraybackslash}}m{{3.5cm}}|
                    >{{\centering\arraybackslash}}m{{3.5cm}}|
                    >{{\centering\arraybackslash}}m{{3.5cm}}|}}
                \hline
                {tab_latex}
                \end{{tabular}}
            \end{{center}}
"""

    # --- Construction du tableau LaTeX pour la correction ---
    lignes_corr = []
    for i, val in enumerate(toutes_valeurs):
        if i == index_bonne_reponse:
            lignes_corr.append(
                rf"\textbf{{{lettres[i]}}} : \textcolor{{red}}{{${val}$}}"
            )
        else:
            lignes_corr.append(rf"\textbf{{{lettres[i]}}} : ${val}$")
    tab_corr = r" & ".join(lignes_corr) + r" \\ \hline"

    correction = identification + rf"""
        \question[1] {enonce}
            \vspace{{-1em}}
            {tab_signes}
            \vspace{{-1em}}
            Parmi les quatre expressions proposées pour la fonction $f$, une seule est possible.
            \vspace{{-2em}}
            \begin{{center}}
                \begin{{tabular}}{{|
                    >{{\centering\arraybackslash}}m{{3.5cm}}|
                    >{{\centering\arraybackslash}}m{{3.5cm}}|
                    >{{\centering\arraybackslash}}m{{3.5cm}}|
                    >{{\centering\arraybackslash}}m{{3.5cm}}|}}
                \hline
                {tab_corr}
                \end{{tabular}}
            \end{{center}}
"""

    return (exo, correction)

def exoP1Type8(id=False):
    """Generate a multiple-choice question about identifying linear functions from graphs."""
    if id:
        identification = r"""exoP1Type8\\"""  
    else:
        identification = r""""""  

    # --- Données aléatoires ---
    x, a, b = sp.symbols('x a b')
    a,b = nonEqRandomValue(n=2, notNull=True, demi=True, tier=True, quart=True)
    autres = []

    # --- Calcul de la bonne réponse ---
    if a>0:
        if b>0:
            bonne_valeur = rf"B"
        else:
            bonne_valeur = rf"A"
    else:
        if b>0:
            bonne_valeur = rf"C"
        else:
            bonne_valeur = rf"D"
    
    toutes_valeurs = ["A", "B", "C", "D"]
    enonce = rf"""La seule droite pouvant correspondre à l’équation $f(x)={Latex(a*x+b)}$ est :\\"""
    # --- Mélange et placement aléatoire ---
    random.shuffle(toutes_valeurs)
    lettres = ["A", "B", "C", "D"]

    # --- Trouver la position correcte ---
    index_bonne_reponse = toutes_valeurs.index(bonne_valeur)
    lettre_bonne_reponse = lettres[index_bonne_reponse]

    # --- Énoncé LaTeX ---
    exo = identification + rf"""
        \question[1] {enonce}
            \begin{{minipage}}[t]{{0.25\textwidth}}
                \begin{{center}}A :\\
                    % --- 1. f1(x) = 0.8x - 1 ---
                    \begin{{tikzpicture}}[scale=0.5, >=stealth]
                        % Axes plus épais, flèches plus petites
                        \draw[line width=1.5pt, ->, >=stealth, shorten >=1pt, shorten <=1pt] (-2,0)--(2,0);
                        \draw[line width=1.5pt, ->, >=stealth, shorten >=1pt, shorten <=1pt] (0,-2)--(0,2);
                        \draw[thick] (-1,-1.6)--(2,0.6);
                    \end{{tikzpicture}}
                \end{{center}}
            \end{{minipage}}
            \begin{{minipage}}[t]{{0.25\textwidth}}
                \begin{{center}}B :\\
                    \begin{{tikzpicture}}[scale=0.5, >=stealth]
                        \draw[line width=1.5pt, ->, >=stealth, shorten >=1pt, shorten <=1pt] (-2,0)--(2,0);
                        \draw[line width=1.5pt, ->, >=stealth, shorten >=1pt, shorten <=1pt] (0,-2)--(0,2);
                        \draw[thick] (-2,-0.6)--(1,1.6); 
                    \end{{tikzpicture}}
                \end{{center}}
            \end{{minipage}}
            \begin{{minipage}}[t]{{0.25\textwidth}}
                \begin{{center}}C :\\
                    \begin{{tikzpicture}}[scale=0.5, >=stealth]
                        \draw[line width=1.5pt, ->, >=stealth, shorten >=1pt, shorten <=1pt] (-2,0)--(2,0);
                        \draw[line width=1.5pt, ->, >=stealth, shorten >=1pt, shorten <=1pt] (0,-2)--(0,2);
                        \draw[thick] (-1,1.6)--(2,-0.6);
                    \end{{tikzpicture}}
                \end{{center}}
            \end{{minipage}}
            \begin{{minipage}}[t]{{0.25\textwidth}}
                \begin{{center}}D :\\
                    \begin{{tikzpicture}}[scale=0.5, >=stealth]
                        \draw[line width=1.5pt, ->, >=stealth, shorten >=1pt, shorten <=1pt] (-2,0)--(2,0);
                        \draw[line width=1.5pt, ->, >=stealth, shorten >=1pt, shorten <=1pt] (0,-2)--(0,2);
                        \draw[thick] (-2,0.6)--(1,-1.6);
                    \end{{tikzpicture}}
                \end{{center}}
            \end{{minipage}}
"""

    # --- Construction du tableau LaTeX pour la correction ---

    correction = identification + rf"""
        \question[1] {enonce}
            \begin{{minipage}}[t]{{0.25\textwidth}}
                \begin{{center}}{rf"""\color{{red}}""" if bonne_valeur=="A" else """"""}A :\\
                    % --- 1. f1(x) = 0.8x - 1 ---
                    \begin{{tikzpicture}}[scale=0.5, >=stealth]
                        % Axes plus épais, flèches plus petites
                        \draw[line width=1.5pt, ->, >=stealth, shorten >=1pt, shorten <=1pt] (-2,0)--(2,0);
                        \draw[line width=1.5pt, ->, >=stealth, shorten >=1pt, shorten <=1pt] (0,-2)--(0,2);
                        \draw[thick] (-1,-1.6)--(2,0.6);
                    \end{{tikzpicture}}
                \end{{center}}
            \end{{minipage}}
            \begin{{minipage}}[t]{{0.25\textwidth}}
                \begin{{center}}{rf"""\color{{red}}""" if bonne_valeur=="B" else """"""}B :\\
                    \begin{{tikzpicture}}[scale=0.5, >=stealth]
                        \draw[line width=1.5pt, ->, >=stealth, shorten >=1pt, shorten <=1pt] (-2,0)--(2,0);
                        \draw[line width=1.5pt, ->, >=stealth, shorten >=1pt, shorten <=1pt] (0,-2)--(0,2);
                        \draw[thick] (-2,-0.6)--(1,1.6); 
                    \end{{tikzpicture}}
                \end{{center}}
            \end{{minipage}}
            \begin{{minipage}}[t]{{0.25\textwidth}}
                \begin{{center}}{rf"""\color{{red}}""" if bonne_valeur=="C" else """"""}C :\\
                    \begin{{tikzpicture}}[scale=0.5, >=stealth]
                        \draw[line width=1.5pt, ->, >=stealth, shorten >=1pt, shorten <=1pt] (-2,0)--(2,0);
                        \draw[line width=1.5pt, ->, >=stealth, shorten >=1pt, shorten <=1pt] (0,-2)--(0,2);
                        \draw[thick] (-1,1.6)--(2,-0.6);
                    \end{{tikzpicture}}
                \end{{center}}
            \end{{minipage}}
            \begin{{minipage}}[t]{{0.25\textwidth}}
                \begin{{center}}{rf"""\color{{red}}""" if bonne_valeur=="D" else """"""}D :\\
                    \begin{{tikzpicture}}[scale=0.5, >=stealth]
                        \draw[line width=1.5pt, ->, >=stealth, shorten >=1pt, shorten <=1pt] (-2,0)--(2,0);
                        \draw[line width=1.5pt, ->, >=stealth, shorten >=1pt, shorten <=1pt] (0,-2)--(0,2);
                        \draw[thick] (-2,0.6)--(1,-1.6);
                    \end{{tikzpicture}}
                \end{{center}}
            \end{{minipage}}
"""

    return (exo, correction)

def exoP1Type9(id=False):
    """Generate a multiple-choice question about the number of solutions of a function equation from its graph."""
    # --- Identification optionnelle ---
    identification = r"""exoP1Type9\\""" if id else r""""""  
    # --- Dictionnaire de fonctions par catégorie ---
    fonctions = {
                "A": [ "0.25*(x+3)*(x+1)*(x-0.5)+1", "0.25*(x+2)*(x+1)*(x-0.5)+1", "-0.25*(x)*(x+1)*(x-4)+1", "0.25*(x)*(x+1)*(x-4)-1" ],
                "B": [ "0.25*(x)*(x+1)*(x-0.5)+1", "-0.25*(x)*(x+1)*(x-0.5)+1" ],
                "C": [ "0.25*(x+5)*(x+2.5)*(x)+1", "-0.25*(x+5)*(x+2.5)*(x)-1" ],
                "D": [ "0.5*(-x+3)*(-x+1.25)*(-x-1.25)+1", "0.5*(x+3)*(x+1.25)*(x-1.25)+1", "0.25*(x)*(x+1)*(x-4)+1", "0.25*(x+1)*(x-2)*(x-4)-1" ],
                }
    # --- Sélection de la bonne réponse et de la fonction correspondante ---
    bonne_valeur = random.choice(list(fonctions.keys()))
    fonction = random.choice(fonctions[bonne_valeur])
    # --- Gabarit commun pour le code LaTeX ---
    question_text = r"""
            \question[1] On donne ci-contre la courbe représentative $\mathcal{C}$ d’une fonction $f$ définie sur l’intervalle $\left[-3 ; 2\right]$.
            On s’intéresse à l’équation $f(x)=0$.\\
            Une seule de ces propositions est exacte :
            \begin{center}
                \begin{tabular}{|>{\arraybackslash}m{9.75cm}|}
                    \hline
                    \textbf{A} : L'équation $f(x)=0$ n'admet aucune solution. \\ \hline
                    \textbf{B} : L'équation $f(x)=0$ admet exactement une solution.\\ \hline
                    \textbf{C} : L'équation $f(x)=0$ admet exactement deux solutions, et ces solutions sont négatives. \\ \hline
                    \textbf{D} : L'équation $f(x)=0$ admet exactement deux solutions, et ces solutions sont de signes contraires. \\
                    \hline
                \end{tabular}
            \end{center}
"""
    # --- Gabarit TikZ commun ---
    tikz_plot = rf"""
        \begin{{center}}
        \begin{{tikzpicture}}
            \begin{{axis}}[
                scale=0.75,
                axis lines=middle, axis line style={{->}},
                xmin=-2.5, xmax=3.5, ymin=-2.5, ymax=3.5,
                grid=both, minor tick num=1,
                ticks=none, enlargelimits=false,
                every axis plot/.style={{very thick}},
                axis equal image
            ]
                \addplot[blue,domain=-2.2:3.2,samples=300] {{{fonction}}};
            \end{{axis}}
        \end{{tikzpicture}}
        \end{{center}}
"""
    # --- Question ---
    exo = rf"""{identification}
        \begin{{minipage}}[t]{{0.65\textwidth}}
        {question_text}
        \end{{minipage}}%
        \hfill
        \begin{{minipage}}[t]{{0.25\textwidth}}
        {tikz_plot}
        \end{{minipage}}
"""
    # --- Correction : met la bonne réponse en rouge ---
    def couleur(l):
        return r"""\color{red}""" if l == bonne_valeur else ""

    correction = rf"""{identification}
        \begin{{minipage}}[t]{{0.65\textwidth}}
        \question[1] On donne ci-contre la courbe représentative $\mathcal{{C}}$ d’une fonction $f$ définie sur l’intervalle $\left[-3 ; 2\right]$.
        On s’intéresse à l’équation $f(x)=0$.\\
        Une seule de ces propositions est exacte :
        \begin{{center}}
            \begin{{tabular}}{{|>{{\arraybackslash}}m{{9.75cm}}|}}
                \hline
                {couleur("A")}\textbf{{A}} : L'équation $f(x)=0$ n'admet aucune solution. \\ \hline
                {couleur("B")}\textbf{{B}} : L'équation $f(x)=0$ admet exactement une solution.\\ \hline
                {couleur("C")}\textbf{{C}} : L'équation $f(x)=0$ admet exactement deux solutions, et ces solutions sont négatives. \\ \hline
                {couleur("D")}\textbf{{D}} : L'équation $f(x)=0$ admet exactement deux solutions, et ces solutions sont de signes contraires. \\
                \hline
            \end{{tabular}}
        \end{{center}}
        \end{{minipage}}%
        \hfill
        \begin{{minipage}}[t]{{0.25\textwidth}}
            {tikz_plot}
        \end{{minipage}}
"""

    return exo, correction

def exoP1Type10(id=False):
    """Generate a multiple-choice question about successive percentage increases."""
    # --- Identification optionnelle ---
    identification = r"""exoP1Type10\\""" if id else r""""""

    # --- Données aléatoires ---
    taux_evolution = random.choice([10, 15, 20, 25, 30, 40, 50])
    bonne_valeur = rf"$P\times (1+\frac{{{taux_evolution}}}{{100}})^2$"
    erreurs = [ rf"$P\times {taux_evolution}\%$", rf"$P\times (1+\frac{{{taux_evolution}}}{{100}})$", rf"\text{{ça dépend}}" ]
    enonce = rf"""Le prix d'un article est noté $P$. Il connait deux augmentations de {taux_evolution}\%."""
    # --- Mélange et placement aléatoire ---
    toutes_valeurs = erreurs + [bonne_valeur]
    random.shuffle(toutes_valeurs)
    lettres = ["A", "B", "C", "D"]
    # --- Trouver la position correcte ---
    index_bonne_reponse = toutes_valeurs.index(bonne_valeur)
    lettre_bonne_reponse = lettres[index_bonne_reponse]
    # --- Construction du tableau LaTeX pour la question ---
    lignes = []
    for i, val in enumerate(toutes_valeurs):
        lignes.append(rf"\textbf{{{lettres[i]}}} : ${val}$")
    tab_latex = r" & ".join(lignes) + r" \\ \hline"
    
    # --- Question ---
    exo = rf"""{identification}
		\question[1] Le prix d'un article est noté $P$. Il connait deux augmentations de {taux_evolution}\%.
		Le prix après ces augmentations est :
		\vspace{{-2em}}
			\begin{{center}}
				\begin{{tabular}}{{|
						>{{\centering\arraybackslash}}m{{3.5cm}}
						|>{{\centering\arraybackslash}}m{{3.5cm}}
						|>{{\centering\arraybackslash}}m{{3.5cm}}
						|>{{\centering\arraybackslash}}m{{3.5cm}}|}}
					\hline
					{tab_latex}
				\end{{tabular}}
			\end{{center}}
"""
    # --- Correction : met la bonne réponse en rouge ---
    def couleur(l):
        return r"""\color{red}""" if l == bonne_valeur else ""
    lignes_corr = []
    for i, val in enumerate(toutes_valeurs):
        if i == index_bonne_reponse:
            lignes_corr.append(
                rf"\textbf{{{lettres[i]}}} : \textcolor{{red}}{{${val}$}}"
            )
        else:
            lignes_corr.append(rf"\textbf{{{lettres[i]}}} : ${val}$")
    tab_corr = r" & ".join(lignes_corr) + r" \\ \hline"

    correction = rf"""{identification}
		\question[1] Le prix d'un article est noté $P$. Il connait deux augmentations de {taux_evolution}\%.
		Le prix après ces augmentations est :
		\vspace{{-2em}}
			\begin{{center}}
				\begin{{tabular}}{{|
						>{{\centering\arraybackslash}}m{{3.5cm}}
						|>{{\centering\arraybackslash}}m{{3.5cm}}
						|>{{\centering\arraybackslash}}m{{3.5cm}}
						|>{{\centering\arraybackslash}}m{{3.5cm}}|}}
					\hline
					{tab_corr}
				\end{{tabular}}
			\end{{center}}
"""

    return exo, correction

def evolSchema2(id=False):
    """Generate a question about completing a percentage change schema."""
    if id:
        identification = r"""evolSchema2\\"""   
    else:
        identification = r""""""
    taux = [10, 20, 25, 30, 40, 50, 75, 80, 90]
    C = random.randint(1,9)*100+random.randint(1,9)*10
    UC = random.sample(taux,1)[0]*(sign(random.randint(-1,1)))
    RC = random.sample(taux,1)[0]*(sign(random.randint(-1,1)))
    CD = random.sample(taux,1)[0]*(sign(random.randint(-1,1)))
    CL = random.sample(taux,1)[0]*(sign(random.randint(-1,1)))
    U = C/(1+UC/100)
    R = C/(1+RC/100)
    D = C*(1+CD/100)
    L = C*(1+CL/100)
    LC = round((C-L)*100/L,2)
    CR = round((R-C)*100/C,2)
    CU = round((U-C)*100/C,2)
    DC = round((C-D)*100/D,2)
    LU = round((U-L)*100/L,2)
    UL = round((L-U)*100/U,2)
    UR = round((R-U)*100/U,2)
    RU = round((U-R)*100/R,2)
    RD = round((D-R)*100/R,2)
    DR = round((R-D)*100/D,2)
    DL = round((L-D)*100/D,2)
    LD = round((D-L)*100/L,2)
    exo = identification+r"""
    \Question[16] Complétez le schéma suivant en utilisant les formules suivantes :\\
    \textit{(Vous donnerez vos résultats arrondis à \textbf{deux chiffres après la virgule})}
    \begin{itemize}
        \item $\displaystyle t=\frac{V_F-V_I}{V_I}$ (taux d'évolution entre 2 valeurs)
        \item $\displaystyle V_I\times (1+t) = V_F$ (appliquer un taux d'évolution)
        \item $\displaystyle V_I = \dfrac{V_F}{(1+t)}$ 
    \end{itemize}
    \begin{center}
        \begin{tikzpicture}
            \tikzstyle{quadri}=[rectangle,draw,text=black]
            \tikzstyle{estun}=[->,>=latex]
            % Noeuds
            \node[quadri,text width=2.5cm, minimum height=1cm, align=center, line width=3pt] (L) at (-5,0) {\fillwithdottedlines{8mm}};
            \node[quadri,text width=2.5cm, minimum height=1cm, align=center, line width=3pt] (C) at (0,0) {"""+str(round(C,2))+r"""};
            \node[quadri,text width=2.5cm, minimum height=1cm, align=center, line width=3pt] (R) at (5,0) {\fillwithdottedlines{8mm}};
            \node[quadri,text width=2.5cm, minimum height=1cm, align=center, line width=3pt] (D) at (0,-3) {\fillwithdottedlines{8mm}};
            \node[quadri,text width=2.5cm, minimum height=1cm, align=center, line width=3pt] (U) at (0,3) {\fillwithdottedlines{8mm}};
            % Flèches
            %L<>C
            \draw[-stealth, thick, ] (L.north east) to node[midway, above, sloped]{...\%} (C.north west);
            \draw[-stealth, thick, ] (C.south west) to node[midway, below, sloped]{"""+str(round(CL,2))+r"""\%} (L.south east);
            %C<>R
            \draw[-stealth, thick, ] (C.north east) to node[midway, above, sloped]{...\%} (R.north west);
            \draw[-stealth, thick, ] (R.south west) to node[midway, below, sloped]{"""+str(round(RC,2))+r"""\%} (C.south east);
            %C<>U
            \draw[-stealth, thick, ] (C.north west) to node[midway, below, sloped]{...\%} (U.south west);
            \draw[-stealth, thick, ] (U.south east) to node[midway, below, sloped]{"""+str(round(UC,2))+r"""\%} (C.north east);
            %C<>D
            \draw[-stealth, thick, ] (D.north west) to node[midway, below, sloped]{...\%} (C.south west);
            \draw[-stealth, thick, ] (C.south east) to node[midway, below, sloped]{"""+str(round(CD,2))+r"""\%} (D.north east);
            %L<>U
            \draw[-stealth, thick, bend left=25] (L.north west) to node[midway, above, sloped]{...\%} (U.north west);
            \draw[-stealth, thick, bend right=25] (U.south west) to node[midway, above, sloped]{...\%} (L.north east);
            %U<>R
            \draw[-stealth, thick, bend left=25] (U.north east) to node[midway, above, sloped]{...\%} (R.north east);
            \draw[-stealth, thick, bend right=25] (R.north west) to node[midway, above, sloped]{...\%} (U.south east);
            %R<>D
            \draw[-stealth, thick, bend left=25] (R.south east) to node[midway, below, sloped]{...\%} (D.south east);
            \draw[-stealth, thick, bend right=25] (D.north east) to node[midway, below, sloped]{...\%} (R.south west);
            %D<>L
            \draw[-stealth, thick, bend left=25] (D.south west) to node[midway, below, sloped]{...\%} (L.south west);
            \draw[-stealth, thick, bend right=25] (L.south east) to node[midway, below, sloped]{...\%} (D.north west);
        \end{tikzpicture}
    \end{center}
    \fillwithlines{105mm}
 """
    correction = identification + r"""
    \Question[16] Complétez le schéma suivant en utilisant les formules suivantes :\\
    \textit{(Vous donnerez vos résultats arrondis à \textbf{deux chiffres après la virgule})}
    \begin{itemize}
        \item $\displaystyle t=\frac{V_F-V_I}{V_I}$ (taux d'évolution entre 2 valeurs)
        \item $\displaystyle V_I\times (1+t) = V_F$ (appliquer un taux d'évolution)
        \item $\displaystyle V_I = \dfrac{V_F}{(1+t)}$ 
    \end{itemize}
    \begin{center}
        \begin{tikzpicture}
            \tikzstyle{quadri}=[rectangle,draw,text=black]
            \tikzstyle{estun}=[->,>=latex]
            % Noeuds
            \node[quadri,text width=2.5cm, minimum height=1cm, align=center, line width=3pt] (L) at (-5,0) {\color{red}"""+str(round(L,2))+r"""};
            \node[quadri,text width=2.5cm, minimum height=1cm, align=center, line width=3pt] (C) at (0,0) {"""+str(round(C,2))+r"""};
            \node[quadri,text width=2.5cm, minimum height=1cm, align=center, line width=3pt] (R) at (5,0) {\color{red}"""+str(round(R,2))+r"""};
            \node[quadri,text width=2.5cm, minimum height=1cm, align=center, line width=3pt] (D) at (0,-3) {\color{red}"""+str(round(D,2))+r"""};
            \node[quadri,text width=2.5cm, minimum height=1cm, align=center, line width=3pt] (U) at (0,3) {\color{red}"""+str(round(U,2))+r"""};
            % Flèches
            %L<>C
            \draw[-stealth, thick, ] (L.north east) to node[midway, above, sloped]{\color{red}"""+str(round(LC,2))+r"""\%} (C.north west);
            \draw[-stealth, thick, ] (C.south west) to node[midway, below, sloped]{"""+str(round(CL,2))+r"""\%} (L.south east);
            %C<>R
            \draw[-stealth, thick, ] (C.north east) to node[midway, above, sloped]{\color{red}"""+str(round(CR,2))+r"""\%} (R.north west);
            \draw[-stealth, thick, ] (R.south west) to node[midway, below, sloped]{"""+str(round(RC,2))+r"""\%} (C.south east);
            %C<>U
            \draw[-stealth, thick, ] (C.north west) to node[midway, below, sloped]{\color{red}"""+str(round(CU,2))+r"""\%} (U.south west);
            \draw[-stealth, thick, ] (U.south east) to node[midway, below, sloped]{"""+str(round(UC,2))+r"""\%} (C.north east);
            %C<>D
            \draw[-stealth, thick, ] (D.north west) to node[midway, below, sloped]{\color{red}"""+str(round(DC,2))+r"""\%} (C.south west);
            \draw[-stealth, thick, ] (C.south east) to node[midway, below, sloped]{"""+str(round(CD,2))+r"""\%} (D.north east);
            %L<>U
            \draw[-stealth, thick, bend left=25] (L.north west) to node[midway, above, sloped]{\color{red}"""+str(round(LU,2))+r"""\%} (U.north west);
            \draw[-stealth, thick, bend right=25] (U.south west) to node[midway, above, sloped]{\color{red}"""+str(round(UL,2))+r"""\%} (L.north east);
            %U<>R
            \draw[-stealth, thick, bend left=25] (U.north east) to node[midway, above, sloped]{\color{red}"""+str(round(UR,2))+r"""\%} (R.north east);
            \draw[-stealth, thick, bend right=25] (R.north west) to node[midway, above, sloped]{\color{red}"""+str(round(RU,2))+r"""\%} (U.south east);
            %R<>D
            \draw[-stealth, thick, bend left=25] (R.south east) to node[midway, below, sloped]{\color{red}"""+str(round(RD,2))+r"""\%} (D.south east);
            \draw[-stealth, thick, bend right=25] (D.north east) to node[midway, below, sloped]{\color{red}"""+str(round(DR,2))+r"""\%} (R.south west);
            %D<>L
            \draw[-stealth, thick, bend left=25] (D.south west) to node[midway, below, sloped]{\color{red}"""+str(round(DL,2))+r"""\%} (L.south west);
            \draw[-stealth, thick, bend right=25] (L.south east) to node[midway, below, sloped]{\color{red}"""+str(round(LD,2))+r"""\%} (D.north west);
        \end{tikzpicture}
    \end{center}
    \fillwithlines{105mm}
"""
    return (exo, correction)

def exoTableauEvolution(id=False, n=10):
    """Generate a question about completing a percentage change table."""
    if id:
        identification = r"""exoTableauEvolution\\"""  
    else:
        identification = r""""""

    LignesExo = r""""""
    LignesCorrection = r""""""
    for i in range(n):
        VI = random.randint(10,90)*10
        TE = random.randint(1,9)*10
        SigneTE = sign(random.randint(-1,1))
        VF = int(VI*(1+SigneTE*TE/100))
        CM = round((1+SigneTE*TE/100),2)  
        TypeLigne = random.randint(1,4)
        match TypeLigne:
            case 1:  # On donne VI et VF, on cherche TE et CM
                LignesExo = LignesExo + r"""                $"""+str(VI)+r"""$ & \dots & \dots & $"""+str(VF)+r"""$ \\
                \hline"""+"\n"
                LignesCorrection = LignesCorrection + r"""                $"""+str(VI)+r"""$ & \color{red}$"""+str(CM)+r"""$ & \color{red}$"""+str(SigneTE*TE)+r"""$ & $"""+str(VF)+r"""$ \\
                \hline"""+"\n"
                pass
            case 2:  # On donne VI et TE, on cherche VF et CM
                LignesExo = LignesExo + r"""                $"""+str(VI)+r"""$ & \dots & $"""+str(SigneTE*TE)+r"""$ & \dots \\
                \hline"""+"\n"
                LignesCorrection = LignesCorrection + r"""                $"""+str(VI)+r"""$ & \color{red}"""+str(CM)+r""" & """+str(SigneTE*TE)+r""" & \color{red}$"""+str(VF)+r"""$ \\
                \hline"""+"\n"
                pass
            case 3:  # On donne VF et TE, on cherche VI et CM
                LignesExo = LignesExo + r"""                \dots & \dots & $"""+str(SigneTE*TE)+r"""$ & $"""+str(VF)+r"""$ \\
                \hline"""+"\n"
                LignesCorrection = LignesCorrection + r"""                \color{red}$"""+str(VI)+r"""$ & \color{red}$"""+str(CM)+r"""$ & $"""+str(SigneTE*TE)+r"""$ & $"""+str(VF)+r"""$ \\
                \hline"""+"\n"
                pass
            case 4:  # On donne VI et CM, on cherche TE et VF
                LignesExo = LignesExo + r"""                $"""+str(VI)+r"""$ & $"""+str(CM)+r"""$ & \dots & \dots \\
                \hline"""+"\n"
                LignesCorrection = LignesCorrection + r"""                $"""+str(VI)+r"""$ & $"""+str(CM)+r"""$ & \color{red}$"""+str(SigneTE*TE)+r"""$ & \color{red}$"""+str(VF)+r"""$ \\
                \hline"""+"\n"
                pass

    exo = identification+r"""
    \Question["""+str(n)+r"""] Copmplétez le tableau suivant :
        \begin{center}
            \begin{multicols}{2}
		$V_I\times\left(1+T_e \right)=V_F$ \\ 
		$T_e=\dfrac{V_F-V_I}{V_I}$\\
		$CM=1+t$\\
	\end{multicols}
	avec
	\begin{multicols}{2}
	$V_I$ : Valeur Initiale \\ $V_F$ : Valeur Finale\\
	$T_e$ : Taux d'évolution \\ $CM$ : Coéfficient Multiplicateur
	\end{multicols}
            \renewcommand{\arraystretch}{1.5} % espace vertical dans le tableau
            
            \begin{tabular}{|
                    >{\centering\arraybackslash}m{2.5cm}
                    |>{\centering\arraybackslash}m{3cm}
                    |>{\centering\arraybackslash}m{3cm}
                    |>{\centering\arraybackslash}m{2.5cm}|}
                \hline
                $V_I$ & $CM$ & $T_e$ & $V_F$ \\
                \hline
                """+LignesExo+r"""
            \end{tabular}
        \end{center}
"""
    correction = identification+r"""
    \Question["""+str(n)+r"""] Copmplétez le tableau suivant :
        \begin{center}
            \begin{multicols}{2}
		$V_I\times\left(1+T_e \right)=V_F$ \\ 
		$T_e=\dfrac{V_F-V_I}{V_I}$\\
		$CM=1+t$\\
	\end{multicols}
	avec
	\begin{multicols}{2}
	$V_I$ : Valeur Initiale \\ $V_F$ : Valeur Finale\\
	$T_e$ : Taux d'évolution \\ $CM$ : Coéfficient Multiplicateur
	\end{multicols}
            \renewcommand{\arraystretch}{1.5} % espace vertical dans le tableau
            
            \begin{tabular}{|
                    >{\centering\arraybackslash}m{2.5cm}
                    |>{\centering\arraybackslash}m{3cm}
                    |>{\centering\arraybackslash}m{3cm}
                    |>{\centering\arraybackslash}m{2.5cm}|}
                \hline
                $V_I$ & $CM$ & $T_e$ & $V_F$ \\
                \hline
                """+LignesCorrection+r"""
            \end{tabular}
        \end{center}
"""

    return (exo, correction)

def suiteAriShema(id=False):

    if id:
        identification = r"""suiteAriShema\\"""
    else:
        identification = r""""""

    # On tir au hasard une lettre pour le nom de la suite
    lowercase_alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    lowercase_alphabet.remove('n') # n ne peut pas être le nom d'une suite
    suite_letter = random.choice(lowercase_alphabet)
    # On retire la lettre choisie de la liste pour éviter les doublons de tirage
    lowercase_alphabet.remove(suite_letter)
    nRef = random.randint(2,5)
    valeurRef = random.randint(2,15)
    raisonSuite = nonEqRandomValue(quart=False, tier=False, demi=True)
    u0 = valeurRef/((raisonSuite[0])**nRef)
    u1 = valeurRef*raisonSuite[0]
    u2 = u1*raisonSuite[0]
    u3 = u2*raisonSuite[0]
    exo=r"""
    """+identification+r"""
    \Question[8] On considère la suite géométrique $("""+suite_letter+r"""_n)$ (avec $n\in \mathbb{N}$) de terme de rang """+str(nRef)+r""" ayant pour valeur """+str(valeurRef)+r""" et de raison $"""+Latex(raisonSuite[0])+r"""$.\\
    Compléter le diagramme en répondant aux questions suivantes :\\
        \begin{center}
            \begin{tikzpicture}
            \node[draw, ellipse, minimum width=2cm, minimum height=1cm] (ovale1) at (0,0) {......};
            \node[below=1mm of ovale1] {$"""+suite_letter+r"""_{"""+str(nRef)+r"""}$}; % Texte plus proche de l'ovale
            
            \node[draw, ellipse, minimum width=2cm, minimum height=1cm] (ovale2) at (3,0) {......};
            \node[below=1mm of ovale2] {$"""+suite_letter+r"""_{"""+str(nRef+1)+r"""}$}; % Texte plus proche de l'ovale
            
            \node[draw, ellipse, minimum width=2cm, minimum height=1cm] (ovale3) at (6,0) {......};
            \node[below=1mm of ovale3] {$"""+suite_letter+r"""_{"""+str(nRef+2)+r"""}$}; % Texte plus proche de l'ovale
            
            \node[draw, ellipse, minimum width=2cm, minimum height=1cm] (ovale4) at (9,0) {......};
            \node[below=1mm of ovale4] {$"""+suite_letter+r"""_{"""+str(nRef+3)+r"""}$}; % Texte plus proche de l'ovale
            
            \draw[->, bend left] (ovale1) to node[above] {$\times .....$} (ovale2);
            \draw[->, bend left] (ovale2) to node[above] {$\times .....$} (ovale3);
            \draw[->, bend left] (ovale3) to node[above] {$\times .....$} (ovale4);
            \end{tikzpicture}
        \end{center}
        \begin{parts}
                \Part Compléter les pointillés ci-dessous pour obtenir les quatre premiers termes de la suite :
                \begin{subparts}
                    \subpart $"""+suite_letter+r"""_{"""+str(nRef)+r"""}=\color{red}{"""+str(valeurRef)+r"""}$
                    \subpart $"""+suite_letter+r"""_{"""+str(nRef+1)+r"""}=\color{red}{"""+suite_letter+r"""_{"""+str(nRef)+r"""}}\times \color{red}{"""+Latex(raisonSuite[0])+r"""}=\color{red}{"""+str(valeurRef)+r"""}\times \color{red}{"""+Latex(raisonSuite[0])+r"""}=\color{red}{-30}$
                    \subpart $"""+suite_letter+r"""_{"""+str(nRef+2)+r"""}=\color{red}{"""+suite_letter+r"""_{"""+str(nRef+1)+r"""}}\times \color{red}{"""+Latex(raisonSuite[0])+r"""}=......$
                    \subpart $"""+suite_letter+r"""_{"""+str(nRef+3)+r"""}=\color{red}{"""+suite_letter+r"""_{"""+str(nRef+2)+r"""}}\times \color{red}{"""+Latex(raisonSuite[0])+r"""}=......$
                    \subpart $a_{4}=\color{red}{15}$
                    \subpart $a_{5}=\color{red}{a_{4}}\times \color{red}{-2}=\color{red}{15}\times \color{red}{-2}=\color{red}{-30}$
                    \subpart $a_{6}=......\times ......=......$
                    \subpart $a_{7}=......\times ......=......$
                \end{subparts}
        \end{parts}
        \fillwithlines{10mm}"""
    correction=r"""
    """+identification+r"""
    """
    return(exo,correction)

def polyDegre2_1(n:int=10, id=False):
    """Generate a set of quadratic equation solving exercises and their solutions."""
    if id:
        identification = r"""polyDegre2_1\\"""
    else:
        identification = r""""""
    item = r"""
    """+identification+r"""
            \Question["""+str(2*n)+r"""] Résoudre les équations suivantes dans $\mathbb{R}$:
            \begin{multicols}{2}
                \begin{enumerate}
"""
    itemCorr = r"""
    """+identification+r"""
            \Question["""+str(2*n)+r"""] Résoudre les équations suivantes dans $\mathbb{R}$:
            \begin{multicols}{2}
                \begin{enumerate}
"""
    for i in range(n):
        a = nonEqRandomValue(quart=True, tier=False, demi=True)[0]**2
        b = nonEqRandomValue(quart=True, tier=False, demi=True)[0]**2
        signe_b = (-1 if random.randint(1,100)%2==0 else 1) 
        x = Symbol('x')
        str_expr1 = str(a)+"*x**2"+(("+"+str(b)) if signe_b>0 else ("-"+str(b)))
        expr1 = sympify(str_expr1)
        solutions1 = real_roots(str_expr1, x)
        item = item + r"""                    \item $"""+latex(expr1).replace("frac","dfrac")+r"""=0$
                        \fillwithlines{30mm}
"""
        if len(solutions1)==0:
            itemCorr = itemCorr + r"""                    \item $"""+latex(expr1).replace("frac","dfrac")+r"""=0$
                    \begin{center}
                    	$ \color{red}{S= \O } $\\
                    	(pas de solutions dans $\mathbb{R}$)
                    \end{center}"""
        if len(solutions1)==1:
            itemCorr = itemCorr + r"""
                    \item $"""+latex(expr1).replace("frac","dfrac")+r"""=0$
                    \begin{center}
                    	$ \color{red}{S=\left\{ """+latex(solutions1[0]).replace("frac","dfrac")+r""" \right\}} $
                    \end{center}"""
        if len(solutions1)==2:
            itemCorr = itemCorr + r"""
                    \item $"""+latex(expr1).replace("frac","dfrac")+r"""=0$
                    \begin{center}
                    	$ \color{red}{S=\left\{ """+latex(solutions1[0]).replace("frac","dfrac")+r""" ; """+latex(solutions1[1]).replace("frac","dfrac")+r""" \right\}} $
                    \end{center}"""
    item = item +r"""
                \end{enumerate}
            \end{multicols}"""
    itemCorr = itemCorr + r"""
                \end{enumerate}
            \end{multicols}"""
    return(item,itemCorr)

def exoProportion(n=10, id=False):
    """Generate exercises and corrections for calculating proportions."""
    if id:
        identification = r"""exoProportion\\"""
    else:
        identification = r""""""
    """
    The function `exoProportion` generates a set of exercises and their corresponding corrections for
    calculating proportions.
    
    :param n: The parameter `n` represents the number of proportions to be calculated. It determines how
    many items will be generated in the exercise and correction. By default, if no value is provided for
    `n`, it will be set to 10, defaults to 10 (optional)
    :return: The function `exoProportion` returns two strings: `exo` and `correction`.
    """
    taux = [10,20,30,40,50,25,75]
    valeur, t = symbols('valeur t')
    item = r""""""
    itemCorrection = r""""""
    for i in range(0,n):
        valeur = random.randint(10,40)*10*2
        t = random.choice(taux)
        item = item + r"""\item $"""+str(t)+r"""\%$ de $"""+str(valeur)+r"""$ = .....
        """
        itemCorrection = itemCorrection + r"""\item $"""+str(t)+r"""\%$ de $"""+str(valeur)+r"""$ = {\color{red}$"""+f"{valeur*t/100:.0f}"+r"""$}
        """
    exo=r"""
    """+identification+r"""
        \Question["""+str(n)+r"""] Calculer les proportions suivantes :
            \begin{multicols}{2}
                \begin{enumerate}
                    """+item+r"""
                \end{enumerate}
            \end{multicols}
    """
    correction=r"""
    """+identification+r"""
        \Question["""+str(n)+r"""] Calculer les proportions suivantes :
            \begin{multicols}{2}
                \begin{enumerate}
                    """+itemCorrection+r"""
                \end{enumerate}
            \end{multicols}
    """
    return(exo,correction)

def exoEvolutionSimple(n=2, id=False):
    """Generate exercises and corrections for calculating simple evolutions."""
    if id:
        identification = r"""exoEvolutionSimple\\"""
    else:
        identification = r""""""
    taux = [10,20,30,40,50,25,75]
    valeur, t = symbols('valeur t')
    item = r""""""
    itemCorrection = r""""""
    for i in range(0,n):
        valeur = random.randint(10,40)*10*2
        t = random.choice(taux)*(sign(random.randint(-1,1)))
        item = item + r"""\item $"""+str(valeur)+r"""$ évolue de $"""+str(t)+r"""\%$ = .....
        """
        itemCorrection = itemCorrection + r"""\item $"""+str(valeur)+r"""$ évolue de $"""+str(t)+r"""\%$ = {\color{red}$"""+f"{valeur*(1+t/100):.0f}"+r"""$}
        """
    exo=r"""
    """+identification+r"""
        \Question["""+str(n)+r"""] Calculer les évolutions suivantes :
            \begin{multicols}{2}
                \begin{enumerate}
                    """+item+r"""
                \end{enumerate}
            \end{multicols}
    """
    correction=r"""
    """+identification+r"""
        \Question["""+str(n)+r"""] Calculer les évolutions suivantes :
            \begin{multicols}{2}
                \begin{enumerate}
                    """+itemCorrection+r"""
                \end{enumerate}
            \end{multicols}
    """
    return(exo,correction)

def exoEvolution(id=False):
    """Generate an exercise and correction about linear regression and percentage decrease."""
    if id:
        identification = r"""exoEvolution\\"""
    else:
        identification = r""""""
    anneeStart=1998
    data =[]
    for i in range(anneeStart, anneeStart+9):
        data.append([i,np.random.randint(4500,8500)])
    txQc = np.random.randint(5,49)
    exo=r"""
    """+identification+r"""
    \Question 
        Le tableau suivant donne le nombre de morts sur les routes françaises par an de 1998 à 2006.

        \begin{center}
            \begin{tabularx}{\linewidth}{|m{2cm}|*{9}{>{\centering \arraybackslash}X|}}\hline
                Année &"""+str(data[0][0])+r""" &"""+str(data[1][0])+r""" &"""+str(data[2][0])+r""" &"""+str(data[3][0])+r""" &"""+str(data[4][0])+r""" &"""+str(data[5][0])+r""" &"""+str(data[6][0])+r""" &"""+str(data[7][0])+r""" &"""+str(data[8][0])+r"""\\ \hline
                Rang $\left(x_i\right)$& 1 &2 &3 &4 &5 &6 &7 &8 &9\\ \hline
                Nombre de morts $\left(y_i\right)$& """+str(data[0][1])+r""" & """+str(data[1][1])+r""" & """+str(data[2][1])+r""" & """+str(data[3][1])+r""" & """+str(data[4][1])+r""" & """+str(data[5][1])+r""" & """+str(data[6][1])+r""" & """+str(data[7][1])+r""" & """+str(data[8][1])+r"""\\ \hline
                \multicolumn{10}{r}{\footnotesize Source: d'après www.securite-routiere.gouv.fr}
            \end{tabularx}
        \end{center}
        \begin{parts}
            \Part[2] Sur le graphique ci-dessous, on a représenté une partie du nuage de points $M_i\left(x_i~;~y_i\right)$.\\
            Compléter ce nuage de points à l'aide du tableau en plaçant le point d'abscisse 4 et le point d'abscisse 7.
            \begin{center}
                \begin{tikzpicture}[scale=0.75]
                    \begin{axis}[
                            grid= both ,
                            minor tick num=1,
                            minor grid style={line width=.1pt, dashed	},
                            major grid style={line width=.4pt},
                            width=0.8\textwidth ,
                            xlabel = {Rang $\left(x_i\right)$} ,
                            ylabel = {Nombre de morts $\left(y_i\right)$} ,
                            xmin = 0, xmax = 15,
                            ymin = 2500, ymax = 10000,
                            yticklabel style={
                                /pgf/number format/.cd,%
                                scaled y ticks = false,
                                set thousands separator={},
                                fixed
                            },
                            %legend entries={Courbe 1, Courbe 2},
                            %legend style={at={(0,1)},anchor=north west}
                            ]
                        \addplot [only marks,mark=*] coordinates {(1,"""+str(data[0][1])+r""") (2,"""+str(data[1][1])+r""") (3,"""+str(data[2][1])+r""")  (5,"""+str(data[4][1])+r""") (6, """+str(data[5][1])+r""")  (8,"""+str(data[7][1])+r""") (9, """+str(data[8][1])+r""")}; % Tracé point à point
                        \addplot [very thick] expression[domain=0:15]{9142.722-485.967*x}; % Équation analytique
                        \addplot [red,dashed,very thick] expression[domain=0:13]{2800}; % Équation analytique
                    \end{axis}
                \end{tikzpicture}
            \end{center}
            \part[2] Sur le graphique ci-dessus est tracée la droite d'ajustement. À l'aide de cette droite d'ajustement, par lecture graphique, déterminer une prévision du nombre de morts en 2010.
                \fillwithlines{10mm}
            \part[2] On a observé en réalité que le nombre de personnes ayant perdu la vie sur les routes françaises en 2010 a diminué de """+str(txQc)+r"""\% par rapport à l'année 2000.
Quel est le nombre réel de victimes sur les routes françaises en 2010 ? On donnera le résultat arrondi à l'unité.
                \fillwithlines{20mm}
        \end{parts}
\clearpage
    """
    correction=r"""
    """+identification+r"""
        \Question 
            Le tableau suivant donne le nombre de morts sur les routes françaises par an de 1998 à 2006.
            \begin{center}
                \begin{tabularx}{\linewidth}{|m{2cm}|*{9}{>{\centering \arraybackslash}X|}}\hline
                    Année &"""+str(data[0][0])+r""" &"""+str(data[1][0])+r""" &"""+str(data[2][0])+r""" &"""+str(data[3][0])+r""" &"""+str(data[4][0])+r""" &"""+str(data[5][0])+r""" &"""+str(data[6][0])+r""" &"""+str(data[7][0])+r""" &"""+str(data[8][0])+r"""\\ \hline
                    Rang $\left(x_i\right)$& 1 &2 &3 &4 &5 &6 &7 &8 &9\\ \hline
                    Nombre de morts $\left(y_i\right)$& """+str(data[0][1])+r""" & """+str(data[1][1])+r""" & """+str(data[2][1])+r""" & """+str(data[3][1])+r""" & """+str(data[4][1])+r""" & """+str(data[5][1])+r""" & """+str(data[6][1])+r""" & """+str(data[7][1])+r""" & """+str(data[8][1])+r"""\\ \hline
                    \multicolumn{10}{r}{\footnotesize Source: d'après www.securite-routiere.gouv.fr}
                \end{tabularx}
            \end{center}
            \begin{parts}
                \Part[2] Sur le graphique ci-dessous, on a représenté une partie du nuage de points $M_i\left(x_i~;~y_i\right)$.\\
                Compléter ce nuage de points à l'aide du tableau en plaçant le point d'abscisse 4 et le point d'abscisse 7.

                \begin{center}
                    \begin{tikzpicture}[scale=0.75]
                        \begin{axis}[
                                grid= both ,
                                minor tick num=1,
                                minor grid style={line width=.1pt, dashed	},
                                major grid style={line width=.4pt},
                                width=0.8\textwidth ,
                                xlabel = {Rang $\left(x_i\right)$} ,
                                ylabel = {Nombre de morts $\left(y_i\right)$} ,
                                xmin = 0, xmax = 15,
                                ymin = 2500, ymax = 10000,
                                yticklabel style={
                                    /pgf/number format/.cd,%
                                    scaled y ticks = false,
                                    set thousands separator={},
                                    fixed
                                },
                                %legend entries={Courbe 1, Courbe 2},
                                %legend style={at={(0,1)},anchor=north west}
                                ]
                            \addplot [only marks,mark=*] coordinates {(1,"""+str(data[0][1])+r""") (2,"""+str(data[1][1])+r""") (3,"""+str(data[2][1])+r""")  (5,"""+str(data[4][1])+r""") (6, """+str(data[5][1])+r""")  (8,"""+str(data[7][1])+r""") (9, """+str(data[8][1])+r""")}; % Tracé point à point
                            \addplot [very thick] expression[domain=0:15]{9142.722-485.967*x}; % Équation analytique
                            \addplot [red,dashed,very thick] expression[domain=0:13]{2800}; % Équation analytique
                            \addplot [red,only marks,mark=*] coordinates {(4,"""+str(data[3][1])+r""") (7,"""+str(data[6][1])+r""")}; % Tracé point à point
                        \end{axis}
                    \end{tikzpicture}
                \end{center}
                \part[2] Sur le graphique ci-dessus est tracée la droite d'ajustement. À l'aide de cette droite d'ajustement, par lecture graphique, déterminer une prévision du nombre de morts en 2010.
%				\fillwithlines{10mm}
                    \begin{solution}
                        environ 2 800
                    \end{solution}
                \part[2] On a observé en réalité que le nombre de personnes ayant perdu la vie sur les routes françaises en 2010 a diminué de """+str(txQc)+r"""\% par rapport à l'année 2000.
Quel est le nombre réel de victimes sur les routes françaises en 2010 ? On donnera le résultat arrondi à l'unité.
%					\fillwithlines{20mm}
                    \begin{solution}
                        En 2000, il y avait """+str(data[2][1])+r""" morts; en 2010 il y en a eu :
                        \begin{center}
                            $"""+str(data[2][1])+r"""\times \left( 1-\dfrac{"""+str(txQc)+r"""}{100}\right)\approx """+str(int(data[2][1]*(1-txQc/100)))+r"""$
                        \end{center}
                    \end{solution}
            \end{parts}
\clearpage
    """
    return(exo, correction)

def exoEvolSuite(id=False):
    """Generate an exercise and correction about evolution of recycling rates."""
    if id:
        identification = r"""exoEvolution\\"""
    else:
        identification = r""""""
    anneeStart=2002
    data =[]
    for i in range(anneeStart, anneeStart+11):
        data.append([i,np.random.randint(450,650)/10])

    q1Start = np.random.randint(0,6)
    q1End = np.random.randint(1,10-q1Start)
    q1End = q1Start+q1End
    q1Taux =  int(round(((data[q1End][1]-data[q1Start][1])/data[q1Start][1])*100,0))
    q2RacineN = (1+q1Taux/100)**((q1End-q1Start)**-1)-1
    q3Taux = np.random.randint(100, 900)/100
    q3Tx2020 = data[10][1]*(1+q3Taux/100)**8
    exo=r"""
    """+identification+r"""
    \Question
                Le tableau suivant indique, sur la période 2002-2012, en France, la proportion de déchets recyclés exprimée en pourcentage des déchets d'emballages ménagers.
                \begin{center}
                    \begin{tabularx}{1.02\linewidth}{|m{2.5cm}|*{11}{>{\centering \arraybackslash}X|}}\hline
                    Année 		&"""+str(data[0][0])+r""" &"""+str(data[1][0])+r""" &"""+str(data[2][0])+r""" &"""+str(data[3][0])+r""" &"""+str(data[4][0])+r""" &"""+str(data[5][0])+r""" &"""+str(data[6][0])+r""" &"""+str(data[7][0])+r""" &"""+str(data[8][0])+r""" &"""+str(data[9][0])+r""" &"""+str(data[10][0])+r"""\\ \hline
                    Pourcentage de
                    déchets recyclés (en \,$\%$)&"""+str(data[0][1])+r""" &"""+str(data[1][1])+r""" &"""+str(data[2][1])+r""" &"""+str(data[3][1])+r""" &"""+str(data[4][1])+r""" &"""+str(data[5][1])+r""" &"""+str(data[6][1])+r""" &"""+str(data[7][1])+r""" &"""+str(data[8][1])+r""" &"""+str(data[9][1])+r""" &"""+str(data[10][1])+r""" \\ \hline
                    \end{tabularx}
                \end{center}
                \begin{parts}
                    \Part[1] Montrer que le taux global d'évolution, arrondi à l'unité, entre """+str(data[q1Start][0])+r""" et """+str(data[q1End][0])+r""" est de $"""+str(q1Taux)+r"""$\,\%.
                        \fillwithlines{30mm}
                    \Part[2] Déterminer le taux annuel moyen entre """+str(data[q1Start][0])+r""" et """+str(data[q1End][0])+r""". On donnera le résultat en pourcentage arrondi au centième.
                        \fillwithlines{30mm}
                    \Part[2] On conjecture qu'à partir de 2012, le taux annuel est de $+ """+str(q3Taux)+r"""$\,\%. Avec ce modèle, quel est le taux de recyclage en 2020 ? On donnera le résultat en pourcentage arrondi au dixième.
                        \fillwithlines{30mm}
                \end{parts}
\clearpage
    """
    correction=r"""
    """+identification+r"""
    \Question
                Le tableau suivant indique, sur la période 2002-2012, en France, la proportion de déchets recyclés exprimée en pourcentage des déchets d'emballages ménagers.
                \begin{center}
                    \begin{tabularx}{1.02\linewidth}{|m{2.5cm}|*{11}{>{\centering \arraybackslash}X|}}\hline
                    Année 		&"""+str(data[0][0])+r""" &"""+str(data[1][0])+r""" &"""+str(data[2][0])+r""" &"""+str(data[3][0])+r""" &"""+str(data[4][0])+r""" &"""+str(data[5][0])+r""" &"""+str(data[6][0])+r""" &"""+str(data[7][0])+r""" &"""+str(data[8][0])+r""" &"""+str(data[9][0])+r""" &"""+str(data[10][0])+r"""\\ \hline
                    Pourcentage de
                    déchets recyclés (en \,$\%$)&"""+str(data[0][1])+r""" &"""+str(data[1][1])+r""" &"""+str(data[2][1])+r""" &"""+str(data[3][1])+r""" &"""+str(data[4][1])+r""" &"""+str(data[5][1])+r""" &"""+str(data[6][1])+r""" &"""+str(data[7][1])+r""" &"""+str(data[8][1])+r""" &"""+str(data[9][1])+r""" &"""+str(data[10][1])+r""" \\ \hline
                    \end{tabularx}
                \end{center}
                \begin{parts}
                    \Part[1] Montrer que le taux global d'évolution, arrondi à l'unité, entre """+str(data[q1Start][0])+r""" et """+str(data[q1End][0])+r""" est de $"""+str(q1Taux)+r"""$\,\%.
%						\fillwithlines{30mm}
                        \begin{solution}
                            \begin{center}
                                $\dfrac{pourcent_{"""+str(data[q1End][0])+r"""}-pourcent_{"""+str(data[q1Start][0])+r"""}}{pourcent_{"""+str(data[q1Start][0])+r"""}}\times 100 = \dfrac{"""+str(data[q1End][1])+r"""-"""+str(data[q1Start][1])+r"""}{"""+str(data[q1Start][1])+r"""}\times 100 \approx """+str(round(((data[q1End][1]-data[q1Start][1])/data[q1Start][1])*100,2))+r"""$ soit """+str(q1Taux)+r"""\%
                            \end{center}
                        \end{solution}
                    \Part[2] Déterminer le taux annuel moyen entre """+str(data[q1Start][0])+r""" et """+str(data[q1End][0])+r""". On donnera le résultat en pourcentage arrondi au centième.
%						\fillwithlines{30mm}
                        \begin{solution}
                            Le taux global qui fait passer de """+str(data[q1Start][0])+r""" à """+str(data[q1End][0])+r""" est de """+str(q1Taux)+r"""\%. Le taux moyen est donc :
                            \begin{center}
                                $t_m=\sqrt["""+str(q1End-q1Start)+r"""]{1+\dfrac{"""+str(q1Taux)+r"""}{100}}-1\approx """+str(round(q2RacineN*100,4))+r"""\%$
                            \end{center}
                        \end{solution}
                    \Part[2] On conjecture qu'à partir de 2012, le taux annuel est de $+ """+str(q3Taux)+r"""$\,\%. Avec ce modèle, quel est le taux de recyclage en 2020 ? On donnera le résultat en pourcentage arrondi au dixième.
%						\fillwithlines{30mm}
                        \begin{solution}
                            De 2012 à 2020, il y a 8 ans, le taux en 2012 était de """+str(data[10][1])+r"""\%. Le taux en 2020 est donc :
                            \begin{center}
                                $"""+str(data[10][1])+r"""\times\left(1+\dfrac{"""+str(q3Taux)+r"""}{100}\right)^8$ soit environ """+str(round(q3Tx2020,2))+r"""\%
                            \end{center}
                        \end{solution}
                \end{parts}
\clearpage
    """
    return(exo, correction)

def exoEvolSchemas(id=False):
    """Generate an exercise and correction about evolution schemas."""
    if id:
        identification = r"""exoEvolSchemas\\"""
    else:
        identification = r""""""
    taux = [0.10, 0.15,0.20,0.25,0.30,0.35,0.40,0.45,0.50,0.55]
    V1 = random.randint(10,80)*10
    t1 = random.choice(taux)*(sign(random.randint(-1,1)))
    
    tr1 = 1/(1+t1)-1
    t2 = random.choice(taux)*(sign(random.randint(-1,1)))
    tr2 = 1/(1+t2)-1
    t3 = random.choice(taux)*(sign(random.randint(-1,1)))
    tr3 = 1/(1+t3)-1
    tg = (1+t1)*(1+t2)*(1+t3)-1
    trg = 1/(1+tg)-1
    V2 = V1*(1+t1)
    V3 = V2*(1+t2)
    V4 = V3*(1+t3)
    
    exo=r"""
\clearpage
"""+identification+r"""
\Question[8] Complétez le schéma suivant en utilisant les formules suivantes :\\
        \textit{(Vous donnerez vos résultats arrondi à deux chiffres après la virgule)}
            \begin{itemize}
                \item $\displaystyle t=\frac{V_F-V_I}{V_I}$ (taux d'évolution entre 2 valeurs)
                \item $\displaystyle V_I\times (1+t) = V_F$ (appliquer un taux d'évolution)
                \item $\displaystyle t_R = \frac{1}{1+t}-1$ (taux réciproque du taux $t$)
            \end{itemize}
            \begin{center}
                \begin{tikzpicture}
                    % Déf. styles
                    \tikzstyle{quadri}=[rectangle,draw,text=black]
                    \tikzstyle{estun}=[->,>=latex]
                    % Noeuds
                    \node[quadri,text width=3cm, minimum height=1cm, align=center] (V1) at (-4,0) {$"""+str(V1)+r"""$};
                    \node[quadri,text width=3cm, minimum height=1cm, align=center] (V2) at (0,0) {\fillwithdottedlines{8mm}};
                    \node[quadri,text width=3cm, minimum height=1cm, align=center] (V3) at (4,0) {\fillwithdottedlines{8mm}};
                    \node[quadri,text width=3cm, minimum height=1cm, align=center] (V4) at (8,0) {\fillwithdottedlines{8mm}};
                    % Taux evolution
                    \node (e) at (-2,1.4) {$"""+f"{t1*100:.2f}"+r"""\%$};
                    \node (e) at (2,1.4) {$"""+f"{t2*100:.2f}"+r"""\%$};
                    \node (e) at (6,1.4) {$"""+f"{t3*100:.2f}"+r"""\%$};
                    
                    \node (e) at (-2,-1.6) {$.....\%$};
                    \node (e) at (2.2,-1.6) {$.....\%$};
                    \node (e) at (6.2,-1.6) {$.....\%$};
                    
                    \node (e) at (2.2,3) {$.....\%$};
                    \node (e) at (2.2,-3) {$.....\%$};
                    % Flèches
                    \draw[-stealth,ultra thick] [bend left](V1.north)to(V2.north);
                    \draw[-stealth,ultra thick] (V2.south)to[bend left](V1.south);
                    
                    \draw[-stealth,ultra thick] [bend left](V2.north)to(V3.north);
                    \draw[-stealth,ultra thick] (V3.south)to[bend left](V2.south);
                    
                    \draw[-stealth,ultra thick] (V3.north)to[bend left](V4.north);
                    \draw[-stealth,ultra thick] (V4.south)to[bend left](V3.south);
                    
                    \draw[-stealth,ultra thick] (V1.north)to[bend left=60](V4.north);
                    \draw[-stealth,ultra thick] (V4.south)to[bend left=60](V1.south);
                \end{tikzpicture}
            \end{center}
            \fillwithlines{105mm}
"""
    correction=r"""
\clearpage
"""+identification+r"""
        \Question[8] Complétez le schéma suivant en utilisant les formules suivantes :\\
        \textit{(Vous donnerez vos résultats arrondi à deux chiffres après la virgule)}
            \begin{itemize}
                \item $\displaystyle t=\frac{V_F-V_I}{V_I}$ (taux d'évolution entre 2 valeurs)
                \item $\displaystyle V_I\times (1+t) = V_F$ (appliquer un taux d'évolution)
                \item $\displaystyle t_R = \frac{1}{1+t}-1$ (taux réciproque du taux $t$)
            \end{itemize}
            \begin{center}
                \begin{tikzpicture}
                    % Déf. styles
                    \tikzstyle{quadri}=[rectangle,draw,text=black]
                    \tikzstyle{estun}=[->,>=latex]
                    % Noeuds
                    \node[quadri,text width=3cm, minimum height=1cm, align=center] (V1) at (-4,0) {$"""+f"{V1:.2f}"+r"""$};
                    \node[quadri,text width=3cm, minimum height=1cm, align=center] (V2) at (0,0) {{\color{red}$"""+f"{V2:.2f}"+r"""$}};
                    \node[quadri,text width=3cm, minimum height=1cm, align=center] (V3) at (4,0) {{\color{red}$"""+f"{V3:.2f}"+r"""$}};
                    \node[quadri,text width=3cm, minimum height=1cm, align=center] (V4) at (8,0) {{\color{red}$"""+f"{V4:.2f}"+r"""$}};
                    % Taux evolution
                    \node (e) at (-2,1.4) {$"""+f"{t1*100:.2f}"+r"""\%$};
                    \node (e) at (2,1.4) {$"""+f"{t2*100:.2f}"+r"""\%$};
                    \node (e) at (6,1.4) {$"""+f"{t3*100:.2f}"+r"""\%$};
                    
                    \node (e) at (-2,-1.6) {{\color{red}$"""+f"{tr1*100:.2f}"+r"""\%$}};
                    \node (e) at (2.2,-1.6) {{\color{red}$"""+f"{tr2*100:.2f}"+r"""\%$}};
                    \node (e) at (6.2,-1.6) {{\color{red}$"""+f"{tr3*100:.2f}"+r"""\%$}};
                    
                    \node (e) at (2.2,3) {{\color{red}$"""+f"{tg*100:.2f}"+r"""\%$}};
                    \node (e) at (2.2,-3) {{\color{red}$"""+f"{trg*100:.2f}"+r"""\%$}};
                    % Flèches
                    \draw[-stealth,ultra thick] [bend left](V1.north)to(V2.north);
                    \draw[-stealth,ultra thick] (V2.south)to[bend left](V1.south);
                    
                    \draw[-stealth,ultra thick] [bend left](V2.north)to(V3.north);
                    \draw[-stealth,ultra thick] (V3.south)to[bend left](V2.south);
                    
                    \draw[-stealth,ultra thick] (V3.north)to[bend left](V4.north);
                    \draw[-stealth,ultra thick] (V4.south)to[bend left](V3.south);
                    
                    \draw[-stealth,ultra thick] (V1.north)to[bend left=60](V4.north);
                    \draw[-stealth,ultra thick] (V4.south)to[bend left=60](V1.south);
                \end{tikzpicture}
            \end{center}
            Pour l'application des taux d'évolution : $\displaystyle V_I\times (1+t) = V_F$
                \begin{enumerate}
                    \item $\displaystyle """+str(V1)+r""" \times (1+\frac{"""+f"{t1*100:.0f}"+r"""}{100})={\color{red}"""+f"{V2:.2f}"+r"""}$
                    \item $\displaystyle """+f"{V2:.2f}"+r""" \times (1+\frac{"""+f"{t2*100:.0f}"+r"""}{100})={\color{red}"""+f"{V3:.2f}"+r"""}$
                    \item $\displaystyle """+f"{V2:.2f}"+r""" \times (1+\frac{"""+f"{t3*100:.0f}"+r"""}{100})={\color{red}"""+f"{V4:.2f}"+r"""}$
                \end{enumerate}
                Pour les taux d'évolution réciproque : $\displaystyle t_R = \frac{1}{1+t}-1$
                \begin{enumerate}
                    \item $\displaystyle \frac{1}{ (1+\frac{"""+f"{t1*100:.0f}"+r"""}{100})}-1={\color{red}"""+f"{tr1*100:.2f}"+r"""\%}$
                    \item $\displaystyle \frac{1}{ (1+\frac{"""+f"{t2*100:.0f}"+r"""}{100})}-1={\color{red}"""+f"{tr2*100:.2f}"+r"""\%}$
                    \item $\displaystyle \frac{1}{ (1+\frac{"""+f"{t3*100:.0f}"+r"""}{100})}-1={\color{red}"""+f"{tr3*100:.2f}"+r"""\%}$
                \end{enumerate}
            Pour le taux global et le taux réciproque global : $\displaystyle t=\frac{V_F-V_I}{V_I}$
                \begin{enumerate}
                    \item $\displaystyle ((1+\frac{"""+f"{t1*100:.0f}"+r"""}{100})\times (1+\frac{"""+f"{t2*100:.0f}"+r"""}{100})\times (1+\frac{"""+f"{t3*100:.0f}"+r"""}{100})-1={\color{red}"""+f"{tg*100:.2f}"+r"""\%}$ \\ ou \\ $\displaystyle \frac{"""+f"{V4:.2f}"+r"""-"""+f"{V1:.2f}"+r"""}{"""+f"{V1:.2f}"+r"""}={\color{red}"""+f"{tg*100:.2f}"+r"""\%}$
                    \item $\displaystyle \frac{1}{ (1+\frac{"""+f"{tg*100:.2f}"+r"""}{100})}-1={\color{red}"""+f"{trg*100:.2f}"+r"""\%}$
                \end{enumerate}
    """
    return(exo, correction)

def exoProba(id=False):
    """Generate an exercise and correction about probabilities."""
    if id:
        identification = r"""exoProba\\"""
    else:
        identification = r""""""
    pT = np.random.randint(10,80)
    pLsachantT = np.random.randint(10,80)
    pLsachantA = np.random.randint(10,80)
    pA=100-pT
    pLBsachantT=100-pLsachantT
    pLBsachantA=100-pLsachantA
    pL = round(pT*pLsachantT+pA*pLsachantA,4)
    exo = r"""
    \clearpage
    """+identification+r"""
        \Question 
            \begin{description}
                \item Dans un lycée, on considère les élèves ayant obtenu le baccalauréat STMG :
                    \setlength\parindent{9mm}
                    \begin{itemize}[label=\textbullet]
                        \item """+str(pT)+r"""\,\% de ces élèves poursuivent leurs études en BTS ou DUT et parmi eux, """+str(pLsachantT)+r"""\,\% après l'obtention du BTS ou DUT poursuivent leurs études et obtiennent une licence.
                        \item Les autres élèves poursuivent d'autres études après le baccalauréat, et parmi eux, """+str(pLsachantA)+r"""\,\% obtiennent une licence.
                    \end{itemize}
                    \setlength\parindent{0mm}
                    On appelle :			
                    \begin{description}
                        \item[$T$] : l'évènement: \og pour suivre ses études en BTS ou DUT\fg{} ;
                        \item[$A$] : l'évènement: \og pour suivre d'autres études après le baccalauréat\fg{} ; 
                        \item[$L$] : l' évènement : \og obtenir une licence \fg.
                        \item[$\overline{L}$]  désigne l'évènement contraire de l'évènement $L$.
                    \end{description}
            \end{description}
            \vspace{0.25cm}
            \begin{parts}
                \Part[6] compléter l'arbre suivant qui modélise la situation:
                    \begin{center}
                        \begin{tikzpicture}[xscale=0.75,yscale=0.75]
                            \tikzstyle{fleche}=[->,>=latex,thick]
                            \tikzstyle{noeud}=[fill=white,circle]
                            \tikzstyle{feuille}=[fill=white]
                            \tikzstyle{etiquette}=[midway,fill=white,draw]
                            \def\DistanceInterNiveaux{4}
                            \def\DistanceInterFeuilles{2}
                            \def\NiveauA{(0)*\DistanceInterNiveaux}
                            \def\NiveauB{(1.5)*\DistanceInterNiveaux}
                            \def\NiveauC{(2.5)*\DistanceInterNiveaux}
                            \def\InterFeuilles{(-1)*\DistanceInterFeuilles}
                            \node[noeud] (R) at ({\NiveauA},{(1.5)*\InterFeuilles}) {$ $};
                            \node[noeud] (Ra) at ({\NiveauB},{(0.5)*\InterFeuilles}) {$T$};
                            \node[feuille] (Raa) at ({\NiveauC},{(0)*\InterFeuilles}) {$L$};
                            \node[feuille] (Rab) at ({\NiveauC},{(1)*\InterFeuilles}) {$\overline{L}$};
                            \node[noeud] (Rb) at ({\NiveauB},{(2.5)*\InterFeuilles}) {$A$};
                            \node[feuille] (Rba) at ({\NiveauC},{(2)*\InterFeuilles}) {$L$};
                            \node[feuille] (Rbb) at ({\NiveauC},{(3)*\InterFeuilles}) {$\overline{L}$};
                            \draw[fleche] (R)--(Ra) node[etiquette] {$ $};
                            \draw[fleche] (Ra)--(Raa) node[etiquette] {$ $};
                            \draw[fleche] (Ra)--(Rab) node[etiquette] {$ $};
                            \draw[fleche] (R)--(Rb) node[etiquette] {$ $};
                            \draw[fleche] (Rb)--(Rba) node[etiquette] {$ $};
                            \draw[fleche] (Rb)--(Rbb) node[etiquette] {$ $};
                        \end{tikzpicture}
                    \end{center}
                \Part[1] Déterminer la valeur de la probabilité $p(T \cap L)$.
                    \fillwithlines{20mm}
                \Part[1] Montrer que $p(L) = """+str(pL/100)+r"""\%$.
                    \fillwithlines{20mm}
                \Part[1] Déterminer la probabilité d'avoir suivi une formation en BTS ou DUT sachant que l'on a obtenu une licence. On arrondira le résultat à  $0,01$\,\%.
                    \fillwithlines{20mm}
                \Part[2] Déterminer la valeur arrondie à  $0,01$\,\% de la probabilité $p_L(A)$. Interpréter.
                    \fillwithlines{20mm}
            \end{parts}
\clearpage
"""
    correction = r"""
    \clearpage
    """+identification+r"""
        \Question 
            \begin{description}
                \item Dans un lycée, on considère les élèves ayant obtenu le baccalauréat STMG :
                    \setlength\parindent{9mm}
                    \begin{itemize}[label=\textbullet]
                        \item """+str(pT)+r"""\,\% de ces élèves poursuivent leurs études en BTS ou DUT et parmi eux, """+str(pLsachantT)+r"""\,\% après l'obtention du BTS ou DUT poursuivent leurs études et obtiennent une licence.
                        \item Les autres élèves poursuivent d'autres études après le baccalauréat, et parmi eux, """+str(pLsachantA)+r"""\,\% obtiennent une licence.
                    \end{itemize}
                    \setlength\parindent{0mm}
                    On appelle :			
                    \begin{description}
                        \item[$T$] : l'évènement: \og pour suivre ses études en BTS ou DUT\fg{} ;
                        \item[$A$] : l'évènement: \og pour suivre d'autres études après le baccalauréat\fg{} ; 
                        \item[$L$] : l' évènement : \og obtenir une licence \fg.
                        \item[$\overline{L}$]  désigne l'évènement contraire de l'évènement $L$.
                    \end{description}
            \end{description}
            \vspace{0.25cm}
            \begin{parts}
                \Part[6] compléter l'arbre suivant qui modélise la situation:
                    \begin{solution}
                        \begin{center}
                            \begin{tikzpicture}[xscale=1,yscale=1]
                                \tikzstyle{fleche}=[->,>=latex,thick]
                                \tikzstyle{noeud}=[fill=white,circle]
                                \tikzstyle{feuille}=[fill=white]
                                \tikzstyle{etiquette}=[midway,fill=white,draw]
                                \def\DistanceInterNiveaux{4}
                                \def\DistanceInterFeuilles{2}
                                \def\NiveauA{(0)*\DistanceInterNiveaux}
                                \def\NiveauB{(1.5)*\DistanceInterNiveaux}
                                \def\NiveauC{(2.5)*\DistanceInterNiveaux}
                                \def\InterFeuilles{(-1)*\DistanceInterFeuilles}
                                \node[noeud] (R) at ({\NiveauA},{(1.5)*\InterFeuilles}) {$ $};
                                \node[noeud] (Ra) at ({\NiveauB},{(0.5)*\InterFeuilles}) {$T$};
                                \node[feuille] (Raa) at ({\NiveauC},{(0)*\InterFeuilles}) {$L$};
                                \node[feuille] (Rab) at ({\NiveauC},{(1)*\InterFeuilles}) {$\overline{L}$};
                                \node[noeud] (Rb) at ({\NiveauB},{(2.5)*\InterFeuilles}) {$A$};
                                \node[feuille] (Rba) at ({\NiveauC},{(2)*\InterFeuilles}) {$L$};
                                \node[feuille] (Rbb) at ({\NiveauC},{(3)*\InterFeuilles}) {$\overline{L}$};
                                \draw[fleche] (R)--(Ra) node[etiquette] {$"""+str(pT)+r"""\%$};
                                \draw[fleche] (Ra)--(Raa) node[etiquette] {$"""+str(pLsachantT)+r"""\%$};
                                \draw[fleche] (Ra)--(Rab) node[etiquette] {$"""+str(pLBsachantT)+r"""\%$};
                                \draw[fleche] (R)--(Rb) node[etiquette] {$"""+str(pA)+r"""\%$};
                                \draw[fleche] (Rb)--(Rba) node[etiquette] {$"""+str(pLsachantA)+r"""\%$};
                                \draw[fleche] (Rb)--(Rbb) node[etiquette] {$"""+str(pLBsachantA)+r"""\%$};
                            \end{tikzpicture}
                        \end{center}
                    \end{solution}
                \Part[1] Déterminer la valeur de la probabilité $p(T \cap L)$.
                    \begin{solution}
                        $p(T\cap L)=p(T)\times p_T(L)="""+str(pT/100)+r"""\times """+str(pLsachantT/100)+r"""="""+str(round(pT/100*pLsachantT/100,4))+r"""$
                    \end{solution}
                \Part[1] Montrer que $p(L) = """+str(pL/100)+r"""\%$.
                    \begin{solution}
                        $p(L) = p(T\cap L)+p(A\cap L) = """+str(round(pT/100*pLsachantT/100,4))+r"""+"""+str(round(pA/100,4))+r"""\times """+str(round(pLsachantA/100,4))+r"""="""+str(round(pT/100*pLsachantT/100,4))+r"""+"""+str(round(pA/100*pLsachantA/100,4))+r"""="""+str(round(pT/100*pLsachantT/100+pA/100*pLsachantA/100,4))+r"""$
                    \end{solution}
                \Part[1] Déterminer la probabilité d'avoir suivi une formation en BTS ou DUT sachant que l'on a obtenu une licence. On arrondira le résultat à  $0,01$\,\%.
                    \begin{solution}
                        La probabilité d'avoir suivi une formation en BTS ou DUT sachant que l'on a obtenu une licence, est : 
                        \begin{center}
                            $p_L(T) =\dfrac{p(L\cap T)}{p(L)}=\dfrac{"""+str(round(pT/100*pLsachantT/100,4))+r"""}{"""+str(round(pT/100*pLsachantT/100+pA/100*pLsachantA/100,4))+r"""}\approx """+str(round((pT/100*pLsachantT/100)/(pT/100*pLsachantT/100+pA/100*pLsachantA/100),4))+r"""$
                        \end{center}
                    \end{solution}
                \Part[2] Déterminer la valeur arrondie à  $0,01$\,\% de la probabilité $p_L(A)$. Interpréter.
                    \begin{solution}
                        \begin{center}
                            $p_L(A)=\dfrac{p(A\cap L)}{p(L)}=\dfrac{"""+str(round(pA/100*pLsachantA/100,4))+r"""}{"""+str(pL/100)+r"""}\approx """+str(round((pA/100*pLsachantA/100)/(pL/100),4))+r"""$
                        \end{center}
                        C'est la probabilité de ne pas avoir suivi une formation en BTS ou DUT sachant que l'on a obtenu une licence.
                    \end{solution}
            \end{parts}
\clearpage
"""
    return(exo, correction)

def exoProba1(id=False):
    """Generate an exercise and correction about probabilities."""
    if id:
        identification = r"""exoProba1\\"""
    else:
        identification = r""""""
    # pS=1
    # effectifCouture=1
    # while (effectifCouture!=0):
    effectifTotal = np.random.randint(low=3,high=8)*100
    effectifStylisme = np.random.randint(low=10,high=20)*10# 50
    effectifDecoupe = np.random.randint(low=5,high=9)*10 # 100
    effectifCouture = effectifTotal-effectifStylisme-effectifDecoupe# 150
    pS = sp.Rational(effectifStylisme,effectifTotal)
    pD = sp.Rational(effectifDecoupe,effectifTotal)
    pC = sp.Rational(effectifCouture,effectifTotal)
    psA = sp.Rational(np.random.randint(25,75),100)
        # print(f"effectifCouture : {effectifCouture}")
    psAb = 1-psA
    pdA = sp.Rational(np.random.randint(25,75),100)
    pdA1 = f"{pdA.evalf()*100:.0f}%"
    pdAb = 1-pdA
    pdAb1 = f"{pdAb.evalf()*100:.0f}%"
    pcA = sp.Rational(np.random.randint(25,75),100)
    pcA1 = f"{pcA.evalf()*100:.0f}%"
    pcAb = 1-pcA
    pcAb1 = f"{pcAb.evalf()*100:.0f}%"
    pS_Inter_A = pS*psA
    pS_Inter_A1 = f"{pS_Inter_A.evalf()*100:.2f}%"
    pD_Inter_A = pD*pdA
    pD_Inter_A1 = f"{pD_Inter_A.evalf()*100:.2f}%"
    pC_Inter_A = pC*pcA
    pC_Inter_A1 = f"{pC_Inter_A.evalf()*100:.2f}%"
    pA = pS_Inter_A + pD_Inter_A + pC_Inter_A
    pA1 = f"{pA.evalf()*100:.2f}%"
    paS = pS_Inter_A/pA
    exo=r"""
    """+identification+r"""
\Question Une entreprise de textile emploie """+str(effectifTotal)+r""" personnes dans le secteur confection. Il est composé de trois ateliers.\\
	L'atelier de stylisme est constitué de """+str(effectifStylisme)+r""" personnes.\\L'atelier de découpe est constitué de """+str(effectifDecoupe)+r""" personnes.\\Le reste du personnel travaille dans l'atelier de couture. Après une étude sur l'absentéisme, le directeur des ressources humaines a constaté que sur une année :
	\begin{enumerate}
		\item $"""+f"{psA.evalf()*100:.0f}"+r"""\%$ des stylistes ont eu au moins une absence;
		\item $"""+f"{pdA.evalf()*100:.0f}"+r"""\%$ du personnel de découpe ont eu au moins une absence;
		\item $"""+f"{pcA.evalf()*100:.0f}"+r"""\%$ du personnel de l'atelier de couture n'ont pas eu d'absence.
	\end{enumerate}
	On choisit une personne au hasard dans cette entreprise et l'on admet que chaque personne a la même probabilité d'être choisie.\\
	On note :
	\begin{enumerate}
		\item S l'évènement : « la personne choisie travaille à l'atelier de stylisme »;
		\item D l'événement : « la personne choisie travaille à l'atelier de découpe »;
		\item C l'événement : « la personne choisie travaille à l'atelier de couture »;
		\item A l'événement : « la personne choisie a eu au moins une absence ».
	\end{enumerate}
	Rappel : Si M et N sont deux événements, on note $\overline{M}$ l'événement contraire de l'événement M et $p_N(M)$ la probabilité de l'événement M sachant N.
	\begin{parts}
		\Part[9] Construire un arbre pondéré décrivant la situation.
			\begin{center}
				% Racine à Gauche, développement vers la droite
				\begin{tikzpicture}[xscale=1,yscale=1]
					% Styles (MODIFIABLES)
					\tikzstyle{fleche}=[->,>=latex,thick]
					\tikzstyle{noeud}=[fill=white,circle]
					\tikzstyle{feuille}=[fill=white,circle]
					\tikzstyle{etiquette}=[midway,fill=white]
					% Dimensions (MODIFIABLES)
					\def\DistanceInterNiveaux{3}
					\def\DistanceInterFeuilles{2}
					% Dimensions calculées (NON MODIFIABLES)
					\def\NiveauA{(0)*\DistanceInterNiveaux}
					\def\NiveauB{(1.5)*\DistanceInterNiveaux}
					\def\NiveauC{(2.5)*\DistanceInterNiveaux}
					\def\InterFeuilles{(-1)*\DistanceInterFeuilles}
					% Noeuds (MODIFIABLES : Styles et Coefficients d'InterFeuilles)
					\node[noeud] (R) at ({\NiveauA},{(2.5)*\InterFeuilles}) {$....$};
					\node[noeud] (Ra) at ({\NiveauB},{(0.5)*\InterFeuilles}) {$....$};
					\node[feuille] (Raa) at ({\NiveauC},{(0)*\InterFeuilles}) {$....$};
					\node[feuille] (Rab) at ({\NiveauC},{(1)*\InterFeuilles}) {$....$};
					\node[noeud] (Rb) at ({\NiveauB},{(2.5)*\InterFeuilles}) {$....$};
					\node[feuille] (Rba) at ({\NiveauC},{(2)*\InterFeuilles}) {$....$};
					\node[feuille] (Rbb) at ({\NiveauC},{(3)*\InterFeuilles}) {$....$};
					\node[noeud] (Rc) at ({\NiveauB},{(4.5)*\InterFeuilles}) {$....$};
					\node[feuille] (Rca) at ({\NiveauC},{(4)*\InterFeuilles}) {$....$};
					\node[feuille] (Rcb) at ({\NiveauC},{(5)*\InterFeuilles}) {$....$};
					% Arcs (MODIFIABLES : Styles)
					\draw[fleche] (R)--(Ra) node[etiquette] {$....$};
					\draw[fleche] (Ra)--(Raa) node[etiquette] {$....$};
					\draw[fleche] (Ra)--(Rab) node[etiquette] {$....$};
					\draw[fleche] (R)--(Rb) node[etiquette] {$....$};
					\draw[fleche] (Rb)--(Rba) node[etiquette] {$....$};
					\draw[fleche] (Rb)--(Rbb) node[etiquette] {$....$};
					\draw[fleche] (R)--(Rc) node[etiquette] {$....$};
					\draw[fleche] (Rc)--(Rca) node[etiquette] {$....$};
					\draw[fleche] (Rc)--(Rcb) node[etiquette] {$....$};
				\end{tikzpicture}
			\end{center}
\clearpage
		\Part Déduire des informations de l'énoncé :
			\begin{multicols}{2}
				\begin{subparts}
					\subpart[3] Les probabilités p(S),p(D) et p(C) des événements S,D et C.
						\fillwithlines{20mm}
					\subpart[3] Les probabilités $p_S(A)$,$p_D(A)$ et $p_C(\overline{A})$.
						\fillwithlines{20mm}
				\end{subparts}
			\end{multicols}
		\Part[3] Calculer la probabilité de l'événement $S\cap A$, notée $p(S\cap A)$.
            \fillwithlines{30mm}
		\Part[8] Démontrer que $p(A) = """+f"{pA.evalf():.4f}"+r"""$
            \fillwithlines{30mm}
		\Part[4] On sait que la personne choisie a eu au moins une absence cette année. Quelle est la probabilité que cette personne soit un styliste ?
            \fillwithlines{30mm}
	\end{parts}
    """
    correction=r"""
    """+identification+r"""
\Question Une entreprise de textile emploie """+str(effectifTotal)+r""" personnes dans le secteur confection. Il est composé de trois ateliers.\\
	L'atelier de stylisme est constitué de """+str(effectifStylisme)+r""" personnes.\\L'atelier de découpe est constitué de """+str(effectifDecoupe)+r""" personnes.\\Le reste du personnel travaille dans l'atelier de couture. Après une étude sur l'absentéisme, le directeur des ressources humaines a constaté que sur une année :
	\begin{enumerate}
		\item $"""+f"{psA.evalf()*100:.0f}"+r"""\%$ des stylistes ont eu au moins une absence;
		\item $"""+f"{pdA.evalf()*100:.0f}"+r"""\%$ du personnel de découpe ont eu au moins une absence;
		\item $"""+f"{pcA.evalf()*100:.0f}"+r"""\%$ du personnel de l'atelier de couture n'ont pas eu d'absence.
	\end{enumerate}
	On choisit une personne au hasard dans cette entreprise et l'on admet que chaque personne a la même probabilité d'être choisie.\\
	On note :
	\begin{enumerate}
		\item S l'évènement : « la personne choisie travaille à l'atelier de stylisme »;
		\item D l'événement : « la personne choisie travaille à l'atelier de découpe »;
		\item C l'événement : « la personne choisie travaille à l'atelier de couture »;
		\item A l'événement : « la personne choisie a eu au moins une absence ».
	\end{enumerate}
	Rappel : Si M et N sont deux événements, on note $\overline{M}$ l'événement contraire de l'événement M et $p_N(M)$ la probabilité de l'événement M sachant N.
	\begin{parts}
		\Part Construire un arbre pondéré décrivant la situation.
			\begin{center}
				% Racine à Gauche, développement vers la droite
				\begin{tikzpicture}[xscale=1,yscale=1]
					% Styles (MODIFIABLES)
					\tikzstyle{fleche}=[->,>=latex,thick]
					\tikzstyle{noeud}=[fill=white,circle]
					\tikzstyle{feuille}=[fill=white,circle]
					\tikzstyle{etiquette}=[midway,fill=white]
					% Dimensions (MODIFIABLES)
					\def\DistanceInterNiveaux{3}
					\def\DistanceInterFeuilles{2}
					% Dimensions calculées (NON MODIFIABLES)
					\def\NiveauA{(0)*\DistanceInterNiveaux}
					\def\NiveauB{(1.5)*\DistanceInterNiveaux}
					\def\NiveauC{(2.5)*\DistanceInterNiveaux}
					\def\InterFeuilles{(-1)*\DistanceInterFeuilles}
					% Noeuds (MODIFIABLES : Styles et Coefficients d'InterFeuilles)
					\node[noeud] (R) at ({\NiveauA},{(2.5)*\InterFeuilles}) {};
					\node[noeud] (Ra) at ({\NiveauB},{(0.5)*\InterFeuilles}) {$S$};
					\node[feuille] (Raa) at ({\NiveauC},{(0)*\InterFeuilles}) {$A$};
					\node[feuille] (Rab) at ({\NiveauC},{(1)*\InterFeuilles}) {$\overline{A}$};
					\node[noeud] (Rb) at ({\NiveauB},{(2.5)*\InterFeuilles}) {$D$};
					\node[feuille] (Rba) at ({\NiveauC},{(2)*\InterFeuilles}) {$A$};
					\node[feuille] (Rbb) at ({\NiveauC},{(3)*\InterFeuilles}) {$\overline{A}$};
					\node[noeud] (Rc) at ({\NiveauB},{(4.5)*\InterFeuilles}) {$C$};
					\node[feuille] (Rca) at ({\NiveauC},{(4)*\InterFeuilles}) {$A$};
					\node[feuille] (Rcb) at ({\NiveauC},{(5)*\InterFeuilles}) {$\overline{A}$};
					% Arcs (MODIFIABLES : Styles)
					\draw[fleche] (R)--(Ra) node[etiquette] {$"""+Latex(pS)+r"""$};
					\draw[fleche] (Ra)--(Raa) node[etiquette] {$"""+f"{psA.evalf()*100:.0f}"+r"""\%$};
					\draw[fleche] (Ra)--(Rab) node[etiquette] {$"""+f"{psAb.evalf()*100:.0f}"+r"""\%$};
					\draw[fleche] (R)--(Rb) node[etiquette] {$"""+Latex(pD)+r"""$};
					\draw[fleche] (Rb)--(Rba) node[etiquette] {$"""+f"{pdA.evalf()*100:.0f}"+r"""\%$};
					\draw[fleche] (Rb)--(Rbb) node[etiquette] {$"""+f"{pdAb.evalf()*100:.0f}"+r"""\%$};
					\draw[fleche] (R)--(Rc) node[etiquette] {$"""+Latex(pC)+r"""$};
					\draw[fleche] (Rc)--(Rca) node[etiquette] {$"""+f"{pcA.evalf()*100:.0f}"+r"""\%$};
					\draw[fleche] (Rc)--(Rcb) node[etiquette] {$"""+f"{pcAb.evalf()*100:.0f}"+r"""\%$};
				\end{tikzpicture}
			\end{center}
\clearpage
		\Part Déduire des informations de l'énoncé :
			\begin{multicols}{2}
				\begin{subparts}
					\subpart Les probabilités p(S),p(D) et p(C) des événements S,D et C.
                    {\color{red}
						$p(S) = """+Latex(pS)+r"""$ ; 
                        $p(D) = """+Latex(pD)+r"""$ ; 
                        $p(C) = """+Latex(pC)+r"""$
                    }
                        \columnbreak
					\subpart Les probabilités $p_S(A)$,$p_D(A)$ et $p_C(\overline{A})$.
                    {\color{red}
						$p_S(A) = """+f"{psA.evalf()*100:.0f}"+r"""\%$ ; 
                        $p_D(A) = """+f"{pdA.evalf()*100:.0f}"+r"""\%$ ; 
                        $p_C(\overline{A}) = """+f"{pcAb.evalf()*100:.0f}"+r"""\%$
                    }
				\end{subparts}
			\end{multicols}
		\Part Calculer la probabilité de l'événement $S\cap A$, notée $p(S\cap A)$.
            \begin{solution}
                \begin{align*}
                    p(S\cap A)  &= p(S) \times p_S(A)\\
                                &= """+Latex(pS)+r""" \times """+Latex(psA)+r"""\\
                                &= """+Latex(pS_Inter_A)+r""" \approx """+f"{pS_Inter_A.evalf()*100:.4f}"+r"""\%
                \end{align*}
            \end{solution}
		\Part Démontrer que $p(A) = """+f"{pA.evalf():.4f}"+r"""$
            \begin{solution}
                \begin{align*}
                    p(A)	&=& &p(S\cap A) &+&  &p(D\cap A)& &+& &p(C\cap a)&\\
                            &=& &"""+Latex(pS_Inter_A)+r""" &+&  &p(D)\times p_D(A)& &+& &p(C)\times p_C(A)&\\
                            &=& &"""+Latex(pS_Inter_A)+r""" &+& &"""+Latex(pD)+r"""\times """+Latex(pdA)+r"""& &+& &"""+Latex(pC)+r"""\times """+Latex(pcA)+r"""&\\
                            &=& &"""+Latex(pS_Inter_A)+r""" &+& &"""+Latex(pD*pdA)+r"""& &+& &"""+Latex(pC*pcA)+r"""&\\
                            &=& &"""+Latex(pS_Inter_A+pD_Inter_A+pC_Inter_A)+r""" \approx"""+f"{pA.evalf():.4f}"+r"""
                \end{align*}
            \end{solution}
		\Part On sait que la personne choisie a eu au moins une absence cette année. Quelle est la probabilité que cette personne soit un styliste ?
            \begin{solution}
                \begin{align*}
                    p(S\cap A)  &= p(A\cap S)\\
                                &= p(A) \times p_A(S)\\
    \dfrac{p(S\cap A)}{p(A)}    &= p_A(S)\\
    \dfrac{"""+Latex(pS_Inter_A)+r"""}{"""+Latex(pA)+r"""} &= p_A(S)\\
    """+Latex(pS_Inter_A/pA)+r""" &= p_A(S) \approx """+f"{paS.evalf():.4f}"+r"""
                \end{align*}
            \end{solution}
	\end{parts}
    """
    return(exo,correction)

def lectureGraphiqueAffine(id=False):
    """Generate an exercise and correction about reading affine functions from a graph."""
    if id:
        identification = r"""lectureGraphiqueAffine\\"""
    else:
        identification = r""""""
    alphabet = list(string.ascii_lowercase)
    fonctions = random.sample(alphabet, 4)
    fonctions.sort()
    traceFonction=r""""""
    questionExo=r""""""
    questionCorr=r""""""
    for f in fonctions:
        k = nonEqRandomValue(n=2, notNull=True, demi=True, tier=False, quart=False)
        p = affine(f, k[0], k[1])
        if p.a>0:
            minX=(-4.5-p.b)/p.a
            maxX=(4.5-p.b)/p.a
        if p.a<0:
            minX=(4.5-p.b)/p.a
            maxX=(-4.5-p.b)/p.a
        if p.a==0:
            minX=-4.5   
        minX=max(-4.5,round(float(minX),2))
        maxX=min(4.5,round(float(maxX),2))
        traceFonction=traceFonction+r"""\draw[domain="""+str(min(minX,maxX))+r""":"""+str(max(minX,maxX))+r""", smooth, variable=\x, blue] plot ({\x}, {"""+str(p.a)+r"""*\x+"""+str(p.b)+r"""}) node[below] {$\mathcal{C}_{"""+p.name+r"""}$};
        """
        questionExo = questionExo + r"""
                \Part $"""+p.name+r"""(x)=.........................$
                \fillwithlines{20mm}
"""
        questionCorr = questionCorr+r"""\Part \color{red}{"""+p.latexString()+r"""}\color{black}
        """
        
    exo=r"""
    \clearpage
    """+identification+r"""
        \Question[8] Fonctions affines\\
        Donnez l'expression algébrique des fonctions affines associées aux droites suivantes :
        \begin{center}
        		\begin{tikzpicture}[scale=1.5,cap=round]
                % Local definitions
                \def\costhirty{0.8660256}

                % Colors
                \colorlet{anglecolor}{green!50!black}
                \colorlet{sincolor}{red}
                \colorlet{tancolor}{orange!80!black}
                \colorlet{coscolor}{blue}

                % Styles
                \tikzstyle{axes}=[]
                \tikzstyle{important line}=[very thick]
                \tikzstyle{information text}=[rounded corners,fill=red!10,inner sep=1ex]

                % Grille
                \draw[style=help lines,step=0.5cm] (-4.4,-4.4) grid (4.4,4.4);
                
				% The graphic
                \begin{scope}[style=axes]
                    \draw[->] (-4.5,0) -- (4.5,0) node[right] {$x$};
                    \draw[->] (0,-4.5) -- (0,4.5) node[above] {$y$};
                    \draw[->, very thick] (0,0) -- (1,0) node[below, midway] {$\vect{i}$};
                    \draw[->, very thick] (0,0) -- (0,1) node[left, midway] {$\vect{j}$};
                    \node[below left] at (-0.15,-0.15) {0};
                    \foreach \x/\xtext in {-4, -3, -2, -1, 0, 1, 2, 3, 4}
                    \draw[xshift=\x cm] (0pt,1pt) -- (0pt,-1pt) node[below,fill=white] {\tiny{$\xtext$}};
                    %
                    \foreach \y/\ytext in {-4, -3, -2, -1, 0, 1, 2, 3, 4}
                        \draw[yshift=\y cm] (1pt,0pt) -- (-1pt,0pt) node[left,fill=white] {\tiny{$\ytext$}};
                \end{scope}
"""+traceFonction+r"""
            \end{tikzpicture}
        \end{center}
        \begin{multicols}{2}
	        	\begin{parts}
"""+questionExo+r"""
        		\end{parts}
        \end{multicols}
    """
    correction=r"""
    \clearpage
    """+identification+r"""
        \Question[8] Fonctions affines\\
        Donnez l'expression algébrique des fonctions affines associées aux droites suivantes :
        \begin{center}
        		\begin{tikzpicture}[scale=1.5,cap=round]
                % Local definitions
                \def\costhirty{0.8660256}

                % Colors
                \colorlet{anglecolor}{green!50!black}
                \colorlet{sincolor}{red}
                \colorlet{tancolor}{orange!80!black}
                \colorlet{coscolor}{blue}

                % Styles
                \tikzstyle{axes}=[]
                \tikzstyle{important line}=[very thick]
                \tikzstyle{information text}=[rounded corners,fill=red!10,inner sep=1ex]

                % Grille
                \draw[style=help lines,step=0.5cm] (-4.4,-4.4) grid (4.4,4.4);
                
				% The graphic
                \begin{scope}[style=axes]
                    \draw[->] (-4.5,0) -- (4.5,0) node[right] {$x$};
                    \draw[->] (0,-4.5) -- (0,4.5) node[above] {$y$};
                    \draw[->, very thick] (0,0) -- (1,0) node[below, midway] {$\vect{i}$};
                    \draw[->, very thick] (0,0) -- (0,1) node[left, midway] {$\vect{j}$};
                    \node[below left] at (-0.15,-0.15) {0};
                    \foreach \x/\xtext in {-4, -3, -2, -1, 0, 1, 2, 3, 4}
                    \draw[xshift=\x cm] (0pt,1pt) -- (0pt,-1pt) node[below,fill=white] {\tiny{$\xtext$}};
                    %
                    \foreach \y/\ytext in {-4, -3, -2, -1, 0, 1, 2, 3, 4}
                        \draw[yshift=\y cm] (1pt,0pt) -- (-1pt,0pt) node[left,fill=white] {\tiny{$\ytext$}};
                \end{scope}
"""+traceFonction+r"""
            \end{tikzpicture}
        \end{center}
        \begin{multicols}{2}
	        	\begin{parts}
"""+questionCorr+r"""
        		\end{parts}
        \end{multicols}
    """
    return(exo,correction)

def exoEvolConsoEau(id=False):
    """Generate an exercise and correction about evolution of water consumption."""
    if id:
        identification = r"""exoEvolConsoEau\\"""
    else:
        identification = r""""""
    Vol1 = random.randint(10,80)*10
    Vol2 = random.randint(10,80)*10
    t = (Vol2-Vol1)/Vol1
    tr = 1/(1+t)-1
    Annee1 = random.randint(2000,2010)
    Annee2 = Annee1+random.randint(4,10)
    n = Annee2-Annee1
    tm = np.power(1+t,1/n)-1
    
    exo=r"""
    \clearpage
    """+identification+r"""
            \Question Une famille a consommé """+str(Vol1)+r""" mètres cubes d'eau en """+str(Annee1)+r""" et """+str(Vol2)+r""" mètres cubes d'eau en """+str(Annee2)+r""".
                \begin{parts}
                    \Part Calculer $t$ le taux d'évolution global en pourcentage (\textit{arrondi au centième}).
                        \fillwithlines{25mm}
                    \Part Calculer $t_R$ le taux d'évolution réciproque global en pourcentage (\textit{arrondi au centième}).
                        \fillwithlines{25mm}
                    \Part Calculer $t_m$ le taux d'évolution moyen global en pourcentage (\textit{arrondi au centième}).
                        \fillwithlines{25mm}
                \end{parts}
    """
    correction=r"""
    \clearpage
    """+identification+r"""
            \Question Une famille a consommé """+str(Vol1)+r""" mètres cubes d'eau en """+str(Annee1)+r""" et """+str(Vol2)+r""" mètres cubes d'eau en """+str(Annee2)+r""".
                \begin{parts}
                    \Part Calculer $t$ le taux d'évolution global en pourcentage (\textit{arrondi au centième}).
                        \begin{center}
                            $\displaystyle t=\frac{V_{Finale}-V_{Initiale}}{V_{Initiale}}$ d'où $\displaystyle t=\frac{"""+str(Vol2)+r"""-"""+str(Vol1)+r"""}{"""+str(Vol1)+r"""}={\color{red}"""+f"{t*100:.2f}"+r"""\%}$
                        \end{center}
                    \Part Calculer $t_R$ le taux d'évolution réciproque global en pourcentage (\textit{arrondi au centième}).
                        \begin{center}
                            $\displaystyle t_R=\frac{1}{1+t}-1$ d'où $\displaystyle t_R=\frac{1}{1+\frac{"""+f"{t*100:.2f}"+r"""}{100}}={\color{red}"""+f"{tr*100:.2f}"+r"""\%}$
                        \end{center}
                    \Part Calculer $t_m$ le taux d'évolution moyen global en pourcentage (\textit{arrondi au centième}).
                        \fillwithlines{25mm}
                \end{parts}
    """
    return(exo, correction)

def exoAffineBourse(id=False):
    if id:
        identification = r"""exoAffineBourse\\"""
    else:
        identification = r""""""
    xa = sp.Rational(0)
    ya = nonEqRandomValue(debut=1,fin=4)
    ya = ya[0]
    xb = nonEqRandomValue(debut=7,fin=9)
    xb = xb[0]
    yb = nonEqRandomValue(debut=1,fin=8)
    yb = yb[0]
    while ya==yb:
        xa = sp.Rational(0)
        ya = nonEqRandomValue(debut=1,fin=4)
        ya = ya[0]
        xb = nonEqRandomValue(debut=7,fin=9)
        xb = xb[0]
        yb = nonEqRandomValue(debut=1,fin=8)
        yb = yb[0]
    
    p = affine("C",1,1)
    p.setFrom2Points(xa,ya,xb,yb)
    # k = nonEqRandomValue(n=2, notNull=True, tier=True)
    # p = affine("f", k[0], k[1])
    if p.a>0:
        pHaut = affine("H" , p.a*sp.Rational(3,4), p.b+1)
        pHaut.setFrom2Points(0,ya+1, xb,yb)
        pBas  = affine("B" , p.a*sp.Rational(5,4) , p.b-1)
        pBas.setFrom2Points(0,ya-1, xb,yb)
    if p.a<0:
        pHaut = affine("H" , p.a*sp.Rational(5,4), p.b+1)
        pHaut.setFrom2Points(0,ya+1, xb,yb)
        pBas  = affine("B" , p.a*sp.Rational(3,4) , p.b-1)
        pBas.setFrom2Points(0,ya-1, xb,yb)
    a=(yb-pHaut.imageDe(0))/(xb-0)
    b=pHaut.imageDe(0)-a*xa
    # print(p)
    # print(pHaut)
    # print(pBas)
    inter = p.intersection(pHaut)
    if inter!=False:
        ch = r"""\addplot [very thin] coordinates {"""
        x=0
        while x <= inter[0]:
            yH = pHaut.imageDe(x)
            yB = pBas.imageDe(x)
            x = x + sp.Rational(1,20)
            y = random.uniform(yB,yH)
            ch = ch + f"({x.evalf():.2f},{y.evalf():.2f}) "
        ch = ch + r"""};
        """

    exo = r"""
    \clearpage
    """+identification+r"""
    \Question Le graphique ci-dessous représente l'évolution d'une action boursière. La droite $(\mathcal{"""+p.name+r"""})$ représente la fonction """+p.latexString()+r""" (moyenne centrée de l'action boursière).
	\begin{center}
		\begin{tikzpicture}[scale=1]
			\begin{axis}[
						grid= both ,
						minor tick num=1,
						minor grid style={line width=.1pt, dashed	},
						major grid style={line width=.4pt},
						width=0.8\textwidth ,
						xlabel = {Heure} ,
						ylabel = {Valeur} ,
						xmin = 0, xmax = 10,
						ymin = 0, ymax = 10,
						yticklabel style={
						/pgf/number format/.cd,%
						scaled y ticks = false,
						set thousands separator={},
						fixed
						},
						%legend entries={Courbe 1, Courbe 2},
						%legend style={at={(0,1)},anchor=north west}
						]
                """+ch+r"""
                \addplot [very thick] expression[domain=0:10]{"""+p.__str__()+r"""} node[above, sloped, pos = 0.2] {($\mathcal{C})$};
                \addplot [dashed, thin] expression[domain=0:10]{"""+pHaut.__str__()+r"""} node[above, sloped, pos = 0.2] {($\mathcal{H}$)}; 
                \addplot [dashed, thin] expression[domain=0:10]{"""+pBas.__str__()+r"""} node[above, sloped, pos = 0.2] {($\mathcal{B}$)};
                \end{axis}
		\end{tikzpicture}
	\end{center}
	\begin{parts}
		\Part[4] déterminez l'expression de la fonction $H(x)$ représenté par la droite $(\mathcal{H})$.
			\fillwithlines{35mm}
		\Part[4] En considérant que la droite $(\mathcal{H})$ représente le maximum de l'action boursière et la droite $(\mathcal{B})$ le minimum de la valeur.\\
			Quelles sont les valeurs minimales et maximales de l'action boursière à 4h et 5h ?
			\fillwithlines{10mm}
		\Part[3] déterminez (par le calcul), le point d'intersection des droites $(\mathcal{C})$ et $(\mathcal{H})$.
			\fillwithlines{40mm}
	\end{parts}
    """
    correction = r"""
    \clearpage
    """+identification+r"""
    \Question Le graphique ci-dessous représente l'évolution d'une action boursière. La droite $(\mathcal{"""+p.name+r"""})$ représente la fonction """+p.latexString()+r""" (moyenne centrée de l'action boursière).
    \begin{center}
        \begin{tikzpicture}[scale=1]
            \begin{axis}[
                        grid= both ,
                        minor tick num=1,
                        minor grid style={line width=.1pt, dashed	},
                        major grid style={line width=.4pt},
                        width=0.8\textwidth ,
                        xlabel = {Heure} ,
                        ylabel = {Valeur} ,
                        xmin = 0, xmax = 10,
                        ymin = 0, ymax = 10,
                        yticklabel style={
                        /pgf/number format/.cd,%
                        scaled y ticks = false,
                        set thousands separator={},
                        fixed
                        },
                        %legend entries={Courbe 1, Courbe 2},
                        %legend style={at={(0,1)},anchor=north west}
                        ]
                """+ch+r"""
                \addplot [very thick] expression[domain=0:10]{"""+p.__str__()+r"""} node[above, sloped, pos = 0.2] {($\mathcal{C})$};
                \addplot [dashed, thin] expression[domain=0:10]{"""+pHaut.__str__()+r"""} node[above, sloped, pos = 0.2] {($\mathcal{H}$)}; 
                \addplot [dashed, thin] expression[domain=0:10]{"""+pBas.__str__()+r"""} node[above, sloped, pos = 0.2] {($\mathcal{B}$)};
                \end{axis}
        \end{tikzpicture}
    \end{center}
    \begin{parts}
        \Part déterminez l'expression de la fonction $H(x)$ représenté par la droite $(\mathcal{H})$.
            \begin{solution}
                On remarque que la représentation graphique de $H(x)$ passe par le point de coordonnées $A(0;"""+Latex(ya+1)+r""")$ et le point de coordonnées $B("""+Latex(xb)+r""";"""+Latex(yb)+r""")$ \\
                La représentation graphique de $H(x)$ est une droite non verticale donc son expression algébrique est de forme affine soit :
                $H(x)=ax+b$ avec $a=\dfrac{y_b-y_a}{x_b-x_a}$ et $b=y_a-ax_a$\\
                en appliquant, on obtient :\\
                \begin{center}
                    $a=\dfrac{"""+Latex(yb-pHaut.imageDe(0))+r"""}{"""+Latex(xb-0)+r"""}="""+Latex(a)+r"""$ et $b="""+Latex(ya)+r"""-"""+Latex(a)+r"""\times """+Latex(xa)+r"""="""+Latex(b)+r"""$
                \end{center}
                d'où {\color{red}$H(x)="""+Latex(a)+r"""x+"""+Latex(b)+r"""$} 
            \end{solution}
        \Part En considérant que la droite $(\mathcal{H})$ représente le maximum de l'action boursière et la droite $(\mathcal{B})$ le minimum de la valeur.\\
                Quelles sont les valeurs minimales et maximales de l'action boursière à 4h et 5h ?
            \begin{solution}
                Les valeurs hautes à 4h et 5h sont $"""+Latex(pHaut.imageDe(4))+r"""$ et $"""+Latex(pHaut.imageDe(5))+r"""$\\
                Les valeurs basses à 4h et 5h sont $"""+Latex(pBas.imageDe(4))+r"""$ et $"""+Latex(pBas.imageDe(5))+r"""$
            \end{solution}
        \Part déterminez (par le calcul), le point d'intersection des droites $(\mathcal{C})$ et $(\mathcal{H})$.
                \begin{solution}
                Les deux droites se croisent lorsque $C(x)=H(x)$.\\
                Nous résolvons donc cette équation :
                \begin{align*}
                    C(x)&=H(x)\\
                    """+p.latexString1()+r"""&="""+pHaut.latexString1()+r"""\\
                    """+Latex(p.a-pHaut.a)+r"""x&="""+Latex(pHaut.b-p.b)+r"""\\
                        x&="""+Latex((pHaut.b-p.b)/(p.a-pHaut.a))+r"""
                \end{align*}
                il reste à calculer l'image par l'une des deux fonctions.
                \begin{align*}
                    C("""+Latex((pHaut.b-p.b)/(p.a-pHaut.a))+r""")&="""+Latex(p.a)+r""" \times """+Latex((pHaut.b-p.b)/(p.a-pHaut.a))+r""" + ("""+Latex(p.b)+r""")\\
                                    &="""+Latex(p.imageDe((pHaut.b-p.b)/(p.a-pHaut.a)))+r"""
                \end{align*}
                donc le point d'intersection de $\mathcal{C}$ et $\mathcal{H}$ a pour coordonnées {\color{red}$("""+Latex((pHaut.b-p.b)/(p.a-pHaut.a))+r""";"""+Latex(p.imageDe((pHaut.b-p.b)/(p.a-pHaut.a)))+r""")$}
            \end{solution}
        \end{parts}
        """
    # print(correction)
    return(exo,correction)

def polyDegre2_Factor(n:int=5):
    if id:
        identification = r"""polyDegre2_Factor\\"""
    else:
        identification = r""""""
    item = r""""""
    itemCorr = r""""""
    for i in range(n):
        alpha = nonEqRandomValue(quart=True, tier=True, demi=True)[0]*(-1 if random.randint(1,100)%2==0 else 1)
        a1 = nonEqRandomValue(quart=True, tier=True, demi=True)[0]*(-1 if random.randint(1,100)%2==0 else 1)
        b1 = nonEqRandomValue(quart=True, tier=True, demi=True)[0]*(-1 if random.randint(1,100)%2==0 else 1)
        a2 = nonEqRandomValue(quart=True, tier=True, demi=True)[0]*(-1 if random.randint(1,100)%2==0 else 1)
        b2 = nonEqRandomValue(quart=True, tier=True, demi=True)[0]*(-1 if random.randint(1,100)%2==0 else 1)
        
        alphastr = latex(alpha).replace("frac","dfrac")
        a1str = latex(a1).replace("frac","dfrac")
        b1str = latex(b1).replace("frac","dfrac")
        a2str = latex(a2).replace("frac","dfrac")
        b2str = latex(b2).replace("frac","dfrac")

        x1str = latex(-b1/a1).replace("frac","dfrac")
        x2str = latex(-b2/a2).replace("frac","dfrac")
        signb1 = r"""""" if b1<0 else r"""+"""
        signb2 = r"""""" if b2<0 else r"""+"""
        item = item + r"""                    \multicolumn{1}{|c|}{$"""+alphastr+r"""\left("""+a1str+r"""x"""+signb1+b1str+r"""\right)\left("""+a2str+r"""x"""+signb2+b2str+r"""\right)$} &   &  \\ \hline
        """
        itemCorr = itemCorr+r"""                    \multicolumn{1}{|c|}{$"""+alphastr+r"""\left("""+a1str+r"""x"""+signb1+b1str+r"""\right)\left("""+a2str+r"""x"""+signb2+b2str+r"""\right)$} & \color{red}{$"""+x1str+r"""$}  &  \color{red}{$"""+x2str+r"""$} \\ \hline
        """
    exo=r"""\clearpage
    """+identification+r"""
    \renewcommand\arraystretch{3}
    \Question["""+str(2*n)+r"""] Pour chacun des produits suivants donnez les valeurs $x_1$ et $x_2$ qui annulent le produit (on donnera les valeurs sous forme exacte et simplifiée) :\\
        \begin{center}
            \begin{tabular}{C{3cm}|C{2cm}|C{2cm}|}
                \cline{2-3} & $x_1$ & $x_2$  \\ \hline
"""+item+r"""
            \end{tabular}
        \end{center}"""
    correction=r"""\clearpage
    """+identification+r"""
    \Question["""+str(2*n)+r"""] Pour chacun des produits suivants donnez les valeurs $x_1$ et $x_2$ qui annulent le produit (on donnera les valeurs sous forme exacte et simplifiée) :\\
        \begin{center}
            \begin{tabular}{C{3cm}|C{2cm}|C{2cm}|}
                \cline{2-3} & $x_1$ & $x_2$  \\ \hline
"""+itemCorr+r"""
            \end{tabular}
        \end{center}"""
    return(exo,correction)

def polyDegre2_DisN1(n:int=1, Niveau:int=2, id=False): 
    if id:
        identification = r"""polyDegre2_DisN1\\"""
    else:
        identification = r""""""
    # Niveau = 1 -> Discriminant avec des entiers
    # Niveau = 2 -> Discriminant avec des fractions
    x = Symbol('x')
    
    for i in range(n):
        # signe_a = (-1 if random.randint(1,100)%2==0 else 1)
        # signe_b = (-1 if random.randint(1,100)%2==0 else 1)
        # signe_c = (-1 if random.randint(1,100)%2==0 else 1)
        if Niveau==1:
            a = random.randint(1,5)*(-1 if random.randint(1,100)%2==0 else 1)
            b = random.randint(1,5)*(-1 if random.randint(1,100)%2==0 else 1)
            c = random.randint(1,5)*(-1 if random.randint(1,100)%2==0 else 1)
            pass
        if Niveau==2:
            a = nonEqRandomValue(quart=True, tier=False, demi=True)[0]*(-1 if random.randint(1,100)%2==0 else 1)
            b = nonEqRandomValue(quart=True, tier=False, demi=True)[0]*(-1 if random.randint(1,100)%2==0 else 1)
            c = nonEqRandomValue(quart=True, tier=False, demi=True)[0]*(-1 if random.randint(1,100)%2==0 else 1)

        delta = b**2-4*a*c
        # while delta!=0:
        #     a = nonEqRandomValue(quart=True, tier=False, demi=True)[0]*(-1 if random.randint(1,100)%2==0 else 1)
        #     b = nonEqRandomValue(quart=True, tier=False, demi=True)[0]*(-1 if random.randint(1,100)%2==0 else 1)
        #     c = nonEqRandomValue(quart=True, tier=False, demi=True)[0]*(-1 if random.randint(1,100)%2==0 else 1)
        #     delta = b**2-4*a*c
        str_expr = str(a)+"*x**2"+(("+"+str(b)) if b>0 else ("-"+str(b)))+"*x"+(("+"+str(c)) if c>0 else ("-"+str(c)))
        expr = sympify(str_expr)
        solutions = real_roots(str_expr, x)
        answer = r"""
        Le polynôme est de la forme $"""+latex(expr).replace("frac","dfrac")+r"""$ avec $a="""+latex(a).replace("frac","dfrac")+r"""$, $b="""+latex(b).replace("frac","dfrac")+r"""$ et $c="""+latex(c).replace("frac","dfrac")+r"""$.\\
                        On calcul le discriminant $\Delta$:
                        \begin{equation*}
                            \begin{array}{l@{}>{\displaystyle}l}
                            \Delta	&{}= b^2-4ac \\
                                    &{}= \left("""+latex(b).replace("frac","dfrac")+r"""\right)^2-4\times\left("""+latex(a).replace("frac","dfrac")+r"""\right)\times\left("""+latex(c).replace("frac","dfrac")+r"""\right)\\
                                    &{}= """+latex(b**2-4*a*c).replace("frac","dfrac")+r"""
                            \end{array}
                        \end{equation*}"""
        if delta<0:
            answer = answer + r"""
						On a donc $\Delta<0$ donc l'équation $"""+latex(expr).replace("frac","dfrac")+r"""=0$ n'a pas de solution dans $\mathbb{R}$."""
            pass
        if delta==0:
            x0 = -b/(2*a)
            answer = answer + r"""
                        On a donc $\Delta=0$ donc l'équation $"""+latex(expr).replace("frac","dfrac")+r"""=0$ admet 1 solution :
                        \begin{equation*}
                            \begin{array}{l@{}>{\displaystyle}l}
                                x_0 &= \dfrac{-b}{2a}\\
                                x_0 &= \dfrac{-\left("""+latex(b).replace("frac","dfrac")+r"""\right)}{2\times """+latex(a).replace("frac","dfrac")+r"""}\\
                                x_0 &= """+latex(x0).replace("frac","dfrac")+r"""
                            \end{array}
                        \end{equation*}
                        L'équation $"""+latex(expr).replace("frac","dfrac")+r"""=0$ admet donc $x_0 = """+latex(x0).replace("frac","dfrac")+r"""$ comme solutions."""
            pass
        if delta>0:
            x1 = (-b-sqrt(delta))/(2*a)
            x2 = (-b+sqrt(delta))/(2*a)
            answer = answer + r"""
                        On a donc $\Delta>0$ donc l'équation $"""+latex(expr).replace("frac","dfrac")+r"""=0$ admet 2 solutions :
                        \begin{equation*}
                        \begin{split}
                            x_1 &= \dfrac{-b-\sqrt{\Delta}}{2a}\\
                            x_1 &= \dfrac{-\left("""+latex(b).replace("frac","dfrac")+r"""\right)-\sqrt{"""+latex(delta).replace("frac","dfrac")+r"""}}{2\times """+latex(a).replace("frac","dfrac")+r"""}\\
                            x_1 &= """+latex(x1).replace("frac","dfrac")+r"""
                        \end{split}
                            \quad\quad et \quad\quad
                        \begin{split}
                            x_2 &= \dfrac{-b+\sqrt{\Delta}}{2a}\\
                            x_2 &= \dfrac{-\left("""+latex(b).replace("frac","dfrac")+r"""\right)+\sqrt{"""+latex(delta).replace("frac","dfrac")+r"""}}{2\times """+latex(a).replace("frac","dfrac")+r"""}\\
                            x_2 &= """+latex(x2).replace("frac","dfrac")+r"""
                        \end{split}
                        \end{equation*}
                        L'équation $"""+latex(expr).replace("frac","dfrac")+r"""=0$ admet donc $x_1 = """+latex(x1).replace("frac","dfrac")+r"""$ et $x_2 = """+latex(x2).replace("frac","dfrac")+r"""$ comme solutions."""
            pass
    exo = r"""
    \clearpage
    """+identification+r"""
    \renewcommand\arraystretch{1}
            \Question[20] Résoudre l'équation suivante dans $\mathbb{R}$ par la méthode du discriminant :
                \begin{enumerate}
                    \item $"""+latex(expr).replace("frac","dfrac")+r"""=0$
                        \fillwithlines{180mm}
                \end{enumerate}"""
    corr = r"""
    \clearpage
    """+identification+r"""
    \renewcommand\arraystretch{1}
            \Question[20] Résoudre les équations suivantes dans $\mathbb{R}$ par la méthode du discriminant :
                \begin{enumerate}
                    \item $"""+latex(expr).replace("frac","dfrac")+r"""=0$\\
                        """+answer+r"""
                \end{enumerate}"""
    return(exo,corr)

def exoDerivation(genCode="9999999999", id=False):
    if id :
        identification = r"""exoDerivation\\"""
    else:
        identification = r""""""
    pts=0
    # On définie les trois points A(xa,ya), B(xb,yb) et C(xc,yc) par lesquels la parabole doit passé
    xa, xb, xc = symbols('xa xb xc')
    ya, yb, yc = symbols('ya yb yc')
    xa = 2+np.random.randint(1,2)*3
    ya = 0.0
    xc = 6+np.random.randint(1,3)*2+1
    yc = 0.0
    xb = (xa+xc)/2.0
    yb = -4.0
    x, a, b, c = symbols('x a b c')
    # On résoud le système d'équations :
    # f(xa)=ya
    # f(xb)=yb
    # f(xc)=yc
    # pour trouver a, b et c de f(x)=ax^2+bx+c

    equations = [
        Eq( xa**2*a+xa*b+c ,  ya ),
        Eq( xb**2*a+xb*b+c ,  yb ),
        Eq( xc**2*a+xc*b+c ,  yc )
    ]

    solution = solve(equations, rational=True)
    a = solution[a]
    b = solution[b]
    c = solution[c]
    a_string = latex(a).replace("\\frac","\dfrac")
    b_string = latex(b).replace("\\frac","\dfrac")
    c_string = latex(c).replace("\\frac","\dfrac")

    Cprim = a*x**2+b*x+c
    delta = b**2-4*a*c
    x1 = (-b-sqrt(delta))/(2*a)
    x1_string = latex(x1).replace("\\frac","\dfrac")
    x2 = (-b+sqrt(delta))/(2*a)
    x2_string = latex(x2).replace("\\frac","\dfrac")
    dd = np.random.randint(10,15)
    C = integrate(Cprim) + dd

    C_coeff = C.as_coefficients_dict()
    u = C_coeff[x**3]*x**3
    v = C_coeff[x**2]*x**2
    w = C_coeff[x]*x
    z = C_coeff[1]
    C_string = latex(C).replace("\\frac","\dfrac")
    coeff_u_string = latex(C_coeff[x**3]).replace("\\frac","\dfrac")
    coeff_v_string = latex(C_coeff[x**2]).replace("\\frac","\dfrac")
    coeff_w_string = latex(C_coeff[x]).replace("\\frac","\dfrac")
    coeff_z_string = latex(C_coeff[1]).replace("\\frac","\dfrac")

    wprim_string = latex(c).replace("\\frac","\dfrac")
    coeff_uprim_string = latex(a).replace("\\frac","\dfrac")
    coeff_vprim_string = latex(b).replace("\\frac","\dfrac")
    coeff_wprim_string = latex(c).replace("\\frac","\dfrac")
    delta = b**2-4*a*c
    rdelta = sqrt(delta)
    rdelta_string = latex(rdelta).replace("\\frac","\dfrac")
    delta_string = latex(delta).replace("\\frac","\dfrac")
    result = C_coeff[x**3]*x2**3+C_coeff[x**2]*x2**2+C_coeff[x]*x2+dd
    result_string = latex(result).replace("\\frac","\dfrac")
    if result.denominator==1:
        result_string = result_string
    else:
        result_string = result_string+r"""\approx """+str(round(result.n(),2))
    exo=r"""
    \clearpage
    """+identification+r"""
    \Question
        Une usine produit des bonbons. Le responsable "production" a modélisé le cout de production de chacune des machines en fonction du poids de bonbons produit pour une machine. Si $x$ est le poids de bonbons produit alors $C(x)$ donne le coût de production au kilogramme en fonction de $x$ avec :
        \begin{center}
            $C(x)="""+C_string+r"""$\\
        \end{center}
        \begin{parts}
            \Part[3] Déterminer $C'(x)$, la fonction dérivée de $C(x)$\\
                \fillwithlines{50mm}
            \Part[3] Résoudre $C'(x)=0$\\
                \fillwithlines{70mm}
            \Part[3] En déduire le signe de $C'$ et les variations de $C$\\
                \fillwithlines{70mm}
            \Part[3] Conclure sur la quantité optimale de production et en donner donc le coût minimal au kilogramme\\
                \fillwithlines{20mm}
        \end{parts}
    """
    correction=r"""
    \clearpage
    """+identification+r"""
    \Question
        Une usine produit des bonbons. Le responsable "production" a modélisé le cout de production de chacune des machines en fonction du poids de bonbons produit pour une machine. Si $x$ est le poids de bonbons produit alors $C(x)$ donne le coût de production au kilogramme en fonction de $x$ avec :
        \begin{center}
            $C(x)="""+C_string+r"""$\\
        \end{center}
        \begin{parts}
            \Part[3] Déterminer $C'(x)$, la fonction dérivée de $C(x)$\\
            \begin{solution}
                La fonction $C(x)$ est de la forme $u+v$ on a donc :
                \begin{center}
                    $C(x)=u+v+w+z$\\
                    avec $u="""+coeff_u_string+r"""x^3$, $v="""+coeff_v_string+r"""x^2$, $w="""+coeff_w_string+r"""x$ et $z="""+str(dd)+r"""$
                \end{center}
                $u$, $v$, $w$ et $z$ sont de la forme $kx^n$ or $(kx^n)'=knx^{n-1}$ on a donc :
                \begin{center}
                    $C'(x)=u'+v'+w'+z'$\\
                    avec $u'="""+coeff_uprim_string+r"""x^2$, $v'="""+coeff_vprim_string+r"""x$, $w'="""+wprim_string+r"""$ et $z'=0$
                \end{center}
                d'où :
                \begin{center}
                    $C'(x)="""+coeff_uprim_string+r"""x^2+"""+coeff_vprim_string+r"""x+"""+coeff_wprim_string+r""" +0$\\
                \end{center}
                et donc :
                \begin{center}
                    $C'(x)="""+coeff_uprim_string+r"""x^2+"""+coeff_vprim_string+r"""x+"""+coeff_wprim_string+r"""$\\
                \end{center}
            \end{solution}
            \Part[3] Résoudre $C'(x)=0$\\
            \begin{solution}
                $C'(x)$ est un polynôme du second degré, on utilise donc la méthode du discriminant.\\
                On écrit donc $C'(x)$ avec :
                \begin{center}
                    $C'(x)=ax^2+bx+c$\\
                    $a="""+latex(a).replace("\\frac","\\dfrac")+r"""$, $b="""+latex(b).replace("\\frac","\\dfrac")+r"""$ et $c="""+latex(c).replace("\\frac","\\dfrac")+r"""$
                \end{center}
                On calcul $\Delta=b^2-4ac$ d'où :
                \begin{align*}
                    \Delta	&=b^2-4ac\\
                            &="""+b_string+r"""^2-4"""+a_string+r""""""+c_string+r"""\\
                            &="""+delta_string+r"""=\left("""+rdelta_string+r"""\right)^2
                \end{align*}

                Donc $\Delta>0$, il y a donc 2 solutions à l'équation $C'(x)=0$
                \begin{multicols}{2}
                \begin{align*}
                    x_1&=\dfrac{-b-\sqrt{\Delta}}{2a}\\
                    x_1&=\dfrac{-\left("""+b_string+r"""\right)-\sqrt{"""+delta_string+r"""}}{2\times+"""+a_string+r"""}\\
                    x_1&=\dfrac{-\left("""+b_string+r"""\right)-"""+rdelta_string+r"""}{2\times+"""+a_string+r"""}\\
                    x_1&="""+x1_string+r"""
                \end{align*}
                
                \begin{align*}
                    x_2&=\dfrac{-b+\sqrt{\Delta}}{2a}\\
                    x_1&=\dfrac{-\left("""+b_string+r"""\right)+\sqrt{"""+delta_string+r"""}}{2\times+"""+a_string+r"""}\\
                    x_1&=\dfrac{-\left("""+b_string+r"""\right)+"""+rdelta_string+r"""}{2\times+"""+a_string+r"""}\\
                    x_2&="""+x2_string+r"""
                \end{align*}
                \end{multicols}
                Les 2 solutions sont donc $x_1="""+x1_string+r"""$ et $x_2="""+x2_string+r"""$
            \end{solution}
            \Part[3] En déduire le signe de $C'$ et les variations de $C$\\
            \begin{solution}
                Le polynôme est du signe de $-a$ entre ses racines d'où le tableau de signe et de variation suivant :
                \begin{center}
                    \begin{tikzpicture}
                        \tkzTabInit{$x$/1,$C'(x)$/1,$C$/3}{$-\infty$,$"""+x1_string+r"""$,$"""+x2_string+r"""$,$\infty$}
                        \tkzTabLine{,+,z,-,z,+}
                        \tkzTabVar{-/$-\infty$,+/$C\left("""+x1_string+r"""\right)$,-/$C\left("""+x2_string+r"""\right)$,+/$+\infty$}
                    \end{tikzpicture}
                \end{center}
            \end{solution}
            \Part[3] Conclure sur la quantité optimale de production et en donner donc le coût minimal au kilogramme\\
            \begin{solution}
                La quantité optimale à produire est $"""+x2_string+r"""$ kilogrammes pour :
                \begin{align*}
                    C("""+x2_string+r""")&="""+coeff_u_string+r"""\times \left("""+x2_string+r"""\right)^3+"""+coeff_v_string+r"""\times \left("""+x2_string+r"""\right)^2+"""+coeff_w_string+r"""\times """+x2_string+r"""+"""+coeff_z_string+r"""\\
                        &="""+result_string+r"""
                \end{align*}
            \end{solution}
        \end{parts}
    """

    return(exo,correction)

def SigneProdQuotient(n:int=1, id=False):
    if id:
        identification = r"""SigneProdQuotient"""
    else:
        identification = r""""""
    # Signe du produit ou du quotient de deux fonctions
    x = Symbol('x')
    a = nonEqRandomValue(debut=2, fin=6, quart=False, tier=False, demi=False)[0]
    a = a*a
    b = nonEqRandomValue(debut=2, fin=6, quart=False, tier=False, demi=False)[0]
    b = b*b
    c = nonEqRandomValue(quart=False, tier=False, demi=False)[0]*(-1 if random.randint(1,100)%2==0 else 1)
    d = nonEqRandomValue(quart=False, tier=False, demi=False)[0]*(-1 if random.randint(1,100)%2==0 else 1)
    e = nonEqRandomValue(quart=False, tier=False, demi=False)[0]*(-1 if random.randint(1,100)%2==0 else 1)
    f = nonEqRandomValue(quart=False, tier=False, demi=False)[0]*(-1 if random.randint(1,100)%2==0 else 1)

    expr = (a*x**2-b)*(c*x+d)/(e*x+f)
    expr_string = latex(expr).replace("frac","dfrac")
    expr2 = (a*x**2-b)*(c*x+d)*(e*x+f)
    expr2_string = latex(expr2).replace("frac","dfrac")
    exo=r"""
    \clearpage
    """+identification+r"""
        \Question Soit la fonction $f$ définie par $\displaystyle f:x \longmapsto """+expr_string+r"""$, 
			\begin{parts}
				\Part[5] Dressez le tableau de signe de la fonction
				\fillwithlines{50mm}
				\Part[3] en déduire la solution de l'inéquation $f(x)\geqslant 0$
				\fillwithlines{10mm}
			\end{parts}
		\Question Soit la fonction $g$ définie par $\displaystyle g:x \longmapsto """+expr2_string+r"""$, 
			\begin{parts}
				\Part[5] Dressez le tableau de signe de la fonction
				\fillwithlines{50mm}
				\Part[3] en déduire la solution de l'inéquation $g(x)\leqslant 0$
				\fillwithlines{10mm}
			\end{parts}"""
    
    correction=r"""
    \clearpage  
    """+identification
    return(exo,correction)

def main():
    exo,corr=exoP1Type2()
    print(exo)
    print(corr)
    pass

if __name__=="__main__":
    main()
    pass