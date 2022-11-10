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

    for letter in roman:
        if not letter in roman_single_digits:
            raise Warning("Invalid Input")
    
    i = 0
    num = 0
    while i < len(roman):
        if i+1 < len(roman) and roman[i:i+2] in roman_double_digits:
            num += roman_double_digits[roman[i:i+2]]
            i += 2
        else:
            num += roman_single_digits[roman[i:i+1]]
            i += 1

    return num


# The following lines calls the function and prints the return
# value to the Console.
# i = convert_roman_to_int("XV")
# print(i)

