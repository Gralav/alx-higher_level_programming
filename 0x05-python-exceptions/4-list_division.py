#!/usr/bin/python3
"""
 * list_division - Write a function that divides element by element 2 lists
 *
 * @my_list_1: This is the input list
 * @my_list_2: This is the input list
 * @list_length: can be bigger than the length of both lists
 *
 * Return: Returns a new list (length = list_length) with all divisions
 * If 2 elements cant be divided, the division result should be equal to 0
 *
"""


def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    result = 0

    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except (ZeroDivisionError):
            print("division by 0")
            result = 0
            continue
        except (TypeError):
            print("wrong type")
            result = 0
            continue
        except IndexError:
            print("out of range")
            result = 0
            continue
        finally:
            new_list.append(result)
    return new_list
