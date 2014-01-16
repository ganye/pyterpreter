import sys
import os
import re

__all__ = ["commands_list",]

_commands = []

files = os.listdir(os.getcwd() + "/commands/list")
pattern = re.compile(r".+\.py$")
for file_ in files:
    if re.match(pattern, file_):
    	if not file_ == "__init__.py":
	        _commands.append(file_[:-3])

commands_list = {}

for command in _commands:
    module = __import__(("commands.list." + command), fromlist=[command.title()])
    klass = getattr(module, command.title())

    commands_list[command] = klass

commands_list['quit'] = commands_list['exit']
commands_list['?'] = commands_list['help']
