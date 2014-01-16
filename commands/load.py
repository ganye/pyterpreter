from basecommand import BaseCommand
import sys

pyterpreter = sys.modules['__main__'] # Used to access variables from the
                                      # main pyterpreter module

class Load(BaseCommand):
    def callback(self, *args):
        pyterpreter.current_module = args[0]
        print "[+] loading module '%s'..." % args[0]
        self.console.current_module = args[0]

    @staticmethod
    def help():
        return "Loads the given module for configuration and usage."
