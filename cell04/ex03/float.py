#!/usr/bin/env python3

a = input("Give me a number:")
b = float(a)
if b.is_integer():
    print("This number is an integer.")
else:
    print("This number is a decimal.")