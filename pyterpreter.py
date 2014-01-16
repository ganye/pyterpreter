#! /usr/bin/python2.7

from commands import *
from commands.commandstack import *
from colors import Color
from console import Console

def parse_input():
	if user_input.split()[0].lower() in commands_list.keys():
		stack = CommandStack(user_input)
	else:
		print "[-] error: '%s' is not a valid command" % user_input

def main():
    while True:
        console.prompt()


if __name__ == "__main__":
    console = Console()
    try:
        main()
    except KeyboardInterrupt:
        console.writeln("losing...")
