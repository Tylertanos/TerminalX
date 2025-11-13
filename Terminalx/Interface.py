"""
interface.py — TerminalX user interface module
Author: Mr. Tanos
"""

from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from utils import get_time

console = Console()


def show_banner(version: str):
    """Display a fancy banner when TerminalX starts."""
    text = Text()
    text.append("\n🧠 TERMINALX\n", style="bold cyan")
    text.append(f"Version {version}\n", style="yellow")
    text.append(f"Started at {get_time()}\n", style="green")
    console.print(Panel(text, expand=False, border_style="blue"))


def show_prompt(username: str, cwd: str):
    """Return a colored prompt string."""
    return f"[bold cyan]{username}@TerminalX[/][white]:[yellow]{cwd}[/]$ "
You can call these functions from core.py to give TerminalX a polished visual experience.
For example, at the start of core.py:


