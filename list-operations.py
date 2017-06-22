"""
Implement a list structure that supports basic operations
orig_list = [10, 20, 30, 40, 50]
item_to_search = 50
item_to_insert = 15
insertion_position = 2
item_to_delete = 40
item_to_merge = 60
item_index_to_update = 4
item_replacement = 99
"""

class MyList(object):

    def __init__(self, *args):
        self.items = [ arg for arg in args ]

    def _traverse(self):
        return [ i for i in self.items ]

    def _search(self, item):
        result = [True for i in self.items if i == item]
        return "Not found" if not result else "Found"

    def _insert(self, item, position):
        return self.items[:position-1] + [item] + self.items[position-1:]

    def _delete(self, item):
        target_index = [ index for index, element in enumerate(self.items) if element == item ]
        if not target_index:
            return self.items
        else:
            position = target_index[0]
            return self.items[:position] + self.items[position+1:]

    def _merge(self, item):
        return self.items + [item]

    def _update(self, new_item, position):
        return self.items[:position-1] + [new_item] + self.items[position:]


l = MyList(10, 20, 30, 40, 50)
assert(l._traverse()) == [10, 20, 30, 40, 50]
assert(l._search(20)) == "Found"
assert(l._search(99)) == "Not found"
assert(l._insert(15, 2)) == [10, 15, 20, 30, 40, 50]
assert(l._delete(40)) == [10, 20, 30, 50]
assert(l._delete(99)) == [10, 20, 30, 40, 50]
assert(l._merge(60)) == [10, 20, 30, 40, 50, 60]
assert(l._update(99, 5)) == [10, 20, 30, 40, 99]
