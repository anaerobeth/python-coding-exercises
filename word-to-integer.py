import random as random

class TextPorter():

    def __init__(self):
        self.word_dictionary = {}
        self.secret_codes = {}
        self.secret = self.register_secret_code()

    def unique_id(self):
        limit = 141167095653376
        return random.randint(1, limit)

    def register_secret_code(self):
        secret = raw_input('Enter your secret key (max 10 characters): ')
        self.secret_codes[secret] = []

        return secret

    def encode(self):
        inputs = raw_input('Enter a series of words: ').split(" ")

        for i in filter(None, inputs):
            word_id = self.unique_id()
            if len(i) <= 10:
                self.word_dictionary[word_id] = i
                self.secret_codes[self.secret].append(word_id)
            else:
                print('The word {} exceeds the word limit and will not be encoded'.format(i))

        print(self.word_dictionary)
        return self.secret_codes


    def decode(self):
        key = raw_input('Enter the integer for decoding: ')

        try:
            return self.word_dictionary[int(key)]
        except:
            return 'That integer is not in the dictionary'

t = TextPorter()
print(t.encode())
print(t.decode())
