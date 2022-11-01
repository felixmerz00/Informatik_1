#!/usr/bin/env python3

from curses.ascii import isdigit
import os

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def get_average_grade(path):
    if not os.path.exists(path):
        return None

    number_of_grades = 0
    sum_grades = 0

    with open(path, 'r') as file:
        for line in file.readlines():
            line_str = line.replace(' ', '')
            if line_str[0] != '#' and ':' in line_str:
                number_of_grades += 1
                list = line_str.split(':')
                sum_grades = sum_grades + float(list[1])
    
    if number_of_grades == 0:
        return 0.0
    return sum_grades / number_of_grades


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(get_average_grade("/Users/felixmerz/Documents/Git_Repositories/Informatik_1/Exercise_5/Task6/public/my_grades.txt"))

