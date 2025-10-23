import subprocess
from pathlib import Path
import tempfile
from exo1STMG import *

def generate_exercise_thumbnail(latex_code: str, output_dir: str, name: str = "exo_preview"):
    """
    Compile un exercice LaTeX (TikZ inclus) en miniature PNG.
    Nécessite : pdflatex + ImageMagick ('magick' ou 'convert') installés.
    """
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # Fichier temporaire LaTeX minimal (classe standalone = idéal pour les extraits TikZ)
    tex_content = rf"""
\documentclass[border=2pt]{{standalone}}
\usepackage{{amsmath,amssymb,tikz,pgfplots,array}}
\pgfplotsset{{compat=newest}}
\begin{{document}}
{latex_code}
\end{{document}}
"""
    tex_file = output_path / f"{name}.tex"
    pdf_file = output_path / f"{name}.pdf"
    png_file = output_path / f"{name}.png"

    tex_file.write_text(tex_content, encoding="utf-8")

    # Compilation silencieuse
    proc = subprocess.run(
        ["pdflatex", "-interaction=nonstopmode", tex_file.name],
        cwd=output_path,
        capture_output=True,
        text=True
    )
    # print(proc.stdout)
    # print(proc.stderr)

    # Conversion du PDF en miniature PNG
    subprocess.run([
        "magick", #"convert",
        "-density", "200", str(pdf_file),
        "-resize", "40%", "-quality", "90",
        str(png_file)
    ], check=True)

    print(f"✅ Miniature générée : {png_file}")
    return png_file

if __name__ == "__main__":
    exercice = "exoP1Type10"
    exo, _ = eval(f"{exercice}()")
    generate_exercise_thumbnail(exo, "/Users/jrh/Documents/00-PyDev/GenExoV2/tmp", f"{exercice}")