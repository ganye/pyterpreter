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
                raise ConsoleError("'%s' is not a valid argument." % key)

    def write(self, output):
        istream.write(output)

    def writeln(self, output):
        istream.write(output + "\n")

    def disable_colors(self):
        colors.disable()

    def enable_colors(self):
        colors.enable()



class ConsoleError(Exception):
    def __init__(self, error):
        self.error = error

    def __repr__(self):
        return self.error
