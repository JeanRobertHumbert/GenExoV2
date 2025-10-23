import os,sys
import random
import unicodedata
import numpy as np
from sympy import *
import matplotlib.pyplot as plt
from fractions import Fraction

from scipy.optimize import bisect

from baseMaths import *
from baseExo import *

def calculMentalFractionN1(n=3, id=False):
    if id : 
        identification = r"""calculMentalFractionN1\\"""
    else:
        identification = r""""""
    itemQ = r""" """
    itemR=r""" """
    for i in range(0,3*n):
        a = random.randint(1,10)
        b = random.randint(1,10)
        c = random.randint(1,10)
        d = random.randint(1,10)
        op = random.randint(1,3)
        if op==1:
            operator = " + "
            answer = sp.Rational(a*d+b*c, b*d)
        if op==2:
            operator = " - "
            answer = sp.Rational(a*d-b*c, b*d)
        if op==3:
            operator = r""" \times """
            answer = sp.Rational(a*c, b*d)
        itemQ=itemQ+r"""                \item $\dfrac{"""+str(a)+r"""}{"""+str(b)+r"""}"""+operator+r"""\dfrac{"""+str(c)+r"""}{"""+str(d)+r"""}=.............$
    """
        itemR=itemR+r"""                \item $\dfrac{"""+str(a)+r"""}{"""+str(b)+r"""}"""+operator+r"""\dfrac{"""+str(c)+r"""}{"""+str(d)+r"""}=\color{red}{\dfrac{"""+str(answer.numerator)+r"""}{"""+str(answer.denominator)+r"""}}$
    """

    exo=r"""
    """+identification+r"""
    \Question Calcul mental : effectuez les calculs suivants :
        \begin{multicols}{3}
            \begin{enumerate}
"""+itemQ+r"""
            \end{enumerate}
        \end{multicols}
    """
    correction=r"""
    """+identification+r"""
    \Question Calcul mental : effectuez les calculs suivants :
        \begin{multicols}{3}
            \begin{enumerate}
"""+itemR+r"""
            \end{enumerate}
        \end{multicols}
    """
    return(exo, correction)

def exoPourcentage2ndv1(id=False):
    if id : 
        identification = r"""exoPourcentage2ndv1\\"""
    else:
        identification = r""""""
    nbEleves, nbFilles, nbGarcons, nb2GT1, nb2GT3, partGarcons, partFilles, part2GT1, part2GT3 = symbols('nbEleves nbFilles nbGarcons nb2GT1 nb2GT3 partGarcons partFilles part2GT1 part2GT3') 
    nbFilles = random.randint(10,20) #values[0]
    nbGarcons = random.randint(5,15) #values[1]
    nbEleves = nbFilles+nbGarcons
    nb2GT1 = random.randint(5,nbEleves-5) #values[2]
    nb2GT3 = nbEleves-nb2GT1
    partGarcons = Rational(nbGarcons/nbEleves)
    partFilles = Rational(nbFilles/nbEleves)
    part2GT1 =  Rational(nb2GT1/nbEleves)
    part2GT3 =  Rational(nb2GT3/nbEleves)
    exo=r"""
    """+identification+r"""
        \Question Un groupe est composé de """+str(nbEleves)+r""" élèves, """+str(nbFilles)+r""" filles et """+str(nbGarcons)+r""" garçons. """+str(nb2GT1)+r""" élèves de ce groupe sont en 2GT1  et les """+str(nb2GT3)+r""" autres viennent de la 2GT3.
            \begin{parts}
                \Part[2] Quelle est la part des garçons dans ce groupe ?
                    \fillwithlines{15mm}
                \Part[2] Quelle est la part des filles dans ce groupe ?
                    \fillwithlines{15mm}
                \Part[2]  Quelle est la part des élèves issus de 2GT1 ?
                    \fillwithlines{15mm}
                \Part[2]  Quelle est la part des élèves issus de 2GT3 ?
                    \fillwithlines{15mm}
            \end{parts}
    """
    correction=r"""
    """+identification+r"""
        \Question Un groupe est composé de """+str(nbEleves)+r""" élèves, """+str(nbFilles)+r""" filles et """+str(nbGarcons)+r""" garçons. """+str(nb2GT1)+r""" élèves de ce groupe sont en 2GT1  et les """+str(nb2GT3)+r""" autres viennent de la 2GT3.
            \begin{parts}
                \Part[2] Quelle est la part des garçons dans ce groupe ?
                    \begin{solution}
                        La part de garçons représente $\dfrac{"""+str(nbGarcons)+r"""}{"""+str(nbEleves)+r"""}\approx """+str(partGarcons.round(4))+r"""$ soit $"""+str(partGarcons.round(4)*100)+r"""\%$
                    \end{solution}
                \Part[2] Quelle est la part des filles dans ce groupe ?
                    \begin{solution}
                        La part de filles représente $\dfrac{"""+str(nbFilles)+r"""}{"""+str(nbEleves)+r"""}\approx """+str(partFilles.round(4))+r"""$ soit $"""+str(partFilles.round(4)*100)+r"""\%$
                    \end{solution}
                \Part[2]  Quelle est la part des élèves issus de 2GT1 ?
                    \begin{solution}
                        La part des élèves de 2GT1 représente $\dfrac{"""+str(nb2GT1)+r"""}{"""+str(nbEleves)+r"""}\approx """+str(part2GT1.round(4))+r"""$ soit $"""+str(part2GT1.round(4)*100)+r"""\%$
                    \end{solution}
                \Part[2]  Quelle est la part des élèves issus de 2GT3 ?
                    \begin{solution}
                        La part des élèves de 2GT3 représente $\dfrac{"""+str(nb2GT3)+r"""}{"""+str(nbEleves)+r"""}\approx """+str(part2GT3.round(4))+r"""$ soit $"""+str(part2GT3.round(4)*100)+r"""\%$
                    \end{solution}
            \end{parts}
    """
    return(exo,correction)

def exoPourcentage2ndv2(id=False):
    if id :
        identification = r"""exoPourcentage2ndv2\\"""
    else:
        identification = r""""""
    nbMachines, nbJoint, nbProg, nbProgOnly, nbProgJoint  = symbols('nbMachines nbJoint nbProg nbProgOnly nbProgJoint') 
    nbMachines = random.randint(300,400)
    nbJoint = random.randint(100,200) #values[1]
    nbProg = nbMachines-nbJoint
    nbProgJoint = random.randint(10,nbProg-50) #values[2]
    nbProgOnly = nbProg-nbProgJoint
    partJoint = Rational(nbJoint/nbMachines)
    partProgOnly = Rational(nbProgOnly/nbMachines)
    exo=r"""
    """+identification+r"""
        \Question Benoît a réparé """+str(nbMachines)+r""" machines à laver. Il a changé le joint sur """+str(nbJoint)+r""" machines et le programmateur sur les autres dont """+str(nbProgJoint)+r""" présentaient aussi un défaut de joint qu'il a aussi remplacé.
            \begin{parts}
                \Part[2] Quel est le pourcentage de machines ayant un joint défectueux ?
                    \fillwithlines{15mm}
                \Part[4] Quel est le pourcentage de machines ayant seulement le programmateur défectueux ?
                    \fillwithlines{15mm}
            \end{parts}
    """
    correction=r"""
    """+identification+r"""
        \Question Benoît a réparé """+str(nbMachines)+r""" machines à laver. Il a changé le joint sur """+str(nbJoint)+r""" machines et le programmateur sur les autres dont """+str(nbProgJoint)+r""" présentaient aussi un défaut de joint qu'il a aussi remplacé.
            \begin{parts}
                \Part[2] Quel est le pourcentage de machines ayant un joint défectueux ?
                    \begin{solution}
                        Sur les """+str(nbMachines)+r""" machines, il y a $"""+str(nbJoint)+r"""$ machines ayant un joint défectueux. Le pourcentage de machines ayant un joint défectueux est donc :
                        \begin{center}
                            $\dfrac{"""+str(nbJoint)+r"""}{"""+str(nbMachines)+r"""}\approx """+str(partJoint.round(4))+r"""$ soit $"""+str(partJoint.round(4)*100)+r"""\%$
                        \end{center}
                    \end{solution}
                \Part[4] Quel est le pourcentage de machines ayant seulement le programmateur défectueux ?
                    \begin{solution}
                        Sur les """+str(nbMachines)+r""" machines, il y a $"""+str(nbMachines)+r"""-"""+str(nbJoint)+r"""$ soit $"""+str(nbProg)+r"""$ machines qui ont le programmateur défectueux mais $"""+str(nbProgJoint)+r"""$ présentent également un joint défectueux.\\
                        Il y a donc $"""+str(nbProg)+r"""-"""+str(nbProgJoint)+r"""$ soit $"""+str(nbProgOnly)+r"""$ machines qui n'ont que le programmateur défectueux.\\
                        La part de machines ayant uniquement le programmateur défectueux est donc :
                        \begin{center}
                            $\dfrac{"""+str(nbProgOnly)+r"""}{"""+str(nbMachines)+r"""}\approx """+str(partProgOnly.round(4))+r"""$ soit $"""+str(partProgOnly.round(4)*100)+r"""\%$
                        \end{center}
                    \end{solution}
            \end{parts}
    """
    return(exo,correction)

