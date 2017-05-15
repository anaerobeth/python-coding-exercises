class SimpleSort():
    """
    Loop through indexes ranging from 1 to length of array:
    set current to value at index
    set pointer to index
    compare current to value before the pointer(tail)
    if tail is greater than current:
        write the tail to array at pointer position
        move the pointer backwards and repeat
        stop when pointer reaches 0 or tail is less
    if pointer is not the same as index:
        write the current to the array at pointer position


    TODO: how to swap positions in array?
    """


    def sort(self):
        array = [3,2,7,5,1]
        for i in range(1, len(array)):
            current =  array[i]
            pointer = i

            while((pointer > 0) and (array[pointer-1] > current)):
                array[pointer] = array[pointer-1]
                pointer = pointer -1

            if pointer != i:
                array[pointer] = current

        return array

s = SimpleSort()
print(s.sort())
