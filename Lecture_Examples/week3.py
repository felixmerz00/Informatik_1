
def conditional_statements():
    list = [2, 4, 6, 8, 10, False]
    if 10 in list:
        print("The list contains the number 10.")
    elif not list[5]:
        print("Value 5 is falsy.")

def falsy_condition():
    n = 6
    while n:
        print(n)
        n-=1


def reverse_string(s):
    new_string = ""
    # Start at length-1, continue until index 0 is reached and done, start from the end
    for i in range(len(s)-1, -1, -1):
        new_string += s[i]
    print(new_string)

def test_enumerate(s):
    for i, el in enumerate(s, 1):
        print(f"({i}, {el})")

# How does string formatting with multiple variables word with the format function?
def test_string_formatting():
    n = 10
    n2 = 20
    print("The first number is {} and the second number is {}.".format(n, n2))

def test_range_function():
    for i in range(0, 20, 2):
        print(i)

# Example 3
import random
def example3():
    rnd = random.randint(0, 127)
    print("Guess the number!")
    n = -1
    while(n != rnd):
        n = int(input("Enter a number between 0 and 127: "))
        if(n < rnd):
            print("too low")
        elif(n > rnd):
            print("too high")
    print("Correct it was the number {}!".format(rnd))



# Example 4
def example4(src, dest, header):
    # Prepare the source file
    f1 = open(src, 'w')
    f1.write("This is line 1 from file 1.\nThis is line 2 from file 1.\nThis is line 3 from file 1.\nThis is line 4 from file 1.\nThis is line 5 from file 1.\n")
    f1.close()

    # Copy the lines from the src and add a header
    with open(dest, 'w') as f2:
        f2.write(header)
        with open(src, 'r') as f1:
            for line in f1.readlines():
                f2.write(line)


# reverse_string("Felix")
# falsy_condition()
# test_enumerate("Felix")
# test_string_formatting()
# test_range_function()
# example3()
example4('file1.txt', "file2.txt", "This is the new header I added.\n")