def genfonctionAffine(id=False):
    if id :
        identification = r"""genfonctionAffine\\"""
    else:
        identification = r""""""
    af, bf, x, f = symbols('af bf x f')
    ag, bg, g = symbols('ag bg g')
    ah, bh, h = symbols('ah bh h')
    values = nonEqRandomValue(n=3, tier=False, notNull=True)
    af = values[0] 
    ag = values[1] 
    ah = values[2]
    values = nonEqRandomValue(n=3, tier=False, notNull=True)
    bf = values[0]
    bg = values[1]
    bh = values[2]
    f = af*x+bf
    g = ag*x+bg
    h = ah*x+bh
    g0 = bg
    g1 = ag*ag.denominator+bg
    solfg = solve(f-g, rational=True)
    solf = solve(f, rational=True)
    xI = (bh-bf)/(af-ah)
    fh = f-h
    yI = af*(bh-bf)/(af-ah)+bf
    # Pour le tableau de signe et variation
    tabSigneVar = r"""
    					\tkzTabLine
					     { , - , z , + , }
					   \tkzTabVar
					     { -/$-\infty$, R/ ,  +/$+\infty$}
    """
    if af<0:
        tabSigneVar = r"""
					   \tkzTabLine
					     { , + , z , - , }
					   \tkzTabVar
					     { +/$+\infty$, R/ ,  -/$-\infty$}
          """
    exo=r"""
    \clearpage
    """+identification+r"""
    \Question Fonctions Affines\\
        Dans le repère orthonormé ci-dessous, la courbe $\mathcal{C}_f$ est la représentation graphique de $f$ une fonction définie par $f(x)="""+Latex(f)+r"""$.
        \begin{center}
            \begin{tikzpicture}
                \begin{axis}[
                        axis x line=middle,
                        axis y line=middle,
                        xmin = -10, xmax = 10,
                        ymin = -10, ymax = 10,
                        xtick distance = 1,
                        ytick distance = 1,
                        grid = both,
                        minor tick num = 1,
                        major grid style = {gray},
                        minor grid style = {gray!25},
                        width = \textwidth,
                        height = \textwidth
                        ]
                    \draw[very thick,->] (axis cs:0,0)->(axis cs:1,0) node[below, midway] {$\vect{i}$};
                    \draw[very thick,->] (axis cs:0,0)->(axis cs:0,1) node[left, midway] {$\vect{j}$};
                    \draw (axis cs:0,0) circle node [left, below] {$O$};
                    \addplot[
                        domain = -9:9,
                        samples = 50,
                        smooth,
                        thick,
                        blue,
                        ] {"""+str(f)+r"""} node[pos=0.35,above,] {$\mathcal{C}_f$};
                    \addplot[
                        domain = -9:9,
                        samples = 50,
                        smooth,
                        thick,
                        green,
                        ] {"""+str(h)+r"""} node[pos=0.55,above,] {$\mathcal{C}_h$};
                \end{axis}
            \end{tikzpicture}
        \end{center}
        \begin{parts}
        \small{
            \Part[2] Représenter la fonction $g(x)="""+Latex(g)+r"""$
                \fillwithlines{25mm}
            \Part[1] Donner le coefficient directeur et l'ordonnée à l'origine de la fonction $g$.
                \fillwithlines{20mm}
            \Part[4] Résoudre $f(x)=g(x)$ et donner une interprétation de votre résultat.
                \fillwithlines{25mm}
            \Part[4] Déterminer l'expression algébrique de la fonction $h$ dont la représentation graphique est la droite $\mathcal{C}_h$
                \fillwithlines{25mm}
            \Part[4] Déterminer les coordonnées du point $I$, intersection de la courbe $\mathcal{C}_f$ et $\mathcal{C}_h$.
                \fillwithlines{25mm}
            \Part[2] Résoudre $f(x)=0$
                \fillwithlines{25mm}
            \Part[4] Compléter le tableau de signe et variations de $f$ ci-dessous
                \begin{center}
                    \begin{tikzpicture}
                        \tkzTabInit %[lgt=3]
                            {$x$ / 1 , Signe de $f$ / 1, Variations de $f$ / 3 }
                            {$+\infty$, , $+\infty$}
                        \tkzTabLine
                            { ,  ,  ,  , }
                        \tkzTabVar
                            { ,  ,  }
                    \end{tikzpicture}
                \end{center}
            }
        \end{parts}
        """
    correction=r"""
    \clearpage
        \Question Fonctions Affines (Correction)\\
        Dans le repère orthonormé ci-dessous, la courbe $\mathcal{C}_f$ est la représentation graphique de $f$ une fonction définie par $f(x)="""+Latex(f)+r"""$.
        \begin{center}
            \begin{tikzpicture}
                \begin{axis}[
                        axis x line=middle,
                        axis y line=middle,
                        xmin = -10, xmax = 10,
                        ymin = -10, ymax = 10,
                        xtick distance = 1,
                        ytick distance = 1,
                        grid = both,
                        minor tick num = 1,
                        major grid style = {gray},
                        minor grid style = {gray!25},
                        width = \textwidth,
                        height = \textwidth
                        ]
                    \draw[very thick,->] (axis cs:0,0)->(axis cs:1,0) node[below, midway] {$\vect{i}$};
                    \draw[very thick,->] (axis cs:0,0)->(axis cs:0,1) node[left, midway] {$\vect{j}$};
                    \draw (axis cs:0,0) circle node [left, below] {$O$};
                    \addplot[
                        domain = -9:9,
                        samples = 50,
                        smooth,
                        thick,
                        blue,
                        ] {"""+str(f)+r"""} node[pos=0.35,above,] {$\mathcal{C}_f$};
                    \addplot[
                        domain = -9:9,
                        samples = 50,
                        smooth,
                        thick,
                        green,
                        ] {"""+str(h)+r"""} node[pos=0.55,above,] {$\mathcal{C}_h$};
                    \addplot[
                        domain = -9:9,
                        samples = 50,
                        smooth,
                        thick,
                        red,
                        ] {"""+str(g)+r"""} node[pos=0.6,above,] {$\mathcal{C}_g$};
                    \draw[red] (axis cs:0,"""+str(g0)+r""") circle(3pt) node [left, below] {$G_1$};
                    \draw[red] (axis cs:"""+str(ag.denominator)+r""","""+str(g1)+r""") circle(3pt) node [left, below] {$G_2$};
                    \draw (axis cs:"""+str(xI)+r""","""+str(yI)+r""") circle(3pt) node [left, below] {$I$};
                \end{axis}
            \end{tikzpicture}
        \end{center}
        \begin{parts}
        \small{
            \Part Représenter la fonction $g(x)="""+Latex(g)+r"""$
    %        			\fillwithlines{25mm}
                \\La fonction $g$ est une fonction affine ( forme $ax+b$). La représentation graphique de $g$ est donc une droite. \\
                Selon le premier axiome d'Euclide, il faut deux points pour définir de façon unique une droite. nous allons donc déterminer deux couples antécédent-image qui constitueront les coordonnées des deux points dont nous avons besoin.
                \begin{enumerate}
                    \item On choisi par commodité 0 comme premier antécédent d'où :\\
                    $g(0)="""+Latex(g0)+r"""$ on a donc le premier point $G_1$ aux coordonnées $(0;"""+Latex(g0)+r""")$
                    \item On détermine maintenant l'image d'un deuxième antécédent d'où :\\
                    $g("""+Latex(ag.denominator)+r""")="""+Latex(g1)+r"""$ on a donc le deuxième point $G_2$ aux coordonnées $("""+Latex(ag.denominator)+r""";"""+Latex(g1)+r""")$
                    \item On place les points $G_1$ et $G_2$ puis on trace la droite passant par ses deux points et on la nomme $\mathcal{C}_g$.
                \end{enumerate}
            \Part Donner le coefficient directeur et l'ordonnée à l'origine de la fonction $g$.
    %        			\fillwithlines{20mm}
                \\Comme énoncé à la question précédente, la fonction $g$ est une fonction affine donc sa forme est $ax+b$ où $a$ est appelé "coefficient directeur" et $b$ "ordonnée à l'origine".\\
                Donc par analogie entre $"""+Latex(g)+r"""$ et $ax+b$, le coefficient directeur est $"""+Latex(ag)+r"""$ et l'ordonnée à l'origine est $"""+Latex(bg)+r"""$.
            \Part Résoudre $f(x)=g(x)$ et donner une interprétation de votre résultat.
    %	        		\fillwithlines{25mm}
                \begin{align*}
                    f(x)&=g(x)\text{    (On remplace $f$ et $g$ par leurs expressions)}\\
                    \Leftrightarrow """+Latex(f)+r""" &= """+Latex(g)+r"""\\
                    \Leftrightarrow """+Latex(f-g)+r""" &= 0\\
                    \Leftrightarrow x &= """+Latex(solfg[0])+r"""
                \end{align*}
                Donc pour que $f(x)=g(x)$ il faut que $x="""+Latex(solfg[0])+r"""$. Cette solution de l'équation est la seule valeur d'antécédent pour laquelle $f$ et $g$ donnent la même image.\\
                Il s'agit donc de l'abscisse du point d'intersection des deux droite représentative de $f$ et $g$ ($\mathcal{C}_f$ et $\mathcal{C}_g$).
                \Part Déterminer l'expression algébrique de la fonction $h$ dont la représentation graphique est la droite $\mathcal{C}_h$
                %	        		\fillwithlines{25mm}
                \\ La courbe $\mathcal{C}_h$ est une droite donc l'expression algébrique de la fonction $h$ est de la forme $ax+b$.\\
                On remarque que $\mathcal{C}_h$ passe par le point $(0;"""+Latex(bh)+r""")$ ce qui signifie que $b="""+Latex(bh)+r"""$.\\
                A partir de ce point, on remarque que si l'on se déplace de """+str(ah.denominator) +r""" sur l'axe des abscisses, on évolue de """+str(ah.numerator)+r""" sur l'axe des ordonnées. On peut en déduire que :\\
                $a=\dfrac{"""+str(ah.numerator)+r"""}{"""+str(ah.denominator) +r"""}$\\
                Donc l'expression de $h$ est $h(x)="""+Latex(h)+r"""$.
            \Part Déterminer les coordonnées du point $I$, intersection de la courbe $\mathcal{C}_f$ et $\mathcal{C}_h$.\\
            %	        		\fillwithlines{25mm}
                Le point $I(x_I;y_I)$ avec $x_I$ solution de $f(x)=h(x)$ et $y_I=f(x_I)=h(x_I)$
                On résous donc $f(x)=h(x)$ :
                \begin{align*}
                    f(x)&=h(x)\text{    (On remplace $f$ et $h$ par leurs expressions)}\\
                    \Leftrightarrow """+Latex(f)+r""" &= """+Latex(h)+r"""\\
                    \Leftrightarrow """+Latex(f-h)+r""" &= 0\\
                    \Leftrightarrow x &= """+Latex(xI)+r"""
                \end{align*}
                Donc $S=\lbrace"""+Latex(xI)+r"""\rbrace$ et $x_I="""+Latex(xI)+r"""$.\\
                On $y_I$ image de la fonction $f$ ou $h$ de $x_I$ :\\
                $y_I="""+Latex(af)+r"""\times"""+Latex(xI)+r"""+"""+Latex(bf)+r"""="""+Latex(yI)+r"""$\\
                Donc $I\left("""+Latex(xI)+r""";"""+Latex(yI)+r"""\right)$
            \Part Résoudre $f(x)=0$\\
                %	        		\fillwithlines{25mm}
                \begin{align*}
                    f(x)&=0\text{    (On remplace $f$ par son expression)}\\
                    \Leftrightarrow """+Latex(f)+r""" &= 0\\
                    \Leftrightarrow """+Latex(af*x)+r""" &= """+Latex(-bf)+r"""\\
                    \Leftrightarrow x &= """+Latex(-bf/af)+r"""
                \end{align*}
                Donc $f(x)=0$ pour $x="""+Latex(-bf/af)+r"""$
            \Part Compléter le tableau de signe et variations de $f$ ci-dessous\\
                \begin{center}
                    \begin{tikzpicture}
                    \tkzTabInit %[lgt=3]
                    {$x$ / 1 , Signe de $f$ / 1, Variations de $f$ / 3 }
                    {$+\infty$, $"""+Latex(-bf/af)+r"""$, $+\infty$}
                    """+tabSigneVar+r"""
                    \end{tikzpicture}
                \end{center}
        }
    \end{parts}
    """

    return(exo,correction)

