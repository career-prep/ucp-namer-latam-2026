class TrieNode:
    def __init__(self):
        # each idx represent a char
        
        self.children = [None]*26

        #check if its the end of the word
        self.validWord = False
    

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    # insert the word to Trie
    def insert(self, word:str) -> None:
        if word is None:
            return 

        curr = self.root

        for c in word:
            idx = ord(c) - ord("a")

            if curr.children[idx] is None:
                curr.children[idx] = TrieNode()
            
            curr = curr.children[idx]
        
        curr.validWord = True
        return 

    # check if the word is in the trie or not
    def isValidWord(self, word:str) -> bool:
        if not word:
            return False

        curr = self.root

        for c in word:
            idx = ord(c) - ord("a")

            if curr.children[idx] is None:
                return False

            curr = curr.children[idx]

        #dont return True since there might be a case where: the word is "cat" but we only have "ca"
        return curr.validWord

    
    # remove word from trie and delete unused node
    """
    idea:
        - In order to remove a word in Trie => we mark the last character
        such that: last_char.validWord = False instead of True
        - from that, we traverse back from that char to root and delete the unused node

        => Approach:
            - traverse down to find the removing word
            - when we reach the last char, last_char.validWord = False
            - after we found the last char of the removed word, we backtrack:
                + we remove and backtrack till we reach the char that belongs to other word
                ( in the example below, we backtrack, remove "t" till reach "a" => we stop at "a")

    
    ex: cat, car, care. We wanna remove cat => t.validWord = False

        c           =>          c
        |                       |
        a                       a
       / \                       \
      t   r                       r  
          |                       |  
          e                       e  

    """
    def remove(self, word: str) -> None:
        
        #check if the current char have any child or not
        def isEmpty(node):
            for i in range(26):
                if node.children[i]:
                    return False
            
            return True
        
        #dfs:
        #   + it traverse down the trie(search), clean up the nodes when comeback (backtrack)
        #   + helper: return node -> keep the child
        #             return None -> delete the child reference
        def helper(node, word, depth): # consider depth as the idx of the char in the word
            if node is None:
                return None
            
            #case 1: reach the end of the word
            if depth == len(word):
                if node.validWord == True:
                    node.validWord = False
                #check if it has children or not, if not => delete 
                # (handle the case when reach a, we not gonna remove a since it has other child: "r")
                if isEmpty(node):
                    del node
                    node = None

                return node

                    
            # case 2: go deeper (since have not reach the last char of word)
            idx = ord(word[depth]) - ord("a")
            node.children[idx] = helper(node.children[idx],word,depth+1)

            # clean up when backtrack
            if node.validWord == False and isEmpty(node):
                del node
                node = None
            
            return node
        
        helper(self.root, word, 0)
        return 

            

        


