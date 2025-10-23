import os,sys
import random
import unicodedata
import numpy as np
from sympy import *
from scipy.stats import binom
from scipy.stats import norm
import matplotlib.pyplot as plt
from fractions import Fraction

from baseMaths import *


def binomial_distribution(n, p):
    """Affiche les probabilités de la loi binomiale B(n, p)"""
    # Valeurs possibles de X
    x_values = list(range(n + 1))
    # Probabilités P(X = k)
    probabilities = [binom.pmf(k, n, p) for k in x_values]
    return x_values, probabilities

def binomial_results(n, p):
    """Retourne les probabilités binomiales sous forme d'une chaîne formatée."""
    x_values = range(n + 1)
    probabilities = [binom.pmf(k, n, p) for k in x_values]
    return " ".join(f"({x},{prob:.4f})" for x, prob in zip(x_values, probabilities))

def suiteAnalyseComp(id=False):
    if id:
        identification = r"""suiteAnalyseComp\\"""
    else:
        identification = r""""""
    C0 = random.randint(20,25)*10000
    tx = random.randint(2,6)
    txEvol = 100+tx
    anDeb = random.randint(2023,2025)
    nMax = random.randint(3,5)
    exo=r"""
    """+identification
    correction=r"""
    """+identification+r"""
            \Question Une entreprise a commencé son activité en """+str(anDeb)+r""" avec un chiffre d'affaires de """+str(C0)+r""" euros. Chaque année, son chiffre d'affaires augmente de """+str(tx)+r"""%.
            \begin{parts}
                \Part Exprimez le chiffre d'affaires de l'entreprise en fonction de l'année n à l'aide d'une suite. L'année """+str(anDeb)+r""" correspond à n=0.\\
                    \color{red}{Le chiffre d'affaires peut être modélisé par une suite géométrique où chaque terme est égal à """+str(txEvol)+r"""\% du précédent. La formule générale de cette suite est 
                    \begin{center}
                        $C_n="""+str(C0)+r""" \times """+f"{txEvol/100:.2f}"+r"""^n$\\
                        avec n le nombre d'années après 2020.
                    \end{center}
                    }\color{black}
                
                \Part Calculez le chiffre d'affaires de l'entreprise pour les années 2021, 2022 et 2023.
                    \color{red}{
                    \begin{itemize}
                    \item Pour 2021 $(n=1)$ , $C_1="""+str(C0)+r"""\times """+f"{txEvol/100:.2f}"+r"""^1 = 210000$
                    \item Pour 2022 $(n=2)$ , $C_2="""+str(C0)+r"""\times """+f"{txEvol/100:.2f}"+r"""^2 \approx 220500$
                    \item Pour 2023 $(n=3)$ , $C_3="""+str(C0)+r"""\times """+f"{txEvol/100:.2f}"+r"""^3 \approx 231525$
                    \end{itemize}
                    }\color{black}
                \Part Calculez le taux d'évolution global du chiffre d'affaires entre 2020 et 2023.\\
                    \color{red}{
                    Le taux d'évolution global de """+str(anDeb)+r""" à 2023 est donné par $\dfrac{C_3-C_0}{C_0}$. Donc : 
                    \begin{center}
                        $\dfrac{231525-"""+str(C0)+r"""}{"""+str(C0)+r"""}\approx 0.1576$ ou $15,76\%$
                    \end{center}
                    }\color{black}
                \Part Comparez ce taux d'évolution avec la somme des taux d'évolution annuels. Expliquez pourquoi ces deux taux sont différents.\\
                \color{red}{
                La somme des taux annuels est simplement $3 \times """+str(nMax)+r"""\%=15\%$. Cette valeur est différente du taux global car le taux d'évolution global considère l'effet cumulatif des augmentations annuelles (c'est le principe des intérêts composés).
                }\color{black}
                \Part Supposons maintenant que l'augmentation annuelle du chiffre d'affaires devient linéaire, avec une augmentation de 10 000 euros chaque année à partir de 2024. Modélisez cette situation à l'aide d'une fonction affine.\\
                \color{red}{
                La nouvelle situation peut être modélisée par une fonction affine :\\
                \begin{center}
                    $C(n)=C_3+10000\times (n-3)$, où n est le nombre d'années après """+str(anDeb)+r""".
                \end{center}
                }\color{black}
                \Part Calculez le chiffre d'affaires prévu pour l'année """+str(anDeb+nMax)+r""" avec cette nouvelle modèle.
                \color{red}{
                \begin{itemize}
                    \item Pour 2025 $(n=5)$: $C(5)=231525+10000\times (5-3)=251525$ euros.
                \end{itemize}
                }\color{black}
                \Part Comparez les chiffres d'affaires prévus pour """+str(anDeb+nMax)+r""" en utilisant les deux modèles (suite géométrique et fonction affine). Lequel est plus avantageux pour l'entreprise ?\\
                \color{red}{
                Avec le modèle géométrique, le chiffre d'affaires en 2025 serait :
                \begin{center}
                    $C_5="""+str(C0)+r"""\times """+f"{txEvol/100:.2f}"+r"""^5\approx 255526$ euros.
                \end{center}
                Avec la fonction affine, le chiffre d'affaires en 2025 est de 251525 euros.\\
                }\color{black}
                \Part Discutez de la pertinence de chaque modèle dans le contexte d'une prévision à long terme.\\
                \color{red}{
                Le modèle géométrique prévoit un chiffre d'affaires légèrement plus élevé en 2025. Cependant, le modèle linéaire pourrait être plus réaliste sur le long terme, car une croissance exponentielle indéfinie est souvent peu probable dans un contexte d'affaires réel.
                }\color{black}
            \end{parts}	
    """
    return(exo,correction)

