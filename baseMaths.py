import os,sys
import random
import unicodedata
import numpy as np
import sympy as sp
from sympy.plotting import plot
import matplotlib.pyplot as plt
from fractions import Fraction
import math
import string

sign = lambda x: -1 if x < 0 else 1

carreP = [1, 2, 4, 9, 16, 25, 36]

def lagrange_interpolation(points, x):
    n = len(points)
    polynomial = 0
    for i in range(n):
        xi, yi = points[i]
        # Construction de la base de Lagrange
        li = 1
        for j in range(n):
            if i != j:
                xj, _ = points[j]
                li *= (x - xj) / (xi - xj)
        # Ajout du terme yi * li(x)
        polynomial += yi * li
    return polynomial

def ratio2Dfrac(a:sp.Rational):
    if a.denominator==1 or a.denominator==-1:
        return """"""

def genPoint(n=1):
    Alphabet = sorted(random.sample(list(string.ascii_uppercase),n))
    xCoord = list(range(-4, 5))
    yCoord = list(range(-4, 5))
    answers=[]
    for i in range(min(n,len(xCoord))):
        randL = Alphabet[i]
        randX = xCoord.pop(random.randrange(len(xCoord)))
        randY = yCoord.pop(random.randrange(len(yCoord)))
        answers.append([randL, randX, randY])
    return(answers)

class Vecteur:
    def __init__(self, nom, x1, y1, x2, y2):
        self.nom = nom
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x = self.x2-self.x1
        self.y = self.y2-self.y1
        self.norme = math.sqrt(self.x**2+self.y**2)

    def latexNom(self):
        return("\\"+self.nom)

    def __str__(self):
        return("\\"+self.nom + " ("+str(self.x)+";"+str(self.y)+")")

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

class affine:
    def __init__(self,name, a, b):
        self.name = name
        self.a = a
        self.b = b
    def __str__(self):
        return(str(self.a) + "*x + "+str(self.b))
    
    def setFrom2Points(self, xa, ya, xb, yb): 
        if (xb-xa)!=0:
            self.a = sp.Rational((yb-ya),(xb-xa))
            self.b = ya-self.a*xa
            self.xa = xa
            self.ya = ya
            self.xb = xb
            self.yb = yb
        else:
            return(None)
        
    def setFromPointVector(self, xa, ya, xu, yu):
        if (xu)!=0:
            self.a = yu/xu
            self.b = ya-self.a*xa
        else:
            return(None)
        
    def imageDe(self, x):       #   Retourne l'image de x par la fonction affine
        return(self.a*x+self.b)
    
    def antecedantDe(self, y):  #   Retourne l'antécédant y par la fonction affine
        if self.a!=0:
            return((y-self.b)/self.a)
        else:
            return(None)
        
    def supTo(self, value=0):   #   Retourne la solution à ax+b>=value (value-b)/a
        if self.a!=0:
            return((value-self.b)/self.a)
        else:
            return(math.inf)
        
    def latexString(self):      #   Retourne la chaine LaTeX de la fonction affine
        out = "$"               #   encapsulée avec un $
        out = out + self.name + '(x)='
        if sp.Rational(self.a).denominator==1:
            if abs(self.a)==1:
                if self.a<0:
                    out = out + "-"
            else:
                out = out + str(abs(self.a))
        else:
            out = out + "\\dfrac{"+str(sp.Rational(self.a).numerator)+"}{"+str(sp.Rational(self.a).denominator)+"}"
        out = out + "x"
        
        if self.b>0:
            out = out + " + "
        if sp.Rational(self.b).denominator==1:
            out = out + str(self.b)
        else:
            if self.b<0:
                out = out + " - "
            out = out + "\\dfrac{"+str(sp.Rational(abs(self.b)).numerator)+"}{"+str(sp.Rational(self.b).denominator)+"}"
        out = out + "$"
        return(out)
    
    def latexString1(self):      #   Retourne la chaine LaTeX de la fonction affine
        out = ""               #   encapsulée avec un $
        # out = out + self.name + '(x)='
        if sp.Rational(self.a).denominator==1:
            if abs(self.a)==1:
                if self.a<0:
                    out = out + "-"
            else:
                out = out + str(abs(self.a))
        else:
            out = out + "\\dfrac{"+str(sp.Rational(self.a).numerator)+"}{"+str(sp.Rational(self.a).denominator)+"}"
        out = out + "x"
        
        if self.b>0:
            out = out + " + "
        if sp.Rational(self.b).denominator==1:
            out = out + str(self.b)
        else:
            if self.b<0:
                out = out + " - "
            out = out + "\\dfrac{"+str(sp.Rational(abs(self.b)).numerator)+"}{"+str(sp.Rational(self.b).denominator)+"}"
        # out = out + "$"
        return(out)
    def intersection(self, droite):
        if (self.a-droite.a)!=0:
            xSol = (sp.Rational(droite.b)-sp.Rational(self.b))/(sp.Rational(self.a)-sp.Rational(droite.a))
            ySol = self.imageDe(xSol)
            return(xSol, ySol)
        else:
            return(False)

