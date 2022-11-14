#!/usr/bin/env python3

# Implement this function
#
# This signature is required for the automated grading to work.
# You must not rename the function or change its list of parameters.
def convert_roman_to_int(roman):
    roman_single_digits = {
        # simple cases
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    roman_double_digits = {
        # compound cases
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900
    }
    roman_single_and_double_digits = sorted(list(roman_single_digits.values()) + list(roman_double_digits.values()))
    skip_next_iteration = False
    out = 0
    found_num = 1
    if roman == "":
        return 0
    for i, roman_digit in enumerate(roman):
        for j in roman:
            if j not in roman_single_digits:
                raise Warning("Invalid Input")
        if skip_next_iteration:
            skip_next_iteration = False
            if i + 1 != len(roman) and roman_single_digits[roman[i + 1]] > num:
                raise Warning("Invalid Input")
            continue
        num = roman_single_digits[roman_digit]
        if i+1 != len(roman) and num < roman_single_digits[roman[i + 1]]:
            if roman_digit + roman[i + 1] not in roman_double_digits:
                raise Warning("Invalid Input")
            num = roman_double_digits[roman_digit + roman[i + 1]]
            skip_next_iteration = True
            if len(roman) > 3 and not i + 3 > len(roman) and roman[i + 2] + roman[i + 3] in roman_double_digits:
                next_double_digit = roman_double_digits[roman[i + 2] + roman[i + 3]]
                if next_double_digit > num:
                    raise Warning("Invalid Input")
        if not i + 4 > len(roman) and (roman_digit == "I" == roman[i + 1] == roman[i + 2] == roman[i + 3] or roman_digit == "X" == roman[i + 1] == roman[i + 2] == roman[i + 3] or roman_digit == "C" == roman[i + 1] == roman[i + 2] == roman[i + 3]):
            raise Warning("Invalid Input")
        if i + 1 != len(roman) and ((roman_digit == "V" and roman[i + 1] == "V") or (roman_digit == "L" and roman[i + 1] == "L") or (roman_digit == "D" and roman[i + 1] == "D")):
            raise Warning("Invalid Input")
        if num > found_num:
            found_num = num
        out += num
        if i != len(roman) and found_num != 1000 and out >= roman_single_and_double_digits[roman_single_and_double_digits.index(found_num) + 1]:
            raise Warning("Invalid Input")

    return out


# The following lines calls the function and prints the return
# value to the Console.
# i = convert_roman_to_int("XV")
# print(i)

