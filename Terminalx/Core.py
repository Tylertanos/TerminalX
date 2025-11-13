"""
core.py — Core engine for TerminalX
Author: Mr. Tanos
"""

import os
import sys
from rich.console import Console
from utils import log, clear_screen, parse_command, command_not_found, get_time
import commands  # your commands.py module

console = Console()


class TerminalX:
    def __init__(self):
        self.running = True
        self.username = os.getenv("USER") or "User"
        self.cwd = os.getcwd()
        self.prompt_symbol = ">"
        self.version = "1.0.0"

    # ---------------------------
    # MAIN LOOP
    # ---------------------------
    def start(self):
        clear_screen()
        log(f"🧠 TerminalX v{self.version} started at {get_time()}", "green")
        console.print(f"Welcome, {self.username}!\nType [bold yellow]help[/] for commands.\n")

        while self.running:
            try:
                user_input = console.input(f"[bold cyan]{self.username}@TerminalX[/][white]:~$ [/]")
                if not user_input.strip():
                    continue

                command, args = parse_command(user_input)

                if command in commands.command_map:
                    func = commands.command_map[command]
                    func(self, *args)
                else:
                    command_not_found(command)

            except KeyboardInterrupt:
                self.exit()
            except Exception as e:
                log(f"Error: {e}", "red")

    # ---------------------------
    # CONTROL FUNCTIONS
    # ---------------------------
    def stop(self):
        """Stop TerminalX gracefully."""
        self.running = False

    def exit(self):
        """Alias to stop with message."""
        log("Exiting TerminalX...", "yellow")
        self.stop()


# ---------------------------
# ENTRY POINT
# ---------------------------
if __name__ == "__main__":
    shell = TerminalX()
    shell.start()
⚙️ How It Works
TerminalX.start() begins the main REPL loop.

Reads user input → parses it using parse_command() from utils.py.

Looks up the command in commands.command_map.

If found → runs the function.

If not → shows “unknown command.”

Ctrl+C (KeyboardInterrupt) or exit stops the shell gracefully.

🧩 Next Step
Now you’ll need commands.py — that file will register and define commands like:

python
Copy code
help, clear, run, exit, time, files, github, etc.
Example quick preview:

python
Copy code
# commands.py
from utils import *

def cmd_help(shell, *args):
    log("Available commands: help, clear, exit, time, files")

def cmd_exit(shell, *args):
    shell.exit()

def cmd_clear(shell, *args):
    clear_screen()

command_map = {
    "help": cmd_help,
    "exit": cmd_exit,
    "clear": cmd_clear
}
