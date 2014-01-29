from colors import Color
from commands.commandstack import CommandStack
from commands import commands_list
import sys
import traceback

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
        if not self.ostream is sys.stdout:
            self.colors.disable()
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
        Reads user input from istream, and then returns the input
        """
        user_input = self.istream.readline()

        return user_input

    def parse_input(self, user_input):
        """
        Checks if a command is valid - if not, prints an error. Else, pop all
        other arguments to a list and then call the command with the given args
        """
        for arg in user_input.split():
            self.stack.push(arg)

        command = self.stack.pop()
        arguments = []
        if not command in commands_list.keys():
            #don't crash if the user accidentally presses enter
            if command==None:
                self.error("please write a command.")
            else:
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
        self.set_color("cyan")
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

    def info(self, message):
        """
        Used for quickly/simply writing an info statement to ostream.
        """
        self.set_color("green")
        self.write("[+] ")
        self.set_color("white")
        self.writeln(message)

    def call(self, command, arguments):
        """
        Execute's the callback funcion for the given command, passing along
        arguments.
        """
        commands_list[command](self)._callback(*arguments)

    def set_module(self, new_module):
        name = new_module.split("/")[-1]
        # Replace /'s with .'s
        mod_path = new_module.replace("/", ".")
        # Strip the first "."
        mod_path = mod_path.lstrip('.')
        
        # Load the actual module class file
        try:
            module = __import__(mod_path, fromlist=[name])
        except SyntaxError, e:
            self.error("module contains a syntax error and cannot be loaded")
            traceback.print_exc(e)
            return
        

        try:
            name = getattr(module, '__module__')
        except AttributeError:
            name = name.title()
        klass = getattr(module, name)
        self.module = klass(self)
        self.current_module = new_module

class ConsoleError(Exception):
    def __init__(self, error):
        self._error = error

    def __repr__(self):
        return "%s" % self._error

    def __str__(self):
        return repr(self._error)
