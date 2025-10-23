import os,sys
import random
import unicodedata
import numpy as np
from sympy import *
import matplotlib.pyplot as plt
from fractions import Fraction

from baseMaths import *



def addClearPage():
    """This function adds a clear page command in LaTeX."""
    exo=r"""
\clearpage
"""
    correction = r"""
\clearpage
"""
    return(exo,correction)

def coeffPoly3Deg(genCode="9999999999"):
    """
    This Python function generates coefficients for a third-degree polynomial, plots the polynomial, and
    saves the plot as an image file.
    
    :param genCode: The `genCode` parameter is a string that represents a generated code used for naming
    the output file. In the provided function `coeffPoly3Deg`, this code is used to save a plot as a PNG
    file with a specific name, defaults to 9999999999 (optional)
    :return: The function `coeffPoly3Deg` returns a list containing the coefficients of a third-degree
    polynomial equation, the constant term, and the file path where the plot of the polynomial function
    is saved. The list has the following structure: `[aa, bb, cc, dd, filepath]`.
    """
    directory = os.path.dirname(__file__)
    xa = 2+np.random.randint(1,3)*3
    ya = 0.0
    xc = 6+np.random.randint(1,3)*2
    yc = 0.0
    xb = (xa+xc)/2.0
    yb = -2.0
    A = np.array([[xa**2,xa,1], [xb**2,xb,1], [xc**2,xc,1]], dtype=float)
    B = np.array([ya,yb,yc], dtype=float)

    sol = np.linalg.solve(A, B)
    dd = np.random.randint(10,15)
    x = np.linspace(0, 15, 30)
    y = (sol[0]*x**3)/3+(sol[1]*x**2)/2+sol[2]*x+dd
    plt.plot(x, y)
    plt.xlim(0,20)
    plt.ylim(-0.5,40)
    plt.title("Coût en fonction de la quantité",fontsize=14)
    plt.xlabel("Quantité -> x",fontsize=12)
    plt.ylabel("Coût -> C(x)",fontsize=12)
    plt.savefig(directory+"\\"+genCode+'-fig1.png')
    plt.show() # affiche la figure a l'ecran
    aa = (sol[0])/3
    bb = (sol[1])/2
    cc = sol[2]
    sol = [aa, bb, cc, dd, directory+"\\"+genCode+'-fig1.png']
    return(sol)

def header(eleve="Non listé", titre="", genCode="0000000000", Correction="Sujet", duree="2 heures", level="TSTMG", points=18, bonus=2, consignes=[]):
    cons=r"""
        
    """
    for c in consignes:
        cons = cons + r"""
            \item """+c+r"""
        """
    header=r"""

%!TEX encoding = UTF-8 Unicode
% !TEX TS-program = lualatex
\documentclass[12pt,%
addpoints,%
%answers%
]{exam}
\usepackage{tikz,tkz-tab, tkz-base}
\usepackage{tkz-euclide}
%\tikzset{every picture/.style={execute at begin picture={\shorthandoff{:;!?};}}}
\tikzstyle{every picture}+=[remember picture]
\tikzstyle{na} = [shape=rectangle,inner sep=0pt]

%\usepackage[french]{babel}
%\addto\extrasfrench{\shorthandoff{:}}
\usepackage{pgfplots}
\pgfplotsset{every tick label/.append style={font=\tiny}}
\usepackage{multicol}
\usepackage{xcolor}
%--------------------------------------------------------------------------------------
\usepackage{mathtools}
\usepackage{enumerate}
\usepackage{fourier}
\usepackage{xspace}
\usepackage{amsmath,amssymb,amstext,makeidx}
\usepackage{fancybox}
\usepackage{tabularx}
\usepackage[normalem]{ulem}
\usepackage{pifont}
\usepackage[euler]{textgreek}
\usepackage{textcomp,enumitem}
\newcommand{\euro}{\eurologo{}}
%\usepackage{pst-plot,pst-tree,pst-func,pstricks-add}
\newcommand{\R}{\mathbb{R}}
\newcommand{\N}{\mathbb{N}}
\newcommand{\D}{\mathbb{D}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\C}{\mathbb{C}}
\usepackage[left=3.5cm, right=3.5cm, top=1.9cm, bottom=2.4cm]{geometry}
\newcommand{\vect}[1]{\overrightarrow{\,\mathstrut#1\,}}
\renewcommand{\theenumi}{\textbf{\arabic{enumi}}}
\renewcommand{\labelenumi}{\textbf{\theenumi.}}
\renewcommand{\theenumii}{\textbf{\alph{enumii}}}
\renewcommand{\labelenumii}{\textbf{\theenumii.}}
\def\Oij{$\left(\text{O}~;~\vect{\imath},~\vect{\jmath}\right)$}
\def\Oijk{$\left(\text{O}~;~\vect{\imath},~\vect{\jmath},~\vect{k}\right)$}
\def\Ouv{$\left(\text{O}~;~\vect{u},~\vect{v}\right)$}

\definecolor{aliceblue}{rgb}{0.94, 0.97, 1.0}
\usepackage{numprint}
\renewcommand\arraystretch{1.1}
\newcommand{\e}{\text{e}}
%\frenchbsetup{StandardLists=true}
%\usepackage{babel}
\usepackage{enumerate}
%---Pour les arbres de probabilités----------------------------------------------------
\usepackage{pstricks,pst-node,pst-tree}
\usepackage{pst-plot,pst-tree,pst-func,pstricks-add}
\usepackage{graphicx}
\usepackage{fancybox}
\usepackage{tabularx}
%---Définition de la page et des marges------------------------------------------------
\setlength{\paperheight}{297mm}
\setlength{\paperwidth}{210mm}
\setlength{\textheight}{27cm}
\setlength{\textwidth}{16cm}
\setlength{\leftmargin}{-1cm}%
\setlength{\rightmargin}{1cm}%
%---Définition de l'entête de page et du pied de page----------------------------------
\pagestyle{headandfoot}
\firstpageheader{\parbox{2cm}{Nom : \\ Prénom :}}
  {}
  {\parbox{2cm}{classe : """+level+r""" \\ Date : \today}}
\firstpagefooter{\tiny{Lycée Léonard De Vinci à Tremblay en France}}{Page \thepage\ / \numpages}{\tiny\parbox{2cm}{"""+eleve+r"""} \\Session 2024-25}
\runningheadrule
\runningfootrule
\lhead{\parbox{2cm}{Nom : \\ Prénom :}}
\chead{"""+titre+r"""\\ \small{"""+Correction+r""" - genCode : """+genCode+r"""}}
\rhead{}
\runningfooter{\tiny{Lycée Léonard De Vinci à Tremblay en France}}{Page \thepage\ / \numpages}{\tiny\parbox{2cm}{"""+eleve+r"""} \\Session 2024-25}

%---Définition de Question-------------------------------------------------------------
\def\Question{	
    \renewcommand*{\questionlabel}{\fbox{Exercice \thequestion : }}
    \question
}
\def\Part{
    \renewcommand*{\partlabel}{\fbox{\thepartno : }}
    \part
}
%--------------------------------------------------------------------------------------

%\usepackage{xparse,xpatch}
% redefine \part command to be \mypart
\appto\parts{\let\exampart\part\let\part\mypart}

\def\multiplechoice{54}
\def\freeresponse{46}
\makeatletter
\ExplSyntaxOn
% this will become a sequence of the part numbers and scores
% like: 1a&10&, 1b&8&, 1c&9&, 2a&6, 2b&8&, 3&12&, 4&14&, ...
\seq_new:N \g_part_scores_seq
\tl_new:N \g_grade_table_tl

\int_new:N \g_total_score_int% this will be the exam score
\int_new:N \g_number_of_scores_int
\NewDocumentCommand\mypart{o}{
  \IfNoValueTF{#1}{\exampart}{
    % don't do anything special inside solutions
    \if@insolution\exampart[#1]
    \else\exampart[#1]
      % store both the part number and score in \g_part_scores_seq
      % together with their column separators for the tabular env
      \tl_set:Nx \l_tmpa_tl { \arabic{question}\alph{partno} }
      \tl_put_right:Nn \l_tmpa_tl {&}
      \tl_put_right:No \l_tmpa_tl {#1}
      \tl_put_right:Nn \l_tmpa_tl {&}
      \seq_gput_right:No \g_part_scores_seq \l_tmpa_tl
      % increment the running total and number of scores
      \int_gadd:Nn \g_total_score_int {#1}
      \int_gincr:N \g_number_of_scores_int
    \fi
  }
}
% print row #1 of the part scores in the grade table
\cs_new:Nn \__add_row_to_grade_table:n {
   \tl_gput_right:Nx \g_grade_table_tl {\seq_item:Nn \g_part_scores_seq {#1}}
   \tl_gput_right:Nn \g_grade_table_tl { & }
   \tl_gput_right:Nx \g_grade_table_tl {\seq_item:Nn \g_part_scores_seq {#1+\g_number_of_scores_int/2}}
   \tl_gput_right:Nn \g_grade_table_tl {\\\hline}
}
\NewDocumentCommand\GradeTable{}{% the new grade table
  % we need an exam number of scores so add two
  % empty cells if we have an odd number
  \int_if_odd:nT {\g_number_of_scores_int} {
      \seq_gput_right:Nn \g_part_scores_seq {&}
      \int_ginc:N \g_number_of_scores_int
  }
  \int_gset:Nn \g_number_of_scores_int {\g_number_of_scores_int}
  \int_gadd:Nn \g_total_score_int { \multiplechoice }
  \int_gadd:Nn \g_total_score_int { \freeresponse }
  % create the grade table
  \tl_gclear:N \g_grade_table_tl
  \int_step_function:nnN {1} {\g_number_of_scores_int/2} \__add_row_to_grade_table:n
  \begin{tabular}{|c|c|c|c|c|c|}\hline
    Question & Points~Possibles & Points~Acquis & Question & Points~Possibles & Points~Acquis \\\hline
    \tl_use:N \g_grade_table_tl
    \multicolumn2{c|}{}&\multicolumn{2}{r|}{\textit{Total}}
        & \int_use:N \g_total_score_int & \\\cline{3-6}
  \end{tabular}
}
\ExplSyntaxOff
\makeatother
%-------------------------------------------------------------------------------------


\hsword{Score:}
\usepackage{lipsum}
\usepackage{mdframed}
\renewenvironment{solution}
{\begingroup\par\parshape0%
\begin{mdframed}[%skipabove=\baselineskip,
%                 innertopmargin=\baselineskip,
%                 innerbottommargin=\baselineskip,
                 userdefinedwidth=\textwidth,
                 backgroundcolor=blue!5]
\textbf{Solution:}\enspace\ignorespaces}
{\end{mdframed}\par\endgroup}

\newcommand*{\Coord}[3]{% 
  \ensuremath{\overrightarrow{#1}\, 
    \begin{pmatrix} 
      #2\\ 
      #3 
    \end{pmatrix}}}

\newcommand*{\Point}[3]{%
    \ensuremath{#1\, 
        \begin{pmatrix} 
            #2\\ 
        #3 
        \end{pmatrix}
    }
}

\usepackage[french]{algorithm2e}%pseudocode

\usepackage{scratch3}
\usepackage{chemfig}

\renewcommand{\thepartno}{\arabic{partno}}
\renewcommand{\thesubpart}{\thepartno.\alph{subpart}}
\renewcommand{\thesubsubpart}{\thesubpart.\arabic{subsubpart}}


\newcolumntype{R}[1]{>{\raggedleft\arraybackslash }b{#1}}
\newcolumntype{L}[1]{>{\raggedright\arraybackslash }b{#1}}
\newcolumntype{C}[1]{>{\centering\arraybackslash }b{#1}}

\setlength{\arrayrulewidth}{1pt}

\begin{document}

\begin{titlepage}

\newcommand{\HRule}{\rule{\linewidth}{0.5mm}} 							% horizontal line and its thickness
\center 
 
% University
\textsc{\LARGE Lycée polyvalent Léonard de Vinci}\\[1cm]

% Document info
\textsc{\Large """+titre+r"""\\ \small{"""+Correction+r""" genCode : """+genCode+r"""}}\\[5cm]
\textsc{\large """+eleve+r"""}\\[1cm] 										% Course Code
\HRule \\[0.8cm]
{ \huge \bfseries Mathématiques}\\[0.7cm]								% Assignment
\HRule \\[5cm]
\large
\emph{Consignes:}\\%[1.5cm]													% Author info
\fbox{%
\begin{minipage}{\textwidth}
   \begin{itemize}[label=$*$]
"""+cons+r"""
        \item L'examen est noté sur un total de """+str(points+bonus)+r""" points ("""+str(points)+r"""+"""+str(bonus)+r""" bonus).
        \item L'épreuve dure """+duree+r""".
    \end{itemize}
\end{minipage}
}

\vfill 
\end{titlepage}

\clearpage

\begin{questions}
"""
    return(header)

def ender(rappel=False):
    if rappel :
        exo=r"""
        \end{questions}
        """+rappelTSTMG()+"""
    \end{document}
        """
    else:
        exo=r"""
        \end{questions}

    \end{document}
        """
    return(exo)

