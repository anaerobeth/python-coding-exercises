class TrieNode:

    def __init__(self, char = ''):
        self.children = [None] * 26  # English alphabet chars
        self.is_end_word = False
        self.char = char


    def mark_leaf(self):
        self.is_end_word = True


    def unmark_leaf(self):
        self.is_end_word = False



class Trie:

    def __init__(self):
        self.root = TrieNode()


    def get_index(self, t):
        return ord(t) - ord('a')


    def insert(self, key):

        """Insert the trie node at the correct index
        Set is_end_word to True for last node
        Cases: common prefix, no common prefix, word exists
        """

        if key == None:
            return

        key = key.lower()
        current = self.root
        index = 0

        for level in range(len(key)):
            index = self.get_index(key[level])

            if current.children[index] == None:
                current.children[index] = TrieNode()
                print(key[level] + ' inserted')
            current = current.children[index]

        current.mark_leaf()
        print(f"'{key}' inserted")


    def search(self, key):

        """Trace the path corresponding to the characters in word
        Check if is_end_word is True (word must end in leafnode)
        Cases: non-existent, word is a substring, word exists
        """

        if key == None:
            return False

        key = key.lower()
        current = self.root
        index = 0

        for level in range(len(key)):
            index = self.get_index(key[level])
            if current.children[index] == None:
                return False
            current = current.children[index]

        if current != None and current.is_end_word:
            print(f'{key} found')
            return True

        return False


    def no_children(self, current):
        for i in range(len(current.children)):
            if current.children[i] != None:
                return Flase
        return True


    def delete_helper(self, key, current, length, level):

        """Unmark end and remove nodes to root if there are no children
        Cases: no suffix/prefix, word is prefix, has common prefix
        """

        deleted = False
        if current == None:
            print('Key does not exist')
            return deleted

        if level == length:
            if self.no_children(current):
                current = None
                deleted = True
            else:
                current.unmark_leaf()
                deleted = False
        else:
            child = current.children[self.get_index(key[level])]
            child_deleted = self.delete_helper(key, child, length, level + 1)
            if child_deleted:
                current.children[self.get_index(key[level])] = None
                if current.is_end_word:
                    deleted = False

                elif self.no_children(current) == False:
                    deleted = False

                else:
                    current = None
                    deleted = True
            else:
                deleted = False

        return deleted


    def delete(self, key):
        if self.root == None or key == None:
            print('None key or empty trie error')
            return
        self.delete_helper(key, self.root, len(key), 0)
        print(f"{key} deleted")

    def count_words(self, root):

        """Trace all paths to all leaf nodes
        Count nodes with is_end_word as True
        """

        count = 0

        if root.is_end_word:
            count += 1

        for i in range(26):
            if root.children[i] != None:
                count += self.count_words(root.children[i])

        return count


trie = Trie()
keys = ['there', 'any', 'the', 'a']
for i in range(len(keys)):
    trie.insert(keys[i])

trie.search('any')
trie.delete('any')


print(trie.count_words(trie.root))
