from base.command import Command
import sys
import os

class Load(Command):
    def callback(self, *args):
    	if not args:
            self.console.error("'load' requires at least one argument")
            return

        # Convert args to a file path
        mod_path = "/modules/" + "/".join(args)
        # In the case of no args, we need to strip the extra /
        mod_path = mod_path.replace("//", "/")
        abs_path = os.getcwd() + mod_path + ".py"

        if not os.path.isfile(abs_path):
        	self.console.error("module '%s' not found" % "/".join(args))
        	return
        elif mod_path.split("/")[-1] == "__init__":
        	self.console.error("module '%s' not found" % "/".join(args))
        	return

        self.console.set_module(mod_path)


    @staticmethod
    def help():
        return "Loads the given module for configuration and usage."