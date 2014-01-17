import sys
import os
import re

__all__ = ["commands_list",]

_commands = []

"""
Look through the commands list folder for commands, then add them to the list
of commands available.
"""
files = os.listdir(os.getcwd() + "/commands/list")
pattern = re.compile(r".+\.py$")
for file_ in files:
    if re.match(pattern, file_):
    	if not file_ == "__init__.py":
	        _commands.append(file_[:-3])

commands_list = {}

"""
Iterate over the list of commands, import the class from the command module,
and then add the class to a dictionary entry for the command.
"""
for command in _commands:
    module = __import__(("commands.list." + command), fromlist=[command.title()])
    klass = getattr(module, command.title())

    commands_list[command] = klass

# 'Synonymous' command declarations.
## TODO: Change this somehow so they don't print when 'help' is run.
commands_list['quit'] = commands_list['exit']
commands_list['?'] = commands_list['help']
