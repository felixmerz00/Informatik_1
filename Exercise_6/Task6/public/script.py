#!/usr/bin/env python3

# use this list of presumably known Whatsapp numbers to check
# whether a trial nr from the function below exists in Whatsapp.
# Note that the grading framework might use different numbers here.
wa_nrs = ["0781111119", "0792653913", "0797763139", "0792793193", "0781139022", "0764320165"]


# This signature is required for the automated grading to work. 
# Do not rename the function or change its list of parameters.
def get_possible_nrs(n):
    # This function accepts a string n for juliets number where one digit is missing.
    # and should return a list of all whatsapp numbers that might belong to juliet 
    possible_numbers = []
    possible_nrs_for_juliet = []
    if len(n) != 9 or not n.startswith("07"):
        return possible_nrs_for_juliet

    for i in range(2, 10):
        for j in range(10):
            possible_numbers.append(n[:i] + str(j) + n[i:])   # All possible numbers
    # Delete possible numbers not connected to WhatsApp
    for number in possible_numbers:
        if number in wa_nrs:
            possible_nrs_for_juliet.append(number)
    return possible_nrs_for_juliet

# For this particular number, the function should find the
# last element in wa_nrs
print(get_possible_nrs("076432165"))
