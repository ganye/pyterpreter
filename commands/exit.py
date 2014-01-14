from basecommand import BaseCommand
import sys

class Exit(BaseCommand):
    @staticmethod
    def callback(*args):
        sys.exit()

    @staticmethod
    def help():
        return "Exits the program cleanly."
