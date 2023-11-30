#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_c = len(sys.argv[1:])
    if arg_c == 1:
        print(arg_c, "argument:")
    elif arg_c == 0:
        print(arg_c, "arguments.")
    else:
        print(arg_c, "arguments:")
    for i in range(arg_c):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
