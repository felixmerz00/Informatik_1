#!/usr/bin/env python3

# Height in M
height = 1.75
# Weight in KG
weight = 80


# Determine the BMI. Change the function
# below to calculate the BMI return which category the result is in.
# Your implementation should work with any specific value.
# You must use the variables defined above.


def get_bmi_category():
    if(height <= 0 or weight < 0):
        return "N/A"
    # You need to change the following part of the function
    # to determine the BMI and return the correct category.
    ratio = weight/(height*height)
    category = ""
    if ratio <= 18.5:
        category = "Underweight"
    elif ratio <= 25:
        category = "Normal weight"
    elif ratio <= 30:
        category = "Pre-obesity"
    elif ratio <= 35:
        category = "Obesity class I"
    elif ratio <= 40:
        category = "Obesity class II"
    else:
        category = "Obesity class III"
    bmi = "BMI: {:.2f}".format(ratio)
    bmi += f", Category: {category}"
    # Return the BMI values and the correct category after you have calculated the BMI.
    return bmi

# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
print(get_bmi_category())
