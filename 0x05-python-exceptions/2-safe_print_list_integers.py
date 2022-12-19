#!/usr/bin/python3
"""
 * safe_print_list_integers - Function that prints the first x  elementsof a
 *                            list and only integers.
 *
 * @my_list: This is the input list
 * @x: Represents the number of elements to access in my_list
 *
 * Return: The real number of integers printed
 *
"""


def safe_print_list_integers(my_list=[], x=0):
    elements = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            elements += 1
        except(TypeError, ValueError):
            continue
    print("")
    return 
