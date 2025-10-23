
import numpy as np

class Matrice:
    """
    Class for matrix operations including addition, subtraction,
    multiplication, transposition, and determinant calculation.
    """
    def __init__(self, data):
        if not all(len(row) == len(data[0]) for row in data):
            raise ValueError("Toutes les lignes doivent avoir la même longueur.")
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def __repr__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

    def __add__(self, other):
        """
        Add two matrices.
        Args:
            other (Matrice): The matrix to add.
        Returns:
            Matrice: The resulting matrix after addition.
        Usage:
            .. code-block:: python
            
                A = Matrice([[1, 2], [3, 4]])
                B = Matrice([[5, 6], [7, 8]])
                C = A + B
        Raises:
            TypeError: If the operand is not a Matrice instance.
            ValueError: If the dimensions of the matrices do not match.
        """
        if not isinstance(other, Matrice):
            raise TypeError("L'opérande doit être une instance de Matrice.")
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Les dimensions des matrices doivent correspondre.")
        result = [[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrice(result)

    def __sub__(self, other):
        """
        Subtract two matrices.
        Args:
            other (Matrice): The matrix to subtract.
        Returns:
            Matrice: The resulting matrix after subtraction.
        Raises:
            TypeError: If the operand is not a Matrice instance.
            ValueError: If the dimensions of the matrices do not match.
        Usage:
            A = Matrice([[5, 6], [7, 8]])
            B = Matrice([[1, 2], [3, 4]])
            C = A - B
        """
        if not isinstance(other, Matrice):
            raise TypeError("L'opérande doit être une instance de Matrice.")
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Les dimensions des matrices doivent correspondre.")
        result = [[self.data[i][j] - other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrice(result)

    def __mul__(self, other):
        """
        Multiply matrix by a scalar or another matrix.
        Args:
            other (int, float, Matrice): The scalar or matrix to multiply with.
        Returns:
            Matrice: The resulting matrix after multiplication.
        Raises:
            TypeError: If the operand is not a scalar or Matrice instance.
            ValueError: If the dimensions are not compatible for matrix multiplication.
        Usage:
            .. code-block:: python
            
                A = Matrice([[1, 2], [3, 4]])
                B = Matrice([[5, 6], [7, 8]])
                C = A * 2
                D = A * B
        """
        if isinstance(other, (int, float)):
            result = [[self.data[i][j] * other for j in range(self.cols)] for i in range(self.rows)]
            return Matrice(result)
        elif isinstance(other, Matrice):
            if self.cols != other.rows:
                raise ValueError("Le nombre de colonnes de la première matrice doit être égal au nombre de lignes de la seconde.")
            result = [[sum(self.data[i][k] * other.data[k][j] for k in range(self.cols)) for j in range(other.cols)] for i in range(self.rows)]
            return Matrice(result)
        else:
            raise TypeError("Multiplication supportée uniquement avec un scalaire ou une autre Matrice.")

    def transpose(self):
        """
        Transpose the matrix.
        Args:
            None
        Returns:
            Matrice: The transposed matrix.
        Usage:
            .. code-block:: python
            
                A = Matrice([[1, 2], [3, 4]])
                B = A.transpose()
        """
        result = [[self.data[j][i] for j in range(self.rows)] for i in range(self.cols)]
        return Matrice(result)

    def determinant(self):
        """
        Calculate the determinant of the matrix.
        Args:
            None
        Returns:
            float: The determinant of the matrix.
        Raises:
            ValueError: If the matrix is not square.
        Usage:
            .. code-block:: python
            
                A = Matrice([[1, 2], [3, 4]])
                det = A.determinant()
        """
        if self.rows != self.cols:
            raise ValueError("Le déterminant est défini uniquement pour les matrices carrées.")
        return round(np.linalg.det(np.array(self.data)), 6)

    def is_square(self):
        """
        Check if the matrix is square.
        Returns:
            bool: True if the matrix is square, False otherwise.
        Usage:
            .. code-block:: python
            
                A = Matrice([[1, 2], [3, 4]])
                print(A.is_square())  # True
        """
        return self.rows == self.cols

    def is_identity(self):
        """
        Check if the matrix is an identity matrix.
        Returns:
            bool: True if the matrix is an identity matrix, False otherwise.
        Usage:
            .. code-block:: python
            
                I = Matrice.identity(3)
                print(I.is_identity())  # True
        """
        if not self.is_square():
            return False
        identity = [[1 if i == j else 0 for j in range(self.cols)] for i in range(self.rows)]
        return self.data == identity

    def is_zero(self):
        """
        Check if the matrix is a zero matrix.
        Returns:
            bool: True if the matrix is a zero matrix, False otherwise.
        Usage:
            .. code-block:: python
            
                Z = Matrice.zero(3, 3)
                print(Z.is_zero())  # True
        """
        return all(all(x == 0 for x in row) for row in self.data)

    @classmethod
    def zero(cls, rows, cols):
        """
        Create a zero matrix of given dimensions.
        Args:
            rows (int): Number of rows.
            cols (int): Number of columns.
        Returns:
            Matrice: A zero matrix of specified dimensions.
        Usage:
            .. code-block:: python
            
                Z = Matrice.zero(3, 3)
        """
        return cls([[0 for _ in range(cols)] for _ in range(rows)])

    @classmethod
    def identity(cls, size):
        """
        Create an identity matrix of given size.
        Args:
            size (int): Size of the identity matrix (size x size).
        Returns:
            Matrice: An identity matrix of specified size.
        Usage:
            .. code-block:: python
            
                I = Matrice.identity(3)
        """
        return cls([[1 if i == j else 0 for j in range(size)] for i in range(size)])

if __name__=='__main__':
    # Exemple d'usage

    # Création de matrices
    A = Matrice([[1, 2], [3, 4]])
    B = Matrice([[5, 6], [7, 8]])

    print("Matrice A :")
    print(A)

    print("\nMatrice B :")
    print(B)

    # Addition
    print("\nA + B :")
    print(A + B)

    # Soustraction
    print("\nA - B :")
    print(A - B)

    # Multiplication par un scalaire
    print("\nA * 3 :")
    print(A * 3)

    # Multiplication de matrices
    print("\nA * B :")
    print(A * B)

    # Transposition
    print("\nTranspose(A) :")
    print(A.transpose())

    # Déterminant
    print("\nDet(A) :")
    print(A.determinant())

    # Matrice identité
    I = Matrice.identity(3)
    print("\nMatrice identité 3x3 :")
    print(I)

    # Vérification identité
    print("\nI est une matrice identité :", I.is_identity())

    # Création d'une matrice nulle
    Z = Matrice.zero(3, 3)
    print("\nMatrice nulle 3x3 :")
    print(Z)

    # Vérification matrice nulle
    print("\nZ est une matrice nulle :", Z.is_zero())
