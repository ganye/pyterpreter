from commands import *

current_module = None
cursor = "> "

def print_console():
	print cursor,
	if current_module:
		print "(" + current_module + ") ",

def wait_for_input():
	global user_input
	print_console()

	user_input = raw_input()

def parse_input():
	if user_input in commands_list.keys():
		commands_list[user_input]()
	else:
		print "[-] error: '%s' is not a valid command" % user_input

def main():
	while True:
		wait_for_input()
		parse_input()


if __name__ == "__main__":
	main()