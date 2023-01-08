#!/usr/bin/pyithon3
def no_c(my_string):
    new_s = ""

    for i in my_string:
        if i is not 'c' and i is not 'C':
            new_s += i
    return (new_s)
