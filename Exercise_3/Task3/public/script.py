#!/usr/bin/env python3

# You can freely adopt these values to try your solution
# with different values.
plain_text = "abc"
shift_by = 1

# perform a ROTn encoding
def rot_n():
    # You need to change the functionality of this function to
    # create the correct 'encoded' string which will be returned
    # at the end of the function.
    # Every character is being mapped to another alphabet that is shifted by 
    # 13 steps, hence the name.
    lower_case_letters = "abcdefghijklmnopqrstuvwxyz"
    upper_case_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encoded = ""
    index_of_current_char = 0
    shift_by_new = shift_by%26
    for c in plain_text:
        if(c in lower_case_letters):
            index_of_current_char = lower_case_letters.find(c)
            encoded += lower_case_letters[(index_of_current_char+shift_by_new)%26]
        elif(c in upper_case_letters):
            index_of_current_char = upper_case_letters.find(c)
            encoded += upper_case_letters[(index_of_current_char+shift_by_new)%26]
        else:
            encoded += c


    # You don't need to change the following line.
    # It simply returns the string created above.
    return encoded

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
print(rot_n())

