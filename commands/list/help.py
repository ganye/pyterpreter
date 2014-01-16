from commands.basecommand import BaseCommand
from commands import commands_list

class Help(BaseCommand):
    @staticmethod
    def callback(*args):
        print ("=" * 80)
        for command in commands_list.keys():
            print "|-- %s%s|" % (command.ljust(8), commands_list[command].help().ljust(67))
        print ("=" * 80)

    @staticmethod
    def help():
        return "Prints the help menu."
