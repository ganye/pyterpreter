
class Option(object):
    def __init__(self, required, help, value=None):
        self._required = required
        self._help = help
        self._value = value

    @property
    def help(self):
        return self._help

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def required(self):
        return self._required