def exoSecondDegreSansDelta(genCode="9999999999", id=False):
    if id :
        identification = r"""exoDerivation\\"""
    else:
        identification = r""""""
    laFunction = gen2ndDeg2Roots()
    x = symbols('x')
    a = laFunction['a']
    b = laFunction['b']
    c = laFunction['c']
    x1 = laFunction['x1']
    x2 = laFunction['x2']
    x1_string = latex(x1).replace('\\frac','\\dfrac')
    x2_string = latex(x2).replace('\\frac','\\dfrac')
    f = laFunction['f']
    # print(f)
    f_string = latex(f).replace('\\frac','\\dfrac')
    f1 = laFunction['f1']
    # print(f1)
    f1_string = latex(f1).replace('\\frac','\\dfrac')
    f2 = laFunction['f2']
    # print(f2)
    f_args0 = f1.args[0]
    f01 = f_args0.args[0]
    f00 = f_args0.args[1]
    f_args1 = f1.args[1]
    f11 = f_args1.args[0]
    f10 = f_args1.args[1]
    sol1 = solve(f_args0,x)
    sol2 = solve(f_args1,x)
    f2_string = latex(f2).replace('\\frac','\\dfrac')
    if a>0:
        variation = r"""{ +/$+\infty$, R/ , -/$"""+Latex(f.subs(x,-b/(2*a)))+r"""$, R/ , +/$+\infty$}"""
        signe = r"""{, + , z ,  , - , , z , + ,}"""
    else:
        variation = r"""{ -/$-\infty$, R/ , +/$"""+Latex(f.subs(x,-b/(2*a)))+r"""$, R/ , -/$-\infty$}"""
        signe = r"""{, - , z ,  , + , , z , - ,}"""
    exo=r"""
    \clearpage
    """+identification+r"""
        \Question Soit $f$ une fonction définie par $"""+f_string+r"""$
            \begin{parts}	
                \Part[4] Montrer que $f(x) = """+f1_string+r"""$
					\fillwithlines{50mm}
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
                            height = \textwidth]
                            \addplot[
                                domain = -10:10,
                                samples = 50,
                                smooth,
                                thick,
                                blue,
                            ] {"""+str(a.evalf(2))+r"""*x*x+"""+str(b.evalf(2))+r"""*x+"""+str(c.evalf(2))+r"""};
                        \end{axis}
                    \end{tikzpicture}
                \end{center}
                \Part[4] Résoudre $f(x)=0$
					\fillwithlines{70mm}
                \Part[4] Compléter le tableau de signe et variations de $f$ ci-dessous
                    \begin{center}
                        \begin{tikzpicture}
                            \tkzTabInit %[lgt=3]
                                {$x$ / 1 , Signe de $f$ / 1, Variations de $f$ / 3 }
                                {$+\infty$, $"""+Latex(min(x1,x2))+r"""$, $"""+Latex(-b/(2*a))+r"""$, $"""+Latex(max(x1,x2))+r"""$, $+\infty$}
                            \tkzTabLine
                                {, , ,  , , , , ,}
                            \tkzTabVar
                                { ,  , ,  , }
    %                        \tkzTabIma{1}{3}{2}{0}
    %                        \tkzTabIma{3}{5}{4}{0}
    %						\tkzTabVal[draw]{1}{3}{0.5}{$0$}{$-e$}
    %						\tkzTabTan{1}{3}{3}{\tiny{$f("""+Latex(-b/(2*a))+r""")$}}
                        \end{tikzpicture}
                    \end{center}
                \end{parts}
    """
    correction=r"""
    \clearpage
    """+identification+r"""
            \Question Soit $f$ une fonction définie par $"""+f_string+r"""$
            \begin{parts}	
                \Part Montrer que $f(x) = """+f1_string+r"""$
%					\fillwithlines{30mm}
                    Il suffit de développer et simplifier l'expression de $f$\\
                    \begin{solution}
                        on développe et simplifie $f(x) = """+f1_string+r"""$ :\\
                        \begin{align*}
                            f(x)&="""+f1_string+r"""\\
                                &="""+latex(f00)+r"""\times """+latex(f10)+r""" + """+latex(f00)+r"""\times """+latex(f11)+r""" + """+latex(f01)+r"""\times """+latex(f10)+r""" + """+latex(f01)+r"""\times """+latex(f11)+r"""\\
                                &="""+latex(f00*f10)+r""" + """+latex(f00*f11)+r""" + """+latex(f01*f10)+r""" + """+latex(f01*f11)+r"""\\
                                &="""+f_string+r"""
                        \end{align*}
                    \end{solution}
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
                            height = \textwidth]
                            \addplot[
                                domain = -10:10,
                                samples = 50,
                                smooth,
                                thick,
                                blue,
                            ] {"""+str(a.evalf(2))+r"""*x*x+"""+str(b.evalf(2))+r"""*x+"""+str(c.evalf(2))+r"""};
                        \end{axis}
                    \end{tikzpicture}
                \end{center}
                \Part Résoudre $f(x)=0$
%					\fillwithlines{70mm}
                \\ En utilisant $f(x)="""+f1_string+r"""$, on a :\\
                    \begin{align*}
                                            f(x) &= 0\\
                        \Leftrightarrow """+f1_string+r""" &= 0
                    \end{align*}
    On a donc une équation 'produit' d'où :
                    \begin{align*}
                        \Leftrightarrow 
                            \begin{cases}
                                """+latex(f_args0)+r""" &= 0 \\
                                """+latex(f_args1)+r""" &= 0
                            \end{cases}
                        \Leftrightarrow 
                            \begin{cases}
                                x = """+latex(sol1[0])+r""" \\
                                x = """+latex(sol2[0])+r"""
                            \end{cases}
                    \end{align*}
    Donc $f(x)=0$ admet pour ensemble de solution $S=\lbrace"""+latex(min(sol1[0],sol2[0]))+r""";"""+latex(max(sol1[0],sol2[0]))+r"""\rbrace$
                \Part Compléter le tableau de signe et variations de $f$ ci-dessous
                    \begin{center}
                    \begin{tikzpicture}
                        \tkzTabInit %[lgt=3]
                            {$x$ / 1 , Signe de $f$ / 1, Variations de $f$ / 3 }
                            {$+\infty$, $"""+latex(min(x1,x2)).replace('\\frac','\\dfrac')+r"""$, $"""+latex(-b/(2*a)).replace('\\frac','\\dfrac')+r"""$, $"""+latex(max(x1,x2)).replace('\\frac','\\dfrac')+r"""$, $+\infty$}
                        \tkzTabLine
                            """+signe+r"""
                        \tkzTabVar
                            """+variation+r"""
                        \tkzTabIma{1}{3}{2}{0}
                        \tkzTabIma{3}{5}{4}{0}
%						\tkzTabVal[draw]{1}{3}{0.5}{$0$}{$-e$}
%						\tkzTabTan{1}{3}{3}{\tiny{$f("""+latex(-b/(2*a)).replace('\\frac','\\dfrac')+r""")$}}
                    \end{tikzpicture}
                \end{center}
            \end{parts}
    """

    return(exo,correction)

def exoVecteurN0(id=False):
    """
    This function generates a LaTeX exercise and its correction for placing points and representing vectors in
    an orthonormal coordinate system.
    :param id: The `id` parameter is a boolean flag that determines whether to include an identification
    string in the generated LaTeX code. If `id` is set to `True`, the identification string
    `exoVecteurN0\` will be included at the beginning of the exercise and correction sections. If `id` is
    set to `False`, no identification string will be included. This parameter allows for optional
    identification of the exercise in the generated LaTeX document.
    :return: The function `exoVecteurN0` returns two strings: `exo` and `correction`. Both strings contain
    LaTeX code for an exercise and its corresponding correction, respectively. The exercise involves
    placing points and representing vectors in an orthonormal coordinate system, while the correction
    provides the same information for reference.
    """
    if id:
        identification = r"""exoVecteurN0\\"""
    else:
        identification = r""""""
    alpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    letters = random.sample(alpha, 6)
    letters.sort()
    x0 = np.random.randint(-6,6)
    y0 = np.random.randint(-6,6)
    x1 = np.random.randint(-6,6)
    y1 = np.random.randint(-6,6)
    x2 = np.random.randint(-6,6)
    y2 = np.random.randint(-6,6)
    x3 = np.random.randint(-6,6)
    y3 = np.random.randint(-6,6)
    x4 = np.random.randint(-6,6)
    y4 = np.random.randint(-6,6)
    x5 = np.random.randint(-6,6)
    y5 = np.random.randint(-6,6)

    exo=r"""
    """+identification+r"""
        \Question Dans le repère orthonormé ci-dessous,
            \begin{parts}
                \Part[6] Placez les points suivants :
                    \begin{multicols}{3}
                        \begin{enumerate}
                            \item $\Point{"""+letters[0]+r"""}{"""+str(x0)+r"""}{"""+str(y0)+r"""}$
                            \item $\Point{"""+letters[1]+r"""}{"""+str(x1)+r"""}{"""+str(y1)+r"""}$
                            \item $\Point{"""+letters[2]+r"""}{"""+str(x2)+r"""}{"""+str(y2)+r"""}$
                            \item $\Point{"""+letters[3]+r"""}{"""+str(x3)+r"""}{"""+str(y3)+r"""}$
                            \item $\Point{"""+letters[4]+r"""}{"""+str(x4)+r"""}{"""+str(y4)+r"""}$
                            \item $\Point{"""+letters[5]+r"""}{"""+str(x5)+r"""}{"""+str(y5)+r"""}$
                        \end{enumerate}
                    \end{multicols}
                \Part[6] Représentez les vecteurs suivants :
                    \begin{multicols}{3}
                        \begin{enumerate}
                            \item $\vect{"""+letters[0]+letters[1]+r"""}$
                            \item $\vect{"""+letters[2]+letters[3]+r"""}$
                            \item $\vect{"""+letters[4]+letters[5]+r"""}$
                            \item $\vect{"""+letters[0]+letters[2]+r"""}$
                            \item $\vect{"""+letters[1]+letters[3]+r"""}$
                            \item $\vect{"""+letters[3]+letters[5]+r"""}$
                        \end{enumerate}
                    \end{multicols}
            \end{parts}
            \begin{center}
                \begin{tikzpicture}
                    \begin{axis}[
                            axis x line=middle, axis y line=middle,
                            xmin = -10, xmax = 10,
                            ymin = -10, ymax = 10,
                            xtick distance = 1, ytick distance = 1,
                            grid = both, minor tick num = 1,
                            major grid style = {gray}, minor grid style = {gray!25},
                            width = \textwidth, height = \textwidth
                            ]
                        \draw[very thick,->] (axis cs:0,0)->(axis cs:1,0) node[below, midway] {$\vect{i}$};
                        \draw[very thick,->] (axis cs:0,0)->(axis cs:0,1) node[left, midway] {$\vect{j}$};		
                        \draw (axis cs:0,0) circle node [left, below] {$O$};
                    \end{axis}

                \end{tikzpicture}
            \end{center}
    \clearpage
    """
    correction=r"""
    """+identification+r"""
        \Question Dans le repère orthonormé ci-dessous,
            \begin{parts}
                \Part[6] Placez les points suivants :
                    \begin{multicols}{3}
                        \begin{enumerate}
                            \item $\Point{"""+letters[0]+r"""}{"""+str(x0)+r"""}{"""+str(y0)+r"""}$
                            \item $\Point{"""+letters[1]+r"""}{"""+str(x1)+r"""}{"""+str(y1)+r"""}$
                            \item $\Point{"""+letters[2]+r"""}{"""+str(x2)+r"""}{"""+str(y2)+r"""}$
                            \item $\Point{"""+letters[3]+r"""}{"""+str(x3)+r"""}{"""+str(y3)+r"""}$
                            \item $\Point{"""+letters[4]+r"""}{"""+str(x4)+r"""}{"""+str(y4)+r"""}$
                            \item $\Point{"""+letters[5]+r"""}{"""+str(x5)+r"""}{"""+str(y5)+r"""}$
                        \end{enumerate}
                    \end{multicols}
                \Part[6] Représentez les vecteurs suivants :
                    \begin{multicols}{3}
                        \begin{enumerate}
                            \item $\vect{"""+letters[0]+letters[1]+r"""}$
                            \item $\vect{"""+letters[2]+letters[3]+r"""}$
                            \item $\vect{"""+letters[4]+letters[5]+r"""}$
                            \item $\vect{"""+letters[0]+letters[2]+r"""}$
                            \item $\vect{"""+letters[1]+letters[3]+r"""}$
                            \item $\vect{"""+letters[3]+letters[5]+r"""}$
                        \end{enumerate}
                    \end{multicols}
            \end{parts}
            \begin{center}
                \begin{tikzpicture}
                    \begin{axis}[
                            axis x line=middle, axis y line=middle,
                            xmin = -10, xmax = 10,
                            ymin = -10, ymax = 10,
                            xtick distance = 1, ytick distance = 1,
                            grid = both, minor tick num = 1,
                            major grid style = {gray}, minor grid style = {gray!25},
                            width = \textwidth, height = \textwidth
                            ]
                        \draw[very thick,->] (axis cs:0,0)->(axis cs:1,0) node[below, midway] {$\vect{i}$};
                        \draw[very thick,->] (axis cs:0,0)->(axis cs:0,1) node[left, midway] {$\vect{j}$};		
                        \draw (axis cs:0,0) circle node [left, below] {$O$};
                        \draw [->,red,very thick] (axis cs:"""+str(x0)+r""","""+str(y0)+r""") -- (axis cs:"""+str(x1)+r""","""+str(y1)+r""");
                        \draw [->,red,very thick] (axis cs:"""+str(x2)+r""","""+str(y2)+r""") -- (axis cs:"""+str(x3)+r""","""+str(y3)+r""");
                        \draw [->,red,very thick] (axis cs:"""+str(x4)+r""","""+str(y4)+r""") -- (axis cs:"""+str(x5)+r""","""+str(y5)+r""");
                        \draw [->,red,very thick] (axis cs:"""+str(x0)+r""","""+str(y0)+r""") -- (axis cs:"""+str(x2)+r""","""+str(y2)+r""");
                        \draw [->,red,very thick] (axis cs:"""+str(x1)+r""","""+str(y1)+r""") -- (axis cs:"""+str(x3)+r""","""+str(y3)+r""");
                        \draw [->,red,very thick] (axis cs:"""+str(x3)+r""","""+str(y3)+r""") -- (axis cs:"""+str(x5)+r""","""+str(y5)+r""");
                        \filldraw[red] (axis cs:"""+str(x0)+r""","""+str(y0)+r""") circle (1pt) node[anchor=south] {"""+letters[0]+r"""};
                        \filldraw[red] (axis cs:"""+str(x1)+r""","""+str(y1)+r""") circle (1pt) node[anchor=south] {"""+letters[1]+r"""};
                        \filldraw[red] (axis cs:"""+str(x2)+r""","""+str(y2)+r""") circle (1pt) node[anchor=south] {"""+letters[2]+r"""};
                        \filldraw[red] (axis cs:"""+str(x3)+r""","""+str(y3)+r""") circle (1pt) node[anchor=south] {"""+letters[3]+r"""};
                        \filldraw[red] (axis cs:"""+str(x4)+r""","""+str(y4)+r""") circle (1pt) node[anchor=south] {"""+letters[4]+r"""};
                        \filldraw[red] (axis cs:"""+str(x5)+r""","""+str(y5)+r""") circle (1pt) node[anchor=south] {"""+letters[5]+r"""};
                        
                    \end{axis}

                \end{tikzpicture}
            \end{center}
    \clearpage
    """
    return(exo,correction)

