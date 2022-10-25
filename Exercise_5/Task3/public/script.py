from collections import defaultdict

# Dataset contains data that will be reverse indexed
dataset = [
    "Hello world",
    "This is the WORLD",
    "hello again"
 ] 

def reverse_index(dataset):
    index_dictionary = {}
    for i, s in enumerate(dataset):
        s_list = s.split(' ')
        for word in s_list:
            if word in index_dictionary:

    

    # don't forget to return your resulting dictionary

# You can see the output of your function here
print(reverse_index(dataset))
