class Polynome:
    def __init__(self, coefficients):
        """
        Initialize a polynomial with given coefficients.
        Coefficients should be a list where the i-th element represents the coefficient for x^i.
        Args:
            coefficients (list of float): Coefficients of the polynomial.
        Usage:
            p = Polynome([1, 0, -2])  # Represents the polynomial 1 - 2x^2
        """
        self.coefficients = coefficients
        self._remove_leading_zeros()

    def _remove_leading_zeros(self):
        """
        Remove leading zeros from the coefficients list to maintain the correct degree.
        """
        while len(self.coefficients) > 1 and self.coefficients[-1] == 0:
            self.coefficients.pop()

    def __repr__(self):
        """
        Return a string representation of the polynomial.
        """
        terms = []
        for i, coef in enumerate(self.coefficients):
            if coef == 0:
                continue
            term = f"{coef}"
            if i == 1:
                term += "x"
            elif i > 1:
                term += f"x^{i}"
            terms.append(term)
        return " + ".join(reversed(terms)) if terms else "0"

    def __add__(self, other):
        """
        Add two polynomials or a polynomial and a scalar.
        Args:
            other (Polynome or float): The polynomial or scalar to add.
        Returns:
            Polynome: The resulting polynomial after addition.
        Usage:
            .. code-block:: python
            
                p1 = Polynome([1, 2])  # 1 + 2x
                p2 = Polynome([3, 4])  # 3 + 4x
                p3 = p1 + p2          # 4 + 6x
                p4 = p1 + 5           # 6 + 2x
        """
        if isinstance(other, Polynome):
            max_deg = max(len(self.coefficients), len(other.coefficients))
            new_coeffs = [0] * max_deg
            for i in range(len(self.coefficients)):
                new_coeffs[i] += self.coefficients[i]
            for i in range(len(other.coefficients)):
                new_coeffs[i] += other.coefficients[i]
            return Polynome(new_coeffs)
        elif isinstance(other, (int, float)):
            new_coeffs = self.coefficients[:]
            new_coeffs[0] += other
            return Polynome(new_coeffs)
        else:
            raise TypeError(f"Unsupported operand type(s) for +: 'Polynome' and '{type(other).__name__}'")

    def __sub__(self, other):
        """
        Subtract two polynomials or a polynomial and a scalar.
        Args:
            other (Polynome or float): The polynomial or scalar to subtract.
        Returns:
            Polynome: The resulting polynomial after subtraction.
        Usage:
            p1 = Polynome([1, 2])  # 1 + 2x
            p2 = Polynome([3, 4])  # 3 + 4x
            p3 = p1 - p2          # -2 - 2x
            p4 = p1 - 5           # -4 + 2x
        """
        if isinstance(other, Polynome):
            return self + (-other)
        elif isinstance(other, (int, float)):
            return self + (-other)
        else:
            raise TypeError(f"Unsupported operand type(s) for -: 'Polynome' and '{type(other).__name__}'")

    def __neg__(self):
        """
        Negate the polynomial.
        Returns:
            Polynome: The negated polynomial.
        Usage:
            p = Polynome([1, -2, 3])  # 1 - 2x + 3x^2
            neg_p = -p                # -1 + 2x - 3x^2
        """
        return Polynome([-coef for coef in self.coefficients])

    def __mul__(self, other):
        """
        Multiply two polynomials or a polynomial and a scalar.
        Args:
            other (Polynome or float): The polynomial or scalar to multiply.
        Returns:
            Polynome: The resulting polynomial after multiplication.
        Usage:
            .. code-block:: python
            
                p1 = Polynome([1, 2])  # 1 + 2x
                p2 = Polynome([3, 4])  # 3 + 4x
                p3 = p1 * p2          # 3 + 10x + 8x^2
                p4 = p1 * 5           # 5 + 10x
        """
        if isinstance(other, Polynome):
            new_coeffs = [0] * (len(self.coefficients) + len(other.coefficients) - 1)
            for i, coef1 in enumerate(self.coefficients):
                for j, coef2 in enumerate(other.coefficients):
                    new_coeffs[i + j] += coef1 * coef2
            return Polynome(new_coeffs)
        elif isinstance(other, (int, float)):
            return Polynome([coef * other for coef in self.coefficients])
        else:
            raise TypeError(f"Unsupported operand type(s) for *: 'Polynome' and '{type(other).__name__}'")

    def __truediv__(self, other):
        """
        Divide two polynomials or a polynomial by a scalar.
        Args:
            other (Polynome or float): The polynomial or scalar to divide by.
        Returns:
            Polynome: The resulting polynomial after division.
        Usage:
            .. code-block:: python
            
                p1 = Polynome([1, -2, 3])  # 1 - 2x + 3x^2
                p2 = Polynome([1, -1])     # 1 - x
                quotient, remainder = p1 / p2  # Quotient and remainder of the division
                p3 = p1 / 2                # (0.5 - x + 1.5x^2)
        """
        if isinstance(other, Polynome):
            dividend = self.coefficients[:]
            divisor = other.coefficients[:]
            if divisor == [0]:
                raise ZeroDivisionError("division by zero polynomial")
            quotient = [0] * (len(dividend) - len(divisor) + 1)
            while len(dividend) >= len(divisor):
                lead_coeff_ratio = dividend[-1] / divisor[-1]
                degree_diff = len(dividend) - len(divisor)
                quotient[degree_diff] = lead_coeff_ratio
                for i in range(len(divisor)):
                    dividend[degree_diff + i] -= divisor[i] * lead_coeff_ratio
                while dividend and dividend[-1] == 0:
                    dividend.pop()
            return Polynome(quotient), Polynome(dividend)
        elif isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("division by zero")
            return Polynome([coef / other for coef in self.coefficients])
        else:
            raise TypeError(f"Unsupported operand type(s) for /: 'Polynome' and '{type(other).__name__}'")

    def __eq__(self, other):
        """
        Check if two polynomials are equal.
        Args:
            other (Polynome or float): The polynomial or scalar to compare.
        Returns:
            bool: True if equal, False otherwise.
        Usage:
            .. code-block:: python
            
                p1 = Polynome([1, 2])  # 1 + 2x
                p2 = Polynome([1, 2])  # 1 + 2x
                p3 = Polynome([2, 3])  # 2 + 3x
                print(p1 == p2)  # True
                print(p1 == p3)  # False
                print(p1 == 1)   # False
        """
        if isinstance(other, Polynome):
            return self.coefficients == other.coefficients
        elif isinstance(other, (int, float)):
            return self.coefficients == [other]
        else:
            return False

    def evaluate(self, x):
        """
        Evaluate the polynomial at a given value of x.
        Args:
            x (float): The value at which to evaluate the polynomial.
        Returns:
            float: The result of the polynomial evaluation.
        Usage:
            p = Polynome([1, -2, 3])  # 1 - 2x + 3x^2
            result = p.evaluate(2)    # 1 - 4 + 12 = 9
        """
        return sum(coef * (x ** i) for i, coef in enumerate(self.coefficients))

    def derivative(self):
        """
        Compute the derivative of the polynomial.
        Returns:
            Polynome: The derivative polynomial.
        Usage:
            .. code-block:: python
            
                p = Polynome([1, -2, 3])  # 1 - 2x + 3x^2
                dp = p.derivative()       # -2 + 6x
        """
        if len(self.coefficients) <= 1:
            return Polynome([0])
        new_coeffs = [i * coef for i, coef in enumerate(self.coefficients)][1:]
        return Polynome(new_coeffs)

    def __call__(self, x):
        """
        Allow the polynomial to be called as a function to evaluate it.
        Args:
            x (float): The value at which to evaluate the polynomial.
        Returns:
            float: The result of the polynomial evaluation.
        Usage:
            .. code-block:: python
            
                p = Polynome([1, -2, 3])  # 1 - 2x + 3x^2
                result = p(2)             # 1 - 4 + 12 = 9
        """
        return self.evaluate(x)


if __name__=='__main__':
    # Exemple d'utilisation
    p1 = Polynome([1, -2, 3])  # 1 - 2x + 3x^2
    p2 = Polynome([0, 4, -1])  # 4x - x^2

    # Affichage
    print("Polynôme p1:", p1)  # 3x^2 - 2x + 1
    print("Polynôme p2:", p2)  # -x^2 + 4x

    # Addition
    print("Addition:", p1 + p2)  # 2x^2 + 2x + 1

    # Soustraction
    print("Soustraction:", p1 - p2)  # 4x^2 - 6x + 1

    # Multiplication
    print("Multiplication:", p1 * p2)  # -3x^4 + 10x^3 - 11x^2 + 4x

    # Division
    quotient, remainder = p1 / Polynome([1, -1])  # Divise p1 par (x - 1)
    print("Quotient:", quotient)  # 3x + 1
    print("Reste:", remainder)  # 4

    # Dérivée
    print("Dérivée de p1:", p1.derivative())  # 6x - 2

    # Évaluation
    print("Évaluation de p1 en x=2:", p1(2))  # 1 - 4 + 12 = 9
