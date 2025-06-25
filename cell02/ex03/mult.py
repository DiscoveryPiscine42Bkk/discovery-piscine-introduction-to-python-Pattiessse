#!/usr/bin/env python3

first_number = int(input("Enter the first number:\n"))
second_number = int(input("Enter the second number:\n"))
result = first_number * second_number
print(first_number, "x", second_number, "=", result)

if result < 0:
    print("This number is negative")
elif result > 0:
    print("This number is positive")
else:
    print("This number is both positive and negative.")