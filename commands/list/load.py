from base.command import Command
import sys

class Load(Command):
    def callback(self, *args):
    	# TODOD: Actually get this working, rather than just changing the
    	#  current_module.
        self.console.writeln("[+] loading module '%s'..." % args[0])
        self.console.current_module = args[0]

    @staticmethod
    def help():
        return "Loads the given module for configuration and usage."