def Latex(expression):
    # if len(expression)>=0:
    return(sp.latex(expression).replace("frac","dfrac"))
    # else:
    #     return(sp.latex(expression).replace("frac","dfrac"))

def nonEqRandomValue(n=1, debut=-3, fin=3, demi=True,quart=True, tier=True, notNull=True):
    """Retourne une liste de n valeurs aléatoires uniques au format sympy Rational

    Args:
        n (int, optional): nombre de valeurs à retourner
        debut (int, optional): Début de l'interval. Defaults to -4.
        fin (int, optional): Fin de l'interval. Defaults to 4.
        notNull (bool, optional): si True, pas de valeurs nulles. Defaults to False.
    """
    values = []
    a = sp.Rational(debut)
    b = sp.Rational(fin)

    v = a
    while v<b:
        values.append(v)
        if tier :
            values.append(sp.Rational(v)+sp.Rational(1, 3))
            values.append(sp.Rational(v)+sp.Rational(2, 3))
        if demi :
            values.append(sp.Rational(v+1/2))
        if quart : 
            values.append(sp.Rational(v+1/4))
            values.append(sp.Rational(v+3/4))
        v = v + 1
    values.append(b)
    if notNull:
        values = [v for v in values if v != 0]
    reponse = []
    for i in range(0,n):
        ind = np.random.randint(0,len(values))
        reponse.append(values[ind])
        values.remove(values[ind])
    
    return(reponse)

def gen2ndDeg2Roots():
    Delta=0
    while not(Delta>0):
        x, a, b, c = sp.symbols('x a b c')
        xa, xb, xc = sp.symbols('xa xb xc')
        ya, yb, yc = sp.symbols('ya yb yc')
        
        xa = sp.Rational(np.random.randint(1,6)*-1/2)
        ya = 0.0
        xc = sp.Rational(np.random.randint(1,6)*1/2)
        yc = 0.0
        xb = (xa+xc)/2.0
        yb = np.random.randint(-4,4)
        if yb==0:
            yb=-1
        equations = [
            sp.Eq( xa**2*a+xa*b+c ,  ya ),
            sp.Eq( xb**2*a+xb*b+c ,  yb ),
            sp.Eq( xc**2*a+xc*b+c ,  yc )
        ]
        solution = sp.solve(equations, rational=True)
        print(solution)
        a = sp.Rational(solution[a])
        b = sp.Rational(solution[b])
        c = sp.Rational(solution[c])
        while c==0:
            xa = sp.Rational(np.random.randint(1,6)*-1/2)
            ya = 0.0
            xc = xa+np.random.randint(1,int(8-xa))
            yc = 0.0
            xb = (xa+xc)/2.0
            yb = np.random.randint(-4,4)
            equations = [
                sp.Eq( xa**2*a+xa*b+c ,  ya ),
                sp.Eq( xb**2*a+xb*b+c ,  yb ),
                sp.Eq( xc**2*a+xc*b+c ,  yc )
            ]
            solution = sp.solve(equations, rational=True)
            print(solution)
            a = sp.Rational(solution[a])
            b = sp.Rational(solution[b])
            c = sp.Rational(solution[c])
        
        Delta = b**2-4*a*c

    rDelta = sp.sqrt(b**2-4*a*c)
    x1 = sp.Rational((-b-rDelta)/(2*a))
    x2 = sp.Rational((-b+rDelta)/(2*a))
    S = -b/a
    P = c/a
    f = a*x**2+b*x+c
    f1 = a*(x-x1)*(x-x2)
    f2 = a*((x+b/(2*a))**2-(b**2-4*a*c)/(2*a))
    result = {'f':f, 'f1':f1, 'f2':f2, 'x1':x1, 'x2':x2, 'a':a, 'b':b, 'c':c, 'Delta':Delta, 'rDelta':rDelta, 'S':S, 'P':P}
    return(result)

def Signe(x):
    if x >= 0: 
        return '+'
    else:
        return '-'

