#Samaksh Arora
#Question 6 - Word Break
#Dynamic programming (Tabulation) + Trie as a parameter
#Time Complexity: O(n^2 * m) where n is the length of string and m is average word length (trie lookup)
#Space Complexity: O(n) for DP array; O(D * m) for trie where D is dictionary size
#Time Spent: >40 minutes


from q1_buildTrie import Trie
def wordBreak(string, dictionary):
    #build the trie
    trie = Trie()
    for word in dictionary:
        trie.insert(word.lower())
    
    string = string.lower()
    lengthOfString = len(string)
    dp = [False] * (lengthOfString + 1)
    dp[0] = True
    for i in range(1, lengthOfString + 1):
        for j in range(i):
            if dp[j] and trie.isValidWord(string[j:i]):
                dp[i] = True
                break
    
    return dp[lengthOfString]

#Test Cases
dictionary = ["Elf","Go","Golf","Man","Manatee","Not","Note","Pig","Quip","Tee","Teen"]
assert wordBreak("mangolf", dictionary) == True
assert wordBreak("manateenotelf", dictionary) == True
assert wordBreak("quipig", dictionary) == False

#Extra:
assert wordBreak("golf", dictionary) == True
assert wordBreak("gonotpig", dictionary) == True
