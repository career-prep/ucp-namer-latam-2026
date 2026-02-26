# Question 7: KAnagrams
# Two strings are considered to be "k-anagrams" if they can be made into anagrams by changing at most k characters in one of the strings. Given two strings and an integer k, determine if they are k-anagrams.
# Examples:
# Input Strings: "apple", "peach"
# Input k: 1
# Output: False
# Input Strings: "apple", "peach"
# Input k: 2
# Output: True
# Input Strings: "cat", "dog"
# Input k: 3
# Output: True
# Input Strings: "debit curd", "bad credit"
# Input k: 1
# Output: True
# Input Strings: "baseball", "basketball"
# Input k: 2
# Output: False

# notes- 
# time complexity - o(N) as it is travelling 1 times in each array
# time taken- around 40 mins
# 2 string increase/ decrease hashmap count

def kanagrams(str1, str2, k):
    if len(str1) != len(str2):
        return False
    hasmap= {}
    for ch in str1:
        if ch in hasmap:
            hasmap[ch] += 1 
        else:
            hasmap[ch] = 1
    
    for ch in str2:
        if ch in hasmap:
            hasmap[ch] -= 1 
        
    total = sum(hasmap.values())

    return total <= k 
print(kanagrams("apple", "peach", 1))
print(kanagrams("debit curd", "bad credit", 1))


