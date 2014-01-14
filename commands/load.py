from basecommand import BaseCommand
import pyterpreter

class Load(BaseCommand):
    @staticmethod
    def callback(args):
        pyterpreter.current_module = args[0]
        print "[+] loading module '%s'..." % args[0]

    @staticmethod
    def help():
        return "Loads the given module for configuration and usage."
