class NumberContainer():

    def __init__(self, arr):
        self.arr = arr
        self.odds = []
        self.evens = []
        self.primes = []
        self.get_primes()
        self.remove_evens()
        self.remove_odds()


    def remove_evens(self):
        self.odds = [el for el in self.arr if el % 2 != 0]


    def remove_odds(self):
        self.evens = [el for el in self.arr if el % 2 == 0]


    def get_primes(self):
        for el in self.arr:
            if el < 3:
                self.primes.append(el)
            else:
                for i in range(2, el):
                    if (el % i) != 0:
                        self.primes.append(el)
                        break




nc = NumberContainer([1, 2, 3, 5])
print(nc.arr)
print('Odds: ', nc.odds)
print('Evens: ', nc.evens)
print('Primes: ', nc.primes)
