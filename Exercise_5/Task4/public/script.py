#!/usr/bin/env python3


# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def min_domino_rotations(top, bottom):
    # Find out which number is on every domino
    # The number must be on the first domino, so we have only two options
    options = (top[0], bottom[0])
    number = options[0]
    for i in range(len(top)):
        if options[0] != top[i] and options[0] != bottom[i]:
            number = options[1]
            break
    for i in range(len(top)):
        if number != top[i] and number != bottom[i]:
            return -1

    # Find out which row has more occurrences of this number
    occur_top = 0
    for i in range(len(top)):
        if number == top[i]:
            occur_top += 1
    
    # Count number of swaps
    number_of_swaps = 0
    if occur_top >= len(top)/2.0:
        for i in range(len(top)):
            if top[i] != number:
                number_of_swaps += 1
    else:
        # Put number in bottom row
        for i in range(len(top)):
            if bottom[i] != number:
                number_of_swaps += 1
    return number_of_swaps


# The following line calls the function which will print # value to the Console.
# This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!

print(min_domino_rotations([2, 6, 2, 1, 2, 2], [5, 2, 4, 2, 3, 2]))
print(min_domino_rotations([3, 5, 1, 2, 6], [3, 6, 3, 3, 6]))