def exoAffineReprEtExpression(id=False):
    if id :
        identification = r"""exoAffineReprEtExpression\\"""
    else:
        identification = r""""""
    n=6
    alphabet = list(string.ascii_lowercase)
    fonctions = random.sample(alphabet, n)
    fonctions.sort()
    # print(fonctions)
    itemRepr = r""""""
    itemLect = r""""""
    itemLectCorrection = r""""""
    addplot = r""""""
    addplotCorrection = r""""""
    f1 = fonctions[:3]
    f2 = fonctions[3:]
    for f in f1:
        k = nonEqRandomValue(n=2, notNull=True, tier=False, quart=False)
        p = affine(f, k[0], k[1])
        pos=0.55
        if p.a>0:
            pos = min(0.95,0.45+p.supTo(5)/10)
        if p.a<0:
            pos = min(0.95,0.45+p.supTo(-5)/10)
            # pos = max(0.1,0.45+p.supTo(5)/10)
            # print("("+str(p.a)+";"+str(p.b)+") -> "+str(p.supTo(5).evalf()))
        addplot = addplot + r"""\addplot[thick, color=red] {"""+str(p.a)+r"""*x+"""+str(p.b)+r"""} node[above, sloped, pos = """+str(pos)+r"""] {$\mathcal{C}_"""+p.name+r"""$};
        """
        itemLect = itemLect + r"""
                            \item $\mathcal{C}_"""+p.name+r"""$ : $"""+p.name+r"""(x)=......................$
        """
        itemLectCorrection = itemLectCorrection + r"""
                            \item $\mathcal{C}_"""+p.name+r"""$ : {\color{red} """+p.latexString()+r"""}
        """
    n=3
    for f in f2:
        k = nonEqRandomValue(n=2, notNull=True, tier=False)
        p = affine(f, k[0], k[1])
        pos=0.55
        if p.a>0:
            pos = min(0.95,0.45+p.supTo(5)/10)
        if p.a<0:
            pos = min(0.95,0.45+p.supTo(-5)/10)
        addplotCorrection = addplotCorrection + r"""\addplot[thick, color=blue] {"""+str(p.a)+r"""*x+"""+str(p.b)+r"""} node[above, sloped, pos = """+str(pos)+r"""] {$\mathcal{C}_"""+p.name+r"""$};
        """
        itemRepr = itemRepr + r"""
        					\item {\color{blue} """+p.latexString()+r"""}
        """

    exo=r"""
    """+identification+r"""
        \Question Représentation et Expression algébrique de fonctions affines
                    \begin{multicols}{2}
                    \begin{parts}
                        \Part[6] Représentez graphiquement les fonctions suivantes :
                        \begin{enumerate}
                            """+itemRepr+r"""
                        \end{enumerate}
                        \Part[6] Donnez les expressions algébrique des fonctions associées aux droites suivantes :
                        \begin{enumerate}
                            """+itemLect+r"""
                        \end{enumerate}
                    \end{parts}
                        \vfill
                        \columnbreak
                        \begin{center}
                            \begin{tikzpicture}[scale=1]
                                \begin{axis}[
                                    scale only axis,
                                    grid=both, % Active le cadrillage principal et secondaire
                                    minor grid style={dashed, gray!50}, % Style du sous-cadrillage
                                    major grid style={solid, black!50}, % Style du cadrillage principal
                                    axis lines=middle,
                                    inner axis line style={=>},
                                    ytick={-5,-4,...,5},
                                    xtick={-5,-4,...,5},
                                    ymin=-5,
                                    ymax=5,
                                    xmin=-5,
                                    xmax=5,
                                ]
                                """+addplot+r"""
                                \end{axis}
                            \end{tikzpicture}
                        \end{center}
                    \end{multicols}
                    Zone de travail :
                    \fillwithlines{90mm}
    """
    correction=r"""
    """+identification+r"""
        \Question Représentation et Expression algébrique de fonctions affines
                    \begin{multicols}{2}
                    \begin{parts}
                        \Part[6] Représentez graphiquement les fonctions suivantes :
                        \begin{enumerate}
                            """+itemRepr+r"""
                        \end{enumerate}
                        \Part[6] Donnez les expressions algébrique des fonctions associées aux droites suivantes :
                        \begin{enumerate}
                            """+itemLectCorrection+r"""
                        \end{enumerate}
                    \end{parts}
                        \vfill
                        \columnbreak
                        \begin{center}
                            \begin{tikzpicture}[scale=1]
                                \begin{axis}[
                                    scale only axis,
                                    grid=both, % Active le cadrillage principal et secondaire
                                    minor grid style={dashed, gray!50}, % Style du sous-cadrillage
                                    major grid style={solid, black!50}, % Style du cadrillage principal
                                    axis lines=middle,
                                    inner axis line style={=>},
                                    ytick={-5,-4,...,5},
                                    xtick={-5,-4,...,5},
                                    ymin=-5,
                                    ymax=5,
                                    xmin=-5,
                                    xmax=5,
                                ]
                                """+addplot+addplotCorrection+r"""
                                \end{axis}
                            \end{tikzpicture}
                        \end{center}
                    \end{multicols}
    """
    return(exo , correction)

def ThalesPythagore(id=False):
    if id :
        identification = r"""ThalesPythagore\\"""
    else:
        identification = r""""""
    values = nonEqRandomValue(n=3, debut=1, fin=5, demi=True, tier=False, notNull=False)
    ab, bd, ac, ad, ce, bc, de = symbols('ab bd ac ad ce bc de') 
    ab = random.randint(1,4) #values[0]
    bd = random.randint(1,3) #values[1]
    ac = random.randint(1,4) #values[2]
    ad = ab+bd
    ce = Rational(ac*ad/ab-ac)
    ae = ac+ce
    bc = sqrt(ab**2+ac**2)
    exo=r"""
        \clearpage
        """+identification+r"""
		\Question Thalès et Pythagore\\
			Dans la figure ci-dessous, $AB="""+str(ab)+r"""$, $DB="""+str(bd)+r"""$, $AC="""+str(ac)+r"""$ et $AE="""+Latex(ae)+r"""$
			\begin{center}
				\begin{tikzpicture}[scale=1] % fixed points
					\tkzDefPoint(2,3){A}
					\tkzDefShiftPoint[A](0:"""+str(ab)+r"""){B}
					\tkzDefShiftPoint[A](90:"""+str(ac)+r"""){C}
					\tkzDefShiftPoint[A](90:"""+str(ae)+r"""){E}					
					\tkzDefShiftPoint[A](0:"""+str(ad)+r"""){D}
					\tkzDefShiftPoint[A](90:"""+str(ac)+r"""){C}
					\tkzDrawSegments(A,B B,C C,A A,D A,E D,E)
%					\tkzMarkSegments[mark=|](A,B A,C)
					\tkzDrawPoints(A,B,C,D,E)
					\tkzLabelPoints(B,D)
					\tkzLabelPoints[above left](A,C,E)
				\end{tikzpicture}
			\end{center}
			\begin{parts}
				\Part[4] Montrer que $(BC)$ et $(DE)$ sont parallèles
					\fillwithlines{35mm}
				\Part[4] Sachant que le triangle $ABC$ est rectangle en $A$
					\begin{enumerate}
						\item Calculer $BC$
							\fillwithlines{30mm}
						\item Calculer $DE$
							\fillwithlines{30mm}
					\end{enumerate}
			\end{parts}
    """
    correction=r"""
    	\clearpage
        """+identification+r"""
		\Question Thalès et Pythagore\\
			Dans la figure ci-dessous, $AB="""+str(ab)+r"""$, $DB="""+str(bd)+r"""$, $AC="""+str(ac)+r"""$ et $AE="""+Latex(ae)+r"""$
			\begin{center}
				\begin{tikzpicture}[scale=1] % fixed points
					\tkzDefPoint(2,3){A}
					\tkzDefShiftPoint[A](0:"""+str(ab)+r"""){B}
					\tkzDefShiftPoint[A](90:"""+str(ac)+r"""){C}
					\tkzDefShiftPoint[A](90:"""+str(ae)+r"""){E}					
					\tkzDefShiftPoint[A](0:"""+str(ad)+r"""){D}
					\tkzDefShiftPoint[A](90:"""+str(ac)+r"""){C}
					\tkzDrawSegments(A,B B,C C,A A,D A,E D,E)
%					\tkzMarkSegments[mark=|](A,B A,C)
					\tkzDrawPoints(A,B,C,D,E)
					\tkzLabelPoints(B,D)
					\tkzLabelPoints[above left](A,C,E)
				\end{tikzpicture}
			\end{center}
			\begin{parts}
				\Part Montrer que $(BC)$ et $(DE)$ sont parallèles\\
%					\fillwithlines{35mm}
					Selon le théorème de Thalès, on a la double égalité suivante :
					\begin{center}
						$\dfrac{AB}{AD}=\dfrac{AC}{AE}=\dfrac{BC}{DE}$
					\end{center}
					On sait que  $AB="""+str(ab)+r"""$, $DB="""+str(bd)+r"""$, $AC="""+str(ac)+r"""$ et $AE="""+str(ae)+r"""$. Donc $AD=AB+BD="""+str(ab)+r"""+"""+str(bd)+r"""="""+str(ad)+r"""$.\\
					On calcule séparément $\dfrac{AB}{AD}=\dfrac{"""+str(ab)+r"""}{"""+str(ad)+r"""}$ et $\dfrac{AC}{AE}=\dfrac{"""+str(ac)+r"""}{"""+Latex(ae)+r"""}="""+Latex(ac/ae)+r"""$\\
					Les deux quotients sont égaux, on peut donc en déduire que $(BC)$ et $(DE)$ sont parallèles.
				\Part Sachant que le triangle $ABC$ est rectangle en $A$
					\begin{enumerate}
						\item Calculer $BC$
%							\fillwithlines{30mm}
							Si le triangle $ABC$ est rectangle en $A$ alors le théorème de Pythagore s'applique et on a donc l'égalité suivante :
							\begin{center}
								$BC^2=AB^2+AC^2$
							\end{center}
							$BC^2="""+str(ab)+r"""^2+"""+str(ac)+r"""^2="""+str(ab**2)+r"""+"""+str(ac**2)+r"""="""+str(bc**2)+r"""$ donc $BC=\sqrt{"""+str(bc**2)+r"""}="""+Latex(bc)+r"""$
						\item Calculer $DE$
%							\fillwithlines{30mm}
							Selon la double égalité de Thalès de la première question, on a :
							\begin{center}
								$\dfrac{AB}{AD}=\dfrac{BC}{DE}$\\
								donc $\dfrac{"""+Latex(ab)+r"""}{"""+Latex(ad)+r"""}=\dfrac{"""+Latex(bc)+r"""}{DE}$\\
								d'où $DE="""+Latex(bc)+r"""\times \dfrac{"""+Latex(ad)+r"""}{"""+Latex(ab)+r"""}="""+Latex(bc*ad/ab)+r"""$
							\end{center}
					\end{enumerate}
			\end{parts}
    """
    return(exo,correction)