def exoVecteurN1(genCode="999999999", id=False):
    """
    This function generates a LaTeX exercise and its correction for placing points and calculating vector
    coordinates and norms in an orthonormal coordinate system.
    :param genCode: The `genCode` parameter is a string that represents a unique identifier or code for
    the generated exercise. It is used to differentiate between different versions of the exercise,
    allowing for easy tracking and organization. This code can be useful for educators or students
    who want to reference a specific version of the exercise.

    :param
    id: The `id` parameter is a boolean flag that determines whether to include an identification
    string in the generated LaTeX code. If `id` is set to `True`, the identification string
    `exoVecteurN1\` will be included at the beginning of the exercise and correction sections. If `id` is
    set to `False`, no identification string will be included. This parameter allows for optional
    identification of the exercise in the generated LaTeX document. 
    :return: The function `exoVecteurN1` returns two strings: `exo` and `correction`. Both strings contain
    LaTeX code for an exercise and its corresponding correction, respectively. The exercise involves
    placing points and calculating vector coordinates and norms in an orthonormal coordinate system,
    while the correction provides the same information for reference.
    """
    if id:
        identification = r"""exoVecteurN1\\"""
    else:
        identification = r""""""
    xa, xb, xc = symbols('xa xb xc')
    ya, yb, yc = symbols('ya yb yc')
    xa = Rational(np.random.randint(0,8)-4)
    ya = Rational(4)
    xb = Rational(np.random.randint(0,8)-4)
    yb = Rational(1)
    xc = Rational(np.random.randint(0,8)-4)
    yc = Rational(-3)
    xa_string = latex(xa).replace('\\frac','\\dfrac')
    ya_string = latex(ya).replace('\\frac','\\dfrac')
    xb_string = latex(xb).replace('\\frac','\\dfrac')
    yb_string = latex(yb).replace('\\frac','\\dfrac')
    xc_string = latex(xc).replace('\\frac','\\dfrac')
    yc_string = latex(yc).replace('\\frac','\\dfrac')
    
    exo=r"""
    \clearpage
    """+identification+r"""
    \Question Soit les points $\Point{A}{\tiny{"""+xa_string+r"""}}{"""+ya_string+r"""}$, $\Point{B}{"""+xb_string+r"""}{"""+yb_string+r"""}$ et $\Point{C}{"""+xc_string+r"""}{"""+yc_string+r"""}$
        \begin{parts}
            \Part[6] Placer les points A, B et C dans le repère orthonormé suivant :
                \begin{center}
                    \begin{tikzpicture}
                        \begin{axis}[					
                            axis x line=middle,
                            axis y line=middle,
                            xmin = -5, xmax = 5,
                            ymin = -5, ymax = 5,
                            xtick distance = 1,
                            ytick distance = 1,
                            grid = both,
                            minor tick num = 1,
                            major grid style = {gray},
                            minor grid style = {gray!25},
                            width = 0.5\textwidth,
                            height = 0.5\textwidth]
                        \end{axis}
                    \end{tikzpicture}
                \end{center}
            \Part[6] Donner les coordonnées des vecteurs :
                \begin{enumerate}
                    \item $\Coord{AB}{"""+str(xb)+r"""-("""+str(xa)+r""")=?}{"""+str(yb)+r"""-("""+str(ya)+r""")=?}$
                        \fillwithlines{15mm}
                    \item $\Coord{AC}{"""+str(xc)+r"""-("""+str(xa)+r""")=?}{"""+str(yc)+r"""-("""+str(ya)+r""")=?}$
                        \fillwithlines{15mm}
                    \item $\Coord{BC}{x_C-x_B=?}{y_C-y_B=?}$
                        \fillwithlines{15mm}
                \end{enumerate}
            \Part[6] Calculer les normes des vecteurs suivants en simplifiant vos résultats :
                \begin{enumerate}
                    \item
                        \begin{align*}
                            \|\vect{AB}\|&=\sqrt{("""+str(xb)+r"""-("""+str(xa)+r"""))^2+("""+str(yb)+r"""-("""+str(ya)+r"""))^2}\\
                                        &=\\
                                        &=\\
                                        &=
                        \end{align*}
                    \item $\|\vect{AC}\|=$
                        \fillwithlines{15mm}
                    \item $\|\vect{BC}\|=$
                        \fillwithlines{15mm}
                \end{enumerate}
        \end{parts}   
    """
    correction=r"""
    \clearpage
    """+identification+r"""
    \Question Soit les points $\Point{A}{\tiny{"""+xa_string+r"""}}{"""+ya_string+r"""}$, $\Point{B}{"""+xb_string+r"""}{"""+yb_string+r"""}$ et $\Point{C}{"""+xc_string+r"""}{"""+yc_string+r"""}$
        \begin{parts}
            \Part[6] Placer les points A, B et C dans le repère orthonormé suivant :
                \begin{center}
                    \begin{tikzpicture}
                        \begin{axis}[					
                            axis x line=middle,
                            axis y line=middle,
                            xmin = -5, xmax = 5,
                            ymin = -5, ymax = 5,
                            xtick distance = 1,
                            ytick distance = 1,
                            grid = both,
                            minor tick num = 1,
                            major grid style = {gray},
                            minor grid style = {gray!25},
                            width = 0.5\textwidth,
                            height = 0.5\textwidth]
                            \addplot[mark=*] coordinates {("""+str(xa)+r""","""+str(ya)+r""")} node[anchor=north west]{$A$};
                            \addplot[mark=*] coordinates {("""+str(xb)+r""","""+str(yb)+r""")} node[anchor=north west]{$B$};
                            \addplot[mark=*] coordinates {("""+str(xc)+r""","""+str(yc)+r""")} node[anchor=north west]{$C$};
                        \end{axis}
                    \end{tikzpicture}
                \end{center}
            \Part[6] Donner les coordonnées des vecteurs :
                \begin{enumerate}
                    \item $\Coord{AB}{"""+str(xb)+r"""-("""+str(xa)+r""")="""+str(xb-xa)+r"""}{"""+str(yb)+r"""-("""+str(ya)+r""")="""+str(yb-ya)+r"""}$ d'où $\Coord{AB}{"""+str(xb-xa)+r"""}{"""+str(yb-ya)+r"""}$
                    \item $\Coord{AC}{"""+str(xc)+r"""-("""+str(xa)+r""")="""+str(xc-xa)+r"""}{"""+str(yc)+r"""-("""+str(ya)+r""")="""+str(yc-ya)+r"""}$ d'où $\Coord{AC}{"""+str(xc-xa)+r"""}{"""+str(yc-ya)+r"""}$
                    \item $\Coord{BC}{"""+str(xc)+r"""-("""+str(xb)+r""")="""+str(xc-xb)+r"""}{"""+str(yc)+r"""-("""+str(yb)+r""")="""+str(yc-yb)+r"""}$ d'où $\Coord{BC}{"""+str(xc-xb)+r"""}{"""+str(yc-yb)+r"""}$
                \end{enumerate}
            \Part[6] Calculer les normes des vecteurs suivants en simplifiant vos résultats :
                \begin{enumerate}
                    \item
                        \begin{align*}
                            \|\vect{AB}\|&=\sqrt{("""+str(xb)+r"""-("""+str(xa)+r"""))^2+("""+str(yb)+r"""-("""+str(ya)+r"""))^2}\\
                                        &=\sqrt{("""+str(xb-xa)+r""")^2+("""+str(yb-ya)+r""")^2}\\
                                        &=\sqrt{"""+str((xb-xa)**2)+r"""+"""+str((yb-ya)**2)+r"""}\\
                                        &="""+latex( sqrt((xb-xa)**2+(yb-ya)**2))+r"""
                        \end{align*}
                    \item 
                        \begin{align*}
                            \|\vect{AC}\|&=\sqrt{("""+str(xc)+r"""-("""+str(xa)+r"""))^2+("""+str(yc)+r"""-("""+str(ya)+r"""))^2}\\
                                        &=\sqrt{("""+str(xc-xa)+r""")^2+("""+str(yc-ya)+r""")^2}\\
                                        &=\sqrt{"""+str((xc-xa)**2)+r"""+"""+str((yc-ya)**2)+r"""}\\
                                        &="""+latex( sqrt((xc-xa)**2+(yc-ya)**2))+r"""
                        \end{align*}
                    \item 
                        \begin{align*}
                            \|\vect{BC}\|&=\sqrt{("""+str(xc)+r"""-("""+str(xb)+r"""))^2+("""+str(yc)+r"""-("""+str(yb)+r"""))^2}\\
                                        &=\sqrt{("""+str(xc-xb)+r""")^2+("""+str(yc-yb)+r""")^2}\\
                                        &=\sqrt{"""+str((xc-xb)**2)+r"""+"""+str((yc-yb)**2)+r"""}\\
                                        &="""+latex( sqrt((xc-xb)**2+(yc-yb)**2))+r"""
                        \end{align*}
                \end{enumerate}
        \end{parts}   
    """
    return(exo,correction)

def genQuestionFormeDevelopper(questions,n=1):
    for i in range(0,n):
        a, b, c, d,x = symbols('a b c d x')
        a = Rational(np.random.randint(1,10)-5)
        if a==0:
            a=1
        b = Rational(np.random.randint(1,10)-5)
        if b==0:
            b=-3
        c = Rational(np.random.randint(1,10)-5)
        if c==0:
            c=-1
        d = Rational(np.random.randint(1,10)-5)
        if d==0:
            d=-2
        expr = (a*x+b)*(c*x+d)
        sol = solve(expr)
        exprExpand = expand(expr)   
        # forme développé
        questions.append(["choice",1, """La forme développé de $"""+latex(expr)+r"""$ est ""","""$"""+latex(exprExpand)+r"""$""", """$"""+latex(exprExpand*x)+r"""$""", """$"""+latex(exprExpand/x)+r"""$"""])
        # # équation affine
        # questions.append(["choice",1, """L'équation $"""+latex(a*x+b)+r"""=0$ a pour solution ""","""$"""+latex(solve(a*x+b))+r"""$""", """$"""+latex(solve(a*x+b-4))+r"""$""", """$"""+latex(solve(a*x+b+2))+r"""$"""])
        # # équation produit
        # questions.append(["choice",1, """L'équation $"""+latex(expr)+r"""=0$ a pour solution ""","""$"""+latex(sol)+r"""$""", """$"""+latex(solve(a*x+b-4))+r"""$""", """$"""+latex(solve(a*x+b+2))+r"""$"""])
        # # Somme de fraction
        # questions.append(["choice",1, """$"""+latex(Rational(a/b))+r"""+"""+latex(Rational(c/d))+r"""=$""","""$"""+latex(Rational(a/b+c/d))+r"""$""", """$"""+latex(Rational(b/a-d/c))+r"""$""", """$"""+latex(Rational(b/a+b/c))+r"""$""", """$"""+latex(Rational(b/a-b/c))+r"""$""",])
        # # Produit de fraction
        # questions.append(["choice",1, """$"""+latex(Rational(a/b))+r"""\times"""+latex(Rational(c/d))+r"""=$""","""$"""+latex(Rational((a/b)*(c/d)))+r"""$""", """$"""+latex(Rational(b/a-d/c))+r"""$""", """$"""+latex(Rational(b/a+b/c))+r"""$""", """$"""+latex(Rational(b/a-b/c))+r"""$""",])
        # # Division de fraction
        # questions.append(["choice",1, """$"""+latex(Rational(a/b))+r"""\div"""+latex(Rational(c/d))+r"""=$""","""$"""+latex(Rational((a/b)/(c/d)))+r"""$""", """$"""+latex(Rational(b/a*d/c-4))+r"""$""", """$"""+latex(Rational(b/a+b/c))+r"""$""", """$"""+latex(Rational(b/a-b/c))+r"""$""",])
       
    return(questions)

