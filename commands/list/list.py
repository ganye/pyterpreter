from base.command import Command
import sys
import os
import re

class List(Command):
    """
    If not arguments are given, lists all modules in the modules folder -
    otherwise, lists all modules in the given folder.
    """
    def callback(self, *args):
        items = []

        if not args:
            args = []

        # Convert args to a file path
        mod_path = "/modules"
        search_path = "%s/%s/" % (mod_path, "/".join(args))
        # In the case of no args, we need to strip the extra /
        search_path = search_path.replace("//", "/")

        try:
            for (dirpath, dirnames, filenames) in os.walk(os.getcwd() + search_path):
                items.extend(dirnames)
                items.extend(filenames)
                break
        except OSError:
            self.console.error("'%s' is not a valid directory" % search_path)
            return
        
        pattern = re.compile(r".+\.py$")
        for item in items:
            # get the absolute path for the item
            abs_path = os.path.abspath(os.getcwd() + search_path + item)
            if re.match(pattern, item):
                if not item == "__init__.py": # Ignore package files
                    item = item.rstrip(".py")
                    self.console.writeln("%s" % (search_path + item))
            # Get the absolute path for the item and check if it is a directory
            elif os.path.isdir(abs_path):
                self.console.writeln("%s/" % (search_path + item))

    @staticmethod
    def help():
        return "Prints a list of all available modules in the given directory."