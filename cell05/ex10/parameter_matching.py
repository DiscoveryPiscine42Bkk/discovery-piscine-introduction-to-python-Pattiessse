#!/usr/bin/env python3

import sys

if len(sys.argv) == 2: # check for the arguments
    userArg = sys.argv[1]
    nextInput = input("What was the parameter? ")
    if userArg == nextInput:
        print("Good job!")
    else:
        print("Nope, sorry...")
else:
    print("none")