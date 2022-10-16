#!/usr/bin/env python3

pwd = "xW+5xW+5"

def is_valid():
    # You need to change the following part of the function
    # to determine if it is a valid password.
    validity = True

    # 1 Has a length of 8-16 chars.
    if (len(pwd) < 8 or len(pwd) > 16):
        validity = False

    # 2 Only contains the characters a-z, A-Z, digits, 
    # or the special chars "+", "-", "*", "/".
    lower_chars = "abcdefghijklmnopqrstuvwxyzöüä"
    upper_chars = lower_chars.upper()
    digits = "0123456789"
    allowed_symbols = "+-*/"
    all_chars = lower_chars+upper_chars+digits+allowed_symbols
    for c in pwd:
        if(not c in all_chars):
            validity = False
    
    # 3 Must contain at least 2 lower case and 2 upper case characters, 
    # 2 digits, and 2 special chars. 
    count = [0, 0, 0, 0]    # [lower case, upper case, digits, special chars]
    for c in pwd:
        if c in lower_chars:
            count[0] += 1
        elif c in upper_chars:
            count[1] += 1
        elif c in digits:
            count[2] += 1
        elif c in allowed_symbols:
            count[3] += 1
    for i in count:
        if i < 2:
            validity = False

    # You don't need to change the following line.
    return validity

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
print(is_valid())

