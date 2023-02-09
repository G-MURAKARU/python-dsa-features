#!/usr/bin/python3

import cmd
from typing import IO, Union


class HelloWorld(cmd.Cmd):
    """
    HelloWorld defines a custom command-line interpreter

    Args:
        cmd (type): parent class from imported module `cmd`
    """

    def __init__(
        self,
        completekey: str = None,
        stdin: IO[str] = None,
        stdout: IO[str] = None,
    ) -> None:
        super().__init__(completekey, stdin, stdout)
        self.prompt = "(yolo) "

    def do_greet(self, line: str):
        """
        do_greet greets somebody

        Args:
            line (str): person's name
        """

        if line:
            print(f"hello {line}")
        else:
            print("hello")

    def do_emptyline():
        pass

    def do_EOF(self, line):
        return True


if __name__ == "__main__":
    HelloWorld().cmdloop()
