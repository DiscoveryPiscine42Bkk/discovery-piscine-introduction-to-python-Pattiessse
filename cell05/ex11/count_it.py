#!/usr/bin/env python3
import sys

num = len(sys.argv)

if num > 1:
    para = print(f"parameter: {num}")
    for i in range(num):
        if sys.argv[i] == sys.argv[0]:
            continue
        print(f"{sys.argv[i]}: {len(sys.argv[i])}")
else:
    print("none")