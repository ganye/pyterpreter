import sys

__all__ = ["commands_list",]

_commands = sorted([
        "exit",
        "help",
        ])

commands_list = {}

for command in _commands:
    module = __import__(("commands." + command), fromlist=[command.title()])
    klass = getattr(module, command.title())

    commands_list[command] = klass
