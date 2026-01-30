from rich.console import Console
from rich.prompt import Prompt

console = Console()


def main_menu():
    console.print("\n[bold cyan]CLOUD COST OPTIMIZER CLI (2026)[/bold cyan]")
    console.print("1. Create Project Profile")
    console.print("2. Exit")

    return Prompt.ask("Select an option", choices=["1", "2"])


def ask_project_description():
    return Prompt.ask("\nEnter project description")


def ask_user_count():
    return int(Prompt.ask("Monthly active users", default="10000"))


def ask_budget():
    return int(Prompt.ask("Monthly budget (₹)", default="50000"))
