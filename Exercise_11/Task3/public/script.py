#!/usr/bin/env python3

import random
from difflib import SequenceMatcher

class WordLogic(object):

    def __init__(self, num_words, len_words):
        self.num_words = num_words
        self.len_words = len_words

    def find_words_with_right_size(self):
        with open("resource/words.txt") as f:
            word_list = f.read().splitlines()
        return [word.upper() for word in word_list if len(word) is self.len_words]


    def is_similar(self, a, b, threshold):
        return SequenceMatcher(None, a, b).ratio() > threshold

    def word_selection(self):
        words = self.find_words_with_right_size()
        random.shuffle(words)

        out_list = words[0:self.num_words // 3]
        some_word = out_list[0]

        for new_word in words[self.num_words // 3:]:

            if len(out_list) == self.num_words:
                break

            if self.is_similar(new_word, some_word, 0.4) and new_word not in out_list:
                out_list.append(new_word)

        return out_list