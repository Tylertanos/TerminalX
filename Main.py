"""
main.py — Entry point for TerminalX
Author: Mr. Tanos
"""

from terminalx import TerminalX
from terminalx.interface import show_banner
from utils import log


def main():
    shell = TerminalX()
    show_banner(shell.version)
    log("Launching TerminalX shell...", "green")
    shell.start()


if __name__ == "__main__":
    main()
