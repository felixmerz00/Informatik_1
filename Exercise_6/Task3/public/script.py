#!/usr/bin/env python3

import os

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def process_data(path_reading, path_writing):
    if not os.path.exists(path_reading):
        # what to do if the input file does not exist?
        return False

    # If the input file does exist, but is empty, 
    # an empty output file should be written.
    if os.stat(path_reading).st_size == 0:
        with open(path_writing, 'w') as f2:
            f2.write('')
            return

    name_list = []  # List of Stings in the format "Firstname,Lastname"
    # Read the names from the file and save them in name_list
    with open(path_reading, 'r') as f1:
        f1.readline()
        for line in f1.readlines():
            if line == "\n":
                name_list.append(",")
            elif ';' in line: # Split by semicolon
                name = line.split(';')
                name[1] = name[1][1:]
                name_list.append(f"{name[1]},{name[0]}")
            else:   # Split by space
                name = line.split()
                name_list.append(f"{name[0]},{name[1]}")
            
    # Read data from file
    # Write a file with header Firstname, Lastname
    with open(path_writing, 'w') as f2:
        f2.write("Firstname,Lastname")
        for name in name_list:
            f2.write(f"\n{name}")




# The following line calls your solution function with the provided input file
# and then attempts to read and print the contents of the resulting output file.
# You do not need to modify these lines.
INPUT_PATH = "/Users/felixmerz/Documents/Git_Repositories/Informatik_1/Exercise_6/Task3/public/my_data.txt"
OUTPUT_PATH = "/Users/felixmerz/Documents/Git_Repositories/Informatik_1/Exercise_6/Task3/public/my_data_processed.txt"
process_data(INPUT_PATH, OUTPUT_PATH)
if os.path.exists(OUTPUT_PATH):
    with open(OUTPUT_PATH) as resultfile:
        print(resultfile.read())
else:
    print("No output file exists")

