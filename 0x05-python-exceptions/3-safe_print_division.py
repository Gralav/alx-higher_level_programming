#!/usr/bin/python3
"""
 * safe_print_division - Function that divides 2 integers and prints the
 *                       result.
 *
 * @a: This is the input first number
 * @b: This is the input second number
 *
 * Return: The value of the division, otherwise: None
"""


def safe_print_division(a, b):
    result = 0
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result
