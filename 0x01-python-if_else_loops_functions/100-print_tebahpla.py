#!/usr/bin/python3
for i in reversed(range(97, 123)):
    c = i
    if (c % 2 != 0):
        c = c - 32
    print("{:c}".format(c), end='')
