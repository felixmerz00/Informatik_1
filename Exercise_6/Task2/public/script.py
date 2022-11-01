#You are completely free to change this variables to check your algorithm.
num1 = 6 
num2 = 28

#Function to check whether two numbers are friendly pairs or not.
# Abundancy is the ratio between the sum of divisors of the 
# number and the number itself. Two **different** numbers 
# with the **same abundancy** form a **friendly pair.**
def isFriendlyPair():
    # preconditions: being natural and different from each other
    if num1 <= 0 or num2 <= 0 or num1 == num2:
        return "Invalid"

    num1_divisors = []
    num2_divisors = []
    for i in range(1, num1):    # Start at 1 to avoid zero division error
        if num1%i == 0:
            num1_divisors.append(i)
    for i in range(1, num2):
        if num2%i == 0:
            num2_divisors.append(i)
    # a is also a divisor of a, but not included int the list of divisors yet
    num1_sum_divisors = num1
    num2_sum_divisors = num2
    for e in num1_divisors:
        num1_sum_divisors += e
    for e in num2_divisors:
        num2_sum_divisors += e
    num1_abundancy = num1_sum_divisors/num1
    num2_abundancy = num2_sum_divisors/num2
    # You need to return a boolean variable that sais if num1 and num2 are friendly pairs.
    return num1_abundancy == num2_abundancy
    
    # The numbers must be valid according to description before determining friendly parity situations. 
    # Return "Invalid" if they are not valid.
   
    return True

#This line prints your method's return so that you can check your output.
print(isFriendlyPair())