def PerimetreEtAire(id=False):
    if id :
        identification = r"""PerimetreEtAire\\"""
    else:
        identification = r""""""
    height = random.randint(6, 9)
    alpha = random.randint(3,10)
    P = random.randint(35,55)
    correction=r"""
\clearpage
"""+identification+r"""
    \Question Dans la figure ci-contre, x est en $cm$.
        \begin{center}
            \begin{tikzpicture}[scale=0.5,cap=round]
                % Define constants for the drawing
                \pgfmathsetmacro{\height}{"""+str(height)+r"""} % Height of rectangle
                \pgfmathsetmacro{\width}{\height/3+"""+str(alpha)+r"""}  % Width of rectangle
                \pgfmathsetmacro{\xval}{\height/3}  
                \pgfmathsetmacro{\less}{\width-\xval}  
                % Draw external shape
                \draw[thick] (0,0) 
                        -- (0,\height/3)
                    -- (\xval,\height/3)
                    -- (\xval,2*\height/3)
                    -- (0,2*\height/3)
                    -- (0,\height)
                    -- (\width,\height)
                    -- (\width,0)
                    -- cycle;
                % Horizontal dimension line (\width-\xval)
                \draw[<->] (\width,\height/2) -- (\xval,\height/2) node[midway, below] {\less cm};
                % Vertical dimension line for x on the left side
                \draw[<->] (-0.5, \height) -- (-0.5,2*\height/3) node[midway, left] {$x$};
                % Notches on the lines
                \draw (0,\height/3/2) node {$\times$};
                \draw (\xval/2,\height/3) node {$\times$};
                \draw (\xval,\height/2) node {$\times$};
                \draw (\xval/2,2*\height/3) node {$\times$};
                \draw (0,5*\height/6) node {$\times$};
                % Correction --------------------
                % Red brace inside the rectangle
                    \draw[decorate, decoration={brace, amplitude=10pt}, red, thick]
                    (0, \height+0.1) -- (\width, \height+0.1) node[midway, yshift=12pt, above] {\textcolor{red}{$x + \less$}};
                    % Red vertical brace
                \draw[decorate, decoration={brace, amplitude=10pt}, red, thick]
                    (\width+0.1, \height) -- (\width+0.1, 0) node[midway, xshift=12pt, right] {\textcolor{red}{$3x$}};
                    %--------------------------------
            \end{tikzpicture}
        \end{center}
        \begin{parts}
            \Part Exprimer en fonction de $x$ le périmètre $P$ de cette figure en cm.\\
            \textcolor{red}{
            La longueur de la partie gauche représente $5\times x$ on a donc :
            \begin{align*}
                P	&= 5x + 3x + 2(x+"""+str(alpha)+r""") \\
                    &= 5x + 3x + 2x + """+str(2*alpha)+r"""\\
                    &= 10x + """+str(2*alpha)+r"""
            \end{align*}
            }
%			\fillwithlines{20mm}
            \Part Exprimer l'aire de la figure en fonction de $x$ en $cm^2$. Factoriser le résultat.\\
            \textcolor{red}{
            L'aire $A$ du grand rectangle est $(x+"""+str(alpha)+r""")(3x)$ mais il faut retrancher l'aire du creux de la partie gauche. on a donc :
            \begin{align*}
                A	&= (x+"""+str(alpha)+r""")(3x)-x^2 \\
                    &= 3x^2+"""+str(3*alpha)+r"""x-x^2\\
                    &= 2x^2+"""+str(3*alpha)+r"""x = x(2x+"""+str(3*alpha)+r""")
            \end{align*}
            }
%			\fillwithlines{20mm}
            \Part Sachant que le périmètre de cette figure est $"""+str(P)+r""" cm$, en déduire la valeur de x. Déterminer l'aire de la figure.
            \begin{multicols}{2}
            \textcolor{red}{
            On résout $P="""+str(P)+r"""$, d'où :
            \begin{align*}
                                    P	&= """+str(P)+r""" \\
                \Leftrightarrow 10x+"""+str(2*alpha)+r"""	&= """+str(P)+r"""\\
                \Leftrightarrow 10x		&= """+str(P)+r"""-"""+str(2*alpha)+r"""\\
                \Leftrightarrow 10x		&= """+str(P-2*alpha)+r"""\\
                \Leftrightarrow x		&= \frac{"""+str(P-2*alpha)+r"""}{10} = """+str((P-2*alpha)/10)+r"""
            \end{align*}
            Donc $x="""+str((P-2*alpha)/10)+r""" cm$\\
            On calcul maintenant l'aire A :
            \begin{align*}
                A	&= x(2x+"""+str(3*alpha)+r""") \\
                    &= """+str((P-2*alpha)/10)+r"""\times(2\times """+str((P-2*alpha)/10)+r"""+"""+str(3*alpha)+r""")\\
                    &= """+str((P-2*alpha)/10)+r"""\times("""+str(2*(P-2*alpha)/10)+r"""+"""+str(3*alpha)+r""")\\
                    &= """+str((P-2*alpha)/10)+r"""\times """+str(2*(P-2*alpha)/10+3*alpha)+r"""\\
                    &= """+str(round((P-2*alpha)/10*(2*(P-2*alpha)/10+3*alpha),2))+r"""
            \end{align*}
            Donc $A="""+str(round((P-2*alpha)/10*(2*(P-2*alpha)/10+3*alpha),2))+r""" cm^2$.
            }
            \end{multicols}
%			\fillwithlines{20mm}
            
        \end{parts}
    """
    exo=r"""
    \clearpage
    """+identification+r"""
    \Question Dans la figure ci-contre, x est en $cm$.
        \begin{center}
            \begin{tikzpicture}[scale=0.5,cap=round]
                % Define constants for the drawing
                \pgfmathsetmacro{\height}{"""+str(height)+r"""} % Height of rectangle
                \pgfmathsetmacro{\width}{\height/3+"""+str(alpha)+r"""}  % Width of rectangle
                \pgfmathsetmacro{\xval}{\height/3}  
                \pgfmathsetmacro{\less}{\width-\xval}  
                % Draw external shape
                \draw[thick] (0,0) 
                        -- (0,\height/3)
                    -- (\xval,\height/3)
                    -- (\xval,2*\height/3)
                    -- (0,2*\height/3)
                    -- (0,\height)
                    -- (\width,\height)
                    -- (\width,0)
                    -- cycle;
                % Horizontal dimension line (\width-\xval)
                \draw[<->] (\width,\height/2) -- (\xval,\height/2) node[midway, below] {\less cm};
                % Vertical dimension line for x on the left side
                \draw[<->] (-0.5, \height) -- (-0.5,2*\height/3) node[midway, left] {$x$};
                % Notches on the lines
                \draw (0,\height/3/2) node {$\times$};
                \draw (\xval/2,\height/3) node {$\times$};
                \draw (\xval,\height/2) node {$\times$};
                \draw (\xval/2,2*\height/3) node {$\times$};
                \draw (0,5*\height/6) node {$\times$};
            \end{tikzpicture}
        \end{center}
        \begin{parts}
            \Part Exprimer en fonction de $x$ le périmètre $P$ de cette figure en cm.
            \fillwithlines{30mm}
            \Part Exprimer l'aire de la figure en fonction de $x$ en $cm^2$. Factoriser le résultat.
 			\fillwithlines{30mm}
            \Part Sachant que le périmètre de cette figure est $"""+str(P)+r""" cm$, en déduire la valeur de x. Déterminer l'aire de la figure.
            \begin{multicols}{2}
            \fillwithlines{35mm}
        \columnbreak
            \fillwithlines{35mm}
            \end{multicols}
        \end{parts}
    """
    return(exo, correction)

