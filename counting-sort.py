def sort(arr):
    """ Given a list of integers from 0-9, return a sorted list """

    counts = {}
    for i in range(10):
        counts[i] = 0

    for num in arr:
        counts[num] += 1

    output = []
    for key in counts.keys():
        for i in range(counts[key]):
            output.append(key)

    print(output)

arr = [1, 4, 1, 2, 7, 5, 2]
sort(arr)
