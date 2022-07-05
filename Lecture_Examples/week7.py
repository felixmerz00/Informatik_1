def get_size(x):
    import numbers
    if not isinstance(x, numbers.Number):
        try:
            x = float(x)
        except ValueError:
            raise TypeError("Input is not a number")
    if x <= 80 or x > 124:
        raise ValueError
    if x <= 90:
        return "XS"
    elif x <= 98:
        return "S"
    elif x <= 104:
        return "M"
    elif x <= 111:
        return "L"
    else:
        return "XL"

def prompt():
    size = input("What size do you need? ")
    try:
        return f"We have the size {get_size(size)} in store."
    except ValueError:
        return "We make custom clothing."
    except TypeError:
        return prompt()

# print(prompt())

assert(get_size(81) == "XS")
assert(get_size(90) == "XS")
assert(get_size(91) == "S")
assert(get_size(98) == "S")
assert(get_size(99) == "M")
assert(get_size(104) == "M")
assert(get_size(105) == "L")
assert(get_size(111) == "L")
assert(get_size(112) == "XL")
assert(get_size(124) == "XL")