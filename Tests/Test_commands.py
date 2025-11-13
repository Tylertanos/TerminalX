"""
test_commands.py — Unit tests for TerminalX commands
Author: Mr. Tanos
"""

import unittest
import os
import tempfile
from terminalx.core import TerminalX
from terminalx import commands


class TestCommands(unittest.TestCase):
    def setUp(self):
        self.shell = TerminalX()

    def test_help_command(self):
        """Should run without error."""
        commands.cmd_help(self.shell)

    def test_clear_command(self):
        """Should clear screen without crash."""
        commands.cmd_clear(self.shell)

    def test_time_command(self):
        """Should show system time."""
        commands.cmd_time(self.shell)

    def test_files_command_empty(self):
        """Should list files successfully."""
        commands.cmd_files(self.shell)

    def test_cd_and_run(self):
        """Change directory and run a simple file."""
        with tempfile.TemporaryDirectory() as tmp:
            old_dir = self.shell.cwd
            commands.cmd_cd(self.shell, tmp)
            self.assertEqual(self.shell.cwd, os.path.abspath(tmp))
            # create a quick script to run
            script_path = os.path.join(tmp, "test_script.py")
            with open(script_path, "w") as f:
                f.write('print("ok")')
            commands.cmd_run(self.shell, script_path)
            commands.cmd_cd(self.shell, old_dir)

    def test_sleep_command(self):
        """Should pause briefly."""
        commands.cmd_sleep(self.shell, "0.1")


if __name__ == "__main__":
    unittest.main()
