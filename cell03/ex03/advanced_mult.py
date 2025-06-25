#!/usr/bin/env python3
import sys

if len(sys.argv) > 1: 
    print("none")
else:
    i = 0
    while i <= 10:
        number = 0
        print(f"Table de {i}: ", end=" ")
        while number <= 10:
            print(f"{i*number}", end = " ")
            if number == 10:
                print(end = "\n")
            number += 1
        i += 1