import sympy as sp

"""
This module defines a Fonction class for mathematical functions, allowing for symbolic manipulation,
including addition, subtraction, multiplication, division, differentiation, integration, and evaluation.
"""
class Fonction:
    def __init__(self, expression, variable='x'):

        self.variable = sp.Symbol(variable)
        if isinstance(expression, str):
            self.expression = sp.sympify(expression)
        else:
            self.expression = sp.sympify(expression)

    def __add__(self, other):
        """
        Add two functions or a function and a scalar.
        Args:
            other (Fonction or int or float): The function or scalar to add.
         Returns:
            Fonction: New Fonction instance representing the sum.
        Usage :
            .. code-block:: python
            
                f1 = Fonction("x**2 + 3*x + 2")
                f2 = Fonction("x - 1")
                f3 = f1 + f2
                print(f3)  # Output: x**2 + 4*x + 1
        Raises:
            TypeError: If the other operand is not a Fonction or a scalar.
        """
        if isinstance(other, Fonction):
            return Fonction(self.expression + other.expression, self.variable.name)
        elif isinstance(other, (int, float)):
            return Fonction(self.expression + other, self.variable.name)
        else:
            raise TypeError(f"Unsupported operand type(s) for +: 'Fonction' and '{type(other).__name__}'")

    def __sub__(self, other):
        """
        Subtract two functions or a function and a scalar.
        Args:
            other (Fonction or int or float): The function or scalar to subtract.
        Returns:
            Fonction: New Fonction instance representing the difference.
        Usage :
            .. code-block:: python
            
                f1 = Fonction("x**2 + 3*x + 2")
                f2 = Fonction("x - 1")
                f3 = f1 - f2
                print(f3)  # Output: x**2 + 2*x + 3
        Raises:
            TypeError: If the other operand is not a Fonction or a scalar.
        """
        if isinstance(other, Fonction):
            return Fonction(self.expression - other.expression, self.variable.name)
        elif isinstance(other, (int, float)):
            return Fonction(self.expression - other, self.variable.name)
        else:
            raise TypeError(f"Unsupported operand type(s) for -: 'Fonction' and '{type(other).__name__}'")

    def __mul__(self, other):
        """
        Multiply two functions or a function and a scalar.
        Args:
            other (Fonction or int or float): The function or scalar to multiply.
        Returns:
            Fonction: New Fonction instance representing the product.
        Usage :
            .. code-block:: python
            
                f1 = Fonction("x**2 + 3*x + 2")
                f2 = Fonction("x - 1")
                f3 = f1 * f2
                print(f3)  # Output: x**3 + 2*x**2 - x - 2
        Raises:
            TypeError: If the other operand is not a Fonction or a scalar.
        """
        if isinstance(other, Fonction):
            return Fonction(self.expression * other.expression, self.variable.name)
        elif isinstance(other, (int, float)):
            return Fonction(self.expression * other, self.variable.name)
        else:
            raise TypeError(f"Unsupported operand type(s) for *: 'Fonction' and '{type(other).__name__}'")

    def __truediv__(self, other):
        """
        Divide two functions or a function by a scalar.
        Args:
            other (Fonction or int or float): The function or scalar to divide by.
        Returns:
            Fonction: New Fonction instance representing the quotient.
        Usage :
            .. code-block:: python
            
                f1 = Fonction("x**2 + 3*x + 2")
                f2 = Fonction("x - 1")
                f3 = f1 / f2
                print(f3)  # Output: (x**2 + 3*x + 2) / (x - 1)
        Raises:
            TypeError: If the other operand is not a Fonction or a scalar.
        """
        if isinstance(other, Fonction):
            return Fonction(self.expression / other.expression, self.variable.name)
        elif isinstance(other, (int, float)):
            return Fonction(self.expression / other, self.variable.name)
        else:
            raise TypeError(f"Unsupported operand type(s) for /: 'Fonction' and '{type(other).__name__}'")

    def __neg__(self):
        """
        Returns the negation of the function.
        Returns:
            Fonction: New Fonction instance representing the negated function.
        Usage :
            .. code-block:: python
            
                f1 = Fonction("x**2 + 3*x + 2")
                f2 = -f1
                print(f2)  # Output: -x**2 - 3*x - 2
        """
        return Fonction(-self.expression, self.variable.name)

    def derivative(self):
        """
        Returns the derivative of the function.
        Returns:
            Fonction: New Fonction instance representing the derivative.
        Usage :
            .. code-block:: python
            
                f1 = Fonction("x**2 + 3*x + 2")
                f2 = f1.derivative()
                print(f2)  # Output: 2*x + 3
        """
        return Fonction(sp.diff(self.expression, self.variable), self.variable.name)

    def integral(self):
        """
        Returns the integral of the function.
        Returns:
            Fonction: New Fonction instance representing the integral.
        Usage :
            .. code-block:: python
            
                f1 = Fonction("x**2 + 3*x + 2")
                f2 = f1.integral()
                print(f2)  # Output: (x**3)/3 + (3*x**2)/2 + 2*x
        """
        return Fonction(sp.integrate(self.expression, self.variable), self.variable.name)

    def evaluate(self, value):
        """
        Evaluates the function at a given value.
        Args:
            value (int or float): The value at which to evaluate the function.
        Returns:
            float: The result of the evaluation.
        Usage :
            .. code-block:: python
            
                f1 = Fonction("x**2 + 3*x + 2")
                result = f1.evaluate(2)
                print(result)  # Output: 12.0
        """
        return float(self.expression.subs(self.variable, value))

    def __call__(self, value):
        """
        Allows the function to be called like a regular function.
        Args:
            value (int or float): The value at which to evaluate the function.
        Returns:
            float: The result of the evaluation.
        Usage :
            .. code-block:: python
            
                f1 = Fonction("x**2 + 3*x + 2")
                result = f1(2)
                print(result)  # Output: 12.0
        """
        return self.evaluate(value)

    def __repr__(self):
        """
        Returns a string representation of the Fonction instance.
        Returns:
            str: String representation of the Fonction instance.
        Usage :
            .. code-block:: python
            
                f1 = Fonction("x**2 + 3*x + 2")
                print(repr(f1))  # Output: Fonction(x**2 + 3*x + 2)
        """
        return f"Fonction({sp.pretty(self.expression)})"

    def __str__(self):
        return f"{self.expression}"


if __name__=='__main__':
    # Exemple d'utilisation
    f1 = Fonction("x**2 + 3*x + 2")  # f(x) = x^2 + 3x + 2
    f2 = Fonction("x - 1")  # f(x) = x - 1

    # Affichage
    print("Fonction f1:", f1)  # x^2 + 3*x + 2
    print("Fonction f2:", f2)  # x - 1

    # Addition
    print("Addition:", f1 + f2)  # x^2 + 4*x + 1

    # Soustraction
    print("Soustraction:", f1 - f2)  # x^2 + 2*x + 3

    # Multiplication
    print("Multiplication:", f1 * f2)  # x^3 + 2*x^2 - x - 2

    # Division
    print("Division:", f1 / f2)  # (x^2 + 3*x + 2) / (x - 1)

    # Dérivée
    print("Dérivée de f1:", f1.derivative())  # 2*x + 3

    # Intégrale
    print("Intégrale de f1:", f1.integral())  # (x**3)/3 + (3*x**2)/2 + 2*x

    # Évaluation
    print("Évaluation de f1 en x=2:", f1(2))  # 2**2 + 3*2 + 2 = 12
