#!/usr/bin/env python3

# This signature is required for the automated grading to work. 
# Do not rename the function or change its list of parameters.
def compress(data):
    # Handle an empty list
    if not data:
        return ((),[])
    # Handle regular input
    key_list = data[0].keys()
    key_tuple = tuple(sorted(key_list))
    value_list = []
    for d in data:
        values_of_key = []
        for key in key_tuple:    
            values_of_key.append(d[key])
        value_list.append(tuple(values_of_key))
    out_t = (key_tuple, value_list)
    return out_t
        


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
data = [{}, {}]
print(compress(data))