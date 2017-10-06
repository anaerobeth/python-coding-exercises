def find_pair(arr, total):
    """Given a list of integers, find pairs that sums up to total"""
    my_dict = {}
    size = len(arr)

    # Insert values to a dict O(n)
    for i in range(size):
        my_dict[arr[i]] = i

    # Loop through each key to find it's complement (total - key) O(n)
    for i in range(size):
        diff = total - arr[i]
        if diff in my_dict:
            print("Pair ({},{}) has the sum of {}".format(arr[i], diff, total))

arr = [1, 2, 4, 5, 8, 5, 9 ]
find_pair(arr, 10)

