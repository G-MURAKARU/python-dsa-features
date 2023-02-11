#!/usr/local/bin/python3

"""
this is the `console` module
this module defines one class, Console
"""

import cmd
from typing import IO


class Console(cmd.Cmd):
    """
    a custom command-line interpreter

    Parameters
    ----------
    cmd.Cmd
        parent class
    """

    FRIENDS = ["Alice", "Adam", "Barbara", "Bob"]
    prompt = "(hbnb) "
    doc_header = "My Documented Commands - do_*() w/ help_*()"
    undoc_header = "My Undocumented Commands - do_*() w/out help_*()"
    misc_header = "Miscellaneous - help_*() w/out do_*()"

    def __init__(
        self,
        completekey: str = "tab",
        stdin: IO[str] | None = None,
        stdout: IO[str] | None = None,
    ) -> None:
        super().__init__(completekey, stdin, stdout)

    def do_greet(self, person: str) -> None:
        """
        greet [person]
        prints a greeting to stdout

        Parameters
        ----------
        person: name of person to greet
        """

        if person and person in self.FRIENDS:
            print(f"hey, {person}!")
        elif person:
            print(f"hi, {person}.")
        else:
            print("hello..?")

    def help_greet(self) -> None:
        """
        prints help info for function greet
        """

        self.print_help_info(self.do_greet.__doc__)

    def complete_greet(self, text, line, begidx, endidx):
        """
        enables autocompletion for the greet command
        """

        # some dummy code
        return (
            [friend for friend in self.FRIENDS if friend.startswith(text)]
            if text
            else self.FRIENDS[:]
        )

    def do_quit(self, line) -> None:
        """
        quits/exits the (hbnb) command-line environment
        """

        return True

    def help_quit(self) -> None:
        """
        prints help info for function greet
        """

        self.print_help_info(self.do_quit.__doc__)

    def do_emptyline():
        """
        overwrites the default emptyline() method
        handles empty line inputs - output = does nothing
        """

        pass

    def do_EOF(self, line):
        """
        responsible for quit() functionality
        processes end-of-file (ctrl/cmd + D) input
        """

        print()
        return True

    @staticmethod
    def print_help_info(help_info: str) -> None:
        """
        helper function to print help info to stdout

        Parameters
        ----------
        help_info: info(docstring) to print
        """

        print("\n".join(line.lstrip() for line in help_info.split("\n")))


if __name__ == "__main__":
    Console().cmdloop(intro="Custom Command Line Interpreter\n")
