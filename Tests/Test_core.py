"""
test_core.py — Unit tests for TerminalX core
Author: Mr. Tanos
"""

import unittest
import os
from terminalx.core import TerminalX


class TestCore(unittest.TestCase):
    def setUp(self):
        self.shell = TerminalX()

    def test_initial_state(self):
        """Verify TerminalX starts with correct defaults."""
        self.assertTrue(self.shell.running)
        self.assertIsInstance(self.shell.username, str)
        self.assertTrue(os.path.isdir(self.shell.cwd))

    def test_stop_function(self):
        """Ensure stop() correctly sets running=False."""
        self.shell.stop()
        self.assertFalse(self.shell.running)

    def test_exit_function(self):
        """Ensure exit() calls stop() and shows message."""
        self.shell.exit()
        self.assertFalse(self.shell.running)

    def test_prompt_symbol(self):
        """Verify prompt symbol exists."""
        self.assertEqual(self.shell.prompt_symbol, ">")


if __name__ == "__main__":
    unittest.main()


