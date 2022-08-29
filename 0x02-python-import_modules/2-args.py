#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num = len(argv)
    print("{:d} {:s}{:s}".format(num - 1, "argument" if num <= 2 else "arguments","." if num == 1 else ":"))
    
    for i, s in enumerate(argv):
            if i > 0:
                print("{:d}: {:s}".format(i, s))
