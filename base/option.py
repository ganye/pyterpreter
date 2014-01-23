
class Option:
    def __init__(self, help, required, value):
        self._help = help
        self._required = required
        self._value = value

    def get(self):
        return self._value

    def set(self, value):
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