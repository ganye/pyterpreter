from base.command import Command
from commands import commands_list

class Help(Command):
    def callback(self, *args):
        self.console.writeln(("=" * 80))
        for command in commands_list.keys():
            self.console.writeln("|-- %s%s|" % (command.ljust(8), commands_list[command].help().ljust(67)))
        self.console.writeln(("=" * 80))

    @staticmethod
    def help():
        return "Prints the help menu."