def genQuestionFormeFactoriser(questions, n=1):
    for i in range(0,n):
        a, b, x = symbols('a b x')
        a = np.random.randint(1,10)-5
        if a==0:
            a=1
        b = np.random.randint(1,10)-5
        if b==0:
            b-=-4
        exprExpand = a**2*x**2+2*a*b*x+b**2
        expr = factor(exprExpand)
        questions.append([
            "choice",
            1,
            r"""La forme factorisé de $"""+latex(exprExpand)+r"""$ est """,
            r"""$"""+latex(expr)+r"""$""",
            r"""$"""+latex(expr*x)+r"""$""",
            r"""$"""+latex(expr/x)+r"""$"""])
    return(questions)

def genQuestionSurfaceHachuree(questions):
    h = random.randint(2,6)
    w = random.randint(6,10)
    xval = 1
    questions.append([
        "choice",
        1,
        r"""
    On considère l'aire de la partie hachurée $A(x)$, dans la figure ci-contre.
		\begin{center}
			\begin{tikzpicture}[scale=0.5,cap=round]
			    % Define constants
			    \pgfmathsetmacro{\width}{"""+str(w)+r"""}  % Width of the rectangle
			    \pgfmathsetmacro{\height}{"""+str(h)+r"""}  % Height of the rectangle
			    \pgfmathsetmacro{\xval}{"""+str(xval)+r"""}  % The x dimension
			    % Outer rectangle
			    \draw[thick] (0,0) rectangle (\width,\height);
			    % Shaded inner rectangle
			    \fill[pattern=north east lines] (0,\xval) rectangle (\width-\xval,\height);
			    % Dimensions
			    \draw[<->] (0,-0.5) -- (\width,-0.5) node[midway, below] {\width};
			    \draw[<->] (\width+0.5,0) -- (\width+0.5,\height) node[midway, right] {\height};
			    % Labels for x dimensions
			    \draw[<->] (-0.5,0) -- (-0.5,\xval) node[midway, left] {$x$};
			    \draw[<->] (\width,\height+0.5) -- (\width-\xval,\height+0.5) node[midway, above] {$x$};
			\end{tikzpicture}
		\end{center}
         L'expression $A(x)$ est égale à :""",
        r"""$("""+str(w)+r"""-x)("""+str(h)+r"""-x)$""",
        r"""$70-x^2$""",
		r"""$(x-5)(x-10)$"""
    ])
    return(questions)

def genQuestionEnsembleNombre(questions, n=1):
    choix = ['N','Z','D','Q', 'R']
    nbType = random.choice(choix)
    good = r""""""

    if nbType == 'N':
        ques = r"""Parmi les nombres suivant, lequel est un entier nautrel ?"""
        good = r""""""+str(random.randint(1,10))+r""""""
        bad1 = r""""""+str(random.randint(-10,-1))+r""""""
        bad2 = r"""\dfrac{"""+str(random.randint(-10,-1))+r"""}{"""+str(random.randint(2,9))+r"""}"""
    elif nbType == 'Z':
        ques = r"""Parmi les nombres suivant, lequel est un entier relatif ?"""
        good = r""""""+str(random.randint(-10,-1))+r""""""
        bad1 = r""""""+str(random.randint(1,10))+r""""""
        bad2 = r"""\dfrac{"""+str(random.randint(-10,-1))+r"""}{"""+str(random.randint(2,9))+r"""}"""
        pass
    elif nbType == 'D':
        ques = r"""Parmi les nombres suivant, lequel est un nombre décimal ?"""
        good = r"""\dfrac{"""+str(random.randint(-10,-1))+r"""}{10^"""+str(random.randint(1,10))+r"""}"""
        bad1 = r""""""+str(random.randint(1,10))+r""""""
        bad2 = r"""\dfrac{\sqrt{"""+str(random.randint(2,3))+r"""}}{"""+str(random.randint(2,5))+r"""}"""
        pass
    elif nbType == 'Q':
        ques = r"""Parmi les nombres suivant, lequel est un nombre rationnel ?"""
        good = r"""\dfrac{"""+str(random.randint(-10,-1))+r"""}{"""+str(random.randint(2,10))+r"""}"""
        reel = [r"""\pi""",r"""\dfrac{\sqrt{\pi}}{"""+str(random.randint(2,5))+r"""}""" , r"""\dfrac{\sqrt{"""+str(random.randint(2,3))+r"""}}{"""+str(random.randint(2,5))+r"""}""" ]
        bad1 = r""""""+random.choice(reel)+r""""""
        bad2 = r"""\dfrac{\sqrt{"""+str(random.randint(2,3))+r"""}}{"""+str(random.randint(2,5))+r"""}"""
        pass
    elif nbType == 'R':
        ques = r"""Parmi les nombres suivant, lequel est un nombre réel ?"""
        reel = [r"""\pi""",r"""\dfrac{\sqrt{\pi}}{"""+str(random.randint(2,5))+r"""}""" , r"""\dfrac{\sqrt{"""+str(random.randint(2,3))+r"""}}{"""+str(random.randint(2,5))+r"""}""" ]
        good = r""""""+random.choice(reel)+r""""""
        bad1 = r"""\dfrac{"""+str(random.randint(-10,-1))+r"""}{10^"""+str(random.randint(1,10))+r"""}"""
        bad2 = r""""""+str(random.randint(1,10))+r""""""
        pass

    # ["choice",1, r"""Parmi les affirmations suivantes, cocher celle qui est vraie :""",r"""$"""+latex(exprExpand)+r"""$""", r"""$"""+latex(exprExpand*x)+r"""$""", r"""$"""+latex(exprExpand/x)+r"""$"""]
    questions.append(["choice",1, ques,good, bad1, bad2])
    
    return(questions)

def exoQCM3ieme(n=5, id=False):
    if id:
        identification = r"""exoQCM3ieme\\"""
    else:
        identification = r""""""
    questions=[
        # ["choice",1, "La représentation graphique d'une fonction affine ($f(x)=ax+b$) est ?","une droite", "une parabole", "une hyperbole", "un point",],
        # ["fillin",1, """La somme de deux nombre négatif est un nombre []""","négatif","positif", "nul"],
        # ["fillin",1, """Le produit de deux nombre positif est un nombre []""","positif","négatif"],
        # ["choice",1, """L'équation $3x-1=0$ admet pour solution $\dfrac{-1}{3}$""","""Faux""", """Vrai"""],
        # ["choice",1, """L'équation $7x+3=0$ admet pour solution $\dfrac{-3}{7}$""","""Vrai""", """Faux"""],
        # ["choice",1, """Lors qu'on lance un dé à 6 faces, on a 1 chance sur 6 d'avoir un 2""","""Vrai""", """Faux"""],
        # ["choice",1, """Le périmètre d'un carré est proportionnel à la longueur des côtés.""","""Vrai""", """Faux"""],
        # ["choice",1, """La masse d'une quantité d'eau est proportionnelle au volume de cette quantité d'eau.""","""Vrai""", """Faux"""],
        # ["choice",1, """La fonction $f(x)=\dfrac{1}{x}$ est une fonction affine.""","""Faux""", """Vrai"""],
        # ["choice",1, """La fonction $f(x)=2x+3$ est une fonction affine.""","""Vrai""", """Faux"""],
        ]
    questions=genQuestionFormeDevelopper(questions,n=10)
    questions=genQuestionFormeFactoriser(questions,n=10 )

    parts=r""""""
    partscorrection=r""""""
    for nb in range(0,n):
        i = np.random.randint(0,len(questions)-1)
        question=questions[i]
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
            
        questions.remove(questions[i])
        
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
    return(exo,correction)


    
def genfonctionHomographique(id=False):
    if id:
        identification = r"""genfonctionHomographique\\"""
    else:
        identification = r""""""
    af, bf, cf, df, ag, bg, cg, dg, x, f, g = symbols('af bf cf df ag bg cg dg x f g')
    values = nonEqRandomValue(n=8, debut=-5, fin=5, demi=False, tier=False, notNull=True)
    af = values[0]
    bf = values[1]
    cf = values[2]
    df = values[3]
    ag = values[4]
    bg = values[5]
    cg = values[6]
    dg = values[7]
    while af*cg-ag*cf!=0:
        values = nonEqRandomValue(n=8, debut=-5, fin=5, demi=False, tier=False, notNull=True)
        af = values[0]
        bf = values[1]
        cf = values[2]
        df = values[3]
        ag = values[4]
        bg = values[5]
        cg = values[6]
        dg = values[7]
    #-La fonction f ---------------------------------------------
    f = (af*x+bf)/(cf*x+df)
    num_f = af*x+bf
    fzero = -bf/af
    denum_f = cf*x+df
    excluded_f = -df/cf
    if fzero<excluded_f:
        fxline = r"""{$+\infty$, $"""+Latex(fzero)+r"""$ , $"""+Latex(excluded_f)+r"""$ , $+\infty$}"""
        fline = r"""{ , """+Signe(f.evalf(subs={x:excluded_f-1}))+r""" , z , """+Signe(f.evalf(subs={x:(excluded_f+fzero)/2}))+r""" , d , """+Signe(f.evalf(subs={x:fzero+1}))+r""" , }"""
        if af>0:
            fxtabline_numerator = r"""{ , - , z , + , + , + , }"""
        else:
            fxtabline_numerator = r"""{ , + , z , - , - , - , }"""
        if cf>0:
            fxtabline_denumerator = r"""{ , - , - , - , z , + , }"""
        else: 
            fxtabline_denumerator = r"""{ , + , + , + , z , - , }"""
    else:
        fxline = r"""{$+\infty$, $"""+Latex(excluded_f)+r"""$ , $"""+Latex(fzero)+r"""$ , $+\infty$}"""
        fline = r"""{ , """+Signe(f.evalf(subs={x:fzero-1}))+r""" , z , """+Signe(f.evalf(subs={x:(excluded_f+fzero)/2}))+r""" , d , """+Signe(f.evalf(subs={x:excluded_f+1}))+r""" , }"""        
        if af>0:
            fxtabline_numerator = r"""{ , - , - , - , z , + , }"""
        else:
            fxtabline_numerator = r"""{ , + , + , + , z , - , }"""
        if cf>0:
            fxtabline_denumerator = r"""{ , - , z , + , + , + , }"""
        else: 
            fxtabline_denumerator = r"""{ , + , z , - , - , - , }"""
    
    
    #-La fonction g ---------------------------------------------
    g = (ag*x+bg)/(cg*x+dg)
    num_g = ag*x+bg
    denum_g = cg*x+dg
    excluded_g = -dg/cg
    expr1 = num_f*denum_g-denum_f*num_g
    sexpr1 = simplify(expr1)
    sol = solve(sexpr1, rational=True)
    A = af*cg-ag*cf
    B = af*df+bf*cg-ag*df-bg*cf
    C = bf*dg-bg*df
    if A!=0:
        DELTA = B**2-4*A*C
        if DELTA>0:
            rDELTA = sqrt(DELTA)
            X1 = (-B-rDELTA)/(2*A)
            X2 = (-B+rDELTA)/(2*A)
            suitefg = r"""
            Il s'agit d'une équation quotient donc l'égalité à $0$ ne dépend que du numérateur.
            Le numérateur est un polynôme du second 
            """
    if A==0:
        if sol==[]:
            suitefg=r"""
                Il n'y a pas de solution car le numérateur et le dénominateur s'annule pour la même valeur de $x$
            """
        else:
            suitefg=r"""
                La solution ne dépend que du numérateur $"""+Latex(sexpr1)+r"""$.\\
                La solution est donc $x="""+Latex(sol[0])+r"""$
            """
    #--------------------------------------------------------------------------------------------------------------
    exo=r"""
        \clearpage
        """+identification+r"""
	\Question Fonctions Homographiques\\
		On considère les fonctions $f$ et $g$ définies par :
		\begin{center}
			$f(x)="""+Latex(f)+r"""$ et $g(x)="""+Latex(g)+r"""$
		\end{center}
	\begin{parts}
		\Part Déterminer l'ensemble de définition de $f$ et $g$.\\
			\fillwithlines{30mm}
		\Part Démontrer que ces fonctions sont des fonctions homographiques.
			\fillwithlines{35mm}
		\Part Résoudre l'équation $f(x)=g(x)$
			\fillwithlines{50mm}
		\Part Compléter le tableau de signe de $f$ ci-dessous
			\begin{center}
				\begin{tikzpicture}
					\tkzTabInit[espcl=4] %[lgt=3]
						{$x$ /1 , Signe de\\$"""+Latex(num_f)+r"""$ /2,Signe de\\$"""+Latex(denum_f)+r"""$ / 2, Signe de $f$/2 }
						"""+fxline+r"""
					\tkzTabLine
						{ ,   ,   ,   ,   ,   , }
					\tkzTabLine
						{ ,   ,   ,   ,   ,   , }
					\tkzTabLine
						{ ,   ,   ,   ,   ,   , }
				\end{tikzpicture}
			\end{center}
	\end{parts}
    """
    correction=r"""
    \clearpage
    """+identification+r"""
	\Question Fonctions Homographiques\\
		On considère les fonctions $f$ et $g$ définies par :
		\begin{center}
			$f(x)="""+Latex(f)+r"""$ et $g(x)="""+Latex(g)+r"""$
		\end{center}
	\begin{parts}
		\Part Déterminer l'ensemble de définition de $f$ et $g$.\\
			\begin{enumerate}
				\item $f$ est définie quand son dénominateur est différent de zéro ($"""+Latex(cf*x+df)+r"""\neq0$)\\
				Le domaine de définition de $f$ est donc $\mathcal{D}_f=]-\infty;"""+Latex(excluded_f)+r"""[\cup]"""+Latex(excluded_f)+r""";+\infty[$\\
				\item $g$ est définie quand son dénominateur est différent de zéro ($"""+Latex(cg*x+dg)+r"""\neq0$)\\
				Le domaine de définition de $g$ est donc $\mathcal{D}_g=]-\infty;"""+Latex(excluded_g)+r"""[\cup]"""+Latex(excluded_g)+r""";+\infty[$
			\end{enumerate}
		\Part Démontrer que ces fonctions sont des fonctions homographiques.
			\begin{center}
				$f(x) = """+Latex(f)+r"""$
			\end{center}
			On a $a="""+Latex(af)+r"""$, $b="""+Latex(bf)+r"""$, $c="""+Latex(cf)+r"""$ et $d="""+Latex(df)+r"""$\\
			On a bien $c\neq 0$ et $ad-bc = """+Latex(af*df)+r""" - """+Latex(bf*cf)+r""" = """+Latex(af*df-bf*cf)+r"""\neq 0$\\
			Par conséquent, $f$ est bien une fonction homographique.
            \begin{center}
				$g(x) = """+Latex(g)+r"""$
			\end{center}
			On a $a="""+Latex(ag)+r"""$, $b="""+Latex(bg)+r"""$, $c="""+Latex(cg)+r"""$ et $d="""+Latex(dg)+r"""$\\
			On a bien $c\neq 0$ et $ad-bc = """+Latex(ag*dg)+r""" - """+Latex(bg*cg)+r""" = """+Latex(ag*dg-bg*cg)+r"""\neq 0$\\
			Par conséquent, $g$ est bien une fonction homographique.
		\Part Résoudre l'équation $f(x)=g(x)$
			\begin{align*}
				f(x) = g(x) & \Leftrightarrow """+Latex(f)+r""" = """+Latex(g)+r""" \\
                            & \Leftrightarrow """+Latex(f)+r""" – """+Latex(g)+r""" = 0\\
                            & \Leftrightarrow \dfrac{\left("""+Latex(num_f)+r"""\right)\times\left("""+Latex(denum_g)+r"""\right)}{\left("""+Latex(denum_f)+r"""\right)\times\left("""+Latex(denum_g)+r"""\right)}-\dfrac{\left("""+Latex(denum_f)+r"""\right)\times\left("""+Latex(num_f)+r"""\right)}{\left("""+Latex(denum_f)+r"""\right)\times\left("""+Latex(denum_g)+r"""\right)}\\
                            & \Leftrightarrow """+Latex((num_f*denum_g-denum_f*num_g)/(denum_f*denum_g))+r""" = 0\\
                            & \Leftrightarrow """+Latex(simplify(num_f*denum_g-denum_f*num_g)/(denum_f*denum_g))+r""" = 0
			\end{align*}
            """+suitefg+r"""
		\Part Compléter le tableau de signe de $f$ ci-dessous
			\begin{center}
				\begin{tikzpicture}
					\tkzTabInit[espcl=4] %[lgt=3]
						{$x$ /1 , Signe de\\$"""+Latex(num_f)+r"""$ /2,Signe de\\$"""+Latex(denum_f)+r"""$ / 2, Signe de $f$/2 }
						"""+fxline+r"""
					\tkzTabLine
						"""+fxtabline_numerator+r"""
					\tkzTabLine
						"""+fxtabline_denumerator+r"""
					\tkzTabLine
						{ ,   ,   ,   ,   ,   , }
				\end{tikzpicture}
			\end{center}
	\end{parts}
    """
    return(exo,correction)

