#! /usr/bin/python2.7

from commands import *
from commands.commandstack import *
from colors import Color
from console import Console

def main():
    while True:
        console.prompt()
        console.get_input()
        console.parse_input()

if __name__ == "__main__":
    console = Console()
    try:
        main()
    except KeyboardInterrupt:
        console.writeln("losing...")
