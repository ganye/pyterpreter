from commands.basecommand import BaseCommand
import sys

class Exit(BaseCommand):
    def callback(self, *args):
        sys.exit()

    @staticmethod
    def help():
        return "Exits the program cleanly."
