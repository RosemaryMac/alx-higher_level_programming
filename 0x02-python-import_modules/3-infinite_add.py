#!/usr/bin/python3
if __name == "__main__":
    from sys import argv
    result = 0
    for s in argv[1:]:
        result += int(s)
        print("{:d}".format(result))
