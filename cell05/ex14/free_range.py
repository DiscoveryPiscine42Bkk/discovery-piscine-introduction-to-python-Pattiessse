#!/usr/bin/env python3
import sys

if len(sys.argv) != 3:
    print("none\n")
else:
    array = []
    for i in range(int(sys.argv[1]), int(sys.argv[2]) + 1):
        array.append(i)
    print(array)
#chmod +x free_range.py