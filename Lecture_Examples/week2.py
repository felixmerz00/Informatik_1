# Example 1
def example1():
    x = 2 + 2 + 5 * 10**2
    print(x)

    x = (1+10**3)*(2+5**2)
    print(x)


# Example 2
def example2():
    name = input("What is your name? ")
    age = input("How old are you? ")
    occupation = input("What is your occupation? ")

    print(f"Hi {name}! I see you are {age} years old and work as a {occupation}.")


# Example 3: Bin Packing Problem
def example3():
    s = input("Enter an amount between 1 and 99 cent: ")
    n = int(s)
    quarters = (n-(n%25))/25
    rest = n-quarters*25
    print(5%10)
    dime = (rest-(rest%10))/10
    rest = rest-dime*10
    nickel = (rest-(rest%5))/5
    rest = rest-nickel*5
    pennies = rest
    print(f"{quarters} quarters, {dime} dime, {nickel} nickel, {pennies} pennies")

# Also example 3 but better (with integer division)
def example3punkt2():
    n = int(input("Enter an amount between 1 and 99 cent: "))
    quarters = n//25
    rest = n%25
    dime = rest//10
    rest = rest%10
    nickel = rest//5
    rest = rest%5
    pennies = rest
    print(f"{quarters} quarters, {dime} dime, {nickel} nickel, {pennies} pennies")

example3punkt2()