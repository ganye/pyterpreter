class Color:
    def __init__(self):
        self.enable()

    def disable(self):
        self.white = ''
        self.red = ''
        self.green = ''
        self.orange = ''
        self.blue = ''
        self.purple = ''
        self.cyan = ''
        self.gray = ''
        self.tan = ''

    def enable(self):
        self.white = '\033[0m'
        self.red = '\033[31m'
        self.green = '\033[32m'
        self.orange = '\033[33m'
        self.blue = '\033[34m'
        self.purple = '\033[35m'
        self.cyan = '\033[36m'
        self.gray = '\033[37m'
        self.tan = '\033[93m'
