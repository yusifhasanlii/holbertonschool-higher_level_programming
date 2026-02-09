#!/usr/bin/python3
import sys
if __name__ == "__main__":
    total = 0
    arguments = sys.argv[1:]
    for i in arguments:
        total += int(i)
    print(total)
