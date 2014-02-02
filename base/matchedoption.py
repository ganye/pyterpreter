from base.option import Option
import re

class MatchedOption(Option):
    pattern = re.compile(r'.')
    def __init__(self, required, help, value=None):
        self._required = required
        self._help = help
        if value:
            self.validate(value)
        else:
            self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self.validate(value)

    def validate(self, value):
        if re.match(self.pattern, value):
            self._value = value
        else:
            raise OptionError("'%s' is not a valid value." % value)

class OptionError(Exception):
    def __init__(self, error):
        self._error = error

    def __repr__(self):
        return "%s" % self._error

    def __str__(self):
        return repr(self._error)