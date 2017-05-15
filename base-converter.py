class BaseConverter():

    def get_input(self, prompt):
        return raw_input(prompt)


    def alphabet_codes(self, word):
        codes = []
        for letter in word:
            codes.append(ord(letter) - 97)

        return codes

    def reverse_codes(self, numbers):
        codes = []
        for digit in numbers[::-1]:
            codes.append(chr(digit + 97))

        return "".join(codes)


    def encode(self):
        code = self.get_input('Enter word to encode: ').lower()

        result = 0
        for index, char in enumerate(self.alphabet_codes(code)[::-1]):
            result += int(char)* 26**index

        return result


    def decode(self):
        num = int(self.get_input('Enter integer to decode: '))

        numbers = []
        keep_going = True

        while keep_going:
            result = num % 26
            numbers.append(result)
            num = num / 26
            if num == 0:
                keep_going = False

        return self.reverse_codes(numbers)


n = BaseConverter()
print(n.encode())
print(n.decode())
