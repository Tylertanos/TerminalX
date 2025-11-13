"""
utils.py — Helper functions for TerminalX
Author: Mr. Tanos
"""

import os
import time
import json
from datetime import datetime
from pathlib import Path
from rich.console import Console

console = Console()


# ---------- PATH & FILE HELPERS ----------
def ensure_dir(path: str):
    """Create a directory if it doesn’t exist."""
    Path(path).mkdir(parents=True, exist_ok=True)


def read_json(file_path: str, default=None):
    """Read JSON safely with fallback."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return default if default is not None else {}


def write_json(file_path: str, data):
    """Write data as JSON safely."""
    ensure_dir(os.path.dirname(file_path))
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def read_text(file_path: str):
    """Read plain text."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return None


def write_text(file_path: str, content: str):
    """Write plain text."""
    ensure_dir(os.path.dirname(file_path))
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)


# ---------- DISPLAY HELPERS ----------
def log(message: str, color="cyan"):
    """Print formatted log with timestamp."""
    timestamp = datetime.now().strftime("%H:%M:%S")
    console.print(f"[{color}][{timestamp}] {message}[/]")


def clear_screen():
    """Clear terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def wait(seconds: float = 1.0):
    """Simple delay (for animation or effects)."""
    time.sleep(seconds)


# ---------- COMMAND HELPERS ----------
def parse_command(input_str: str):
    """
    Parse a terminal input into (command, args).
    Example: 'run test.py' → ('run', ['test.py'])
    """
    parts = input_str.strip().split()
    if not parts:
        return None, []
    return parts[0].lower(), parts[1:]


def command_not_found(cmd: str):
    """Handle unknown command gracefully."""
    log(f"Unknown command: '{cmd}'", color="red")


# ---------- FILE UTILITIES ----------
def list_files(directory="."):
    """List all files in the directory."""
    try:
        return os.listdir(directory)
    except FileNotFoundError:
        return []


# ---------- SYSTEM INFO ----------
def get_platform():
    """Return current OS info."""
    return os.name, os.sys.platform


def get_time():
    """Return formatted system time."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
💡 What It Does
Handles JSON, text, and directories safely

Manages display and colored logs

Adds command parsing for your TerminalX shell

Provides utilities for file listing, screen clearing, and timing

🧠 Example Usage
python
Copy code
from utils import *

log("Welcome to TerminalX!")
cmd, args = parse_command("run main.py")

if cmd == "run":
    log(f"Running {args[0]}")
else:
    command_not_found(cmd)
