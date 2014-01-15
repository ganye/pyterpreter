from colors import Color
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
        self.set_color("red")
        self.write(self.cursor + " ")
        self.set_color("white")

class ConsoleError(Exception):
    def __init__(self, error):
        self._error = error

    def __repr__(self):
        return "%s" % self._error

    def __str__(self):
        return repr(self._error)
