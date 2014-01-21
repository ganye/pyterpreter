from base.command import Command

class Set(Command):
    def callback(self, *args):
        if len(args) < 2:
            self.console.debug("expected at least 2 arguments, got %s"
                 % len(args))

        if args[0] in self.console.module.options:
            self.console.module.set(args[0], args[1])
        else:
            self.console.error("'%s' is not a valid option" % args[0])
            return


    @staticmethod
    def help():
        return "Change the current module's given property"