def loiBinomiale(id=False):
    if id:
        identification = r"""loiBinomiale\\"""
    else:
        identification = r""""""
    n = random.randint(20,40)
    p = random.randint(10,40)/100
    k = random.randint(1,int(n*p))
    leq = k+1
    pXk = binom.pmf(k, n, p)
    pXinfK = binom.cdf(leq, n, p)
    exo=r"""
    """+identification+r"""
            \Question Une entreprise fabrique des composants électroniques. On sait que la probabilité qu'un composant soit défectueux est de $p="""+str(p)+r"""$. L'entreprise prélève un échantillon aléatoire de $n="""+str(n)+r"""$ composants.
        \begin{center}
            \begin{tikzpicture}
                \begin{axis}[
                    ybar,
                    symbolic x coords={"""+",".join(map(str, range(n + 1)))+r"""},
                    xtick=data,
                    ymin=0,
                    ymax=0.4,
                    ylabel={Probabilité},
                    xlabel={Nombre de composants défectueux}
                ]
                \addplot coordinates {"""+binomial_results(n, p)+r"""};
                \end{axis}
            \end{tikzpicture}
        \end{center}
        \begin{enumerate}
            \item Modéliser la variable aléatoire $X$ représentant le nombre de composants défectueux dans l'échantillon.\\
            \fillwithlines{20mm}
            \item Déterminer l'espérance et l'écart-type de $X$.\\
            \fillwithlines{30mm}
            \item Calculer la probabilité qu'il y ait exactement """+str(k)+r""" composants défectueux.\\
            \fillwithlines{30mm}
            \item Calculer la probabilité qu'il y ait au plus """+str(leq)+r""" composants défectueux.\\
            \fillwithlines{30mm}
        \end{enumerate}"""
    correction=r"""
    """+identification+r"""
            \Question Une entreprise fabrique des composants électroniques. On sait que la probabilité qu'un composant soit défectueux est de $p="""+str(p)+r"""$. L'entreprise prélève un échantillon aléatoire de $n="""+str(n)+r"""$ composants.
        \begin{center}
            \begin{tikzpicture}
                \begin{axis}[
                    ybar,
                    symbolic x coords={"""+",".join(map(str, range(n + 1)))+r"""},
                    xtick=data,
                    ymin=0,
                    ymax=0.4,
                    ylabel={Probabilité},
                    xlabel={Nombre de composants défectueux}
                ]
                \addplot coordinates {"""+binomial_results(n, p)+r"""};
                \end{axis}
            \end{tikzpicture}
        \end{center}
        \begin{enumerate}
            \item Modéliser la variable aléatoire $X$ représentant le nombre de composants défectueux dans l'échantillon.\\
            \color{red}
            La variable aléatoire $X$ suit une loi binomiale de paramètres $n="""+str(n)+r"""$ et $p="""+str(p)+r"""$, soit $X \sim \mathcal{B}("""+str(n)+r""","""+str(p)+r""")$.
            \color{black}
            \item Déterminer l'espérance et l'écart-type de $X$.\\
            \color{red}
            L'espérance est donnée par $E(X) = n \times p = """+str(n)+r""" \times """+str(p)+r""" = """+str(round(n*p,3))+r"""$. \\
            L'écart-type est $\sigma_X = \sqrt{np(1-p)} = \sqrt{"""+str(n)+r""" \times """+str(p)+r""" \times """+str(round(1-p,2))+r"""} \approx 0.9747$.
            \color{black}
            \item Calculer la probabilité qu'il y ait exactement """+str(k)+r""" composants défectueux.\\
            \color{red}
            La probabilité que $X="""+str(k)+r"""$ est :
                  \[
                  P(X="""+str(k)+r""") = \binom{"""+str(n)+r"""}{"""+str(k)+r"""} (0.05)^"""+str(k)+r""" ("""+str(round(1-p,2))+r""")^{"""+str(n-k)+r"""} \approx """+str(round(pXk,4))+r""".
                  \]
            \color{black}
            \item Calculer la probabilité qu'il y ait au plus """+str(leq)+r""" composants défectueux.\\
            \color{red}
            La probabilité que $X \leq """+str(leq)+r"""$ est :
                  \[
                  P(X\leq """+str(leq)+r""") = P(X=0) + ... + P(X="""+str(leq)+r""")
                  \]
                  
                  \[
                  P(X\leq """+str(leq)+r""") \approx """+str(round(pXinfK,4))+r""".
                  \]
            \color{black}
        \end{enumerate}"""
    return(exo,correction)

