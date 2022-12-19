#!/usr/bin/python3

"""
 * safe_print_list - Function that print 'x' elements of a list.
 *
 * @my_list: This is the input list
 * @x: Represents the number of elements to print
 *
 * Return: The real number of elements printed
"""


def safe_print_list(my_list=[], x=0):
    elements = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            elements += 1
        except IndexError:
            break
    print()
    return elements
