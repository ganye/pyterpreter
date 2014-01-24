#! /usr/bin/python2.7

from commands import *
from commands.commandstack import *
from colors import Color
from console import Console
import os
import sys
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="File to read the input from. " +
            "Used for simple, automatic deployment.")
    parser.add_argument("-o", "--output", help="File to send output to.")

    args = parser.parse_args()

    return args

def main():
    while True:
        console.prompt()
        console.get_input()
        console.parse_input()

if __name__ == "__main__":
    if not os.geteuid() == 0:
        sys.exit('[-] Please run as root.')

    args = parse_args()
    kwargs = {}
    if args.input:
        istream = file(args.input)
        kwargs['istream'] = istream
    if args.output:
        ostream = file(args.output, "w+")
        kwargs['ostream'] = ostream

    console = Console(**kwargs)
    try:
        main()
    except KeyboardInterrupt:
        console.writeln("losing...")
