#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num = len(argv)
    if num == 0:
        print("{:d} arguments.".format(num))
    elif num == 1:
        print("{:d} argument: ".format(num))
        print("{:d}: {:s}".format(num, argv))
    else:
        print("{:d} {:s}{:s}".format(num, argv))
    

        for i, s in enumerate(num):
            if i > 0:
                print("{:d}: {:s}".format(i, s))
