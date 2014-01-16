
class BaseCommand:
    def __init__(self, console):
        self.console = console
        
    def _callback(self, *args):
        if((args) and (args[0] in ["help","?"])):
            self.console.writeln(self.help())
        else:
            self.callback(*args)

    def callback(self, *args):
        raise NotImplementedError()

    @staticmethod
    def help():
        raise NotImplementedError()
