#!/usr/bin/env python3

# As mentioned in the hints, you might want to use the math package
import math

# You can change this value to your liking. Depending on your implementation larger values of n might take quite some time.
n = 997

# perform the Sieve of Eratosthenes algorithm and return all primes <= n
def sieve_of_eratosthenes():
    # You need to change the functionality of this function to
    # create a (sorted) list of all primes <= n which will then be returned.
    # Use the Sieve of Eratosthenes algorithm from the description.
    # You may change the following initialization of the list to be returned.
    if(n <= 1):
        return ["empty"]
    elif(n == 2):
        return [2]
    elif(n == 3):
        return [2, 3]

    max_prime = math.sqrt(n)
    primes_up_to_n = range(2, n+1)
    j = 0
    while(primes_up_to_n[j] <= max_prime):
        new_list = []
        new_list.extend(primes_up_to_n[:j+1])
        for i in range(j+1, len(primes_up_to_n)):
            if(primes_up_to_n[i] % primes_up_to_n[j] != 0):
                new_list.append(primes_up_to_n[i])
        primes_up_to_n = new_list
        j += 1

    # You don't need to change the following line.
    # It simply returns the list created above.
    return primes_up_to_n 

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.