#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!

def merge(a, b):
    # If one or both lists are empty, the empty list should be returned.
    if not a or not b:
        return []
    mergelist = []

    len_a = len(a)
    len_b = len(b)
    if len_a > len_b:
        for i in range(len_a):
            if i < len_b:
                mergelist.append((a[i], b[i]))
            else:
                mergelist.append((a[i], b[-1]))
    else:
        for i in range(len_b):
            if i < len_a:
                mergelist.append((a[i], b[i]))
            else:
                mergelist.append((a[-1], b[i]))

    return mergelist



# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(merge([0, 1, 2], [5, 6]))
