import random as random

class TextPorter():

    def __init__(self):
        self.word_dictionary = {}

    def unique_id(self):
        limit = 141167095653376
        return random.randint(1, limit)

    def encode(self):
        inputs = raw_input('Enter a series of words: ').split(" ")

        for i in inputs:
            if len(i) <= 10:
                self.word_dictionary[self.unique_id()] = i
        print(self.word_dictionary)

t = TextPorter()
t.encode()

