from rich.console import Console
from rich.table import Table

console = Console()

table = Table(title="Exemple de Table")

table.add_column("Nom", justify="left", style="cyan", no_wrap=True)
table.add_column("Âge", justify="center", style="magenta")
table.add_column("Ville", justify="right", style="green")

table.add_row("Alice", "30", "Paris")
table.add_row("Bob", "25", "Lyon")
table.add_row("Charlie", "35", "Marseille")

console.print(table)