def LectureGraphhiqueEtEtudeFonction(id=False):
    if id :
        identification = r"""LectureGraphhiqueEtEtudeFonction\\"""
    else:
        identification = r""""""
    # Définir la variable symbolique
    x = symbols('x')
    a = symbols('a')
    b = symbols('b')
    c = symbols('c')
    
    # Partie A
    xMin_val = random.randint(-9,-5)
    xMax_val = random.randint(5, 9)
    # Paramètres de la fenêtre
    xMin, xMax = -10, 10
    yMin, yMax = -10, 10
    points = []

    points = generate_crossing_points(xMin_val,xMax_val)
    
    # # Calcul des valeurs minimale et maximale des ordonnées
    # x_values = [point[0] for point in points]
    # y_values = [point[1] for point in points]
    # xMin = min(x_values)
    # xMax = max(x_values)
    # yMin = min(y_values)
    # yMax = max(y_values)
    
    points_string = ' '.join(f"({x:.2f}, {y:.2f})" for x, y in points)

    point_aleatoire = random.choice(points)
    points_Appart = random.choice(points)
    points_Appart = (points_Appart[0], points_Appart[1]+random.randint(-1, 1))
    

    # Vérification si le point appartient à la liste
    if points_Appart in points:
        Corr1 = r"""$A\notin \mathcal{C}_f$ : Le point $A$ appartient à $\mathcal{C}_f$ car il se trouve sur la courbe, (l'image de son abscisse par la fonction est graphiquement correcte)"""
    else:
        Corr1 = r"""$A\notin \mathcal{C}_f$ : Le point $A$ n'appartient pas à $\mathcal{C}_f$ car il ne se trouve pas sur la courbe représentative de la fonction, (l'image de son abscisse par la fonction est graphiquement incorrecte)"""
    
    abscisses_zero = [x for x, y in points if y == 0]
    
    if len(abscisses_zero)>1:
        Corr2=r"""Les antécédents de 0 sont : """+' ; '.join(f"{x}" for x in abscisses_zero)#str(abscisses_zero)
    if len(abscisses_zero)==1:
        Corr2=r"""L'antécédents de 0 est """+' '.join(f"{x}" for x in abscisses_zero)#str(abscisses_zero)
    if len(abscisses_zero)==0:
        Corr2=r"""0 n'a pas d'antécédents pour cette fonction."""
    
    # Partie B
    Coeffs = nonEqRandomValue(n=3, debut=-2, fin=3)
    a = Coeffs[0]
    b = Coeffs[1]
    c = Coeffs[2]
    g = a*x**2+b*x+c
    g_str_latex = r""""""
    # Coeff a
    if a==1 :
        g_str_latex = g_str_latex + r"""x^2"""
    elif a==-1 :
        g_str_latex = g_str_latex + r"""-x^2"""
    else :
        g_str_latex = g_str_latex + latex(a).replace('\\frac','\\dfrac')+r"""x^2"""
     # Coeff b
    if b==1 :
        g_str_latex = g_str_latex + r"""+x"""
    elif b==-1 :
        g_str_latex = g_str_latex + r"""-x"""
    else :
        if b<0 :
            g_str_latex = g_str_latex + r"""-""" + latex(-1*b).replace('\\frac','\\dfrac')+r"""x"""
        else :
            g_str_latex = g_str_latex + r"""+""" + latex(b).replace('\\frac','\\dfrac')+r"""x"""
    # Coeff c
    if c==1 :
        g_str_latex = g_str_latex + r"""+1"""
    elif b==-1 :
        g_str_latex = g_str_latex + r"""-1"""
    else :
        if c<0 :
            g_str_latex = g_str_latex + r"""-""" + latex(-1*c).replace('\\frac','\\dfrac')
        else :
            g_str_latex = g_str_latex + r"""+""" + latex(b).replace('\\frac','\\dfrac')
    DgMin = int(random.uniform(-10, -b/(2*a)))
    DgMax = int(random.uniform( -b/(2*a), 10))
    g_points = nonEqRandomValue(n=8, debut=int(-b/(2*a))-4, fin=int(-b/(2*a))+4, tier=False)
    g_points = sorted(g_points)
    
    Ant1 = int(random.uniform( DgMin, DgMax))
    Img1 = g.subs(x, Ant1)
    Ant2 = int(g.subs(x, -b/(2*a)))
    Img2 = g.subs(x, Ant2)
    
    g_Img = [g.subs(x,value) for value in g_points]
    g_Img_num =  [round(value.evalf(), 2) for value in g_Img]
    g_points_string = ' '.join(f"({x:.2f}, {y:.2f})" for x, y in list(zip(g_points, g_Img_num)))
    # if a.is_rational :
    #     g_str_latex = g_str_latex+r"""\dfrac{"""+str(a.numerator)+r"""}{"""+str(a.denominator)+r"""}x^2"""
    # else:
    #     g_str_latex = g_str_latex+str(a)+r"""x^2"""
    # if b.is_rational :
    #     g_str_latex = g_str_latex+r"""+\dfrac{"""+str(b.numerator)+r"""}{"""+str(b.denominator)+r"""}x"""
    # else:
    #     g_str_latex = g_str_latex+r"""+"""+str(b)+r"""x"""
    exo=r"""
    """+identification+r"""
    \Question Lecture Graphique et Étude de fonction\\
       Soit $\mathcal{C}_f$ la représentation graphique d'une fonction $f$ , donnée ci-dessous.
        \begin{center}
            \begin{tikzpicture}[scale=1,cap=round]
                \begin{axis}[
                        axis x line=middle, axis y line=middle,
                        xmin = """+str(xMin-1)+r""", xmax = """+str(xMax+1)+r""",
                        ymin = """+str(yMin-1)+r""", ymax = """+str(yMax+1)+r""",
                        xtick distance = 1, ytick distance = 1,
                        grid = both, minor tick num = 1,
                        major grid style = {gray}, minor grid style = {gray!25},
                        width = \textwidth, height = \textwidth,
                        axis equal image
                    ]
                    \draw[very thick,->] (axis cs:0,0)->(axis cs:1,0) node[below, midway] {$\vect{i}$};
                    \draw[very thick,->] (axis cs:0,0)->(axis cs:0,1) node[left, midway] {$\vect{j}$};
                    \draw (axis cs:0,0) circle node [left, below] {$O$};
                    \addplot[blue, thick, smooth] coordinates {
                        """+points_string+r"""
                    } node[pos=0.05, above, yshift=5pt] {$C_f$};
                \end{axis}
            \end{tikzpicture}
        \end{center}
        \begin{parts}
            \Part Partie A - Étude de la fonction $f$.
                \begin{subparts}
                    \subpart Lire l'ensemble de définition de la fonction $f$.
                        \fillwithlines{10mm}
                    \subpart  Par lecture graphique, quelle est l'image de """+str(point_aleatoire[0])+r""" par la fonction $f$.
                        \fillwithlines{10mm}
                    \subpart  Le point $A("""+str(points_Appart[0])+r""" ; """+str(points_Appart[1])+r""")$ appartient-il à la courbe $\mathcal{C}_f$? Justifier.
                        \fillwithlines{10mm}
                    \subpart  Déterminer graphiquement, les éventuels antécédents de 0. On laissera apparaitre les traits de construction sur le graphique.
                        \fillwithlines{10mm}
                \end{subparts}
\clearpage
            \Part B - Étude de la fonction $g$\\
                On considère la fonction $g$ définie sur $\mathcal{D}_g=["""+str(DgMin)+r"""; """+str(DgMax)+r"""]$ par l'expression : $g(x)="""+g_str_latex+r"""$
                \begin{subparts}
                    \subpart Calculer l'image de """+str(Ant1)+r""" par la fonction $g$
                        \fillwithlines{20mm}
                    \subpart Sans calculatrice, Calculer $g("""+str(Ant2)+r""")$. Le résultat final doit être présenté sous la forme d'une fraction.
                        \fillwithlines{20mm}
                    \subpart Le point $A("""+str(points_Appart[0])+r"""; """+str(points_Appart[1])+r""")$ appartient-il à la courbe $\mathcal{C}_g$? Justifier votre réponse.
                        \fillwithlines{20mm}
                    \subpart Compléter, à l'aide de la calculatrice, le tableau de valeurs suivant :
                        \begin{center}
                            \begin{tabular}{|c|c|c|c|c|c|c|c|c|}
                            \hline 
                                $x$ & $"""+str(Latex(g_points[0]))+r"""$ & $"""+str(Latex(g_points[1]))+r"""$ & $"""+str(Latex(g_points[2]))+r"""$ & $"""+str(Latex(g_points[3]))+r"""$ & $"""+str(Latex(g_points[4]))+r"""$ & $"""+str(Latex(g_points[5]))+r"""$ & $"""+str(Latex(g_points[6]))+r"""$ & $"""+str(Latex(g_points[7]))+r"""$ \\ 
                            \hline 
                                $g(x)$ &   &   &   &   &   &   &   &   \\
                            \hline 
                            \end{tabular} 
                        \end{center}
                    \subpart On note $\mathcal{C}_g$ la courbe représentative de la fonction $g$. Tracer $\mathcal{C}_g$ dans le repère donné ci-dessus.
                    \subpart Résoudre graphiquement l'équation $f(x)=g(x)$
                        \fillwithlines{20mm}
                \end{subparts}
    \end{parts}
    """
    correction=r"""
    """+identification+r"""
    \Question Lecture Graphique et Étude de fonction\\
       Soit $\mathcal{C}_f$ la représentation graphique d'une fonction $f$ , donnée ci-dessous.
        \begin{center}
            \begin{tikzpicture}[scale=1,cap=round]
                \begin{axis}[
                        axis x line=middle, axis y line=middle,
                        xmin = """+str(xMin-1)+r""", xmax = """+str(xMax+1)+r""",
                        ymin = """+str(yMin-1)+r""", ymax = """+str(yMax+1)+r""",
                        xtick distance = 1, ytick distance = 1,
                        grid = both, minor tick num = 1,
                        major grid style = {gray}, minor grid style = {gray!25},
                        width = \textwidth, height = \textwidth,
                        axis equal image
                    ]
                    \draw[very thick,->] (axis cs:0,0)->(axis cs:1,0) node[below, midway] {$\vect{i}$};
                    \draw[very thick,->] (axis cs:0,0)->(axis cs:0,1) node[left, midway] {$\vect{j}$};
                    \draw (axis cs:0,0) circle node [left, below] {$O$};
                    \addplot[blue, thick, smooth] coordinates {
                        """+points_string+r"""
                    } node[pos=0.05, above, yshift=5pt] {$C_f$};
                    \addplot[red, thick, smooth] coordinates {
                        """+g_points_string+r"""
                    } node[pos=0.05, above, yshift=5pt] {$C_g$};
                \end{axis}
            \end{tikzpicture}
        \end{center}
        \begin{parts}
            \Part Partie A - Étude de la fonction $f$.
                \begin{subparts}
                    \subpart Lire l'ensemble de définition de la fonction $f$.\\
                        \textcolor{red}{
                        Le domaine de définition est $\mathcal{D}_f=] """+str(xMin_val)+r""" ; """+str(xMax_val)+r""" [$
                        }
                    \subpart  Par lecture graphique, quelle est l'image de """+str(point_aleatoire[0])+r""" par la fonction $f$.\\
                        \textcolor{red}{
                        L'image de $"""+str(point_aleatoire[0])+r"""$ par la fonction $f$ est $"""+str(point_aleatoire[1])+r"""$
                        }
                    \subpart  Le point $A("""+str(points_Appart[0])+r""" ; """+str(points_Appart[1])+r""")$ appartient-il à la courbe $\mathcal{C}_f$? Justifier.\\
                        \textcolor{red}{
                        """+Corr1+r"""
                        }
                    \subpart  Déterminer graphiquement, les éventuels antécédents de 0. On laissera apparaitre les traits de construction sur le graphique.\\
                        \textcolor{red}{
                        """+Corr2+r"""
                        }
                \end{subparts}
\clearpage
            \Part B - Étude de la fonction $g$\\
                On considère la fonction $g$ définie sur $\mathcal{D}_g=["""+str(DgMin)+r"""; """+str(DgMax)+r"""]$ par l'expression : $g(x)="""+g_str_latex+r"""$
                \begin{subparts}
                    \subpart Calculer l'image de """+str(Ant1)+r""" par la fonction $g$\\
                        \textcolor{red}{
                            \begin{align*}
                                g("""+str(Ant1)+r""") &= """+latex(Img1)+r"""
                            \end{align*}
                        }
                    \subpart Sans calculatrice, Calculer $g("""+str(Ant2)+r""")$. Le résultat final doit être présenté sous la forme d'une fraction.\\
                        \textcolor{red}{
                            \begin{align*}
                                g("""+str(Ant2)+r""") &= """+latex(Img2)+r"""
                            \end{align*}
                        }
                    \subpart Le point $A("""+str(points_Appart[0])+r"""; """+str(points_Appart[1])+r""")$ appartient-il à la courbe $\mathcal{C}_g$? Justifier votre réponse.
                        \fillwithlines{20mm}
                    \subpart Compléter, à l'aide de la calculatrice, le tableau de valeurs suivant :
                        \begin{center}
                            \begin{tabular}{|c|c|c|c|c|c|c|c|c|}
                            \hline 
                                $x$ & $"""+str(Latex(g_points[0]))+r"""$ & $"""+str(Latex(g_points[1]))+r"""$ & $"""+str(Latex(g_points[2]))+r"""$ & $"""+str(Latex(g_points[3]))+r"""$ & $"""+str(Latex(g_points[4]))+r"""$ & $"""+str(Latex(g_points[5]))+r"""$ & $"""+str(Latex(g_points[6]))+r"""$ & $"""+str(Latex(g_points[7]))+r"""$ \\ 
                            \hline 
                                %$g(x)$ & • & • & • & • & • & • & • & • \\
                                $g(x)$ & $"""+str(Latex(g_Img[0]))+r"""$ & $"""+str(Latex(g_Img[1]))+r"""$ & $"""+str(Latex(g_Img[2]))+r"""$ & $"""+str(Latex(g_Img[3]))+r"""$ & $"""+str(Latex(g_Img[4]))+r"""$ & $"""+str(Latex(g_Img[5]))+r"""$ & $"""+str(Latex(g_Img[6]))+r"""$ & $"""+str(Latex(g_Img[7]))+r"""$ \\
                            \hline
                                $g(x)$ & $"""+f"{round(g_Img_num[0], 2):.2f}"+r"""$ & $"""+f"{round(g_Img_num[1], 2):.2f}"+r"""$ & $"""+f"{round(g_Img_num[2], 2):.2f}"+r"""$ & $"""+f"{round(g_Img_num[3], 2):.2f}"+r"""$ & $"""+f"{round(g_Img_num[4], 2):.2f}"+r"""$ & $"""+f"{round(g_Img_num[5], 2):.2f}"+r"""$ & $"""+f"{round(g_Img_num[6], 2):.2f}"+r"""$ & $"""+f"{round(g_Img_num[7], 2):.2f}"+r"""$ \\ 
                            \hline 
                            \end{tabular} 
                        \end{center}
                    \subpart On note $\mathcal{C}_g$ la courbe représentative de la fonction $g$. Tracer $\mathcal{C}_g$ dans le repère donné ci-dessus.\\
                        Cf la courbe rouge représenté ci-dessus.
                    \subpart Résoudre graphiquement l'équation $f(x)=g(x)$
                        \fillwithlines{20mm}
                \end{subparts}
    \end{parts}
    """

    
    return(exo, correction)