def proba_Bacterie(id=False):
    if id:
        identification = r"""proba_Bacterie\\"""
    else:
        identification = r""""""
        
    # Paramètres de la question
    tauxContamination = random.randint(5,30)/100 #0.15
    tauxTestPositifContamine = 1-random.randint(1,15)/100 #0.996
    tauxTestNegatifNonContamine = 1-random.randint(1,15)/100 #0.976
    tauxTestPositifNonContamine = 1 - tauxTestNegatifNonContamine
    
    pB = tauxContamination
    pBbar = 1 - tauxContamination
    pBT = tauxTestPositifContamine
    pBbarT = tauxTestPositifNonContamine
    pBTbar = 1 - tauxTestPositifContamine
    pBbarTbar = tauxTestNegatifNonContamine
    
    
    exo=r"""
    """+identification+r"""
        \Question Une épidémie due à une bactérie s'est développée dans une grande ville. Afin de lutter contre cette épidémie en distribuant de façon raisonnée un antibiotique adapté, un organisme de santé a mis au point un test de dépistage. \\
        On admet que :
        \begin{itemize}[label=\textbullet]
            \item """+str(tauxContamination*100)+r"""\% de la population est contaminée par cette bactérie
            \item Le test est positif dans """+str(tauxTestPositifContamine*100)+r"""\% des cas pour une personne contaminée par cette bactérie.
            \item Le test est négatif dans """+str(tauxTestNegatifNonContamine*100)+r"""\% des cas pour une personne non contaminée par cette bactérie.
        \end{itemize}
        Une personne est choisie au hasard dans cette ville. On admet que chaque personne a la même probabilité d'être choisie. On considère les événements suivants :
        \begin{itemize}[label=\textbullet]
            \item B : « La personne choisie est contaminée par la bactérie »
            \item T : « Pour la personne choisie, le test est positif »
        \end{itemize}
        Dans chaque question, les résultats numériques seront donnés sous forme décimale exacte.
        \begin{enumerate}
            \item Compléter l'arbre de probabilité ci-dessous :
                \begin{center}
                    \begin{tikzpicture}[
                      grow=right, 
                      %sloped,
                      scale=0.8,
                      level distance=4cm,
                      level 1/.style={sibling distance=3.5cm},
                      level 2/.style={sibling distance=2.5cm},
                      every node/.style = {font=\footnotesize},
                      edge from parent/.style = {draw, -latex}
                      ]
                    
                      \node{$\Omega$}
                        child {
                          node {$\overline{B}$}
                          child {
                            node {$\overline{T}$}
                            edge from parent
                            node[above] {\makebox[1cm]{\dotfill}}
                          }
                          child {
                            node {$T$}
                            edge from parent
                            node[above] {\makebox[1cm]{\dotfill}}
                          }
                          edge from parent
                          node[above] {\makebox[1cm]{\dotfill}}
                        }
                        child {
                          node {$B$}
                          child {
                            node {$\overline{T}$}
                            edge from parent
                            node[above] {\makebox[1cm]{\dotfill}}
                          }
                          child {
                            node {$T$}
                            edge from parent
                            node[above] {\makebox[1cm]{\dotfill}}
                          }
                          edge from parent
                          node[above] {\makebox[1cm]{\dotfill}}
                        };
                    \end{tikzpicture}
                \end{center}
            \item Quelle est la probabilité que le test soit négatif sachant que la personne choisie est contaminée par la bactérie ?
            \fillwithlines{20mm}
            \item Calculer la probabilité que la personne choisie soit contaminée par la bactérie, et que pour elle le test soit positif.
            \fillwithlines{20mm}
            \item Quelle est la probabilité que, pour la personne choisie, le test soit positif ?
            \fillwithlines{20mm}
            \item Calculer la probabilité que le test donne un résultat faux.
            \fillwithlines{20mm}
                        
        \end{enumerate}
"""
    correction=r"""
    """+identification+r"""
        \Question Une épidémie due à une bactérie s'est développée dans une grande ville. Afin de lutter contre cette épidémie en distribuant de façon raisonnée un antibiotique adapté, un organisme de santé a mis au point un test de dépistage. \\
        On admet que :
        \begin{itemize}[label=\textbullet]
            \item """+str(tauxContamination*100)+r"""\% de la population est contaminée par cette bactérie
            \item Le test est positif dans """+str(tauxTestPositifContamine*100)+r"""\% des cas pour une personne contaminée par cette bactérie.
            \item Le test est négatif dans """+str(tauxTestNegatifNonContamine*100)+r"""\% des cas pour une personne non contaminée par cette bactérie.
        \end{itemize}
        Une personne est choisie au hasard dans cette ville. On admet que chaque personne a la même probabilité d'être choisie. On considère les événements suivants :
        \begin{itemize}[label=\textbullet]
            \item B : « La personne choisie est contaminée par la bactérie »
            \item T : « Pour la personne choisie, le test est positif »
        \end{itemize}
        Dans chaque question, les résultats numériques seront donnés sous forme décimale exacte.
        \begin{enumerate}
            \item Compléter l'arbre de probabilité ci-dessous :
                \begin{center}
                    \begin{tikzpicture}[
                      grow=right, 
                      %sloped,
                      scale=0.8,
                      level distance=4cm,
                      level 1/.style={sibling distance=3.5cm},
                      level 2/.style={sibling distance=2.5cm},
                      every node/.style = {font=\footnotesize},
                      edge from parent/.style = {draw, -latex}
                      ]
                    
                      \node{$\Omega$}
                        child {
                          node {$\overline{B}$}
                          child {
                            node {$\overline{T}$}
                            edge from parent
                            node[above] {\makebox[1cm]{\color{red}"""+str(round(pBbarTbar*100,2))+r"""\%\color{black}}}
                          }
                          child {
                            node {$T$}
                            edge from parent
                            node[above] {\makebox[1cm]{\color{red}"""+str(round(pBbarT*100,2))+r"""\%\color{black}}}
                          }
                          edge from parent
                          node[above] {\makebox[1cm]{\color{red}"""+str(round(pBbar*100,2))+r"""\%\color{black}\dotfill}}
                        }
                        child {
                          node {$B$}                 
                          child {
                            node {$\overline{T}$}
                            edge from parent
                            node[above] {\makebox[1cm]{\color{red}"""+str(round(pBTbar*100,2))+r"""\%\color{black}}}
                          }
                          child {
                            node {$T$}
                            edge from parent
                            node[above] {\makebox[1cm]{\color{red}"""+str(round(pBT*100,2))+r"""\%\color{black}}}
                          }
                          edge from parent
                          node[above] {\makebox[1cm]{\color{red}"""+str(round(pB*100,2))+r"""\%\color{black}}}
                        };
                    \end{tikzpicture}
                \end{center}
            \item Quelle est la probabilité que le test soit négatif sachant que la personne choisie est contaminée par la bactérie ?\\
                \color{red}
                En lisant l'arbre pondéré de probabilité, on obtient :
                \begin{align*}
                    p_B(T)   &= """+str(round(pBT,2))+r"""\%
                \end{align*}
                \color{black}
            \item Calculer la probabilité que la personne choisie soit contaminée par la bactérie, et que pour elle le test soit positif.\\
                \color{red}
                Cette probabilité correspond au chemin B puis T de l'arbre de probabilité. Or le probabilité qu'un chemin se réalise est le produit des branches qui composent le chemin. On a donc :
                \begin{align*}
                    p(B\cap T)	&= p(B) \times p_B(T)\\
                                &= """+str(round(pB,2))+r""" \times """+str(round(pBT,2))+r"""\\
                                &= """+str(round(pB*pBT,2))+r"""\%
                \end{align*}
                \color{black}
            \item Quelle est la probabilité que, pour la personne choisie, le test soit positif ?\\
                \color{red}
                    Cette probabilité correspond à la somme des probabilité des chemins qui mènent à un test positif. On donc :\\
                        \begin{align*}
                            p(T)	&= p(B\cap T) + p(\overline{B}\cap T)\\
                                    &= p(B) \times p_B(T) + p(\overline{B}) \times p_{\overline{B}}(T)\\
                                    &= """+str(round(pB,2))+r""" \times """+str(round(pBT,2))+r""" + """+str(round(pBbar,2))+r""" \times """+str(round(pBbarT,2))+r"""\\
                                    &= """+str(round(pB*pBT + pBbar*pBbarT,2))+r"""\%
                        \end{align*}
                \color{black}
            \item Calculer la probabilité que le test donne un résultat faux.\\
                \color{red}
                        Dans le même esprit que la question précédante, cette probabilité correspond à la somme des probabilité des chemins qui mènent à un test négatif. On donc :\\
                        \begin{align*}
                                p(\overline{T})	&= p(B\cap \overline{T}) + p(\overline{B}\cap \overline{T})\\
                                                &= p(B) \times p_B(\overline{T}) + p(\overline{B}) \times p_{\overline{B}}(\overline{T})\\
                                                &= """+str(round(pB,2))+r""" \times """+str(round(pBTbar,2))+r""" + """+str(round(pBbar,2))+r""" \times """+str(round(pBbarTbar,2))+r"""\\
                                                &= """+str(round(pB*pBTbar + pBbar*pBbarTbar,2))+r"""\%
                        \end{align*}
                \color{black}
                        
        \end{enumerate}
  """
    
    return(exo,correction)

