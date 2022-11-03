#You are completely free to change this variables to check your algorithm.
num1 = 6 
num2 = 28

#Function to check whether two numbers are friendly pairs or not.
# Abundancy is the ratio between the sum of divisors of the 
# number and the number itself. Two **different** numbers 
# with the **same abundancy** form a **friendly pair.**
def isFriendlyPair():
    # preconditions: being natural and different from each other
    if num1 <= 0 or num2 <= 0 or num1 == num2 or num1 != round(num1) or num2 != round(num2):
        return "Invalid"

    sum_divisors1 = num1
    sum_divisors2 = num2
    for i in range(1, num1):    # Start at 1 to avoid zero division error
        if num1%i == 0:
            sum_divisors1 += i
    for i in range(1, num2):
        if num2%i == 0:
            sum_divisors2 += i
    abundancy1 = sum_divisors1/num1
    abundancy2 = sum_divisors2/num2
    # You need to return a boolean variable that sais if num1 and num2 are friendly pairs.
    return abundancy1 == abundancy2

#This line prints your method's return so that you can check your output.
#print(isFriendlyPair())