def MilieuEtDistance(id=False):
    if id :
        identification = r"""MilieuEtDistance\\"""
    else:
        identification = r""""""
    xa, ya, xb, yb, xc, yc, xd, yd = symbols('xa,ya,xb,yb,xc,yc,xd,yd')
    
    values = nonEqRandomValue(n=4, debut=-7, fin=-2, tier=False, quart=False, notNull=False)
    xa = random.choice(values)
    ya = random.choice(values)*-1
    values = nonEqRandomValue(n=1, debut=2, fin=7, tier=False, quart=False, notNull=False)
    xb = values[0]
    yb = ya
    xc = xb
    values = nonEqRandomValue(n=1, debut=-7, fin=-2, tier=False, quart=False, notNull=False)
    yc = values[0]
    xd = xa
    yd = yc
    AB = sqrt((xb-xa)**2+(yb-ya)**2)
    AD = sqrt((xd-xa)**2+(yd-ya)**2)
    BD = sqrt((xd-xb)**2+(yd-yb)**2)
    xe = (xa+xc)/2
    ye = (ya+yc)/2
    xf = (xb+xd)/2
    yf = (yb+yd)/2
    exo = r"""
    """+identification+r"""
	\Question Repérage\\
        \textit{\textbf{Rappels :} Soit $A\left(x_a ; y_a\right)$ et $B\left(x_b ; y_b\right)$ deux points du plan \Oij \\
        Dans un repère, les coordonnées du milieu de $[AB]$ sont : $\displaystyle \left( \dfrac{x_a+x_b}{2} ; \dfrac{y_a+y_b}{2} \right)$\\
        Dans un repère orthonormé, la distance $AB$ est égale à : $\displaystyle AB = \sqrt{(x_b-x_a)^2+(y_b-y_a)^2}$ }
        \begin{center}
            \begin{tikzpicture}
                \begin{axis}[					
                    axis x line=middle,
                    axis y line=middle,
                    xmin = -9, xmax = 9,
                    ymin = -9, ymax = 9,
                    xtick distance = 1,
                    ytick distance = 1,
                    grid = both,
                    minor tick num = 1,
                    major grid style = {gray},
                    minor grid style = {gray!25},
                    width = 0.75\textwidth,
                    height = 0.75\textwidth]
                \end{axis}
            \end{tikzpicture}
        \end{center}
        Soient $A$, $B$, $C$ et $D$ les points de coordonnées respectives : $A\left("""+Latex(xa)+r"""; """+Latex(ya)+r"""\right)$, $B\left("""+Latex(xb)+r"""; """+Latex(yb)+r"""\right)$, $C\left("""+Latex(xc)+r"""; """+Latex(yc)+r"""\right)$ et $D\left("""+Latex(xd)+r"""; """+Latex(yd)+r"""\right)$. 
        \begin{parts}
            \Part Placer les points $A$, $B$, $C$ et $D$ dans le repère ci-dessus.
            \Part 
                \begin{subparts}
                    \subpart Calculer les coordonnées de $E$ milieu de $[AC]$.
                    \fillwithlines{15mm}
                    \subpart Calculer les coordonnées de F milieu de $[BD]$.
                    \fillwithlines{15mm}
                    \subpart Que peut en déduire pour la nature du quadrilatère $ABCD$? Justifier votre réponse.
                    \fillwithlines{15mm}

                \end{subparts}
            \Part 
                \begin{subparts}
                        \subpart Calculer la longueur $BD$
                        \fillwithlines{15mm}
\clearpage
                        \subpart On admet que $AB = """+Latex(AB)+r"""$ et $AD = """+Latex(AD)+r"""$. Montrer que le triangle $ABD$ est rectangle en $A$. Montrer que $ABD$ est rectangle en $A$.\\
                        \fillwithlines{20mm}
                        \subpart Que peut-on déduire pour la nature du quadrilatère $ABCD$? Justifier votre réponse.
                        \fillwithlines{10mm}

                \end{subparts}
            \fillwithlines{20mm}
        \end{parts}
    """
    correction = r"""
    """+identification+r"""
	\Question Repérage\\
        \textit{\textbf{Rappels :} Soit $A\left(x_a ; y_a\right)$ et $B\left(x_b ; y_b\right)$ deux points du plan \Oij \\
        Dans un repère, les coordonnées du milieu de $[AB]$ sont : $\displaystyle \left( \dfrac{x_a+x_b}{2} ; \dfrac{y_a+y_b}{2} \right)$\\
        Dans un repère orthonormé, la distance $AB$ est égale à : $\displaystyle AB = \sqrt{(x_b-x_a)^2+(y_b-y_a)^2}$ }
        \begin{center}
            \begin{tikzpicture}
                \begin{axis}[					
                    axis x line=middle,
                    axis y line=middle,
                    xmin = -9, xmax = 9,
                    ymin = -9, ymax = 9,
                    xtick distance = 1,
                    ytick distance = 1,
                    grid = both,
                    minor tick num = 1,
                    major grid style = {gray},
                    minor grid style = {gray!25},
                    width = 0.75\textwidth,
                    height = 0.75\textwidth]
                    \addplot[only marks, red, mark=x] coordinates {("""+str(xa)+r""", """+str(ya)+r""")};
                    \node[label={above left:$A$}] at (axis cs:"""+str(xa)+r""","""+str(ya)+r""") {};
                    \addplot[only marks, red, mark=x] coordinates {("""+str(xb)+r""", """+str(yb)+r""")};
                    \node[label={above right:$B$}] at (axis cs:"""+str(xb)+r""", """+str(yb)+r""") {};
                    \addplot[only marks, red, mark=x] coordinates {("""+str(xc)+r""", """+str(yc)+r""")};
                    \node[label={below right:$C$}] at (axis cs:"""+str(xc)+r""","""+str(yc)+r""") {};
                    \addplot[only marks, red, mark=x] coordinates {("""+str(xd)+r""", """+str(yd)+r""")};
                    \node[label={below left:$D$}] at (axis cs:"""+str(xd)+r""", """+str(yd)+r""") {};
                    % Milieu de AC
                    \addplot[only marks, red, mark=x] coordinates {("""+str(xe)+r""", """+str(ye)+r""")};
                    \node[label={below :$E$}] at (axis cs:"""+str(xe)+r""", """+str(ye)+r""") {};
                    % Milieu de BD
                    \addplot[only marks, red, mark=x] coordinates {("""+str(xf)+r""", """+str(yf)+r""")};
                    \node[label={above :$F$}] at (axis cs:"""+str(xf)+r""", """+str(yf)+r""") {};
                    % Ajout du segment AB
                    \addplot[thick, red] coordinates {("""+str(xa)+r""", """+str(ya)+r""") ("""+str(xb)+r""", """+str(yb)+r""")};
                    % Ajout du segment BC
                    \addplot[thick, red] coordinates {("""+str(xb)+r""", """+str(yb)+r""") ("""+str(xc)+r""", """+str(yc)+r""")};
                    % Ajout du segment CD
                    \addplot[thick, red] coordinates {("""+str(xc)+r""", """+str(yc)+r""") ("""+str(xd)+r""", """+str(yd)+r""")};
                    % Ajout du segment DA
                    \addplot[thick, red] coordinates {("""+str(xd)+r""", """+str(yd)+r""") ("""+str(xa)+r""", """+str(ya)+r""")};
                \end{axis}
            \end{tikzpicture}
        \end{center}
        Soient $A$, $B$, $C$ et $D$ les points de coordonnées respectives : $A\left("""+Latex(xa)+r"""; """+Latex(ya)+r"""\right)$, $B\left("""+Latex(xb)+r"""; """+Latex(yb)+r"""\right)$, $C\left("""+Latex(xc)+r"""; """+Latex(yc)+r"""\right)$ et $D\left("""+Latex(xd)+r"""; """+Latex(yd)+r"""\right)$. 
        \begin{parts}
            \Part Placer les points $A$, $B$, $C$ et $D$ dans le repère ci-dessus.
            \Part 
                \begin{subparts}
                    \subpart Calculer les coordonnées de $E$ milieu de $[AC]$.\\
                    \textcolor{red}{
                        Les coordonnées de $E$ milieu de $[AC]$ sont : $\displaystyle E\left( \dfrac{x_a+x_c}{2} ; \dfrac{y_a+y_c}{2} \right)$\\
                        d'où : $\displaystyle E\left( """+Latex(xe)+r""" ; """+Latex(ye)+r""" \right)$
                    }
                    \fillwithlines{15mm}
                    \subpart Calculer les coordonnées de F milieu de $[BD]$.\\
                    \textcolor{red}{
                        Les coordonnées de $F$ milieu de $[BD]$ sont : $\displaystyle F\left( \dfrac{x_b+x_d}{2} ; \dfrac{y_b+y_d}{2} \right)$\\
                        d'où : $\displaystyle F\left( """+Latex(xf)+r""" ; """+Latex(yf)+r""" \right)$
                    }
                    \fillwithlines{15mm}
                    \subpart Que peut en déduire pour la nature du quadrilatère $ABCD$? Justifier votre réponse.\\
                    \textcolor{red}{
                        On peut en déduire ABCD est un parallèlogramme car les diagonales se coupent en leurs milieu.
                    }
                    \fillwithlines{15mm}

                \end{subparts}
            \Part 
                \begin{subparts}
                        \subpart Calculer la longueur $BD$\\
                    \textcolor{red}{
                        La longueur $BD$ est donnér par : $\displaystyle BD = \sqrt{\left(x_d-x_b\right)^2+\left(y_d-y_b\right)^2}$\\
                        d'où : $\displaystyle BD = \sqrt{\left("""+Latex(xd)+r"""-"""+Latex(xb)+r"""\right)^2+\left("""+Latex(yd)+r"""-"""+Latex(yb)+r"""\right)^2}$ donc $BD = """+Latex(BD)+r"""$ 
                    }
                        \fillwithlines{15mm}
                        \subpart On admet que $AB = """+Latex(AB)+r"""$ et $AD = """+Latex(AD)+r"""$.\\
                        Montrer que le triangle $ABD$ est rectangle en $A$. Montrer que $ABD$ est rectangle en $A$.\\
                        \textcolor{red}{
                            D'après le théorème de Pythagore, le triangle $ABD$ est rectangle en $A$ si : $BD^2 = AB^2 + AD^2$
                            \begin{align*}
                                BD^2 &= \left("""+Latex(BD)+r"""\right)^2 = """+Latex(BD**2)+r"""\\
                                AB^2 + AD^2 &= \left("""+Latex(AB)+r"""\right)^2 + \left("""+Latex(AD)+r"""\right)^2\\
                                            &= """+Latex(AB**2)+r""" + """+Latex(AD**2)+r"""\\
                                            &= """+Latex(AB**2+AD**2)+r"""
                            \end{align*}
                            On a donc $BC^2 = AB^2 + AC^2$, ainsi, d'après le théorème de Pythagore, le triangle $ABD$ est rectangle en A. Son hypoténuse est [BD]. 
                        }
                        \fillwithlines{20mm}
                        \subpart Que peut-on déduire pour la nature du quadrilatère $ABCD$? Justifier votre réponse.
                        \fillwithlines{10mm}

                \end{subparts}
            \fillwithlines{20mm}
        \end{parts}
    """
    return(exo, correction)

