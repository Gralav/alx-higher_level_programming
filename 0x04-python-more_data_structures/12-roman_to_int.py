#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    my_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    number_current = 0
    number_before = 0
    character_before = ""
    count = 0
    for i in roman_string:
        if i in my_dict:
            number_current += my_dict[i]
            if number_before < my_dict[i]:
                number_current -= number_before * 2
            number_before = my_dict[i]
            if i == character_before:
                count += 1
                if count == 3:
                    return 0
            else:
                count = 0
            character_before = i[:]
    return number_current
