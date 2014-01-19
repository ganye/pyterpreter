from base.option import Option

class Module:
    info = {}
    options = []

    def __init__(self, console):
        self.console = console
        self.initialize()

    def initialize(self):
        raise NotImplementedError()

    def setup(self):
        raise NotImplementedError()

    def run(self):
        raise NotImplementedError()

    def update_info(self, info):
        for key, value in info.items():
            self.info[key] = value

    def set_options(self, options):
        """
        Initalize all the options for a module.
        'options' should be a dict; the key for each item is the variable
        to set for the module, and value is a tuple containing a 'help' string,
        and a default value.
        """
        for key, value in options.items():
            help = value[0]
            if len(value) > 1:
                setattr(self, key, Option(help, value[1]))
            else:
                setattr(self, key, Option(help, None))
            self.options.append(key)

    def set(self, key, value):
        option = getattr(self, key)
        option.set(value)

    def help(self):
        self.console.writeln(("=" * 80))
        for key in self.options:
            option = getattr(self, key)
            self.console.writeln("|-- %s%s|" % (key.ljust(8), option.help().ljust(67)))
        self.console.writeln(("=" * 80))