from colors import Color
from commands.commandstack import CommandStack
from commands import commands_list
import sys

class Console:
    colors = Color()
    cursor = ">"
    current_module = None
    ostream = sys.stdout
    istream = sys.stdin

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key in ["cursor", "ostream", "istream"]:
                setattr(self, key, value)
            else:
                raise ConsoleError("unexpected keyword argument '%s'" % key)
        self.stack = CommandStack(self)

    def write(self, output):
        self.ostream.write(output)

    def writeln(self, output):
        self.write(output + "\n")

    def set_color(self, color):
        try:
            newcolor = getattr(self.colors, color)
        except AttributeError:
            raise ConsoleError("invalid color '%s'" % color)
        else:
            self.write(newcolor)

    def disable_colors(self):
        self.colors.disable()

    def enable_colors(self):
        self.colors.enable()

    def prompt(self):
        self.set_color("blue")
        self.write(self.cursor + " ")
        if self.current_module:
            self.set_color("bold")
            self.write("(%s) " % self.current_module)
        self.set_color("white")

        self.get_input()
        self.parse_input()

    def get_input(self):
        user_input = self.istream.readline()
        for arg in user_input.split():
            self.stack.push(arg)

    def parse_input(self):
        command = self.stack.pop()
        arguments = []
        while not self.stack.is_empty():
            arguments.append(self.stack.pop())

        if command in commands_list.keys():
            self.call(command, arguments)
        else:
            self.error("command '%s' not found." % command)

    def error(self, error):
        self.set_color("red")
        self.write("[-] error: ")
        self.set_color("white")
        self.writeln(error)

    def debug(self, message):
        self.set_color("dark_blue")
        self.write("[*] debug: ")
        self.set_color("white")
        self.writeln(message)

    def call(self, command, arguments):
        commands_list[command](self)._callback(*arguments)

class ConsoleError(Exception):
    def __init__(self, error):
        self._error = error

    def __repr__(self):
        return "%s" % self._error

    def __str__(self):
        return repr(self._error)
