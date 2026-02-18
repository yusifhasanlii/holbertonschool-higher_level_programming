#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string not isinstance(roman_string, str):
        return 0
    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 100
    }
    total = 0
    length = len(roman_string)
    for i in range(length):
        current_val = roman_dict[roman_string[i]]
        if i < length - 1 and current_val < roman_dict[roman_string[i+1]]:
            total -= current_val
        else:
            total += current_val
    return total
