from _commands import *
import sys

__all__ = ["commands_list",]

def _exit():
	sys.exit()

commands_list = {
	"exit"	:	_exit,
}