def exoBonusAgeDuCapitaine(id=False):
    if id:
        identification = r"""exoBonusAgeDuCapitaine\\"""
    else:
        identification = r""""""
    exo=r"""
    \clearpage
    """+identification+r"""
        \Question On s'intéresse à la population féminine du Portugal. Nous savons qu'en 2010 il y avait 5 171 286 hommes et 5 504 286 femmes.\\
            On sélectionne au hasard 3 personnes de ce pays, avec remise et de manière indépendante. A chaque tirage, on regarde si la personne est un homme ou une femme.\\
            On peut modéliser cette expérience aléatoire par $n$ épreuves indépendantes de Bernoulli de paramètre $p$, avec $S$ le succès, c'est-à-dire que la personne tirée soit une femme, et $E$ l'échec, c'est-à-dire que la personne tirée ne soit pas une femme.
			\begin{parts}
				\Part[3] Calculer le paramètre $p$ de la loi Binomiale (la probabilité $p(S)$ de succès de l'événement $S$ « la personne tirée est une femme »)
				\fillwithlines{25mm}
			\end{parts}
		\Question (BONUS) - Un voilier de 37 mètres de long monté de 3 mâts est manœuvré par 18 matelots. La surface des voiles représente 632 $m^2$. La structure du navire comprend 3 ponts dont la cale.\\
		3 Sous-Officiers s'occupent du fonctionnement du navire. L'un d'entre-eux est assigné à la navigation.
            \begin{parts}
                \Part Quel est l'âge du Capitaine ? (toutes réponses sera évaluées)
                \fillwithlines{25mm}
            \end{parts}
    """
    correction=r"""
    \clearpage
    """+identification+r"""
		\Question (BONUS) - Un voilier de 37 mètres de long monté de 3 mâts est manœuvré par 18 matelots. La surface des voiles représente 632 $m^2$. La structure du navire comprend 3 ponts dont la cale.\\
		3 Sous-Officiers s'occupent du fonctionnement du navire. L'un d'entre-eux est assigné à la navigation.
		\begin{parts}
			\Part Quel est l'âge du Capitaine ? (toutes réponses sera évaluées)\\
			Le Capitaine a l'âge qu'il faut pour être Capitaine
		\end{parts}
    """
    return(exo,correction)

def rappelTSTMG():
    exo=r"""
    \clearpage

\section{Rappel de cours}
	\subsection{Les symboles mathématiques}
		\begin{center}
			\begin{tabular}{p{8cm}p{7cm}}
				\textit{Symboles} & \textit{Exemples} \\ \hline
				$\exists$  : Il existe & \\ \hline
				$\exists!$ : Il existe un et un seul & \\ \hline
				$\nexists$ : Il n'existe pas & \\ \hline
				$\forall$ : Quelque soit & $\forall$ \\ \hline
				$\lor$ : ou & \\ \hline
				$\land$ : et & \\ \hline
				$\Rightarrow$ : implique & $a^2 = 25 \Rightarrow a=5$ \\ \hline
				$\Leftrightarrow$ : est équivalent à & $a=b \Leftrightarrow b=a$\\ \hline
				$\perp$ : est perpendiculaire à & \\ \hline
				$\not\perp$ : n'est pas perpendiculaire à & \\ \hline
				$\|$ : est parallèle à & \\ \hline
				$\nparallel$ : n'est pas parallèle à & \\ \hline
				$\in$ : appartient à & $\left\{ 4 \right\} \in \left\{ 1,2,3,4,5,6,7 \right\}$ \\ \hline
				$\notin$ : n'appartient pas à & $\left\{ 10 \right\} \notin \left\{ 1,2,3,4,5,6,7 \right\} $\\ \hline
				$<$ : est inférieure à  & $5<9$ \\ \hline
				$\leqslant$ : est inférieure ou égale à & \\ \hline
				$>$ : est supérieure à & $4>3$\\ \hline
				$\geqslant$ : est supérieure ou égale à & \\ \hline
				$\mapsto$ ou $\longmapsto$  : associe & $f:x\longmapsto 2x+1$ \\ \hline
				
			\end{tabular}
		\end{center}
\clearpage
	\subsection{Les puissances}
		\begin{tabular}{p{6.5cm}p{8.5cm}}
		%						\hline 
								\textit{Formules} & \textit{Exemples} \\ 
								\hline 
								${ a }^{ 0 }=1$ & ${ 12 }^{ 0 }=1$ \rule[-15pt]{0pt}{40pt}\\ \hline
								${ a }^{ 1 }=a$ & ${ 7 }^{ 1 }=7$ \rule[-15pt]{0pt}{40pt}\\ \hline
								${ a }^{ 2 }=a\times a$ & ${ 5 }^{ 2 }=5\times5=25$ \rule[-15pt]{0pt}{40pt}\\ \hline
								${ a }^{ 3 }=a\times a\times a$ & ${ 2 }^{ 3 }=2\times2\times2=8$ \rule[-15pt]{0pt}{40pt}\\ \hline
								${ a }^{ n }=a\times a\times.....\times a$ & ${ 3 }^{ 4 }=3\times3\times3\times3=81$ \rule[-15pt]{0pt}{40pt}\\ \hline
								$\displaystyle { a }^{ \frac{1}{2} }=\sqrt{a}=\sqrt[2]{a}$ & $\displaystyle { 9 }^{ \frac{1}{2} }=\sqrt{9}=\sqrt[2]{9}=3$ \rule[-15pt]{0pt}{40pt}\\ \hline
								$\displaystyle { a }^{ \frac{1}{n} }=\sqrt[n]{a}$ & $\displaystyle { 27 }^{ \frac{1}{3} }=\sqrt[3]{27}=3$ car $3\times3\times3=27$ \rule[-15pt]{0pt}{40pt}\\ \hline
								$\displaystyle { a }^{ n }\times{ a }^{ m }={ a }^{ n+m }$ & $\displaystyle { 10 }^{ 2 }\times{ 10 }^{ 7 }={ 10 }^{ (2+7) }={ 10 }^{ 9 }$ \rule[-15pt]{0pt}{40pt}\\ \hline
								$\displaystyle \frac{1}{{ a }^{ m }}={ a }^{ -m }$ & $\displaystyle \frac{1}{{ 10 }^{ 2 }}={ 10 }^{ -2 }$ \rule[-15pt]{0pt}{40pt}\\ \hline
								$\displaystyle \frac{{ a }^{ n }}{{ a }^{ m }}={ a }^{ n-m }$ & $\displaystyle \frac{{ 10 }^{ 4 }}{{ 10 }^{ 3 }}={ 10 }^{ (4-3) }={ 10 }^{ 1 }=10$ \rule[-15pt]{0pt}{40pt}\\ \hline
								$\displaystyle \frac{{ a }^{ n }}{{ a }^{ m }}={ a }^{ (n-m) }$ & $\displaystyle \frac{{ 10 }^{ 5 }}{{ 10 }^{ 2 }}={ 10 }^{ 5-2 }={10}^{3}$ \rule[-20pt]{0pt}{50pt}\\ 
		\end{tabular}
\clearpage

\section{Développer}

	\textbf{Développer} un produit, c'est l'écrire sous la forme d'une somme (ou d'une différence). 

	\begin{enumerate}
		\item $k(a+b)=ka+kb$
		\item $k(a-b)=ka-kb$
		\item $(a+b)(c+d)=ac+ad+bc+bd$
	\end{enumerate}

	Identités remarquables (Développement) :
	\begin{enumerate}
		\item $\displaystyle {(a+b)}^{2}={a}^{2}+2ab+{b}^{2}$
		\item $\displaystyle {(a-b)}^{2}={a}^{2}-2ab+{b}^{2}$
		\item $\displaystyle (a+b)(a-b)=a^{2}-b^{2}$
	\end{enumerate}
		
\section{Factoriser}
	\textbf{Factoriser} une somme (ou une différence), c'est l'écrire sous la forme d'un produit. 

	\begin{enumerate}
		\item $ka+kb=k(a+b)$
		\item $ka-kb=k(a-b)$
	\end{enumerate}
	k est le facteur commun 

	\begin{enumerate}
		\item \textbf{Avec des carrés :}\\
		Pour factoriser ${(x+1)}^{2}+(x+1)(x+2)$, on utilise le fait que ${(x+1)}^{2}=(x+1)(x+1)$ ce qui fait apparaître le facteur commun $(x+1)$ :\\
		$(x+1)^{2}+(x+1)(x+2)=\color{red}{(x+1)}\color{black}{(x+1)}+\color{red}{(x+1)}\color{black}{(x+2)}$\\
		$=(x+1)[(x+1)+(x+2)]$\\
		$=(x+1)(2x+3)$
		\item \textbf{Attention à ne pas oublier le 1 !}\\
		Pour factoriser $x^{2}-x$ on écrit que $x^{2}=x\times x$ et $x=x\times 1$;\\
		$x$ est alors facteur commun :\\
		$x^{2}-x = \color{red}{x} \color{black}{\times x}-\color{red}{x}\color{black}{\times 1 =} \color{red}{x} \color{black}{(x-1)}$
	\end{enumerate}

	Identités remarquables (Factorisation) :
	\begin{enumerate}
		\item $a^2+2ab+b^2=(a+b)^2$
		\item $a^2-2ab+b^2=(a-b)^2$
		\item $(a+b)(a-b)=a^2-b^2$
	\end{enumerate}
\clearpage

	\section{Probabilité}
		\begin{itemize}
			\item $P(\Omega)=1$ et $P(\varnothing)=0$
			\item Pour tout évènement $A$, $0\leqslant P(A)\leqslant 1$
			\item Dans une situation d'équiprobabilité, pour tout évènement $A$,
				\begin{center}
					$P(A)=\dfrac{\text{Nombre d'issues de A}}{\text{Nombre totale d'issues}}$
				\end{center}
			\item $P(\bar{A})=1-P(A)$
			\item $P(A\cup B)=P(A)+P(B)-P(A\cap B)$
			\item $\bar{A\cup B}=\bar{A}\cap\bar{B}$ et $\bar{A\cap B}=\bar{A}\cup\bar{B}$
			\item $P_A(B)=\dfrac{P(A\cap B)}{P(A)}$ d'où $P(A\cap B)=P(A)\times P_A(B)$
		\end{itemize}
	\section{Nombre de Bernoulli}
		\begin{center}
			$\frac{n!}{k!(n - k)!} = \binom{n}{k} = C_{n}^k$
		\end{center}
	\section{Loi Binomiale}

			\begin{itemize}
			\item $P(X=k)=\binom{n}{k}\times p^k\times (1-p)^{(n-k)}$
			\item $P(X=k)$ est la probabilité d'obtenir exactement k succès parmi les n expériences.
			\item $P(X\leqslant k)$ est la probabilité d'obtenir au plus k succès parmi les n expériences.
			\item $P(X>k)=1-P(X\leqslant k)$
		\end{itemize}
	\section{Taux d'évolution}
		\begin{itemize}
			\item Une quantité évolue d'une valeur initiale $y_1$ à une valeur finale $y_2$. Le taux d'évolution $t$ de $y_1$ à $y_2$ est : $t=\dfrac{y_1-y_2}{y_1}$
			\item Faire subir une évolution de taux $t$, c'est multiplier une quantité par le coefficient multiplicateur $1+t$
		\end{itemize}
			
	\section{Taux réciproque}
		\begin{itemize}
			\item Si une quantité subit une évolution de taux $t\neq-1$, l'évolution réciproque de taux $t'$ vérifie $t'=\dfrac{1}{1+t}-1$
		\end{itemize}
	\section{Évolution successives}
		\begin{itemize}
			\item Si une quantité subit $n$ évolutions de taux respectifs $t_1$, $t_2$,..., $t_n$ , alors le taux global $T$ vérifie $T=(1+t_1)(1+t_2)...(1+t_n)-1$
		\end{itemize}
	\section{Taux d'évolution moyen}
		\begin{itemize}
			\item Racine $n^{ième}$ :Soit $n$ un entier supérieur ou égal à 2, et $a$ un réel positif. La racine $n^{ième}$ du réel $a$ est le réel positif $x$ tel que $x^n=a$. On note ce réel $a^{\frac{1}{n}}$ (et aussi $\sqrt[n]{a}$)
			\item Si une quantité subit $n$ évolutions dont le taux global est $T$, alors le taux moyen $t_M$ vérifie $t_M =(1+ T)^{\frac{1}{n}}-1$
		\end{itemize}
    """

    return(exo)

