#! /usr/bin/python2.7

from commands import *
from commands.commandstack import *
from colors import Color

cursor = "> "
current_module = None

def print_console():
	print cursor,
	if current_module:
		print "(" + current_module + ") ",

def wait_for_input():
	global user_input
	print_console()

	user_input = raw_input()

def parse_input():
	if user_input.split()[0].lower() in commands_list.keys():
		stack = CommandStack(user_input)
	else:
		print "[-] error: '%s' is not a valid command" % user_input

def main():
	while True:
		wait_for_input()
		parse_input()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print "losing Pyterpreter..."
