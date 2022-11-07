#!/usr/bin/env python3

# This signature is required for the automated grading to work. 
# Do not rename the function or change its list of parameters.
def analyze(posts):
    out_dict = {}
    for post in posts:  # Iterate over strings in given list
        post = post.split() # Separate string into individual words
        for word in post:   # Iterate over words in the given string
            if word[0] == '#':
                # A non digit or non alpha char terminates the hashtag
                end_index = 1
                while(end_index < len(word) and (word[end_index].isdigit() or word[end_index].isalpha())):
                    end_index += 1
                word = word[1:end_index]    # Cut away the # symbol
                if word == "":  # If there are two consequtive hashtags, the word might be empty
                    continue
                if not word in out_dict:
                    out_dict[word] = 1
                else:
                    out_dict[word] += 1
    return out_dict



# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
posts = [
    "hi #weekend",
    "good morning #zurich #limmat",
    "spend my #weekend in #zurich",
    "#zurich <3"]
print(analyze(posts))
