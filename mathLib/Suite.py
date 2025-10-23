import sympy as sp

class Suite:
    def __init__(self, expression=None, variable='n', recurrence=None, u0=None):
        """
        Initialise une suite mathématique.
        :param expression: Expression explicite (par exemple, 'n**2 + 1').
        :param variable: Nom de la variable (par défaut 'n').
        :param recurrence: Fonction lambda pour la récurrence (par exemple, lambda u, n: u + 2).
        :param u0: Valeur initiale pour les suites définies par récurrence.
        """
        self.variable = sp.Symbol(variable)
        self.expression = sp.sympify(expression) if expression else None
        self.recurrence = recurrence
        self.u0 = u0

    def term(self, n):
        """
        Calcule le terme u_n de la suite.
        :param n: Indice du terme (doit être un entier non négatif).
        :return: Valeur du terme u_n.
        """
        if n < 0:
            raise ValueError("Index n doit être un entier non négatif.")
        if self.expression:
            # Suite définie explicitement
            return float(self.expression.subs(self.variable, n))
        elif self.recurrence and self.u0 is not None:
            # Suite définie par récurrence
            u = self.u0
            for _ in range(n):
                u = self.recurrence(u, _)
            return u
        else:
            raise ValueError("La suite n'a pas de définition explicite ou récurrente.")

    def sum(self, n):
        """
        Calcule la somme des n premiers termes de la suite.
        :param n: Nombre de termes à sommer.
        :return: Somme des termes de 0 à n inclus.
        """
        if n < 0:
            raise ValueError("Index n doit être un entier non négatif.")
        return sum(self.term(i) for i in range(n + 1))

    def __repr__(self):
        if self.expression:
            return f"Suite explicite: u(n) = {sp.pretty(self.expression)}"
        elif self.recurrence and self.u0 is not None:
            return f"Suite récurrente: u(0) = {self.u0}, u(n) = f(u(n-1), n)"
        else:
            return "Suite non définie"

# Exemple d'utilisation
# Suite explicite : u(n) = n^2 + 1
suite_exp = Suite(expression="n**2 + 1")

# Suite récurrente : u(n) = u(n-1) + 2 avec u(0) = 1
suite_rec = Suite(recurrence=lambda u, n: u + 2, u0=1)

# Affichage
print("Suite explicite :", suite_exp)
print("Suite récurrente :", suite_rec)

# Calcul de termes
print("u(5) (explicite) :", suite_exp.term(5))  # 5^2 + 1 = 26
print("u(5) (récurrente) :", suite_rec.term(5))  # 1, 3, 5, 7, 9, ...

# Somme des n premiers termes
print("Somme des 5 premiers termes (explicite) :", suite_exp.sum(5))  # 1 + 2^2 + 3^2 + ... + 5^2 + 1
print("Somme des 5 premiers termes (récurrente) :", suite_rec.sum(5))  # 1 + 3 + 5 + 7 + 9
