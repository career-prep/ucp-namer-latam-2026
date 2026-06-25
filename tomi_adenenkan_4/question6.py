

class Node:
    def __init__(self):
        self.children = {}
        self.end = False
        
class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, data):
        head = self.root

        for ch in data:
            if ch not in head.children:
                head.children[ch] = Node()
            head = head.children[ch]

        head.end = True

    """def search(self, data):
        head = self.root

        for ch in data:
            if ch not in head.children:
                return False
            head = head.children[ch]
            if head.end == True:
                head = self.root

        return head.end
        """
    def search(self, word):
        head = self.root
        res = []
        check = ""
        for c in word:
            if c not in head.children:
                print(res)
                head = self.root
                if c in head.children:
                    head = head.children[c]
            else:
                head = head.children[c]
            check += c
            if head.end == True:
                print(f"first done, char = {c}")
                res.append(check)
                check = ""

        if check:
            res.append(check)
        print(res)
                
                

        return "".join(res) == word

lsst = ["elf", "go", "golf", "man", "manatee", "not", "note", "pig", "quip", "tee", "teen"]
tri = Trie()
for each in lsst:
    tri.insert(each)
print(tri.search("manateenotelf"))
