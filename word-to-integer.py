import random as random

class TextPorter():

    def __init__(self):
        self.word_dictionary = {}

    def unique_id(self):
        limit = 141167095653376
        return random.randint(1, limit)

    def encode(self):
        inputs = raw_input('Enter a series of words: ').split(" ")

        for i in filter(None, inputs):
            if len(i) <= 10:
                self.word_dictionary[self.unique_id()] = i
            else:
                print('The word {} exceeds the word limit and will not be encoded'.format(i))

        return self.word_dictionary


    def decode(self):
        key = raw_input('Enter the integer for decoding: ')

        try:
            return self.word_dictionary[int(key)]
        except:
            return 'That integer is not in the dictionary'

t = TextPorter()
print(t.encode())
print(t.decode())
