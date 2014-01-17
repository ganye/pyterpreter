from commands.basecommand import BaseCommand
import sys

class Load(BaseCommand):
    def callback(self, *args):
    	# TODOD: Actually get this working, rather than just changing the
    	#  current_module.
        print "[+] loading module '%s'..." % args[0]
        self.console.current_module = args[0]

    @staticmethod
    def help():
        return "Loads the given module for configuration and usage."
