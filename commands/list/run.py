from base.command import Command

class Run(Command):
    def callback(self, *args):
        cont = True
        for raw_option in self.console.module.options:
            option_property = getattr(self.console.module, raw_option)
            if not option_property.value and option_property.required:
                self.console.error("'%s' option not set" % raw_option)
                cont = False

        if cont:
            self.console.module.run()

    @staticmethod
    def help():
        return "Execute the currently loaded module."