from base.command import Command

class Options(Command):
    def callback(self, *args):
#        import pdb; pdb.set_trace()
        if self.console.current_module:
            self.console.module.help()

        else:
            self.console.error("no currently loaded module")

    @staticmethod
    def help():
        return "Lists all the options for the currently loaded module"