def etudePolynome(id=False):
    if id:
        identification = r"""etudePolynome\\"""
    else:
        identification = r""""""
    a = nonEqRandomValue(n=1, debut=1, fin=3, demi=True, quart=True, tier=False)[0]
    x = symbols('x')
    f = x*(x-a**2)*(x+a**2)
    f_expand = expand(f)
    f_prime = (x*sqrt(3)-a)*(x*sqrt(3)+a)
    f_prime_expand = expand(f_prime)
   
    # print(f"f(x)={Latex(f)}")
    # print(f"f(x)={Latex(f_expand)}")
    # print(f"f'(x)={Latex(f_prime)}")
    # print(f"f'(x)={Latex(f_prime_expand)}")
    exo=r"""
    """+identification+r"""
    \Question Soit la fonction $f$ définie par $"""+Latex(f_expand)+r"""$ sur $\mathbb{R}$\\
        \begin{parts}
            \Part[2] Montrez que $f(x)="""+Latex(f)+r"""$
                \fillwithlines{35mm}
            \Part[2] En déduire les solutions de l'équation $f(x)=0$
                \fillwithlines{35mm}
            \Part[9] Complétez le tableau de signe de f(x)
                \begin{center}
                    \begin{tikzpicture}
                        \tkzTabInit[lgt=4,espcl=2]
                        {$x$ /1,
                        Signe de $x$ /1,
                        Signe de $\left("""+Latex((x-a**2))+r"""\right)$ /1,
                        Signe de $\left("""+Latex((x+a**2))+r"""\right)$ /1,
                        Signe de $f(x)$ /1}
                        {$-\infty$,$?$,$0$,$?$,$+\infty$}
                        \tkzTabLine{   ,   , t ,   , z ,   , t ,   ,  } % Signe de x
                        \tkzTabLine{   ,   , t ,   , t ,   , z ,   ,  } % Signe 1
                        \tkzTabLine{   ,   , z ,   , t ,   , t ,   ,  } % Signe 2
                        \tkzTabLine{   ,   , z ,   , z ,   , z ,   ,  } % Signe de f
                    \end{tikzpicture}
                \end{center}
            \Part[4] A partir de la forme développée de $f$, déterminez $f'(x)$ la fonction dérivée de $f(x)$
                \fillwithlines{30mm}
            \Part[2] Montrez que $f'(x)="""+Latex(f_prime)+r"""$
                \fillwithlines{30mm}
            \Part[4] Résoudre $f'(x)=0$
                \fillwithlines{30mm}
            \Part[6] Complétez le tableau de signe de $f'(x)$
                \begin{center}
                \begin{tikzpicture}
                \tkzTabInit[lgt=4,espcl=2]
                {$x$ /1,
                 /2,
                 /2,
                Signe de $f'(x)$ /1}
                {$-\infty$,$?$,$?$,$+\infty$}
                \tkzTabLine{   ,   , z ,   , t ,   ,  } % Signe 1
                \tkzTabLine{   ,   , t ,   , z ,   ,  } % Signe 2
                \tkzTabLine{   ,   , z ,   , z ,   ,  } % Signe de f'
                \end{tikzpicture}
                \end{center}
            \Part[6] En déduire le tableau de variation de $f(x)$
                    \begin{center}
                    \begin{tikzpicture}
                \tkzTabInit[lgt=3,espcl=3]%
                    {$x$ /1, Variations de $f$ /3}%
                    {$-\infty$, $?$, $?$, $+\infty$}
                %\tkzTabVar{-/ $-\infty$, +/ $M$, -/ $m$, +/ $+\infty$}
                \end{tikzpicture}
            \end{center}
        \end{parts}
"""
    correction=r"""
    """+identification+r"""
    """
    return(exo,correction)


def main():
    exo,correction = etudePolynome()
    print(exo)
    pass

if __name__ == '__main__':
    main()