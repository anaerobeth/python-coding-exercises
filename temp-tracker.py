"""
TempTracker
Temperature in Fahrenheit, range 0..110
"""

class TempTracker():
    values = []

    def __init__(self, *args):
        for arg in args:
            self.values.append(arg)

    def insert(self, temp):
        self.values.append(temp)

    def get_max(self):
        return sorted(self.values)[-1]

    def get_min(self):
        return sorted(self.values)[0]

    def get_mean(self):
        total = 0
        for value in self.values:
            total += value
        return total / len(self.values)

    def get_mode(self):
        values_dict = {}
        for value in self.values:
            if value not in values_dict:
                values_dict[value] = 1
            else:
                values_dict[value] += 1

        sorted_values = sorted(values_dict.items(), key=lambda x: x[1])
        return sorted_values[-1][0]

t = TempTracker(12, 14, 20)
print(t.values)
t.insert(20)
print(t.values)
print(t.get_max())
print(t.get_min())
print(t.get_mean())
print(t.get_mode())
