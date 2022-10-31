#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def invert(d):
    # implement this function
    new_d = {}
    for key in d:
        cur_val = d[key]
        if cur_val in new_d:
            new_d[cur_val].append(key)
        else:
            new_d[cur_val] = [key]
    sorted(new_d)
    return new_d


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(invert({"a":1, "b":1, "c":3}))
