from base.option import Option

class Module(object):
    def __init__(self, console):
        self.info = {}
        self.options = []
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
            setattr(self, key, value)
            self.options.append(key)
        '''
        for key, value in options.items():
            required = value[0]
            default=None
            help = value[1]

            if len(value) > 2:
                default = value[2]

            setattr(self, key, Option(help, required=required, value=default))
            self.options.append(key)
        '''

    def set(self, key, value):
        option = getattr(self, key)
        option.value = value

    @property
    def help(self):
        for key in self.options:
            option = getattr(self, key)
            self.console.writeln("|-- %s%s" % (key.ljust(16), option.help))