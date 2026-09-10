class Node:
    def __init__(self, val):
        self.children = {}
        self.val = val
        self.is_end = False
class WordDictionary:

    def __init__(self):
        self.root = Node(None)

    def addWord(self, word: str) -> None:
        curr = self.root

        for letter in word:
            if letter in curr.children:
                curr = curr.children[letter]
            else:
                curr.children[letter] = Node(letter)
                curr = curr.children[letter]
        curr.is_end = True
        

    def search(self, word: str) -> bool:
        def dfs(j, node):
            curr = node
            for i in range(j, len(word)):
                if word[i] == '.':
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                                return True 
                    return False
                else:
                    if word[i] not in curr.children:
                        return False
                    curr = curr.children[word[i]]

            return curr.is_end

        return dfs(0, self.root)