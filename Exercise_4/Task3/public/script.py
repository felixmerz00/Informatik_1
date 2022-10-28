#!/usr/bin/env python3

import os

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def absolute_value(a):
    a = abs(a)
    return a


# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def gcd(a, b):
    # implement this function
    if a == 0 and b == 0:
        return None
    if a < 0:
        a = absolute_value(a)
    if b < 0:
        b = absolute_value(b)
    
    if a >= b:
        if(b == 0):
            return absolute_value(a)
        else:
            return gcd(b, a % b)
            # This function runs as long as a is not devidable by b.
            # As soon as a is devidable by b, b which will be the new a is returned,
            # because of the if statement above.
    elif b > a:
        if (a == 0):
            return absolute_value(b)
        else:
            return gcd(a, b % a)


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
a = 6
b = 6
print(f"greatest common divisor of {a} and {b} is = {gcd(a, b)}")

