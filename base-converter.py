class BaseConverter():

    """
    Accepts a string input and converts up to 10 chars of input to ascii
    Then accepts an integer input and converts it to character

    """

    def alphabet_codes(self, word):
        codes = [ ord(letter) - 97 for letter in word ]

        return codes


    def reverse_codes(self, numbers):
        codes =  [ chr(digit + 97) for digit in numbers[::-1] ]

        return "".join(codes)


    def encode(self, item):
        result = 0
        for index, char in enumerate(self.alphabet_codes(item)[::-1]):
            result += int(char)* 26**index

        return result


    def decode(self):
        num = int(input('Enter integer to decode: '))

        numbers = []
        num = 1

        while num != 0:
            numbers.append(num % 26)
            num = num // 26

        return self.reverse_codes(numbers)


    def run(self):
        message = []
        phrase = input('Enter phrase to encode: ')

        if isinstance(phrase, str):
            for word in phrase.lower().split(" "):
                if len(word) > 10:
                    print("'{}' exceeds character limit and has been removed".format(word))
                else:
                    message.append(word)

            for item in message:
                print(self.encode(item))

            print(self.decode())
        else:
            print('Invalid input')


n = BaseConverter()
n.run()
