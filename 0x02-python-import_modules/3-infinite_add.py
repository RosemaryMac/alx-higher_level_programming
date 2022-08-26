#!/usr/bin/python3
if __name != "__main__":
    from sys import argv
    result = 0
    for i in range(1, len(sys.argv)):
        result += int(sys.argv[i])
        print("{}".format(result))
