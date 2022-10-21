#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!

# Recursive solution
def fac(n):
    # implement this function
    if(n == 0 or n == 1):
        return 1
    else:
        return n * fac(n-1)

# Iterative solution
def fac_iterative(n):
    result = 1
    for i in range(1, n+1):
        result = i*result
    return result


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print("fac({}) = {}".format(8, fac(8)))