def genVecteurs(n=6, xmin=-6, ymin=-6, xmax=6, ymax=6):
    lettresGrecs = ["alpha","beta","gamma","delta","epsilon","zeta","eta","theta","iota","kappa","lambda","mu","nu","xi","pi","rho","sigma","tau","upsilon","phi","chi","psi","omega"]
    letters = random.sample(lettresGrecs, n)
    letters.sort()
    v = []
    for l in letters:
        x1 = random.randint(xmin,xmax)
        y1 = random.randint(ymin,ymax)
        if x1>=0:
            x2 = x1+random.randint(-6,-1)
        else:
            x2 = x1+random.randint(1,6)
        if y1>=0:
            y2 = y1+random.randint(-6,-1)
        else:
            y2 = y1+random.randint(1,6)
        myV = Vecteur(l,x1,y1,x2,y2)
        v.append(myV)
    return(v)

def test():
    n=10
    alphabet = list(string.ascii_lowercase)
    fonctions = random.sample(alphabet, n)
    fonctions.sort()
    print(fonctions)
    for f in fonctions:
        k = nonEqRandomValue(n=2, notNull=True, tier=True)
        p = affine(f, k[0], k[1])
        pos=0.55
        # if p.a>0:
        #     pos = min(0.95,0.45+p.supTo(5)/10)
        if p.a<0:
            pos = max(0.1,0.45+p.supTo(5)/10)
            print("("+str(p.a)+";"+str(p.b)+") -> "+str(p.supTo(5).evalf()))
            ret = r"""\addplot[thick] {"""+str(p.a)+r"""*x+"""+str(p.b)+r"""} node[above, sloped, pos = """+str(pos)+r"""] {$\mathcal{C}_"""+p.name+r"""$};"""
            print(ret)

def calculer_facteurs_premiers(nombre):
    facteurs_premiers = []
    i = 2
    while nombre > 1:
        while nombre % i == 0:
            facteurs_premiers.append(i)
            nombre = nombre / i
        i = i + 1
    return facteurs_premiers

def genPolynome(degreeMin=2, degreeMax=3, n=5):
    alpha = list(string.ascii_lowercase)
    letters = random.sample(alpha, n)
    letters.sort()
    retour=[]
    for i in range(n):
        x = sp.symbols('x')
        degree=random.randint(degreeMin,degreeMax)
        p = sp.random_poly(x, degree, -5, 5)
        p1 = sp.diff(p,x)
        retour.append([letters[i], p, p1])
    return(retour)

def generate_crossing_points(xMin=-9, xMax=9, yMin=-9, yMax=9):
    points = []
    x = xMin
    step_x = 1
    y = int(random.uniform(yMin/2, yMax/2))
    points.append((x, y))
    last_y = y
    x = x + step_x
    mean = [0]
    last_mean = [0]
    move = random.choice([-4, -3.5, -3, -2.5, -2, -1.5, 1.5, 2, 2.5, 3, 3.5, 4])
    last_move=0
    mean.append(move)
    while x <= xMax:
        if sum(last_mean) / len(last_mean) > sum(mean) / len(mean) :
            move=move*-1
        y = last_y + move#random.uniform(-3, 3)
        if y>9 : y=9
        if y<-9 : y=-9
        # Vérifier si y et last_y sont de signes différents (franchissement de l'axe des abscisses)
        if y * last_y < 0:  # Signes opposés, donc franchissement
            # On s'assure que le franchissement se fasse sur une abscisse entière ou demi
            crossing_x = x + 0.5 if x % 1 == 0 else x
            points.append((crossing_x, 0))  # Ajouter le point de franchissement
        else:
            # Ajouter le nouveau point
            points.append((x, y))
        last_move=move
        move = random.choice([-4, -3.5, -3, -2.5, -2, -1.5, 1.5, 2, 2.5, 3, 3.5, 4])
        last_y = y
        x = x + step_x

    # Trier les points en fonction de l'abscisse
    points = sorted(points, key=lambda point: point[0])

    return points




class Ssuite():
    def __init__(self, type='A', U0=0, raison=0, k=0, name='u'):
        # type = 'A', 'G' ou 'Q'
        #       'A' Un = U0+n*raison
        #       'G' Un = U0*raison**n
        # TODO: 'Q' 
        self.type = type
        self.U0 = U0
        self.raison = raison
        self.name=name
        self.k = k
    
    def __str__(self):
        if self.type=='A':
            return(f"${self.name}_n={self.name}_{n-1}+({self.raison})")
        elif self.type=='G':
            return(f"${self.name}_n={self.name}_{n-1}\times ({self.raison})")
        pass







if __name__=="__main__":
    # vecteurs = genVecteurs()
    # p=affine("AB",1,1)
    # p.setFrom2Points(1,1,3,3)
    print(generate_crossing_points())

