#!/usr/bin/env python3

# You can freely adopt this number to print pyramids of different sizes
h = 5

# build a string 
def build_string_pyramid():

    # You need to change the functionality of this function to
    # create the correct 'encoded' string which will be returned
    # at the end of the function.
    s = ""
    if h == 0:
        return s
    s = ""
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

    # Enter your code here
    # use nested loops and the range() function

    # You don't need to change the following line.
    # It simply returns the string created above.
    return s

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# See the console output and compare it to the image in the task description
print(build_string_pyramid())



