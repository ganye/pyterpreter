from base.command import Command
import sys

class Exit(Command):
    def callback(self, *args):
        sys.exit()

    @staticmethod
    def help():
        return "Exits the program cleanly."
