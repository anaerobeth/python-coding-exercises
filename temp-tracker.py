"""
TempTracker
Temperature in Fahrenheit, range 0..110
"""
from collections import Counter
import sys

class TempTracker():
    values = []
    num_values = 0
    max_val = -sys.maxsize
    min_val = sys.maxsize
    total_values = 0

    def __init__(self, *args):
        for arg in args:
            self.update_values(arg)

    def insert(self, arg):
        self.update_values(arg)

    def get_max(self):
        return self.max_val

    def get_min(self):
        return self.min_val

    def get_mean(self):
        return self.total_values / self.num_values

    def get_mode(self):
        values_dict = {}
        for value in self.values:
            if value not in values_dict:
                values_dict[value] = 1
            else:
                values_dict[value] += 1

        # if values are numeric:
        # return Counter(values_dict).most_common()[0][0]

        sorted_values = sorted(values_dict.items(), key=lambda x: x[1])
        return sorted_values[-1][0]

    def update_values(self, arg):
        self.num_values += 1
        self.values.append(arg)
        if arg > self.max_val:
            self.max_val = arg
        if arg < self.min_val:
            self.min_val = arg
        self.total_values += arg



t = TempTracker(12, 14, 20)
print(t.num_values)
t.insert(20)
print(t.num_values)
print(t.get_max())
print(t.get_min())
print(t.get_mean())
print(t.get_mode())
