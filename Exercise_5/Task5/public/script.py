#!/usr/bin/env python3


# Complete the following to implement the described hamming distance function.
# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!

# s1 and s2 must have the same length
def get_hamming_dist(s1, s2):
    dif_count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            dif_count += 1
    return dif_count

def hamming_dist(signal_1, signal_2):
    # Perhaps, one or both sensors lost power during the recording and 
    # now you have datasets of different length or two empty datasets. 
    # In this case, your function should return the string "Empty signal 
    # on at least one of the sensors".
    if len(signal_1["data"]) != len(signal_2) or len(signal_2) == 0:
        return "Empty signal on at least one of the sensors"
    # Compare signal1["data"][i] with signal_2[i]
    # If Hamming distance > 0 append a tuple 
    # (signal1["data"][i], signal_2[i], hamming_distance) to the output list
    output_list = []
    for i in range(len(signal_2)):
        s1 = signal_1["data"][i]
        s2 = signal_2[i]
        # If one of the Hamming distances cannot be computed because the lengths 
        # of corresponding strings differ, your function should return the string 
        # "Sensor defect detected" instead.
        if len(s1) != len(s2):
            return "Sensor defect detected"
        h = get_hamming_dist(s1, s2)
        if h > 0:
            output_list.append((s1, s2, h))
    return output_list

# The following lines print your function's output for an exemplary input to the console.
# Note that this does not include any of the mentioned edge cases for defective sensors or signals of different lenghts.
# Try to write your own tests for this.

signal_sensor_1 = {"times": [0, 1, 2, 3, 4, 5],
                   "data": ["00101110", "11001011", "11110000", "01000011", "11001101", "00011011"]}
signal_sensor_2 = ("00101110", "11001001", "11110011", "01111011", "11001101", "00011011")
print(hamming_dist(signal_sensor_1, signal_sensor_2))
