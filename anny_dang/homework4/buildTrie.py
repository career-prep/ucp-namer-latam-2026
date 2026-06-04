class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.validWord = False 

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        """
        idea:
        - have cur = self.root
        - for loop to walk through each character in word 
            - index = ord(that character) - ord("a")
            - if that self.children at that index = None
                -> self.chilren at that index = TrieNode()
            - cur = self.children at that index 
        
        - cur.validWord = True
        
        time: O(n) (n: number of characters in word)
        space: O(n)
        """
        cur = self.root
        for w in word:
            idx = ord(w) - ord('a')
            if cur.children[idx] == None:
                cur.children[idx] = TrieNode()
            cur = cur.children[idx]

        cur.validWord = True
        return 
    
    def isValidWord(self, word):
        """
        idea:
        - have cur = self.root
        - for loop to walk through each character
            - idx = ord(w) - ord('a')
            - if not exist -> return False
            cur = cur.children[idx]
        
        if cur.validWord = True -> return True else False 

        time: O(n)
        space: O(1)
        """
        if not word:
            return False
        
        cur = self.root
        for w in word:
            idx = ord(w) - ord('a')
            if cur.children[idx] == None:
                return False
            cur = cur.children[idx]
        
        return True if cur.validWord == True else False

    def remove(self, word):
        """
        idea:
        - if word is not a valid word in trie -> return
        - helper function to check if current node has no children
            - for loop through each child in current node
                - if child exists -> return False
            - return True

        - helper recursion dfs(cur, i)
            - cur = current node
            - i = current index in word

        - base case:
            - if i == len(word):
                - mark current node validWord = False
                - if current node has no children -> return True
                - else -> return False

        - recursive case:
            - get idx = ord(word[i]) - ord("a")
            - recurse on cur.children[idx] with i + 1
            - if child node should be deleted:
                - set cur.children[idx] = None

        - while backtracking:
            - if current node has no children and current node is not a valid word
                -> return True
            - else -> return False

        time: O(n) (n = number of characters in word)
        space: O(n) because of recursion stack
        """ 
        if not self.isValidWord(word):
            return
        
        def isNoChildren(node):
            for child in node.children:
                if child is not None:
                    return False
            
            return True 

        def dfs(cur, i):
            if i == len(word):
                cur.validWord = False
                return isNoChildren(cur)
            
            idx = ord(word[i]) - ord('a')
            child = cur.children[idx]

            shouldDeleteChild = dfs(child, i + 1)

            if shouldDeleteChild:
                cur.children[idx] = None
            
            return isNoChildren(cur) and not cur.validWord
        
        return dfs(self.root, 0)
