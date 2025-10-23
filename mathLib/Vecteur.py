import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

"""Module Vecteur
    This module defines a 2D/3D vector class with basic operations and plotting capabilities.
"""
class Vecteur:
    def __init__(self, x: float, y: float, z: float = 0.0, name:str=None):
        """
        Initialize a Vecteur instance.
        Parameters:
            x (float): The x component of the vector.
            y (float): The y component of the vector.
            z (float, optional): The z component of the vector. Defaults to 0.0 for 2D vectors.
            name (str, optional): An optional name for the vector.
        Usage:
            v = Vecteur(1, 2, 3, name="v1") # Creates a 3D vector with components (1, 2, 3) and name "v1"
        """
        self.x = x
        self.y = y
        self.z = z
        self.name=name

    def __add__(self, other):
        """
        Add two vectors.
        Parameters:
            other (Vecteur): The vector to add.
        Returns:
            Vecteur: The resulting vector after addition.
        Usage:
            .. code-block:: python

                v1 = Vecteur(1, 2)
                v2 = Vecteur(3, 4)
                v3 = v1 + v2  # Results in Vecteur(4, 6)
        """
        if isinstance(other, Vecteur):
            return Vecteur(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            raise TypeError(f"Unsupported operand type(s) for +: 'Vecteur' and '{type(other).__name__}'")

    def __sub__(self, other):
        """
        Subtract two vectors.
        Parameters:
            other (Vecteur): The vector to subtract.
        Returns:
            Vecteur: The resulting vector after subtraction.
        Usage:
            .. code-block:: python
            
                v1 = Vecteur(4, 5, 6)
                v2 = Vecteur(1, 2, 3)
                v3 = v1 - v2  # Results in Vecteur(3, 3, 3)
        """
        if isinstance(other, Vecteur):
            return Vecteur(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            raise TypeError(f"Unsupported operand type(s) for -: 'Vecteur' and '{type(other).__name__}'")

    def __mul__(self, other):
        """
        Multiply the vector by a scalar or compute the dot product with another vector.
        Parameters:
            other (float or Vecteur): The scalar to multiply by or the vector for dot product.
        Returns:
            Vecteur or float: The resulting vector after scalar multiplication or the dot product result.
        """
        if isinstance(other, (int, float)):
            # Multiplication par un scalaire
            return Vecteur(self.x * other, self.y * other, self.z * other)
        elif isinstance(other, Vecteur):
            # Produit scalaire
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:
            raise TypeError(f"Unsupported operand type(s) for *: 'Vecteur' and '{type(other).__name__}'")

    def __truediv__(self, other):
        """
        Divide the vector by a scalar.
        Parameters:
            other (float): The scalar to divide by.
        Returns:
            Vecteur: The resulting vector after division.
        Raises:
            ZeroDivisionError: If division by zero is attempted.
        Usage:
            .. code-block:: python

                v = Vecteur(2, 4, 6)
                v_divided = v / 2  # Results in Vecteur(1, 2, 3)
        """
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("division by zero")
            return Vecteur(self.x / other, self.y / other, self.z / other)
        else:
            raise TypeError(f"Unsupported operand type(s) for /: 'Vecteur' and '{type(other).__name__}'")

    def cross(self, other):
        """
        Compute the cross product of two vectors.
        Parameters:
            other (Vecteur): The vector to compute the cross product with.
        Returns:
            Vecteur: The resulting vector after the cross product.
        Raises:
            TypeError: If the other operand is not a Vecteur.
        Usage:
            .. code-block:: python
            
                v1 = Vecteur(1, 0, 0)
                v2 = Vecteur(0, 1, 0)
                v3 = v1.cross(v2)  # Results in Vecteur(0, 0, 1)
        """
        if not isinstance(other, Vecteur):
            raise TypeError(f"Unsupported operand type(s) for cross product: 'Vecteur' and '{type(other).__name__}'")
        return Vecteur(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x,
        )

    def norm(self):
        """
        Calculate the norm (magnitude) of the vector.
        Returns:
            float: The norm of the vector.
        Usage:
            .. code-block:: python
            
                v = Vecteur(3, 4, 0)
                magnitude = v.norm()  # Results in 5.0
        """
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def normalize(self):
        """
        Normalize the vector (make it a unit vector).
        Returns:
            Vecteur: The normalized vector.
        Raises:
            ValueError: If attempting to normalize a zero vector.
        Usage:
            .. code-block:: python
            
                v = Vecteur(3, 4, 0)
                v_normalized = v.normalize()  # Results in Vecteur(0.6, 0.8, 0.0)
        """
        norm = self.norm()
        if norm == 0:
            raise ValueError("Cannot normalize a zero vector")
        return self / norm

    def __eq__(self, other):
        """
        Check if two vectors are equal.
        Parameters:
            other (Vecteur): The vector to compare with.
        Returns:
            bool: True if the vectors are equal, False otherwise.
        Usage:
            .. code-block:: python
            
                v1 = Vecteur(1, 2, 3)
                v2 = Vecteur(1, 2, 3)
                are_equal = (v1 == v2)  # Results in True
        """
        if isinstance(other, Vecteur):
            return math.isclose(self.x, other.x) and math.isclose(self.y, other.y) and math.isclose(self.z, other.z)
        else:
            return False

    def __neg__(self):
        """
        Negate the vector.
        Returns:
            Vecteur: The negated vector.
        Usage:
            .. code-block:: python
            
                v = Vecteur(1, -2, 3)
                v_negated = -v  # Results in Vecteur(-1, 2, -3)
        """
        return Vecteur(-self.x, -self.y, -self.z)

    def __repr__(self):
        """
        Official string representation of the Vecteur.
        Returns:
            str: The string representation of the vector.
        Usage:
            .. code-block:: python
            
                v = Vecteur(1, 2, 3)
                repr_str = repr(v)  # Results in "Vecteur(1, 2, 3)
        """
        return f"Vecteur({self.x}, {self.y}, {self.z})"

    def __str__(self):
        """
        Informal string representation of the Vecteur.
        Returns:
            str: The string representation of the vector.
        Usage:
            .. code-block:: python
            
                v = Vecteur(1, 2, 3)
                str_str = str(v)  # Results in "(1, 2, 3)
        """
        return f"({self.x}, {self.y}, {self.z})"

    def plot(self, plt, origin=(0, 0, 0), color='b', label=None):
        """
        Plot the vector using matplotlib.
        Parameters:
            plt: The matplotlib.pyplot module.
            origin (tuple): The origin point from which to plot the vector.
            color (str): The color of the vector in the plot.
            label (str, optional): An optional label for the vector.
        Usage:
            .. code-block:: python
            
                v = Vecteur(1, 2, 3)
                v.plot(plt, origin=(0, 0, 0), color='r', label='v1')
        """
        if self.z != 0:
            # Pour les vecteurs 3D
            ax = plt.gca(projection='3d')
            ax.quiver(
                origin[0], origin[1], origin[2],  # Coordonnées de l'origine
                self.x, self.y, self.z,  # Composantes du vecteur
                color=color
            )
            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_zlabel('Z')
            if label:
                ax.text(
                    origin[0] + self.x, 
                    origin[1] + self.y, 
                    origin[2] + self.z, 
                    label, color=color
                )
        else:
            # Pour les vecteurs 2D
            plt.quiver(
                origin[0], origin[1],  # Coordonnées de l'origine
                self.x, self.y,  # Composantes du vecteur
                angles='xy', scale_units='xy', scale=1, color=color
            )
            plt.xlim(-10, 10)
            plt.ylim(-10, 10)
            plt.xlabel('X')
            plt.ylabel('Y')
            if self.name:
                plt.text(origin[0] + self.x, origin[1] + self.y, self.name, color=color)

if __name__ == '__main__':
     # Exemple d'utilisation
    v1 = Vecteur(x=1, y=2, name="v1")
    v2 = Vecteur(x=4, y=-5, name="v2")
    v3 = v1 + v2
    v3.name="v1+v2"
    # Graphique 2D
    plt.figure()
    v1.plot(plt, color='r')
    v2.plot(plt, color='b')
    v3.plot(plt, color='b', label="v3")
    plt.title("Représentation des vecteurs 2D")
    plt.grid()
    plt.axhline(0, color='black', lw=0.5)
    plt.axvline(0, color='black', lw=0.5)
    plt.gca().set_aspect('equal')
    plt.show()

    