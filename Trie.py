class TrieNode(object):
    def __init__(self, c):
        self.letter = c
        self.children = [None] * 26
        self.end = False
        self.prefix_count = 1

class Trie(object):
    def __init__(self):
        self.root = TrieNode('*')

    def insert(self, word):
        curr = self.root
        for letter in word:
            if not curr.children[ord(letter)-ord('a')]:
                n = TrieNode(letter)
                curr.children[ord(letter)-ord('a')] = n
                curr = curr.children[ord(letter)-ord('a')]
            else:
                curr = curr.children[ord(letter)-ord('a')]
                curr.prefix_count +=1
        curr.end = True


    def search(self, word):
        curr = self.root
        for letter in word:
            if curr.children[ord(letter)-ord('a')] is None:
                return False
            curr = curr.children[ord(letter)-ord('a')]
        if curr.end:
            return True
        return False

    def prefix(self, word):
        curr = self.root
        for letter in word:
            if curr.children[ord(letter)-ord('a')] is None:
                return False
            curr = curr.children[ord(letter)-ord('a')]
        return True

a = Trie()
a.insert('a')
a.insert('a')
print (a.root.children[ord('a')-ord('a')].prefix_count)

"""\
       .children[ord('h')-ord('a')] \
       .children[ord('i')-ord('a')] \
       .children[ord('s')-ord('a')].prefix_count)"""