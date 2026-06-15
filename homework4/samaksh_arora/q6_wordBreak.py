#Samaksh Arora
#Question 6 - Word Break
#Dynamic programming (Tabulation) + Trie as a parameter
#Time Complexity:
#Space Complexity:
#Time Spent:


from homework4.samaksh_arora.q1_buildTrie import Trie
def canBreakWord(string, dictionary):
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
assert canBreakWord("mangolf", dictionary) == True
assert canBreakWord("manateenotelf", dictionary) == True
assert canBreakWord("quipig", dictionary) == False

#Extra: 
assert canBreakWord("golf", dictionary) == True
assert canBreakWord("gonotpig", dictionary) == False
