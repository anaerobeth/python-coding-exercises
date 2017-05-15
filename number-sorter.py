class SimpleSort():

    def sort(self):
        array = [3,2,7]
        temp = [array.pop()]

        for index, num in enumerate(temp):
            if len(array) >= 1:
                item = array.pop()
            else:
                break
            if num > item:
                temp.insert(index, item)
            else:
                temp.insert(index+1, item)

        return temp

s = SimpleSort()
print(s.sort())
