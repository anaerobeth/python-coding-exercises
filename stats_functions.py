from collections import Counter
import mergesort as ms

def calculate_statistics(values):
    mean = sum(values) / len(values)

    sorted_values = ms.sorter(values)
    median = sorted_values[int(len(values) / 2)]

    # Counter(values).most_common(1) => [(value, count)]
    mode = Counter(values).most_common(1)[0][0]

    return (mean, median, mode)


values = [ 10, 30, 40, 20, 50, 10]
mean, median, mode = calculate_statistics(values)

print("Mean: {mean} Median: {median} Mode: {mode}".format(mean=mean, median=median, mode=mode))


