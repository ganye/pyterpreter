
class Option:
    def __init__(self, help, value):
        self._help = help
        self.value = value

    def get(self):
        return self.value

    def set(self, new):
        self.value = new

    def help(self):
        return self._help