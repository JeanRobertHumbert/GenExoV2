import math
"""
Module for complex number operations.
Provides a Complexe class with methods for addition, subtraction,
multiplication, division, conjugation, modulus, and argument calculation.
"""
class Complexe:
    """Class representing a complex number.
    Attributes:
        real (float): The real part of the complex number.
        imag (float): The imaginary part of the complex number.
    
    Methods:
        __add__(self, other): Addition of two complex numbers.
        __sub__(self, other): Subtraction of two complex numbers.
        __mul__(self, other): Multiplication of two complex numbers.
        __truediv__(self, other): Division of two complex numbers.
        conjugate(self): Returns the conjugate of the complex number.
        modulus(self): Returns the modulus of the complex number.
        argument(self): Returns the argument of the complex number in radians.
    """
    def __init__(self, real: float, imag: float):
        self.real = real
        self.imag = imag
    
    def __add__(self, other):
        """
        Addition of two complex numbers.
        Args:
            other (Complexe or float): The complex number or real number to add.
        Returns:
            Complexe: The result of the addition.
        Usage:
            .. code-block:: python
            
                z1 = Complexe(1, 2)
                z2 = Complexe(3, 4)
                z3 = z1 + z2  # z3 is Complexe(4, 6)
        """
        if isinstance(other, Complexe):
            return Complexe(self.real + other.real, self.imag + other.imag)
        elif isinstance(other, (int, float)):
            return Complexe(self.real + other, self.imag)
        else:
            raise TypeError(f"Unsupported operand type(s) for +: 'Complexe' and '{type(other).__name__}'")

    def __sub__(self, other):
        """
        Subtraction of two complex numbers.
         Args:
            other (Complexe or float): The complex number or real number to subtract.
         Returns:
            Complexe: The result of the subtraction.
        Usage:
            .. code-block:: python
            
                z1 = Complexe(3, 4)
                z2 = Complexe(1, 2)
                z3 = z1 - z2  # z3 is Complexe(2, 2)
        """
        if isinstance(other, Complexe):
            return Complexe(self.real - other.real, self.imag - other.imag)
        elif isinstance(other, (int, float)):
            return Complexe(self.real - other, self.imag)
        else:
            raise TypeError(f"Unsupported operand type(s) for -: 'Complexe' and '{type(other).__name__}'")

    def __mul__(self, other):
        """
        Multiplication of two complex numbers.
         Args: 
            other (Complexe or float): The complex number or real number to multiply.
         Returns:
            Complexe: The result of the multiplication.
        Usage:
            .. code-block:: python
            
                z1 = Complexe(1, 2)
                z2 = Complexe(3, 4)
                z3 = z1 * z2  # z3 is Complexe(-5, 10)
        """
        if isinstance(other, Complexe):
            real_part = self.real * other.real - self.imag * other.imag
            imag_part = self.real * other.imag + self.imag * other.real
            return Complexe(real_part, imag_part)
        elif isinstance(other, (int, float)):
            return Complexe(self.real * other, self.imag * other)
        else:
            raise TypeError(f"Unsupported operand type(s) for *: 'Complexe' and '{type(other).__name__}'")

    def __truediv__(self, other):
        """
        Division of two complex numbers.
         Args:
            other (Complexe or float): The complex number or real number to divide by.
         Returns:
            Complexe: The result of the division.
        Usage:
            .. code-block:: python
            
                z1 = Complexe(1, 2)
                z2 = Complexe(3, 4)
                z3 = z1 / z2  # z3 is Complexe(0.44, 0.08)
        Raises:
            ZeroDivisionError: If division by zero occurs.
        """
        if isinstance(other, Complexe):
            denom = other.real**2 + other.imag**2
            if denom == 0:
                raise ZeroDivisionError("division by zero")
            real_part = (self.real * other.real + self.imag * other.imag) / denom
            imag_part = (self.imag * other.real - self.real * other.imag) / denom
            return Complexe(real_part, imag_part)
        elif isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("division by zero")
            return Complexe(self.real / other, self.imag / other)
        else:
            raise TypeError(f"Unsupported operand type(s) for /: 'Complexe' and '{type(other).__name__}'")

    def __neg__(self):
        """
        Negation of the complex number.
         Returns:
            Complexe: The negated complex number.
        Usage:
            .. code-block:: python
            
                z = Complexe(1, -2)
                neg_z = -z  # neg_z is Complexe(-1, 2)
        """
        return Complexe(-self.real, -self.imag)

    def __eq__(self, other):
        """
        Equality check between two complex numbers.
         Args:
            other (Complexe or float): The complex number or real number to compare.
         Returns:
            bool: True if equal, False otherwise.
        Usage:
            .. code-block:: python
            
                z1 = Complexe(1, 2)
                z2 = Complexe(1, 2)
                z3 = Complexe(2, 3)
                print(z1 == z2)  # True
                print(z1 == z3)  # False
        """
        if isinstance(other, Complexe):
            return self.real == other.real and self.imag == other.imag
        elif isinstance(other, (int, float)):
            return self.real == other and self.imag == 0
        else:
            return False

    def conjugate(self):
        """
        Returns the conjugate of the complex number.
         Returns:
            Complexe: The conjugate of the complex number.
        Usage:
            .. code-block:: python
            
                z = Complexe(3, 4)
                conj_z = z.conjugate()  # conj_z is Complexe(3, -4)
        """
        return Complexe(self.real, -self.imag)

    def modulus(self):
        """
        Returns the modulus of the complex number.
         Returns:
            float: The modulus of the complex number.
        Usage:
            .. code-block:: python
            
                z = Complexe(3, 4)
                mod_z = z.modulus()  # mod_z is 5.0
        """
        return math.sqrt(self.real**2 + self.imag**2)

    def argument(self):
        """
        Returns the argument of the complex number in radians.
         Returns:
            float: The argument of the complex number in radians.
        Usage:
            .. code-block:: python
            
                z = Complexe(1, 1)
                arg_z = z.argument()  # arg_z is 0.7853981633974483 (π/4)
        """
        return math.atan2(self.imag, self.real)

    def __repr__(self):
        """
        String representation of the complex number.
         Returns:
            str: The string representation of the complex number.
        Usage:
            .. code-block:: python
            
                z = Complexe(3, -4)
                print(repr(z))  # "3 - 4i"
        """
        sign = '+' if self.imag >= 0 else '-'
        return f"{self.real} {sign} {abs(self.imag)}i"

    # For convenience, allow complex representation in string form
    def __str__(self):
        """
        String representation of the complex number.
         Returns:
            str: The string representation of the complex number.
        """
        return self.__repr__()


if __name__=='__main__':

    """
    Example usage of the Complexe class.
    """
    z1 = Complexe(3, 4)
    z2 = Complexe(1, -2)

    # Addition
    print("Addition:", z1 + z2)  # 4 + 2i
    # Soustraction
    print("Soustraction:", z1 - z2)  # 2 + 6i
    # Multiplication
    print("Multiplication:", z1 * z2)  # 11 + 2i
    # Division
    print("Division:", z1 / z2)  # -1.4 + 1.8i
    # Conjugaison
    print("Conjugaison:", z1.conjugate())  # 3 - 4i
    # Module
    print("Module:", z1.modulus())  # 5.0
    # Argument
    print("Argument (en radians):", z1.argument())  # 0.9272952180016122 (~53.13°)
