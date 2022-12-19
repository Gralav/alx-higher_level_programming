#!/usr/bin/python3
import sys
"""
 * safe_print_integer_err - Function that prints an integer
 *
 * @value: value can be any type (integer, string, etc.)
 *
 * Return: True if value has been correctly printed (it means
 *         the value is an integer)
 *         Otherwise, returns False and prints in stederr the error precede by
 *         "Exception:"
"""


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except(TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return False
    return True