def QCMSeconde(n=1, id=False):
    if id :
        identification = r"""QCMSeconde\\"""
    else:
        identification = r""""""
    questions = []
    questions=genQuestionFormeDevelopper(questions, n=1)
    questions=genQuestionFormeFactoriser(questions, n=1)
    questions=genQuestionSurfaceHachuree(questions)

    questions=genQuestionEnsembleNombre(questions)
    parts=r""""""
    partscorrection=r""""""
    nbQuestions = len(questions)
    for q in questions:
        # i = np.random.randint(0,len(questions)-1)
        question=q
        if question[0]=="choice": # Si la question est de type 'choice'
            parts=parts+r"""\Part["""+str(question[1])+r"""] """+question[2]+r"""\\
            \fcolorbox{blue}{white}{
                \begin{oneparcheckboxes}\checkboxchar{$\Box$}
            """
            partscorrection=partscorrection+r"""\Part["""+str(question[1])+r"""] """+question[2]+r"""\\
            \fcolorbox{blue}{white}{
                \begin{oneparcheckboxes}\checkboxchar{$\Box$}
            """
            choices = question[3:]
            theRightOne = False
            for j in range(0,len(choices)):
                k = np.random.randint(0,len(choices))
                if k==0 and not(theRightOne):
                    theRightOne = True
                    parts = parts+r"""
                    \CorrectChoice """+str(choices[k])+r"""
                    """
                    partscorrection = partscorrection+r"""
                    \CorrectChoice \fcolorbox{red}{lightgray}{"""+str(choices[k])+r"""}
                    """
                else:
                    parts = parts+r"""
                    \choice """+str(choices[k])+r"""
                    """
                    partscorrection = partscorrection+r"""
                    \choice """+str(choices[k])+r"""
                    """
                choices.remove(choices[k])
            parts=parts+r"""
                \end{oneparcheckboxes}
            }\\
            \rule{\linewidth}{1pt}
            """
            partscorrection=partscorrection+r"""
                \end{oneparcheckboxes}
            }\\
            \rule{\linewidth}{1pt}
            """
                
        if question[0]=="fillin": # Si la question est de type 'fillin'
            parts=parts+r"""\Part[1] """+question[2].replace( "[]",r"""\fillin[""" + str(question[3]) +r"""]""" )+r"""\\
            \rule{\linewidth}{1pt}
            """
            partscorrection=partscorrection+r"""\Part[1] """+question[2].replace(r"""[]""",r"""\textbf{"""+str(question[3])+r"""}""")+r"""\\
            \rule{\linewidth}{1pt}
            """
        # questions.remove(questions[i])
        
    exo=r"""
    \clearpage
    """+identification+r"""
        \Question Dans ce questionnaire à choix multiple, cocher la bonne réponse (1 bonne réponse par question)
            \begin{parts}
            """+parts+r"""
            \end{parts}
    """
    correction=r"""
    \clearpage
    """+identification+r"""
        \Question Dans ce questionnaire à choix multiple, cocher la bonne réponse (1 bonne réponse par question)
            \begin{parts}
            """+partscorrection+r"""
            \end{parts}
    """
    return(exo, correction)



    
    return(exo, correction)
    
