# Example 1: Recursive function that counts the number of characters in a string
def example1(s):
    if(s == ""):    # Base case
        return 0
    return 1 + example1(s[1:])  # Recursive call

# Example 2: Returns the sum of the digits of an integer
def example2(n):
    sum = 0
    while(n != 0):
        sum += n%10
        n //= 10
    return sum

# Example 3: Compute the n-th number of the fibonacci sequence
def example3(n):
    if n == 0 or n == 1:
        return 1
    return example3(n-1)+example3(n-2)

# print(example1("Felix"))
# print(example2(1234))
# print(example2(143))
# print(example2(9387503))
print(example3(22))