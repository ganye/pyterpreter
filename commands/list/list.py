from base.basecommand import BaseCommand
import os
import re

class List(BaseCommand):
    """
    If not arguments are given, lists all modules in the modules folder -
    otherwise, lists all modules in the given folder.
    """
    def callback(self, *args):
        items = []

        if len(args) > 1:
            self.console.error('too many arguments: expected one or fewer, got %s' % len(args))
            return
        elif not args:
            args = [""]
        
        try:
            items = os.listdir(os.getcwd() + "/modules/" + args[0])
        except OSError:
            self.console.error("'%s' is not a valid directory" % args[0])
            return
        
        pattern = re.compile(r".+\.py$")
        for item in items:
            if re.match(pattern, item):
                if not item == "__init__.py": # Ignore package files
                    self.console.writeln("/modules/%s/%s" 
                        % (args[0], item[:-3])) # Strip the .py

    @staticmethod
    def help():
        return "Prints a list of all available modules in the given directory."