def exoLireCoordVecteurs(id=False):
    if id:
        identification = r"""exoLireCoordVecteurs\\"""
    else:
        identification = r""""""
    vecteurs = genVecteurs()
    vectors = r"""
    """
    quest=r"""
    """
    for v in vecteurs:
        quest = quest + r"""
        \item $\Point{\underset{"""+v.nom+r"""}{\vect{"""+v.latexNom()+r"""}}}{.........}{..........}$
        """
        vectors = vectors + r"""
                        \draw [->,blue,very thick] (axis cs:"""+str(v.x1)+r""","""+str(v.y1)+r""") -- (axis cs:"""+str(v.x2)+r""","""+str(v.y2)+r""") node[above, midway] {$\vect{"""+v.latexNom()+r"""}$};
                        \filldraw[blue] (axis cs:"""+str(v.x1)+r""","""+str(v.y1)+r""") circle (1pt);
                        \filldraw[blue] (axis cs:"""+str(v.x2)+r""","""+str(v.y2)+r""") circle (1pt);
        """
    exo=r"""
    """+identification+r"""
    \Question Dans le repère orthonormé ci-dessous,
            \begin{parts}
                \Part[12] Lire les coordonnées des vecteurs suivants :
                    \begin{multicols}{3}
                        \begin{enumerate}
    """+quest+r"""
                        \end{enumerate}
                    \end{multicols}
            \end{parts}
            
            \begin{center}
                \begin{tikzpicture}
                    \begin{axis}[
                            axis x line=middle,
                            axis y line=middle,
                            xmin = -7, xmax = 7,
                            ymin = -7, ymax = 7,
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
    """+vectors+r"""
                    \end{axis}

                \end{tikzpicture}
            \end{center}
    """
    quest=r"""
    """
    for v in vecteurs:
        quest = quest + r"""
        \item $\Point{\underset{"""+v.nom+r"""}{\vect{"""+v.latexNom()+r"""}}}{"""+str(v.x)+r"""}{"""+str(v.y)+r"""}$
        """
    correction=r"""
    """+identification+r"""
    \Question Dans le repère orthonormé ci-dessous,
            \begin{parts}
                \Part[12] Lire les coordonnées des vecteurs suivants :
                    \begin{multicols}{3}
                        \begin{enumerate}
"""+quest+r"""
                        \end{enumerate}
                    \end{multicols}
            \end{parts}
            
            \begin{center}
                \begin{tikzpicture}
                    \begin{axis}[
                            axis x line=middle,
                            axis y line=middle,
                            xmin = -7, xmax = 7,
                            ymin = -7, ymax = 7,
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
"""+vectors+r"""
                    \end{axis}

                \end{tikzpicture}
            \end{center}
    """
    # print(exo)
    return(exo,correction)

def exoResoudreEqProduitN1(n=6, id=False):
    if id:
        identification = r"""exoResoudreEqProduitN1\\"""
    else:
        identification = r""""""
    alphabet = list(string.ascii_lowercase)
    lettres = random.sample(alphabet, n)
    lettres.sort()
    eq = r""""""
    eqCorrection = r""""""
    for l in lettres:
        k = nonEqRandomValue(n=2, notNull=True, tier=True)
        k.sort()
        a = Latex(k[0])
        b = Latex(k[1])
        if k[0]>0:
            a = r"""+"""+a
        if k[1]>0:
            b = r"""+"""+b
        eq = eq + r"""					\item $("""+l+a+r""")("""+l+b+r""")=0 $
                            \begin{flushright}
                                    $\Longrightarrow S=\lbrace................\rbrace$
                            \end{flushright}
"""
        eqCorrection = eqCorrection + r"""					\item $("""+l+a+r""")("""+l+b+r""")=0 $
                            \begin{flushright}
                                    $\Longrightarrow S=\lbrace{\color{red} """+Latex(-1*k[1])+r""";"""+Latex(-1*k[0])+r"""}\rbrace$
                            \end{flushright}
"""

    exo=r"""
    """+identification+r"""
            \Question["""+str(n*2)+r"""] Résoudre les équations suivantes :
        		\begin{multicols}{2}
		        	\begin{enumerate}
"""+eq+r"""
		        	\end{enumerate}
        		\end{multicols}
    """
    correction=r"""
    """+identification+r"""
            \Question["""+str(n*2)+r"""] Résoudre les équations suivantes :
        		\begin{multicols}{2}
		        	\begin{enumerate}
"""+eqCorrection+r"""
		        	\end{enumerate}
        		\end{multicols}
    """
    # print(correction)
    return(exo,correction)

def exoResoudreEqProduitN2(n=6, id=False):
    if id:
        identification = r"""exoResoudreEqProduitN2\\"""
    else:
        identification = r""""""
    alphabet = list(string.ascii_lowercase)
    lettres = random.sample(alphabet, n)
    lettres.sort()
    eq = r""""""
    eqCorrection = r""""""
    for l in lettres:
        k = nonEqRandomValue(n=4, notNull=True, tier=True)
        k.sort()
        # (ax+b)(cx+d)=
        a = Latex(k[0])
        b = Latex(k[1])
        c = Latex(k[2])
        d = Latex(k[3])
        s = [-k[1]/k[0],-k[3]/k[2]]
        s.sort()
        if k[1]>0:
            b = r"""+"""+b
        if k[3]>0:
            d = r"""+"""+d
        eq = eq + r"""					\item $("""+a+l+b+r""")("""+c+l+d+r""")=0 $
                            \begin{flushright}
                                    $\Longrightarrow S=\lbrace................\rbrace$
                            \end{flushright}
"""
        eqCorrection = eqCorrection + r"""					\item $("""+a+l+b+r""")("""+c+l+d+r""")=0 $
                            \begin{flushright}
                                    $\Longrightarrow S=\lbrace{\color{red} """+Latex(s[0])+r""";"""+Latex(s[1])+r"""}\rbrace$
                            \end{flushright}
"""

    exo=r"""
    """+identification+r"""
            \Question["""+str(n*2)+r"""] Résoudre les équations suivantes :
        		\begin{multicols}{2}
		        	\begin{enumerate}
"""+eq+r"""
		        	\end{enumerate}
        		\end{multicols}
    """
    correction=r"""
    """+identification+r"""
            \Question["""+str(n*2)+r"""] Résoudre les équations suivantes :
        		\begin{multicols}{2}
		        	\begin{enumerate}
"""+eqCorrection+r"""
		        	\end{enumerate}
        		\end{multicols}
    """
    # print(correction)
    return(exo,correction)

def exoCalculeMentalN1(n=6, id=False):
    if id:
        identification = r"""exoCalculeMentalN1\\"""
    else:
        identification = r""""""
    q = r""""""
    rq = r""""""
    for i in range(1,n+1):
        # print(i)
        a = random.randint(1,9)
        b = random.randint(1,9)
        op = random.randint(1,3)
        if op==1:
            operator = " + "
            answer = a+b
        if op==2:
            operator = " - "
            answer = a-b
        if op==3:
            operator = r""" \times """
            answer = a*b
        q = q + r"""
        \item $"""+str(a)+operator+str(b)+r""" = ...............$"""
        rq = rq + r"""
        \item $"""+str(a)+operator+str(b)+r""" = {\color{red}"""+str(answer)+r"""}$"""
    exo = r"""
    """+identification+r"""
    	\Question["""+str(n)+r"""] Calculer les expressions suivantes :
		\begin{multicols}{3}
			\begin{enumerate}
"""+q+r"""
			\end{enumerate}
		\end{multicols}
        """
    correction = r"""
    """+identification+r"""
    	\Question["""+str(n)+r"""] Calculer les expressions suivantes :
		\begin{multicols}{3}
			\begin{enumerate}
"""+rq+r"""
			\end{enumerate}
		\end{multicols}
        """
    # print(exo)
    # print(correction)
    return(exo,correction)

def exoAffineSigneVariation(n=2, id=False):
    if id:
        identification = r"""exoAffineSigneVariation\\"""
    else:
        identification = r""""""
    alphabet = list(string.ascii_lowercase)
    fonctions = random.sample(alphabet, n)
    fonctions.sort()
    exo = r""""""+identification+r"""
    """
    correction = r""""""+identification+r"""
    """
    for f in fonctions:
        k = nonEqRandomValue(n=2, notNull=True, demi=False, tier=False)
        p = affine(f, k[0], k[1])
        exo = exo + r"""
\Question[10] Complétez le tableau de signe et de variation pour \\"""+p.latexString()+r"""\\
    \begin{center}
        \begin{tikzpicture}
            \tkzTabInit{$x$ / 1 , Signe de $"""+p.name+r"""$ / 2, Variation de $"""+p.name+r"""$ / 2}{ , , }
        \end{tikzpicture}
    \end{center}
"""
        correction = correction + r"""
\Question[10] Complétez le tableau de signe et de variation pour \\"""+p.latexString()+r"""\\
    \begin{center}
        \begin{tikzpicture}
            \tkzTabInit{$x$ / 1 , Signe de $"""+p.name+r"""$ / 2, Variation de $"""+p.name+r"""$ / 2}{$-\infty$, ${\color{red}"""+Latex(p.antecedantDe(0))+r"""}$, $+\infty$}
            \tkzTabLine{, \text{{\color{red}"""+Signe(-1*p.a)+r"""} } , {\color{red}0}, \text{{\color{red}"""+Signe(p.a)+r"""}} , }
            \tkzTabVar{"""+Signe(-1*p.a)+r"""/ ${\color{red}"""+Signe(-1*p.a)+r"""\infty}$, R/ 0 , """+Signe(p.a)+r"""/ ${\color{red}"""+Signe(p.a)+r"""\infty}$}
            \tkzTabIma{1}{3}{2}{${\color{red}0}$}
        \end{tikzpicture}
    \end{center}
"""
    # print(exo)
    # print(correction)
    return(exo,correction)

