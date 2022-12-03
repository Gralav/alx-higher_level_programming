#!/usr/bin/python
def no_c(my_string):
    new_string = ''
    for i in my_string:
        if i in ['c', 'C']:
            continue
        new_string = new_string + i
        return new_string