def simplificationRacine(id=False):
    if id :
        identification = r"""simplificationRacine\\"""
    else:
        identification = r""""""
    
    exo = r""""""+identification
    correction = r""""""+identification
    
    a, b, c, d = symbols('a,b,c,d')
    alpha, beta = symbols('alpha,beta')
    liste1 = [2, 3, 5, 6, 7, 11]
    # Choisir un nombre au hasard
    nombres_au_hasard = random.sample(liste1, 4)
    a = nombres_au_hasard[0]
    b = nombres_au_hasard[1]
    c = nombres_au_hasard[2]
    d = nombres_au_hasard[3]
    alpha = random.randint(2,5)
    beta = random.randint(2,5)
    Q = f"A=\\sqrt{{{a*b**2}}}-{alpha}\\sqrt{{{a*c**2}}}+{beta}\\sqrt{{{a}}}+\\sqrt{{{a*d**2}}}"
    Q0 = f"		A   &=\\sqrt{{{a*b**2}}}-{alpha}\\sqrt{{{a*c**2}}}+{beta}\\sqrt{{{a}}}+\\sqrt{{{a*d**2}}}"
    Q1 = f"			&=\\sqrt{{{a}\\times {b**2}}}-{alpha}\\sqrt{{{a}\\times {c**2}}}+{beta}\\sqrt{{{a}}}+\\sqrt{{{a}\\times {d**2}}}"
    Q2 = f"			&=\\sqrt{{{a}\\times {b}^2}}-{alpha}\\sqrt{{{a}\\times {c}^2}}+{beta}\\sqrt{{{a}}}+\\sqrt{{{a}\\times {d}^2}}"
    Q3 = f"			&=\\sqrt{{{a}}}\\times \\sqrt{{{b}^2}}-{alpha}\\sqrt{{{a}}}\\times \\sqrt{{{c}^2}}+{beta}\\sqrt{{{a}}}+\\sqrt{{{a}}}\\times \\sqrt{{{d}^2}}"
    Q4 = f"			&={b}\\sqrt{{{a}}}-{alpha*c}\\sqrt{{{a}}}+{beta}\\sqrt{{{a}}}+{d}\\sqrt{{{a}}}"
    Q5 = f"			&={b-alpha*c+beta+d}\\sqrt{{{a}}}"
    
    QQ = f"C=\\left({b}\\sqrt{{{c}}}-{d}\\right)\\left({b}\\sqrt{{{c}}}+{d}\\right)"
    QQ0 = f"		C   &=\\left({b}\\sqrt{{{c}}}-{d}\\right)\\left({b}\\sqrt{{{c}}}+{d}\\right)"
    QQ1 = f"			&={b}\\sqrt{{{c}}}\\times{b}\\sqrt{{{c}}}+{b}\\sqrt{{{c}}}\\times{d}-{d}\\times{b}\\sqrt{{{c}}}-{d}\\times{d}"
    QQ2 = f"			&={c*b**2-d**2}"
 
    exo = exo +r"""
    \Question Simplifiez les expressions suivantes :\\
        \begin{enumerate}
            \item $"""+Q+r"""$
                \fillwithlines{32mm}
            \item $B=\left(\sqrt{2}+2\right)^2$
                \fillwithlines{20mm}
            \item $"""+QQ+r"""$
                \fillwithlines{32mm}
        \end{enumerate}
"""
    correction = correction +r"""
    \Question Simplifiez les expressions suivantes :\\
        \begin{enumerate}
            \item $"""+Q+r"""$
                \color{red}
                \begin{align*}
"""+Q0+r"""\\
"""+Q1+r"""\\
"""+Q2+r"""\\
"""+Q3+r"""\\
"""+Q4+r"""\\
"""+Q5+r"""
                \end{align*}	
                \color{black}
            \item $B=\left(\sqrt{2}+2\right)^2$
                \color{red}
                \begin{align*}
                B   &=\left(\sqrt{"""+str(beta)+r"""}+"""+str(beta)+r"""\right)^2\\
                    &=\left(\sqrt{"""+str(beta)+r"""}+"""+str(beta)+r"""\right)\times\left(\sqrt{"""+str(beta)+r"""}+"""+str(beta)+r"""\right)\\
                    &=\sqrt{"""+str(beta)+r"""}\times\sqrt{"""+str(beta)+r"""}+\sqrt{"""+str(beta)+r"""}\times """+str(beta)+r"""+"""+str(beta)+r"""\times\sqrt{"""+str(beta)+r"""}+"""+str(beta)+r"""\times """+str(beta)+r"""\\
                    &="""+str(beta)+r"""+2\times """+str(beta)+r"""\times \sqrt{"""+str(beta)+r"""}+"""+str(beta**2)+r"""\\
                    &="""+str(beta+beta**2)+r"""+"""+str(2*beta)+r"""\sqrt{"""+str(beta)+r"""}
                \end{align*}
                \color{black}
            \item $"""+QQ+r"""$
                \color{red}
                \begin{align*}
"""+QQ0+r"""\\
"""+QQ1+r"""\\
"""+QQ2+r"""
                \end{align*}	
                \color{black}
        \end{enumerate}
"""
    return(exo, correction)

def unSeulRadical(id=False):
    if id :
        identification = r"""simplificationRacine\\"""
    else:
        identification = r""""""
    
    exo = r""""""+identification
    correction = r""""""+identification
    a, b, c = symbols('a,b,c')
    alpha, beta = symbols('alpha,beta')
    liste1 = [2, 3, 5, 6, 7, 11]
    values = nonEqRandomValue(n=3, debut=2, fin=7, demi=False, tier=False, quart=False, notNull=True)
    a = values[0]
    b = values[1]
    c = values[2]
    alpha = a**2+c*b**2
    beta = 2*a*b*sqrt(c)
    X = f"""{a}-{b}\sqrt{{{c}}}"""
    Y = f"""{a}+{b}\sqrt{{{c}}}"""
    print(X)
    print(Y)
    
    exo = exo + r"""
        \Question On donne $a="""+X+r"""$ et $b="""+Y+r"""$
            \begin{enumerate}
                \item Calculez $a\times b$. Que peut-on en déduire ?
                    \fillwithlines{32mm}
                \item Calculez $a^2$, $b^2$ et $\dfrac{a}{b}$
                    \fillwithlines{40mm}
                \item Vérifiez que $\dfrac{a}{b}+\dfrac{b}{a}$ est un entier naturel.
                    \fillwithlines{32mm}
                \item Soit $\displaystyle X=\sqrt{\left("""+str(a**2+c*b**2)+r"""-"""+str(2*a*b)+r"""\sqrt{"""+str(c)+r"""}\right)}$ et $\displaystyle Y=\sqrt{\left("""+str(a**2+c*b**2)+r"""+"""+str(2*a*b)+r"""\sqrt{"""+str(c)+r"""}\right)}$\\
                    Écrivez $X$ et $Y$ avec un seul radical
                    \fillwithlines{40mm}
            \end{enumerate}"""
    correction = exo
    return(exo,correction)

def variationEtLectureGraphique(id=False):
    if id :
        identification = r"""variationEtLectureGraphique\\"""
    else:
        identification = r""""""
        
    fonctions = [
        {
            "name": "f", # nom de la fonction
            "x": [-7, -5, -3, -1,  0,  2], # mettre les 6 x en ordre croissant
            "y": [-4,  0,  1,  2,  1,  0]  # mettre les 6 y en fonction des x
        },
        {
            "name": "g", # nom de la fonction
            "x": [-7, -5, -4, -2,  0,  1], # mettre les 6 x en ordre croissant
            "y": [-1,  0,  1,  2,  3,  0]  # mettre les 6 y en fonction des x
        }
        ]
    fonction_choisie = random.choice(fonctions)
    foncName = fonction_choisie['name']
    x = fonction_choisie['x']
    y = fonction_choisie['y']
    xForTab = "& "+" & ".join(f"${xi}$" for xi in x)
    coordonnees = " ".join(f"({xi},{yi})" for xi, yi in zip(x, y))
    exo=identification+r"""
    \Question Lecture Graphique et Étude de fonction\\
       Soit $\mathcal{C}_"""+foncName+r"""$ la représentation graphique d'une fonction $"""+foncName+r"""$ sur l'intervalle $[-9;9]$, donnée ci-dessous.
        \begin{multicols}{2}
	        \begin{enumerate}
	        		\item Complétez le tableau de valeurs de $"""+foncName+r"""$:\\
	        		\begin{tabular}{|c|c|c|c|c|c|c|}
                            \hline
                                $x$    """+xForTab+r""" \\
                            \hline
                                $"""+foncName+r"""(x)$ &  &  &  &  &  &  \\
                            \hline
                            \end{tabular}
	        		\item Dressez le tableau de variations de $"""+foncName+r"""$:\\•
	        			\begin{tikzpicture}[scale=0.70]
					   \tkzTabInit{$x$ / 1 , $"""+foncName+r"""(x)$ / 3}{$ $, $ $, $ $}
					\end{tikzpicture}
	        		\item Résoudre graphiquement $"""+foncName+r"""(x)\ge 1$
	        \end{enumerate}
	            \begin{tikzpicture}[scale=0.5,cap=round]
	                \begin{axis}[
	                        axis x line=middle, axis y line=middle,
	                        xmin = -9, xmax = 9,
	                        ymin = -5, ymax = 5,
	                        xtick distance = 1, ytick distance = 1,
	                        grid = both, minor tick num = 1,
	                        major grid style = {gray}, minor grid style = {gray!25},
	                        width = \textwidth, height = \textwidth,
	                        axis equal image
	                    ]
	                    \draw[very thick,->] (axis cs:0,0)->(axis cs:1,0) node[below, midway] {$\vect{i}$};
	                    \draw[very thick,->] (axis cs:0,0)->(axis cs:0,1) node[left, midway] {$\vect{j}$};
	                    \draw (axis cs:0,0) circle node [left, below] {$O$};
	                    \addplot[blue, thick, smooth] coordinates {
	                        """+coordonnees+r"""
	                    } node[pos=0.05, above, yshift=5pt] {$C_"""+foncName+r"""$};
	                \end{axis}
	            \end{tikzpicture}
        \end{multicols}"""
    correction=identification+r""""""
    return(exo,correction)
    



def main():
    exo,correction=variationEtLectureGraphique()

    print(exo)
    pass

if __name__ == '__main__':
    main()