def exoSimpleSysEq1(id=False):
    if id:
        identification = r"""exoSimpleSysEq1\\"""
    else:
        identification = r""""""
    nbMoisBresil, nbMoisPortugal, nbBresil, nbPortugal, nbMots = symbols('nbMoisBresil nbMoisPortugal nbBresil nbPortugal nbMots')
    nbMoisBresil = random.randint(5, 10)
    nbMoisPortugal = random.randint(5, 10)
    nbBresil = random.randint(10,15)*10
    nbPortugal = random.randint(10,15)*10
    nbMots = nbMoisPortugal*nbPortugal+nbMoisBresil*nbBresil
    totMois = nbMoisBresil+nbMoisPortugal
    
    exo=r"""
    """+identification+r"""
    \Question[8] Henri a passé """+str(totMois)+r""" mois en tout au Portugal et au Brésil pour apprendre le portugais.\\
        Au Portugal, il a appris """+str(nbPortugal)+r""" nouveaux mots en moyenne par mois, et au Brésil il a appris """+str(nbBresil)+r""" nouveaux mots en moyenne par mois. Au total, il a appris """+str(nbMots)+r""" nouveaux mots.  
        Combien de temps Henri a-t-il passé au Portugal et combien de temps a-t-il passé au Brésil ?
            \fillwithlines{80mm}
"""
    correction=r"""
    """+identification+r"""
    \Question[8] Henri a passé """+str(totMois)+r""" mois en tout au Portugal et au Brésil pour apprendre le portugais.\\
Au Portugal, il a appris """+str(nbPortugal)+r""" nouveaux mots en moyenne par mois, et au Brésil il a appris """+str(nbBresil)+r""" nouveaux mots en moyenne par mois. Au total, il a appris """+str(nbMots)+r""" nouveaux mots.  
Combien de temps Henri a-t-il passé au Portugal et combien de temps a-t-il passé au Brésil ?

        \begin{solution}

            On peut utiliser les informations données pour établir un système d'équations à deux inconnues.\\
            On note x le nombre de mois passé au Portugal, et y le nombre de mois passé au Brésil.

            En conséquence, on peut écrire la première équation suivante :
            \begin{center}
                $x + y = """+str(totMois)+r"""$\\
                \textit{	Henri a passé """+str(totMois)+r""" mois au total au Portugal et au Brésil}
            \end{center}
            et la seconde équation :
            \begin{center}
                    $"""+str(nbPortugal)+r"""x + """+str(nbBresil)+r"""y = """+str(nbMots)+r"""$\
                    \textit{Henri a appris """+str(nbMots)+r""" mots en tout}
            \end{center}
            On a donc le système d'équation suivant :
            \begin{equation}
                \left\lbrace
                    \begin{aligned}
                        x + y = """+str(totMois)+r"""\\
                        """+str(nbPortugal)+r"""x + """+str(nbBresil)+r"""y = """+str(nbMots)+r"""
                    \end{aligned}
                \right.
            \end{equation}
            Dans la première équation on isole $x$ ce qui donne :
            \begin{equation}
                \left\lbrace
                    \begin{aligned}
                        x = """+str(totMois)+r"""-y\\
                        """+str(nbPortugal)+r"""x + """+str(nbBresil)+r"""y = """+str(nbMots)+r"""
                    \end{aligned}
                \right.
                \end{equation}
            On remplace dans la deuxième équation $x$ par sa nouvelle expression en fonction de $y$ ce qui donne :
            \begin{equation}
                \left\lbrace
                    \begin{aligned}
                        x &= """+str(totMois)+r"""-y\\
                        """+str(nbPortugal)+r"""\times("""+str(totMois)+r"""-y) + """+str(nbBresil)+r"""y &= """+str(nbMots)+r"""
                    \end{aligned}
                \right.
            \end{equation}
            la deuxième équation est maintenant une équation à une seule inconnue, on développe et on simplifie la deuxième équation :
            \begin{equation}
                \left\lbrace
                    \begin{aligned}
                        x &= """+str(totMois)+r"""-y\\
                        """+str(nbPortugal*totMois)+r""" + """+str(nbBresil-nbPortugal)+r"""y &= """+str(nbMots)+r"""
                    \end{aligned}
                \right.
            \end{equation}
            On résout la deuxième équation ce qui donne :
            \begin{equation}
                \left\lbrace
                    \begin{aligned}
                        x &= """+str(totMois)+r"""-y\\
                        y &= \dfrac{"""+str(nbMots)+r"""-"""+str(nbPortugal*totMois)+r"""}{"""+str(nbBresil-nbPortugal)+r"""}="""+str((nbMots-nbPortugal*totMois)/(nbBresil-nbPortugal))+r"""
                    \end{aligned}
                \right.
            \end{equation}
            On remplace cette valeur de y dans la première équation :
            \begin{equation}
                \left\lbrace
                    \begin{aligned}
                        x &= """+str(totMois)+r"""-"""+str(nbMoisBresil)+r""" = """+str(nbMoisPortugal)+r"""\\
                        y &= """+str(nbMoisBresil)+r"""
                    \end{aligned}
                \right.
            \end{equation}
            Donc, Henri a passé """+str(nbMoisPortugal)+r""" mois au Portugal et """+str(nbMoisBresil)+r""" mois au Brésil.
        \end{solution}
"""
    print(exo)
    return(exo,correction)

def exoDerivationN1(n=10, id=False):  # Dérivation de polynômes
                                # Mise en oeuvre de :
                                # (kx^n)'=knx^(n-1) et (f=u+v)'=u'+v'
    if id:
        identification = r"""exoDerivationN1\\"""
    else:
        identification = r""""""
    pts = 2*n
    polynomes = genPolynome(n=10)
    items=r""""""
    itemsCorrection=r""""""
    for polynome in polynomes:
        nom = polynome[0]
        fonction = polynome[1]
        derivee = polynome[2]
        items = items + r"""
        \item $"""+polynome[0]+r"""(x)$="""+fonction._repr_latex_()+r"""\\
            $"""+polynome[0]+r"""'(x)$=............................................\\"""
        itemsCorrection = itemsCorrection + r"""
        \item $"""+polynome[0]+r"""(x)$="""+fonction._repr_latex_()+r"""\\
                $"""+polynome[0]+r"""'(x)$={\color{red}"""+derivee._repr_latex_()+r"""}"""
    exo=r"""
    """+identification+r"""
    \Question[10] Déterminez la dérivée des fonctions suivantes :
			\begin{multicols}{2}
				\begin{enumerate}
   """+items+r"""
				\end{enumerate}
			\end{multicols}
    """
    correction=r"""
    """+identification+r"""
    \Question[10] Déterminez la dérivée des fonctions suivantes :
			\begin{multicols}{2}
				\begin{enumerate}
   """+itemsCorrection+r"""
				\end{enumerate}
			\end{multicols}
    """
    return(exo, correction)

def exoDerivationN2(n=4, id=False):
    if id:
        identification = r"""exoDerivationN2\\"""
    else:
        identification = r""""""
    # Dérivation de polynômes
    # Mise en oeuvre de :
    #   (kx^n)'=knx^(n-1) et (f=u+v)'=u'+v'
    #   (uv)'=u'v+uv'
    # 1 pt pour la formule
    # 1 pt pour u'
    # 1 pt pour v'
    # 2 pts pour la dérivée
    pts=5*n
    alpha = list(string.ascii_lowercase)
    alpha.remove('x')
    alpha.remove('u')
    alpha.remove('v')
    letters = random.sample(alpha, n)
    letters.sort()
    items = r""""""
    itemsCorrection = r""""""
    for i in range(n):
        polynomes = genPolynome(n=2, degreeMin=2, degreeMax=3)
        name = letters[i]
        u = polynomes[0][1]
        uLatex = u._repr_latex_().replace('$', '')
        u1 = polynomes[0][2] # Dérivée de u
        u1Latex = u1._repr_latex_().replace('$', '')
        v = polynomes[1][1]
        vLatex = v._repr_latex_().replace('$', '')
        v1 = polynomes[1][2] # Dérivée de v
        v1Latex = v1._repr_latex_().replace('$', '')
        u1v = u1*v
        u1vSimplified = u1v.expand()._repr_latex_().replace('$', '')
        u1vLatex = u1._repr_latex_().replace('$', '')
        uv1 = u*v1
        uv1Simplified = uv1.expand()._repr_latex_().replace('$', '')
        uv1Latex = uv1._repr_latex_().replace('$', '')
        f = u*v
        f = f.expand()
        fLatex = f._repr_latex_().replace('$', '')
        f1 = sp.diff(f)
        f1Latex = f1._repr_latex_().replace('$', '')
        items = items + r"""
        \item $"""+name+r"""(x)=("""+uLatex+r""")("""+vLatex+r""")$
            \fillwithlines{55mm}"""
        itemsCorrection = itemsCorrection + r"""
        \item $"""+name+r"""(x)=("""+uLatex+r""")("""+vLatex+r""")$\\
            La fonction $"""+name+r"""$ est de la forme $"""+name+r"""(x)=u\times v$ avec :
            \begin{center}
                $u="""+uLatex+r"""$ et $v="""+vLatex+r"""$
            \end{center}
            La dérivée de la fonction $"""+name+r"""$ est $"""+name+r"""'(x)=u'v+uv'$\\
            On détermine $u'$ et $v'$ :
            \begin{align*}
                u'="""+u1Latex+r"""\\
                v'="""+v1Latex+r"""
            \end{align*}
            On a donc :
            \begin{align*}
                """+name+r"""'(x)=(\overbrace{"""+u1Latex+r"""}^{u'})(\overbrace{"""+vLatex+r"""}^{v})+(\overbrace{"""+uLatex+r"""}^{u})(\overbrace{"""+v1Latex+r"""}^{v'})
            \end{align*}
            On développe et on simplifie ce qui donne :
            \begin{align*}
                """+name+r"""'(x)&=("""+u1vSimplified+r""")+("""+uv1Simplified+r""")\\
                \Leftrightarrow """+name+r"""'(x)&="""+f1Latex+r"""
            \end{align*}"""
    # print(items)
    exo=r"""
    \clearpage
    """+identification+r"""
    \Question["""+str(pts)+r"""] Déterminez la dérivée des fonctions suivantes :
        \begin{enumerate}
        """+items+r"""
            \end{enumerate}
    """
    correction=r"""
    \clearpage
    """+identification+r"""
    \Question["""+str(pts)+r"""] Déterminez la dérivée des fonctions suivantes :
        \begin{enumerate}
        """+itemsCorrection+r"""
            \end{enumerate}
    """
    return(exo, correction)

def exoDerivationN3(n=2, id=False):
    if id:
        identification = r"""exoDerivationN3\\"""
    else:
        identification = r""""""
    # Dérivation de polynômes
    # Mise en oeuvre de :
    #   (kx^n)'=knx^(n-1) et (f=u+v)'=u'+v'
    #   (u/v)'=(u'v-uv')/v2
    # 1 pt pour la formule
    # 1 pt pour u'
    # 1 pt pour v'
    # 2 pts pour la dérivée
    pts=5*n
    alpha = list(string.ascii_lowercase)
    alpha.remove('x')
    alpha.remove('u')
    alpha.remove('v')
    letters = random.sample(alpha, n)
    letters.sort()
    items = r""""""
    itemsCorrection = r""""""
    for i in range(n):
        polynomes = genPolynome(n=2, degreeMin=2, degreeMax=3)
        name = letters[i]
        u = polynomes[0][1]
        uLatex = u._repr_latex_().replace('$', '')
        u1 = polynomes[0][2] # Dérivée de u
        u1Latex = u1._repr_latex_().replace('$', '')
        v = polynomes[1][1]
        vLatex = v._repr_latex_().replace('$', '')
        v1 = polynomes[1][2] # Dérivée de v
        v1Latex = v1._repr_latex_().replace('$', '')
        u1v = u1*v
        u1vSimplified = u1v.expand()._repr_latex_().replace('$', '')
        u1vLatex = u1._repr_latex_().replace('$', '')
        uv1 = u*v1
        uv1Simplified = uv1.expand()._repr_latex_().replace('$', '')
        uv1Latex = uv1._repr_latex_().replace('$', '')
        f = u*v
        f = f.expand()
        fLatex = f._repr_latex_().replace('$', '')
        f1 = sp.diff(f)
        f1Latex = f1._repr_latex_().replace('$', '')
        items = items + r"""
        \item $"""+name+r"""(x)=("""+uLatex+r""")("""+vLatex+r""")$
            \fillwithlines{55mm}"""
        itemsCorrection = itemsCorrection + r"""
        \item $"""+name+r"""(x)=("""+uLatex+r""")("""+vLatex+r""")$\\
            La fonction $"""+name+r"""$ est de la forme $"""+name+r"""(x)=u\times v$ avec :
            \begin{center}
                $u="""+uLatex+r"""$ et $v="""+vLatex+r"""$
            \end{center}
            La dérivée de la fonction $"""+name+r"""$ est $"""+name+r"""'(x)=u'v+uv'$\\
            On détermine $u'$ et $v'$ :
            \begin{align*}
                u'="""+u1Latex+r"""\\
                v'="""+v1Latex+r"""
            \end{align*}
            On a donc :
            \begin{align*}
                """+name+r"""'(x)=(\overbrace{"""+u1Latex+r"""}^{u'})(\overbrace{"""+vLatex+r"""}^{v})+(\overbrace{"""+uLatex+r"""}^{u})(\overbrace{"""+v1Latex+r"""}^{v'})
            \end{align*}
            On développe et on simplifie ce qui donne :
            \begin{align*}
                """+name+r"""'(x)&=("""+u1vSimplified+r""")+("""+uv1Simplified+r""")\\
                \Leftrightarrow """+name+r"""'(x)&="""+f1Latex+r"""
            \end{align*}"""
    # print(items)
    exo=r"""
    \clearpage
    """+identification+r"""
    \Question["""+str(pts)+r"""] Déterminez la dérivée des fonctions suivantes :
        \begin{enumerate}
        """+items+r"""
            \end{enumerate}
    """
    correction=r"""
    \clearpage
    """+identification+r"""
    \Question["""+str(pts)+r"""] Déterminez la dérivée des fonctions suivantes :
        \begin{enumerate}
        """+itemsCorrection+r"""
            \end{enumerate}
    """
    return(exo, correction)

