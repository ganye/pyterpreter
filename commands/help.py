from basecommand import BaseCommand
from . import commands_list

class Help(BaseCommand):
    @staticmethod
    def callback(*args):
        print ("=" * 80)
        for command in commands_list.keys():
            print "|-- %s\t\t%s" % (command, commands_list[command].help())

    @staticmethod
    def help():
        return "Prints the help menu."
