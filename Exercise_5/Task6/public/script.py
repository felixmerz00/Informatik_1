#!/usr/bin/env python3

from curses.ascii import isdigit
import os

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def get_average_grade(path):
    if not os.path.exists(path):
        return None
    number_of_grades = 0
    sum_of_grades = 0
    with open(path, 'r') as f:
        for line in f.readlines():
            if line == "\n" or line[0] == '#':
                continue
            line = line.split(':')
            line = line[1]
            while not line[0].isdigit(): # Delete the spaceing infront of the grade
                line = line[1:]
            if "\n" in line:
                line = line[:-1]    # Delete the newline char (the last line might not have a newline char)
            grade = int(line)
            sum_of_grades += grade
            number_of_grades += 1
    if number_of_grades == 0:
        return 0.0
    return round(sum_of_grades/number_of_grades, 2)


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(get_average_grade("/Users/felixmerz/Documents/Git_Repositories/Informatik_1/Exercise_5/Task6/public/my_grades.txt"))