def exoVecteurAffine2nd(id=False):
    if id:
        identification = r"""exoVecteurAffine2nd\\"""
    else:
        identification = r""""""
    pts=5
    corpsP = r""""""
    corpsVcorr = r""""""
    corpsV = r""""""
    markPoints = r""""""
    markVector = r""""""
    Points = genPoint(4)
    # print(Points)
    PPoints = Points.copy()
    FPoints = Points.copy()
    
    
    # Fonction affines
    drawFunc = r"""
    """
    Funcs = []
    for i in range(2):
        p1=FPoints.pop(random.randrange(len(FPoints)))
        p2=FPoints.pop(random.randrange(len(FPoints)))
        f = affine(p1[0]+p2[0],1,1)
        f.setFrom2Points(p1[1], p1[2],p2[1], p2[2])
        if f.a>=0:
            Dmin = max(-4.5,f.antecedantDe(-4.5))
            Dmax = min(4.5,f.antecedantDe(4.5))
        else:
            Dmin = max(-4.5,f.antecedantDe(4.5))
            Dmax = min(4.5,f.antecedantDe(-4.5))

        drawFunc = drawFunc + r"""
        \draw[domain="""+str(Dmin)+r""":"""+str(Dmax)+r""", smooth, variable=\x, blue] plot ({\x}, {"""+str(f.a)+r"""*\x+"""+str(f.b)+r"""}) node[below] {$\mathcal{C}_{"""+f.name+r"""}$};
        """
        Funcs.append(f)

    # Vecteurs
    Vs = []
    for i in range(2):
        p1=PPoints.pop(random.randrange(len(PPoints)))
        p2=PPoints.pop(random.randrange(len(PPoints)))
        v = Vecteur(p1[0]+p2[0],p1[1],p1[2],p2[1],p2[2])
        # print(v)
        corpsVcorr = corpsVcorr + r"""
                    $\Point{\vect{"""+v.nom+r"""}}{\color{red}"""+str(v.x)+r"""}{\color{red}"""+str(v.y)+r"""}$\\
"""
        corpsV = corpsV + r"""
                    $\Point{\vect{"""+v.nom+r"""}}{.........}{.........}$\\
"""
        markVector = markVector + r"""
                    \draw[-{Latex[length=4mm, width=2mm]}, very thick, red] ("""+str(v.x1)+r""","""+str(v.y1)+r""") -- ("""+str(v.x2)+r""","""+str(v.y2)+r""") node[below, midway] {$\vect{"""+v.nom+r"""}$};
"""        
        Vs.append(v)
    # Points
    for p in Points:
        corpsP = corpsP + r"""
                    $\Point{"""+p[0]+r"""}{"""+str(p[1])+r"""}{"""+str(p[2])+r"""}$\\
"""
        markPoints = markPoints + r"""
                    \node[mark size=3pt,color=red,left] at ("""+str(p[1])+r""","""+str(p[2])+r""") {$"""+p[0]+r"""$};
					\draw[red,fill=red] ("""+str(p[1])+r""","""+str(p[2])+r""") circle (1pt);
"""
    exo = r"""
    """+identification+r"""
        \Question Les vecteurs et fonctions affines
        \begin{center}
            \begin{tikzpicture}[scale=1.25,cap=round]
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
                
                % The graphic
                \draw[style=help lines,step=0.5cm] (-4.4,-4.4) grid (4.4,4.4);

                \begin{scope}[style=axes]
                    \draw[->] (-4.5,0) -- (4.5,0) node[right] {$x$};
                    \draw[->] (0,-4.5) -- (0,4.5) node[above] {$y$};
                    \draw[->, very thick] (0,0) -- (1,0) node[below, midway] {$\vect{i}$};
                    \draw[->, very thick] (0,0) -- (0,1) node[left, midway] {$\vect{j}$};
                    \draw (0,0) node[left, below] {$O$};
                    \foreach \x/\xtext in {-4, -3, -2, -1, 0, 1, 2, 3, 4}
                        \draw[xshift=\x cm] (0pt,1pt) -- (0pt,-1pt) node[below,fill=white] {\tiny{$\xtext$}};
                    %				
                    \foreach \y/\ytext in {-4, -3, -2, -1, 0, 1, 2, 3, 4}
                        \draw[yshift=\y cm] (1pt,0pt) -- (-1pt,0pt) node[left,fill=white] {\tiny{$\ytext$}};
                \end{scope}
                """+drawFunc+r"""
            \end{tikzpicture}	
        \end{center}
            \begin{parts}
            \Part[4] Dans le repère orthonormée $(O, \vect{i}, \vect{j})$ ci-dessus, placez les points suivants :
                \begin{multicols}{4}
                    \begin{center}
                        """+corpsP+r"""
                    \end{center}
                \end{multicols}
            \Part[6] Représentez les vecteurs suivants en donnant leurs coordonnées :
                \begin{multicols}{2}
                    \begin{center}
"""+corpsV+r"""
                    \end{center}
                \end{multicols}
            \Part[6] Donnez les équations affines des droites suivantes :
                \begin{multicols}{2}
                    La droite $("""+Funcs[0].name+r""")$ :
                    \fillwithlines{55mm}

                    \columnbreak
                    La droite $("""+Funcs[1].name+r""")$ :
                    \fillwithlines{55mm}
                \end{multicols}
		\end{parts}
"""

    correction = r"""
    """+identification+r"""
        \Question Les vecteurs et fonctions affines
        \begin{center}
            \begin{tikzpicture}[scale=1.25,cap=round]
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
                
                % The graphic
                \draw[style=help lines,step=0.5cm] (-4.4,-4.4) grid (4.4,4.4);

                \begin{scope}[style=axes]
                    \draw[->] (-4.5,0) -- (4.5,0) node[right] {$x$};
                    \draw[->] (0,-4.5) -- (0,4.5) node[above] {$y$};
                    \draw[->, very thick] (0,0) -- (1,0) node[below, midway] {$\vect{i}$};
                    \draw[->, very thick] (0,0) -- (0,1) node[left, midway] {$\vect{j}$};
                    \draw (0,0) node[left, below] {$O$};
                    \foreach \x/\xtext in {-4, -3, -2, -1, 0, 1, 2, 3, 4}
                        \draw[xshift=\x cm] (0pt,1pt) -- (0pt,-1pt) node[below,fill=white] {\tiny{$\xtext$}};
                    %				
                    \foreach \y/\ytext in {-4, -3, -2, -1, 0, 1, 2, 3, 4}
                        \draw[yshift=\y cm] (1pt,0pt) -- (-1pt,0pt) node[left,fill=white] {\tiny{$\ytext$}};
                \end{scope}
                
                """+markPoints+r"""
                """+markVector+r"""
                """+drawFunc+r"""
            \end{tikzpicture}	
        \end{center}
            \begin{parts}
            \Part[4] Dans le repère orthonormée $(O, \vect{i}, \vect{j})$ ci-dessus, placez les points suivants :
                \begin{multicols}{4}
                    \begin{center}
                        """+corpsP+r"""
                    \end{center}
                \end{multicols}
            \Part[6] Représentez les vecteurs suivants en donnant leurs coordonnées :
                \begin{multicols}{2}
                    \begin{center}
"""+corpsVcorr+r"""
                    \end{center}
                \end{multicols}
            \Part[6] Donnez les équations affines des droites suivantes :
                \begin{multicols}{2}
                    La droite $("""+Funcs[0].name+r""")$ :
%                    \fillwithlines{55mm}
						Les points $"""+Funcs[0].name[0]+r"""$ et $"""+Funcs[0].name[1]+r"""$ appartiennent à la droite donc leurs coordonnées vérifient l'équation de la droite d'où :\\
$\begin{cases}
"""+str(Funcs[0].ya)+r""" &= a\times """+str(Funcs[0].xa)+r"""+b\\
"""+str(Funcs[0].yb)+r""" &= a\times """+str(Funcs[0].xb)+r"""+b
\end{cases}$\\
En résolvant ce système on trouve a="""+Latex(Funcs[0].a)+r""" et b="""+Latex(Funcs[0].b)+r""" d'où :\\
$\color{red}("""+Funcs[0].name+r""") : y = """+Latex(Funcs[0].a)+r"""x"""+Latex(Funcs[0].b)+r"""$\\


                    \columnbreak
                    La droite $("""+Funcs[1].name+r""")$ :
%                    \fillwithlines{55mm}
						Les points $"""+Funcs[1].name[0]+r"""$ et $"""+Funcs[1].name[1]+r"""$ appartiennent à la droite donc leurs coordonnées vérifient l'équation de la droite d'où :\\
$\begin{cases}
"""+str(Funcs[1].ya)+r""" &= a\times """+str(Funcs[1].xa)+r"""+b\\
"""+str(Funcs[1].yb)+r""" &= a\times """+str(Funcs[1].xb)+r"""+b
\end{cases}$\\
En résolvant ce système on trouve a="""+Latex(Funcs[1].a)+r""" et b="""+Latex(Funcs[1].b)+r""" d'où :\\
$\color{red}("""+Funcs[1].name+r""") : y = """+Latex(Funcs[1].a)+r"""x"""+Latex(Funcs[1].b)+r"""$
                \end{multicols}
		\end{parts}
"""
    return(exo, correction)

def suiteGenerale(id=False):
    if id:
        identification = r"""suiteGenerale\\"""
    else:
        identification = r""""""
    v0 = random.randint(115,130)
    r = random.randint(2,5)
    tx = random.randint(1,6)
    q = 1-tx/100
    ag = random.randint(0,1)
    nbMois = random.randint(2,6)
    
    if ag: # Arithmétique
        question = r"""\Question Une personne décide de suivre un régime amaigrissant qui doit lui permettre de perdre """+str(r)+r""" kg par mois. Son poids initial est de """+str(v0)+r""" kg.\\"""
        q1Answer = r"""\color{red}{La suite est arithmétique car on retire à chaque fois """+str(r)+r""" kg au poids du mois précédent}\color{black}"""
        q2Answer = r"""\begin{center}
                $\color{red}{v_n=v_{n-1}-"""+str(r)+r"""}$
            \end{center}
                        """
        q3Answer = r"""\begin{center}
        \color{red}{$v_"""+str(nbMois)+r"""="""+f"{(v0-nbMois*r):.2f}"+r"""$}\color{black}
    \end{center}"""
    else: # Géométrique
        question=r"""\Question Une personne décide de suivre un régime amaigrissant qui doit lui permettre de perdre """+str(tx)+r"""\% de son poids par mois. Son poids initial est de """+str(v0)+r""" kg.\\"""
        q1Answer = r"""\color{red}{La suite est géométrique car on multiplie à chaque fois par $(1-\dfrac{"""+str(tx)+r"""}{100})$ le poids du mois précédent}\color{black}"""
        q2Answer = r"""\begin{center}
                    $\color{red}{v_n=v_{n-1}\times (1-\dfrac{"""+str(tx)+r"""}{100})}$
                \end{center}
                        """
        q3Answer = r"""\begin{center}
        \color{red}{$v_"""+str(nbMois)+r"""="""+f"{(v0*(q**nbMois)):.2f}"+r"""$}\color{black}
    \end{center}"""
    
    exo=identification+question+r"""
        On pose $v_0="""+str(v0)+r""" kg$ et on note $v_n$ son poids après $n$ mois.
            \begin{parts}
                \Part[1] Quelle est la nature de la suite (cocher la bonne réponse) ?\\
                    \begin{oneparcheckboxes}
                        \choice Arithmétique
                        \choice Géométrique
                        \choice Quelconque
                    \end{oneparcheckboxes}
                \Part[3] Donnez l'expression de $v_n$ en fonction de $v_{n-1}$ :
                \fillwithlines{20mm}
                \Part[2] Donnez le poids de cette personne après """+str(nbMois)+r""" mois (arrondir le résultat au centième) ?
                \fillwithlines{20mm}
        \end{parts}
"""
    correction=identification+question+r"""
    On pose $v_0="""+str(v0)+r""" kg$ et on note $v_n$ son poids après $n$ mois.
        \begin{parts}
            \Part[1] Quelle est la nature de la suite (cocher la bonne réponse) ?\\
                """+q1Answer+r"""
            \Part[3] Donnez l'expression de $v_n$ en fonction de $v_{n-1}$ :
            """+q2Answer+r"""
            \Part[2] Donnez le poids de cette personne après """+str(nbMois)+r""" mois (arrondir le résultat au centième) ?
            """+q3Answer+r"""
    \end{parts}
"""
    return(exo, correction)

def main():
    exo,correction=suiteGenerale()
    print(exo)
    print(correction)
    pass

if __name__ == '__main__':
    main()