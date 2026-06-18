# spent 45 minutes

class TrieNode:
    def __init__(self) -> None:
        self.children = {} # size of 26
        self.valid_word = False # indicates if this node marks the end of a word
    
    
class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
        
        
    def insert(self, word: str) -> None:
        """Adds a word to the trie"""
        # Add word
        curr = self.root
        for char in word: 
            if char not in curr.children: # Create path if DNE
                curr.children[char] = TrieNode()
                
            curr = curr.children[char] # Follow path in trie
            
        # Mark as valid word
        curr.valid_word = True
        
        
    def is_valid_word(self, word: str) -> bool: 
        """Returns true if word is ADDED in trie; otherwise false"""
        # Iterate through trie using word characters
        curr = self.root
        for char in word:
            if char not in curr.children: # Fail if path not found
                return False
            curr = curr.children[char]
            
        return curr.valid_word
        
        
    def remove(self, word: str) -> None:
        """Removes a word from the trie and deletes the unused nodes"""
        
        # helper
        def dfs(node: TrieNode, idx: int) -> bool:
            """Returns True if `node` should be deleted (unused branch)."""
            # Reached end of word
            if idx == len(word):
                # Unmark the word if it exists
                if not node.valid_word:
                    return False
                node.valid_word = False
                # Mark for deletion only if no words continue further
                return len(node.children) == 0 
            
            char = word[idx]
            if char not in node.children: # Path DNE
                return False
            
            
            # Delete edge if child branch is now unused
            child = node.children[char]
            if dfs(child, idx+1):
                del node.children[char]
            
            # Delete parent if it has no children and is not a word
            return len(node.children) == 0 and not node.valid_word
        
    
        dfs(self.root, 0)



def run_tests() -> None:
    print("Running tests")
    trie = Trie()

    # Empty tests: is_valid_word()
    assert not trie.is_valid_word("cat")
    trie.remove("cat")


    # insert() and valid_word tests
    trie.insert("cat")
    assert trie.is_valid_word("cat")

    trie.insert("car")
    trie.insert("card")
    trie.insert("catch")

    assert trie.is_valid_word("cat")
    assert trie.is_valid_word("car")
    assert trie.is_valid_word("card")
    assert trie.is_valid_word("catch")
    assert not trie.is_valid_word("ca")
    assert not trie.is_valid_word("random")
    assert not trie.is_valid_word("cardx")

    
    # remove() tests
    # Prefix words
    trie.remove("car")
    assert not trie.is_valid_word("car")
    assert trie.is_valid_word("card")
    assert trie.is_valid_word("cat")
    assert trie.is_valid_word("catch")

    # Nonexistent word
    trie.remove("dne")
    assert trie.is_valid_word("cat")
    assert trie.is_valid_word("card")
    assert trie.is_valid_word("catch")
    assert not trie.is_valid_word("dne")

    # Suffix words
    trie.insert("car")
    trie.remove("card")
    assert not trie.is_valid_word("card")
    assert trie.is_valid_word("car")

    # Full path cleanup
    trie.remove("cat")
    trie.remove("catch")
    trie.remove("car")
    assert not trie.is_valid_word("cat")
    assert not trie.is_valid_word("car")
    assert not trie.is_valid_word("card")
    assert not trie.is_valid_word("catch")
    assert not trie.is_valid_word("ca")
    assert not trie.is_valid_word("c")


    print()
    print("PASS")


if __name__ == "__main__":
    run_tests()
