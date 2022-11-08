#!/usr/bin/env python3

# This signature is required for the automated grading to work. 
# Do not rename the function or change its list of parameters.
def analyze(posts):
    out_dict = {}
    for post in posts:  # Iterate over strings in given list
        post = post.split(' ') # Separate string into individual words
        for word in post:   # Iterate over words in the given string
            if '#'in word:
                # Cut away all non digit and non alpha chars at the beginning of the word
                while(not word[0].isdigit() and not word[0].isalpha()):
                    word = word[1:]
                # If start_index == len(word), the hashtag is empty. E.g.: for a word "#####"
                # Cut away all non digit or non alpha chars at the end of the word
                while(not word[len(word)-1].isdigit() and not word[len(word)-1].isalpha()):
                    word = word[:len(word)-1]
                # Find non ascii chars in the middle of the word which would terminate the string
                for i in range(len(word)):
                    if not word[i].isdigit or not word[i].isalpha():
                        word = word[:i]
                        break

                if word == "":  # If there are two consequtive hashtags, the word might be empty
                    continue
                elif not word in out_dict:
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
# print(analyze(posts))