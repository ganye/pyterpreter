from colors import Color
from commands.commandstack import CommandStack
from commands import commands_list
import sys

class Console:
    """
    Main class used for handling the actually input/output of the program.

    TODO:
        - More commands/finish current commands.
        - Read settings from a configuration file. Preferably JSON.
    """
    colors = Color()
    cursor = ">"
    current_module = None
    module = None
    ostream = sys.stdout
    istream = sys.stdin

    def __init__(self, **kwargs):
        """
        Constructor for the console. Only accepts 'cursor', 'ostream' and
        'istream' kwargs.
        """
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
        """
        Prints the cursor, as well as the currently loaded module if available,
        and then waits for input.
        """
        self.set_color("blue")
        self.write(self.cursor + " ")
        if self.current_module:
            self.set_color("bold")
            self.write("(%s) " % self.current_module)
        self.set_color("white")

    def get_input(self):
        """
        Reads input from istream, then pushes all the commands onto the 
        CommandStack for handling.
        """
        user_input = self.istream.readline()
        for arg in user_input.split():
            self.stack.push(arg)

    def parse_input(self):
        """
        Checks if a command is valid - if not, prints an error. Else, pop all
        other arguments to a list and then call the command with the given args
        """
        command = self.stack.pop()
        arguments = []
        if not command in commands_list.keys():
            self.error("command '%s' not found." % command)
            self.writeln("Enter 'help' or '?' to get a list of commands")
            while not self.stack.is_empty():
                self.stack.pop()
            return

        while not self.stack.is_empty():
            arguments.append(self.stack.pop())
        
        self.call(command, arguments)

    def error(self, error):
        """
        Used for quickly/simply writing an error to ostream.
        """
        self.set_color("red")
        self.write("[-] error: ")
        self.set_color("white")
        self.writeln(error)

    def warn(self, message):
        """
        Used for quickly/simply writing a warning to ostream.
        """
        self.set_color("light_red")
        self.write("[-] warning: ")
        self.set_color("white")
        self.writeln(message)

    def debug(self, message):
        """
        Used for quickly/simply writing a debug statement to ostream.
        """
        self.set_color("dark_blue")
        self.write("[*] debug: ")
        self.set_color("white")
        self.writeln(message)

    def call(self, command, arguments):
        """
        Execute's the callback funcion for the given command, passing along
        arguments.
        """
        commands_list[command](self)._callback(*arguments)

    def set_module(self, new_module):
        self.current_module = new_module

        tmp = new_module.split("/")[-1]
        # Replace /'s with .'s
        mod_path = new_module.replace("/", ".")
        # Strip the first "."
        mod_path = mod_path.lstrip('.')
        
        # Load the actual module class file
        module = __import__(mod_path, fromlist=[tmp.title()])
        klass = getattr(module, tmp.title())
        
        self.module = klass(self)

class ConsoleError(Exception):
    def __init__(self, error):
        self._error = error

    def __repr__(self):
        return "%s" % self._error

    def __str__(self):
        return repr(self._error)
