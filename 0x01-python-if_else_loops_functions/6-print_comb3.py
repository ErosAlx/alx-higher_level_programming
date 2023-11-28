#!/usr/bin/python3
for i in range(10):
    for x in range(i, 10):
        if (i < x):
            if i != 8 and i != 9:
                print("{:d}{:d}".format(i,x), end=" ,")
            else:
                print("{:d}{:d}".format(i,x), end="\n")
