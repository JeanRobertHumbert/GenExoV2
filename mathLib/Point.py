class Point():
    def __init__(self, x, y, z=0, nom=""):
        self.x = x
        self.y = y
        self.z = z
        self.nom = nom
        
    def __str__(self) -> str:
        return f"{self.nom}( {self.x:.2f} ; {self.y:.2f} )"
    def __format__(self, format_spec:str):
        match format_spec:
            # You should add this new command in your document context definition
            # for a correct compilation of LaTeX functions.
            # \newcommand{\vect}[1]{\overrightarrow{\,\mathstrut#1\,}}
            case 'Latexnom':
                return(r""""""+self.nom+r"""""")
            case 'Latex2DV':
                return(r""""""+self.nom+r"""\begin{pmatrix} """+str(self.x)+r""" \\ """+str(self.y)+r""" \end{pmatrix}""")
            case 'Latex2DH':
                return(r""""""+self.nom+r"""\left("""+str(self.x)+r""" ; """+str(self.y)+r"""\right)""")
            case 'Latex3DV':
                return(r""""""+self.nom+r"""\begin{pmatrix} """+str(self.x)+r""" \\ """+str(self.y)+r""" \\ """+str(self.z)+r""" \end{pmatrix}""")
            case 'Latex3DH':
                return(r""""""+self.nom+r"""\left("""+str(self.x)+r""" ; """+str(self.y)+r""" ; """+str(self.z)+r"""\right)""")
            case _:
                raise ValueError(f'Unknow format specifier ->{format_spec}...')
    
if __name__=="__main__":
    A = Point(x=4, y=5, nom="A")
    print(A)
    print(f"{A:Latex2DV}")
        