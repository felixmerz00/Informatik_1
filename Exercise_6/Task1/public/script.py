#!/usr/bin/env python3

# You can freely adopt this number to print pyramids of different sizes
h = 5

# build a string 
def build_string_pyramid():
    s = ""
    if h == 0:
        return s
    for i in range(h):  # Upper half of pyramid
        s += "1"
        for j in range(2, i+2):
            s = s + f"*{j}"
        s += "\n"
    
    for i in range(h-1, 0, -1):    # Lower half of pyramid
        s += "1"
        for j in range(2, i+1):
            s = s + f"*{j}"
        s += "\n"
    s = s[:-1]  # Take away the last newlie char
    return s

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# See the console output and compare it to the image in the task description
print(build_string_pyramid())



