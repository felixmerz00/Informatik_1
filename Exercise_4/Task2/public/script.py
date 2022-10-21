#!/usr/bin/env python3

# I found this online: 
# "The number of moves of disk number k is 2^(k-1)"

# Number of disks: number of moves
# 1: 1
# 2: 2^1 + 1 = 3
# 3: 2^2 + 3 = 7
# 4: 2^3 + 7 = 15


# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!
def req_steps(num_disks):
    # Number of moves equals the number of moves of the new, biggest disk plus
    # the number of moves of the pile of num_disks-1
    if num_disks == 1:
        return 1
    num_moves = 2**(num_disks-1) + req_steps(num_disks-1)

    return num_moves


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print("For moving {} disks, {} steps are required.".format(3, req_steps(3)))

