from datetime import datetime
import csv
import json
import os
import argparse
from copy import deepcopy
import subprocess
import shutil
from pathlib import Path
from rich.progress import Progress, BarColumn, TimeRemainingColumn, MofNCompleteColumn
from concurrent.futures import ThreadPoolExecutor, as_completed
from rich.progress import Progress, BarColumn, MofNCompleteColumn, TimeRemainingColumn
import random

from exo2GT import *
from exo1STMG import *
from exoTSTMG import *

def getEleves(fichier):
    """Récupère dans une liste la première colonne d'un CSV sauf la première ligne

    Args:
        fichier (str): Le nom du fichier avec l'extension
                        exemple : 'Export TSTMG1.csv'
    """    
    directory = os.path.dirname(__file__)
    filepath = os.path.join(directory, "csv", fichier)

    listeEleves = []
    with open(filepath, newline='', encoding='utf8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='"')
        for row in spamreader:
            listeEleves.append(row[0])
    
    return listeEleves[1:]

class Examen():
	"""Classe représentant un examen de mathématiques.
	Attributs :
	- title : Titre de l'examen (ex : "Devoir Surveillé n°1")
	- subtitle : Sous-titre de l'examen (ex : "Sujet")
	- dateOfExam : Date de l'examen (objet datetime.date ou chaîne au format "JJ/MM/AAAA")
	- session : Session scolaire (ex : "2024-25")
	- duree : Durée de l'examen (ex : "1 heure")
	- points : Points totaux de l'examen (ex : "23")
	- bonus : Points de bonus (ex : "2")
	- school : Nom de l'établissement scolaire (ex : "Lycée Léonard De Vinci")
	- schoolTown : Ville de l'établissement scolaire (ex : "Tremblay-en-France")
	- teacher : Nom de l'enseignant (ex : "Jean-Robert Humbert")
	- genCode : Code généré pour l'examen (ex : "0000000000")
	- consignes : Liste des consignes pour l'examen
	- exercices : Liste des exercices (chaînes de code à évaluer)
	"""
	def __init__(self,
				title: str = "Devoir",
				subtitle: str = "Sujet",
				dateOfExam = None,
				session: str = "2024-25",
				duree: str = "1 heure",
				points: str = "23",
				bonus: str = "2",
				school: str = "Lycée Léonard De Vinci",
				schoolTown: str = "Tremblay-en-France",
				teacher: str = "Jean-Robert Humbert",
				genCode: str = "0000000000",
				exercices: list = [],
				eleve = None,
				):
		
		self.title = title
		self.subtitle = subtitle
		self.dateOfExam = dateOfExam
		self.session = session
		self.duree = duree
		self.points = points
		self.bonus = bonus
		self.school = school
		self.schoolTown = schoolTown
		self.teacher = teacher
		self.genCode = genCode
		self.consignes = ["La calculatrice est autorisée",
						  "Le téléphone n’est pas autorisé, même comme calculatrice",
						  "Le bonus est accordé selon la qualité de la rédaction et du soin",
						  ]
		self.exercices = exercices
		self.eleve = eleve
		# Gestion de la date et de la session
		if isinstance(dateOfExam, str):
			try:
				# Essaie plusieurs formats possibles (avec ou sans zéro)
				self.dateOfExam = datetime.strptime(dateOfExam, "%d/%m/%Y").date()
			except ValueError:
				try:
					self.dateOfExam = datetime.strptime(dateOfExam, "%d %B %Y").date()
				except ValueError:
					raise ValueError(
						f"Format de date non reconnu : {dateOfExam}. "
						"Utilisez le format JJ/MM/AAAA, ex : '12/09/2024'."
					)
		else:
			# Assume que c'est déjà un objet date
			self.dateOfExam = dateOfExam
		if self.dateOfExam:# Si une date est fournie, calcule la session
			if self.dateOfExam.month >= 9:# Septembre ou plus tard
				self.session = f"{self.dateOfExam.year}-{self.dateOfExam.year + 1}"
			else:# Avant septembre
				self.session = f"{self.dateOfExam.year - 1}-{self.dateOfExam.year}"
	# Date formatée
	def formatted_date(self):
		"""Retourne la date au format JJ/MM/AAAA (pour LaTeX, PDF, etc.)"""
		if self.dateOfExam:
			return self.dateOfExam.strftime("%d/%m/%Y")
		return ""
	# Affichage de l’examen
	def __str__(self):
		return( self.title )
	# Préambule LaTeX
	def preambule(self, correction:bool =False ) -> str:
		"""Retourne le préambule LaTeX commun à tous les examens."""
		latex_preamble = rf"""
% --- Préambule LaTeX ---
%!TEX encoding = UTF-8 Unicode
% !TEX TS-program = lualatex
\documentclass[12pt,%
addpoints,%
%answers%
]{{exam}}
% --- Importation des packages LaTeX ---
\usepackage{{tikz,tkz-tab, tkz-base}}
\usepackage{{tkz-euclide}}
\tikzstyle{{every picture}}+=[remember picture]
\tikzstyle{{na}} = [shape=rectangle,inner sep=0pt]
\usepackage{{pgfplots}}
\pgfplotsset{{every tick label/.append style={{font=\tiny}}}}
\usepackage{{multicol}}
\usepackage{{xcolor}}
\usepackage{{mathtools}}
\usepackage{{enumerate}}
\usepackage{{fourier}}
\usepackage{{xspace}}
\usepackage{{amsmath,amssymb,amstext,makeidx}}
\usepackage{{fancybox}}
\usepackage{{tabularx}}
\usepackage[normalem]{{ulem}}
\usepackage{{pifont}}
\usepackage[euler]{{textgreek}}
\usepackage{{textcomp,enumitem}}
\newcommand{{\euro}}{{\eurologo{{}}}}
%\usepackage{{pst-plot,pst-tree,pst-func,pstricks-add}}
\newcommand{{\R}}{{\mathbb{{R}}}}
\newcommand{{\N}}{{\mathbb{{N}}}}
\newcommand{{\D}}{{\mathbb{{D}}}}
\newcommand{{\Z}}{{\mathbb{{Z}}}}
\newcommand{{\Q}}{{\mathbb{{Q}}}}
\newcommand{{\C}}{{\mathbb{{C}}}}
\usepackage[left=3.5cm, right=3.5cm, top=1.9cm, bottom=2.4cm]{{geometry}}
\newcommand{{\vect}}[1]{{\overrightarrow{{\,\mathstrut#1\,}}}}
\renewcommand{{\theenumi}}{{\textbf{{\arabic{{enumi}}}}}}
\renewcommand{{\labelenumi}}{{\textbf{{\theenumi.}}}}
\renewcommand{{\theenumii}}{{\textbf{{\alph{{enumii}}}}}}
\renewcommand{{\labelenumii}}{{\textbf{{\theenumii.}}}}
\def\Oij{{$\left(\text{{O}}~;~\vect{{\imath}},~\vect{{\jmath}}\right)$}}
\def\Oijk{{$\left(\text{{O}}~;~\vect{{\imath}},~\vect{{\jmath}},~\vect{{k}}\right)$}}
\def\Ouv{{$\left(\text{{O}}~;~\vect{{u}},~\vect{{v}}\right)$}}

\definecolor{{aliceblue}}{{rgb}}{{0.94, 0.97, 1.0}}
\usepackage{{numprint}}
\renewcommand\arraystretch{{1.1}}
\newcommand{{\e}}{{\text{{e}}}}
\usepackage{{enumerate}}

%---Pour les arbres de probabilités----------------------------------------------------
\usepackage{{pstricks,pst-node,pst-tree}}
\usepackage{{pst-plot,pst-tree,pst-func,pstricks-add}}
\usepackage{{graphicx}}
\usepackage{{fancybox}}
\usepackage{{tabularx}}

%---Définition de la page et des marges------------------------------------------------
\setlength{{\paperheight}}{{297mm}}
\setlength{{\paperwidth}}{{210mm}}
\setlength{{\textheight}}{{25.5cm}}
\setlength{{\textwidth}}{{16cm}}
\setlength{{\leftmargin}}{{-1cm}}%
\setlength{{\rightmargin}}{{1cm}}%

%---Définition de l'entête de page et du pied de page----------------------------------
\pagestyle{{headandfoot}}
\firstpageheader{{\parbox{{2cm}}{{Nom : \\ Prénom :}}}}
{{}}
{{\parbox{{2cm}}{{classe :  \\ Date : \today}}}}
\firstpagefooter{{\tiny{{Lycée Léonard De Vinci à Tremblay en France}}}}{{Page \thepage\ / \numpages}}{{\tiny\parbox{{2cm}}{{}} \\Session {self.session}}}
\runningheadrule
\runningfootrule
\lhead{{\parbox{{2cm}}{{Nom : \\ Prénom :}}}}
\chead{{{self.title} \small{{{"""Correction""" if correction else """Sujet"""} - genCode : {self.genCode}}}}}
\rhead{{}}
\runningfooter{{\tiny{{{self.school} à {self.schoolTown}}}}}{{Page \thepage\ / \numpages}}{{\tiny\parbox{{2cm}}{{}} Session {self.session}}}

%---Définition de Question-------------------------------------------------------------
\def\Question{{	
	\renewcommand*{{\questionlabel}}{{\fbox{{Exercice \thequestion : }}}}
	\question
}}
\def\Part{{
	\renewcommand*{{\partlabel}}{{\fbox{{\thepartno : }}}}
	\part
}}
%--------------------------------------------------------------------------------------
% --- Définition du tableau de notes -------------------------------------------------
\appto\parts{{\let\exampart\part\let\part\mypart}}

\def\multiplechoice{{54}}
\def\freeresponse{{46}}
\makeatletter
\ExplSyntaxOn
\seq_new:N \g_part_scores_seq
\tl_new:N \g_grade_table_tl
\int_new:N \g_total_score_int
\int_new:N \g_number_of_scores_int

\NewDocumentCommand\mypart{{o}}{{
	\IfNoValueTF{{#1}}{{\exampart}}{{
		\if@insolution\exampart[#1]
		\else\exampart[#1]
		\tl_set:Nx \l_tmpa_tl {{ \arabic{{question}}\alph{{partno}} }}
		\tl_put_right:Nn \l_tmpa_tl {{&}}
		\tl_put_right:No \l_tmpa_tl {{#1}}
		\tl_put_right:Nn \l_tmpa_tl {{&}}
		\seq_gput_right:No \g_part_scores_seq \l_tmpa_tl
		\int_gadd:Nn \g_total_score_int {{#1}}
		\int_gincr:N \g_number_of_scores_int
		\fi
	}}
}}

\cs_new:Nn \__add_row_to_grade_table:n {{
	\tl_gput_right:Nx \g_grade_table_tl {{\seq_item:Nn \g_part_scores_seq {{#1}}}}
	\tl_gput_right:Nn \g_grade_table_tl {{ & }}
	\tl_gput_right:Nx \g_grade_table_tl {{\seq_item:Nn \g_part_scores_seq {{#1+\g_number_of_scores_int/2}}}}
	\tl_gput_right:Nn \g_grade_table_tl {{\\\hline}}
}}

\NewDocumentCommand\GradeTable{{}}{{
	\int_if_odd:nT {{\g_number_of_scores_int}} {{
		\seq_gput_right:Nn \g_part_scores_seq {{&}}
		\int_ginc:N \g_number_of_scores_int
	}}
	\int_gset:Nn \g_number_of_scores_int {{\g_number_of_scores_int}}
	\int_gadd:Nn \g_total_score_int {{ \multiplechoice }}
	\int_gadd:Nn \g_total_score_int {{ \freeresponse }}
	\tl_gclear:N \g_grade_table_tl
	\int_step_function:nnN {{1}} {{\g_number_of_scores_int/2}} \__add_row_to_grade_table:n
	\begin{{tabular}}{{|c|c|c|c|c|c|}}\hline
		Question & Points~Possibles & Points~Acquis & Question & Points~Possibles & Points~Acquis \\\hline
		\tl_use:N \g_grade_table_tl
		\multicolumn2{{c|}}{{}}&\multicolumn{{2}}{{r|}}{{\textit{{Total}}}}
		& \int_use:N \g_total_score_int & \\\cline{{3-6}}
	\end{{tabular}}
}}
\ExplSyntaxOff
\makeatother
%-------------------------------------------------------------------------------------
%---Définition de Solution-------------------------------------------------------------
\hsword{{Score:}}
\usepackage{{lipsum}}
\usepackage{{mdframed}}
\renewenvironment{{solution}}
{{\begingroup\par\parshape0%
	\begin{{mdframed}}[userdefinedwidth=\textwidth,backgroundcolor=blue!5]
		\textbf{{Solution:}}\enspace\ignorespaces}}
	{{\end{{mdframed}}\par\endgroup}}

\newcommand*{{\Coord}}[3]{{% 
	\ensuremath{{\overrightarrow{{#1}}\, 
		\begin{{pmatrix}} 
			#2\\ 
			#3 
\end{{pmatrix}}}}}}
\newcommand*{{\Point}}[3]{{%
	\ensuremath{{#1\, 
		\begin{{pmatrix}} 
			#2\\ 
			#3 
		\end{{pmatrix}}
	}}
}}
\usepackage[french]{{algorithm2e}}%pseudocode
\usepackage{{scratch3}}
\usepackage{{chemfig}}
\renewcommand{{\thepartno}}{{\arabic{{partno}}}}
\renewcommand{{\thesubpart}}{{\thepartno.\alph{{subpart}}}}
\renewcommand{{\thesubsubpart}}{{\thesubpart.\arabic{{subsubpart}}}}
\newcolumntype{{R}}[1]{{>{{\raggedleft\arraybackslash }}b{{#1}}}}
\newcolumntype{{L}}[1]{{>{{\raggedright\arraybackslash }}b{{#1}}}}
\newcolumntype{{C}}[1]{{>{{\centering\arraybackslash }}b{{#1}}}}
\setlength{{\arrayrulewidth}}{{1pt}}

% --- Début du document ---

"""
		return latex_preamble
	# En-tête et pied de page LaTeX
	def metadata_latex(self, correction:bool =False ) -> str:
		"""Retourne l’en-tête et le pied de page personnalisés."""
		return fr"""
% --- En-tête et pied de page ---
\pagestyle{{headandfoot}}
\firstpageheader{{\parbox{{2cm}}{{Nom : \\ Prénom :}}}}{{}}{{\parbox{{2cm}}{{Classe : \\ Date : {self.dateOfExam}}}}}
\firstpagefooter{{\tiny{{{self.school}}}}}{{Page \thepage\ / \numpages}}{{\tiny{{Session {self.session}}}}}
\runningheadrule
\runningfootrule
\lhead{{\parbox{{2cm}}{{Nom : \\ Prénom :}}}}
\chead{{{self.title} {exam.formatted_date()} \\ \small{{{"""Correction""" if correction else """Sujet"""} – genCode : {self.genCode}}}}}
\rhead{{}}
\runningfooter{{\tiny{{{self.school}}}}}{{Page \thepage\ / \numpages}}{{\tiny{{Session {self.session}}}}}
"""
	# Page de titre LaTeX
	def titlepage_latex(self, correction:bool=False) -> str:
		"""Génère dynamiquement la page de titre LaTeX."""
		return fr"""
% --- Page de titre ---
\begin{{titlepage}}
\newcommand{{\HRule}}{{\rule{{\linewidth}}{{0.5mm}}}}
\center

\textsc{{\LARGE {self.school}}}\\[1cm]
\textsc{{\Large {self.title} \\ \small{{{"""Correction""" if correction else """Sujet"""} - genCode : {self.genCode}}}}}\\[5cm]
\textsc{{\large {self.eleve if self.eleve else ''} }}\\[1cm]
\HRule \\[0.8cm]
{{\huge \bfseries Mathématiques}}\\[0.7cm]
\HRule \\[5cm]

\large
\emph{{Consignes :}}\\[0.5cm]
\fbox{{
\begin{{minipage}}{{\textwidth}}
\begin{{itemize}}%[label=$*$]
	{''.join([f'\n\t\\item {consigne}' for consigne in self.consignes])}
	\item L’examen est noté sur un total de {int(self.points)+int(self.bonus)} points (dont {self.bonus} points de bonus)
	\item L’épreuve dure {self.duree}.
\end{{itemize}}
\end{{minipage}}
}}
\vfill
\end{{titlepage}}

\clearpage

\begin{{questions}}
"""
	# Fin du document LaTeX
	def end_document_latex(self) -> str:
		"""Retourne la fin du document LaTeX."""
		return r"""

        \end{questions}

    \end{document}
	"""
	# Assemble le document complet LaTeX
	def build_exam(self) -> str:
		"""Assemble le document complet LaTeX."""
		#
		sujet_latex = r""""""+self.preambule(correction=False)
		sujet_latex += self.metadata_latex(correction=False)
		sujet_latex += "\n\\begin{document}\n"
		sujet_latex += self.titlepage_latex(correction=False)+"\n"
		
		correction_latex = r""""""+self.preambule(correction=True)
		correction_latex += self.metadata_latex(correction=True)
		correction_latex += "\n\\begin{document}\n"
		correction_latex += self.titlepage_latex(correction=True)+"\n"
		# Ajout des exercices
		for func_call in self.exercices:
			try:
				# ⚠️ eval évalue la chaîne comme du code Python
				exo, correction = eval(func_call)
				sujet_latex += exo + "\n"
				correction_latex += correction + "\n"
			except Exception as e:
				print(f"Erreur lors de l’exécution de {func_call} : {e}")
		# Fin du document
		sujet_latex += self.end_document_latex()
		correction_latex += self.end_document_latex()

		return (sujet_latex, correction_latex)
# -----------------------------------------------------------------------------------
# Compile un fichier LaTeX en PDF
def make_pdf(filepath:str, output_dir:str):
	"""Compile un fichier LaTeX en PDF."""
	subprocess.run(['pdflatex', '-quiet', '-interaction=nonstopmode', f'-output-directory={output_dir}', filepath], cwd=os.path.dirname(filepath))
	subprocess.run(['pdflatex', '-quiet', '-interaction=nonstopmode', f'-output-directory={output_dir}', filepath], cwd=os.path.dirname(filepath))

# Supprime les fichiers auxiliaires générés par LaTeX
def clean_aux_dir(directory: str) -> list[str]:
    d = Path(directory)
    patterns = ["*.aux","*.log","*.out","*.toc","*.nav","*.snm",
                "*.fls","*.fdb_latexmk","*.synctex.gz","*.bbl","*.blg","*.lof","*.lot"]
    removed = []
    for pat in patterns:
        for f in d.glob(pat):
            try:
                f.unlink()
                removed.append(str(f))
            except OSError:
                pass
    return removed

# Déplace les fichiers PDF générés vers un répertoire spécifique
def move_pdfs(source_dir: str, destination_dir: str) -> list[str]:
	"""
	Déplace tous les fichiers PDF du répertoire `source_dir` vers `destination_dir`.
	Crée le répertoire de destination s’il n’existe pas.
	Retourne la liste des fichiers déplacés.
	"""
	src = Path(source_dir)
	dst = Path(destination_dir)
	dst.mkdir(parents=True, exist_ok=True)

	moved_files = []

	for pdf_file in src.glob("*.pdf"):
		try:
			target = dst / pdf_file.name
			shutil.move(str(pdf_file), str(target))
			moved_files.append(str(target))
		except Exception as e:
			print(f"⚠️ Erreur lors du déplacement de {pdf_file.name} : {e}")

	if not moved_files:
		print("Aucun fichier PDF trouvé à déplacer.")
	else:
		print(f"{len(moved_files)} fichier(s) déplacé(s) vers {dst}")

	return moved_files

# Déplace les fichiers TeX générés vers un répertoire spécifique
def move_texs(source_dir: str, destination_dir: str) -> list[str]:
	"""
	Déplace tous les fichiers PDF du répertoire `source_dir` vers `destination_dir`.
	Crée le répertoire de destination s’il n’existe pas.
	Retourne la liste des fichiers déplacés.
	"""
	src = Path(source_dir)
	dst = Path(destination_dir)
	dst.mkdir(parents=True, exist_ok=True)

	moved_files = []

	for pdf_file in src.glob("*.tex"):
		try:
			target = dst / pdf_file.name
			shutil.move(str(pdf_file), str(target))
			moved_files.append(str(target))
		except Exception as e:
			print(f"⚠️ Erreur lors du déplacement de {pdf_file.name} : {e}")

	if not moved_files:
		print("Aucun fichier PDF trouvé à déplacer.")
	else:
		print(f"{len(moved_files)} fichier(s) déplacé(s) vers {dst}")

	return moved_files

# --- Lecture du fichier JSON ---
def load_exam_from_json(filepath: str) -> Examen:
	with open(filepath, "r", encoding="utf-8") as f:
		config = json.load(f)

	meta = config["meta"]
	exercices = config["exercices"]
	return( meta, exercices )

    # # --- Création de l'objet Examen ---
    # exam = Examen(
    #     level=meta["classes"][0],
    #     title=meta["title"],
    #     dateOfExam=meta["dateOfExam"],
    #     genCode="auto-json",
    #     source=meta.get("source", "GenExoV2"),
    # )

    # # --- Construction dynamique de la liste des exercices ---
    # exam.exercices = [
    #     f"{exo_name}()" for exo_name, repeat in exercices.items() for _ in range(repeat)
    # ]

    # # --- Métadonnées supplémentaires (facultatives) ---
    # exam.points = meta.get("points", 0)
    # exam.bonus = meta.get("bonus", 0)
    # exam.duree = meta.get("duree", "—")
    # exam.consignes = meta.get("consignes", [])
    # exam.csv_file = meta.get("CSVfile", None)
    # exam.nb_anonymous = meta.get("nbAnonymous", 0)

if __name__ == "__main__":
	eleves = None
	nb_Generic = 1
	path = os.path.dirname(__file__)
	output_dir_pdf = os.path.join(path, "pdf")
	output_dir_tex = os.path.join(path, "tex")
	# Création du répertoire de sortie s'il n'existe pas
	if not os.path.exists(output_dir_pdf):
		os.makedirs(output_dir_pdf)
		

	# Définition de l’examen ---------------------------------------------------------------
	meta, exercices = load_exam_from_json(os.path.join(path, "20251103-TSTMG.json"))
	title = meta.get("title", "Evaluation")
	dateOfExam =meta.get("dateOfExam", None)
	points = meta.get("points", 0)
	bonus = meta.get("bonus", 0)
	duree = meta.get("duree", "1 heure")
	genCode = str(random.randint(1111111111,9999999999))
	exam = Examen(title=title, dateOfExam=dateOfExam, genCode=genCode, points=points, bonus=bonus, duree=duree)
	consignes = meta.get("consignes", None)
	if consignes:
		exam.consignes = consignes
	else:
		exam.consignes=[
							"La calculatrice n'est pas autorisée",
							"Le téléphone n’est pas autorisé, même comme calculatrice",
							"Le bonus est accordé selon la qualité de la rédaction et du soin",
						]
	
	if exercices:
		exam.exercices = [
		f"{exo['name']}()" for exo in exercices for _ in range(exo.get("repeat", 1))
	]
	else:
		exam.exercices = [
					"exoTableauEvolution()",
					"addClearPage()",
					"evolSchema2()",
					]
	classe = meta.get("classe", None )
	CSVFile = meta.get("CSVfile", None )
	if CSVFile:
		eleves = getEleves(CSVFile)
	if eleves : # Génération pour chaque élève
		directory = os.path.dirname(__file__)
		with Progress(
						"[progress.description]{task.description}",  # texte dynamique
						BarColumn(),
						MofNCompleteColumn(),
						"[progress.percentage]{task.percentage:>3.0f}%",
						TimeRemainingColumn(),
					) as progress:
			task = progress.add_task("Génération PDF", total=len(eleves))
			for eleve in eleves:
				genCode = str(random.randint(1111111111,9999999999))
				exam.genCode = genCode
				progress.update(task, description=f"Génération PDF : [bold cyan]{eleve:<20}[/bold cyan]")
				d = exam.dateOfExam.strftime("%Y%m%d") if exam.dateOfExam else "nodate"
				filepathSujet = os.path.join(output_dir_tex, d+"-Sujet-"+eleve.replace(" ","_"))
				filepathCorrection = os.path.join(output_dir_tex, d+"-Correction-"+eleve.replace(" ","_"))
				exam.eleve = eleve
				sujet, correction = exam.build_exam()
				# Sauvegarde des fichiers LaTeX
				with open(f"{filepathSujet}.tex", "w", encoding="utf-8") as f:
					f.write(sujet)
				with open(f"{filepathCorrection}.tex", "w", encoding="utf-8") as f:
					f.write(correction)
				# Compilation des fichiers LaTeX en PDF
				make_pdf(filepathSujet + '.tex', output_dir_pdf)
				make_pdf(filepathCorrection + '.tex', output_dir_pdf)
				progress.advance(task)
		# Nettoyage des fichiers auxiliaires
		clean_aux_dir(output_dir_pdf)
		# Déplace les PDF dans le répertoire de sortie
		move_pdfs(output_dir_pdf, os.path.join(output_dir_pdf, classe, d))
		move_texs(output_dir_tex, os.path.join(output_dir_pdf, classe, d, "TeXs"))
	nbAnonymous = meta.get("nbAnonymous", 0)
	if nbAnonymous > 0:
		for i in range(nbAnonymous):
			genCode = str(random.randint(1111111111,9999999999))
			exam.genCode = genCode
			sujet, correction = exam.build_exam()
			directory = os.path.dirname(__file__)
			d = exam.dateOfExam.strftime("%Y%m%d") if exam.dateOfExam else "nodate"
			filepathSujet = os.path.join(output_dir_tex, d+"-"+genCode+"-Sujet")
			filepathCorrection = os.path.join(output_dir_tex, d+"-"+genCode+"-Correction")
			# Sauvegarde des fichiers LaTeX
			with open(filepathSujet + '.tex', "w", encoding="utf-8") as f:
				f.write(sujet)
			with open(filepathCorrection + '.tex', "w", encoding="utf-8") as f:
				f.write(correction)
			# Compilation des fichiers LaTeX en PDF
			make_pdf(filepathSujet + '.tex', output_dir_pdf)
			make_pdf(filepathCorrection + '.tex', output_dir_pdf)
			# Nettoyage des fichiers auxiliaires
			clean_aux_dir(output_dir_pdf)
			# Déplace les PDF dans le répertoire de sortie
			move_pdfs(output_dir_pdf, os.path.join(output_dir_pdf, "Generic"))
			move_texs(output_dir_tex, os.path.join(output_dir_pdf, "Generic", "TeXs"))

