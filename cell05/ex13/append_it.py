#!/usr/bin/env python3
import sys
if len(sys.argv) == 1:
    print("none\n")
else:
    for i in range(1, len(sys.argv)):
        if not sys.argv[i].endswith("ism"):
            print(sys.argv[i]+"ism")
#chmod +x append_it.py