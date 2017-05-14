import random as random

class TextLocker():
    """
       Accepts a secret code and a message to lock and returns an integer to the user. To retrieve the original message, the user must give the correct secret key and integer combination.
    """

    def __init__(self):
        self.word_dictionary = {}
        self.secret_codes = {}
        self.secret_messages = {}
        self.message_key = ''
        self.secret = self.register_secret_code()


    def unique_id(self):
        limit = 141167095653376
        return random.randint(1, limit)


    def register_secret_code(self):
        secret = raw_input('Enter your secret key: ')
        self.message_key = self.unique_id()
        self.secret_codes[secret] = self.message_key
        self.secret_messages[self.message_key] = []
        return secret


    def encode(self):
        inputs = raw_input('Enter a series of words: ').split(" ")

        for i in filter(None, inputs):
            word_id = self.unique_id()
            if len(i) <= 10:
                self.word_dictionary[word_id] = i
                self.secret_messages[self.message_key].append(word_id)
            else:
                print('The word {} exceeds the word limit and will not be encoded'.format(i))

        print('Use this code to retrieve the original message: {}'.format(self.secret_codes[self.secret]))


    def decode(self):
        message = []
        secret_key = raw_input('Enter your secret key: ')
        message_key = raw_input('Enter an integer for decoding: ')

        try:
            if self.secret_codes[secret_key] == int(message_key):
                words = self.secret_messages[int(message_key)]
                for word in words:
                    message.append(self.word_dictionary[word])

            return " ".join(message)

        except:
            print('There is no message for that secret and integer combination')


    def decode_message(self):
        result = self.decode()

        print 'Your decoded message is "{}"'.format(result)


t = TextLocker()
t.encode()
t.decode_message()
