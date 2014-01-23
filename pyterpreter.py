#! /usr/bin/python2.7

from commands import *
from commands.commandstack import *
from colors import Color
from console import Console
import os
import sys

def main():
    while True:
        console.prompt()
        console.get_input()
        console.parse_input()

if __name__ == "__main__":
    if not os.geteuid() == 0:
        sys.exit('[-] Please run as root.')
    console = Console()
    try:
        main()
    except KeyboardInterrupt:
        console.writeln("losing...")
