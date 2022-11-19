#!/usr/bin/env python3

# The signatures of this class and its public methods are required for the automated grading to work. 
# You must not change the names or the list of parameters. 
# You may introduce private/protected utility methods though.
class ProfanityFilter:

    def __init__(self, keywords, template):
        # Save the keywords in an instance variable sorted by the length of the word in decreasing order
        self.keywords = sorted(keywords, key = lambda word: len(word), reverse = True)
        self.template = template
    
    def __clean(self, profanity):
        # E.g. template = ":***#", profanity = motherfucker, 
        # ":***#" * (12//5) + ":***#"[:12%5] 
        # = ":***#" * 2 + ":***#"[:2] 
        # = ":***#:***#:*"
        return self.template * (len(profanity)//len(self.template)) + self.template[:len(profanity)%len(self.template)]

    def filter(self, msg):
        msg_list = msg.split()
        for word_index in range(len(msg_list)):
            for profanity in self.keywords:
                if profanity in msg_list[word_index]:
                    msg_list[word_index] = msg_list[word_index].replace(profanity, self.__clean(profanity))
        return " ".join(msg_list)



# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
    offensive_msg = "abc defghi mastard jklmno"
    clean_msg = f.filter(offensive_msg)
    print(clean_msg)  # abc defghi ?#$?#$? jklmno
