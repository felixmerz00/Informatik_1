#!/usr/bin/env python3

# The signatures of this class and its public methods are required for the automated grading to work. 
# You must not change the names or the list of parameters. 
# You may introduce private/protected utility methods though.
class ProfanityFilter:

    def __init__(self, keywords, template):
        # Save the keywords in an instance variable sorted by the length of the word in decreasing order
        self.__keywords = sorted(keywords, key = len, reverse = True)
        for i, keyword in enumerate(self.__keywords):
            self.__keywords[i] = keyword.lower()
        self.__template = template
    
    def __clean(self, profanity):
        # E.g. template = ":***#", profanity = motherfucker, 
        # ":***#" * (12//5) + ":***#"[:12%5] 
        # = ":***#" * 2 + ":***#"[:2] 
        # = ":***#:***#:*"
        return self.__template * (len(profanity)//len(self.__template)) + self.__template[:len(profanity)%len(self.__template)]

    def filter(self, msg):
        msg_list = msg.split()
        for word_index in range(len(msg_list)):
            for profanity in self.__keywords:
                current_word_lower = msg_list[word_index].lower()
                while profanity in current_word_lower:   # It must be case insensitive
                    # Find the sequence of the profanity in the current word
                    # I want to get the exact sequence with the correct caseing
                    i_profanity = current_word_lower.find(profanity)    # Get the start index of profanity
                    current_profanity = msg_list[word_index][i_profanity:i_profanity+len(profanity)]
                    msg_list[word_index] = msg_list[word_index].replace(current_profanity, self.__clean(profanity))
                    current_word_lower = msg_list[word_index].lower()
        return " ".join(msg_list)



# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
#if __name__ == '__main__':
#    f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
#    offensive_msg = "abc defghi mastard jklmno"
#    clean_msg = f.filter(offensive_msg)
#    print(clean_msg)  # abc defghi ?#$?#$? jklmno
