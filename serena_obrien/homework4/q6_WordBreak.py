# Time complexity: O(n^2)
# Space complexity: O(n)

# Technique: Dynamic programming: memoization
# Could a Trie be used in this problem to optimize over string slicing?

def WordBreak(s: str, dictionary: list):
    memo = {}
    
    word_set = set()
    for word in dictionary:
        word_set.add(word.lower())

    s = s.lower()

    def f(i):
        if i == len(s):
            return True
        
        if i in memo:
            return memo[i]
        
        for j in range(i + 1, len(s) + 1):
            if s[i:j] in word_set and f(j):
                memo[i] = True
                return True
            
        memo[i] = False
        return False
    
    return f(0)

if __name__ == "__main__":
    dictionary = ["Elf", "Manatee", "Quip", "Go", "Golf", "Man", "Not", "Note", "Pig", "Quip", "Tee", "Teen"]
    inputs = ["mangolf", "manateenotelf", "quipig"]

    for i in inputs:
        print(f"{i}: {WordBreak(i, dictionary)}")

# ~ time spent: ~30 minutes