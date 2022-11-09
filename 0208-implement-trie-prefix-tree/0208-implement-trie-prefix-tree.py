class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict()
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode() # set the root node as empty

    def insert(self, word: str) -> None:
        cur = self.root
        for letter in word:
            if letter not in cur.children:
                cur.children[letter] = TrieNode()
            cur = cur.children[letter]
        cur.isWord = True
            

    def search(self, word: str) -> bool:
        cur = self.root
        for letter in word:
            if letter not in cur.children:
                return False    
            cur = cur.children[letter]
        return cur.isWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for letter in prefix:
            if letter not in cur.children:
                return False
            cur = cur.children[letter]
        return True
        
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)