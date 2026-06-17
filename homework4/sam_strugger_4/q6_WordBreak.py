# O(n * m) time complexity and O(n) space complexity
# I'm going to come back and solve this another time with a trie

# Plan
"""
I am trying to decide between a trie or dp approach to this problem. 
DP is significantly easier for me to visualize so I'll go with that. 

What we can do:
Iterate through the str and at each point in the string stop and see if it's 
a valid word. If it it is a valid word we mark it in an array of corresponding
indexes. The catch is that we can only mark it as valid if there is a valid word leading into
it
"""
def wordBreak(dictionary, str):
    dp = [0] * (len(str)+1)
    dp[0] = 1 # do this so that no characters is "true" 
    dictionary = set(dictionary)

    # Doing an O(n) operation at the beginning to get the longest word
    # will reduce the time complexity of our nested for loops 
    # so we don't get O(n^2)

    longest_word = 0
    for word in dictionary:
        if len(word) > longest_word:
            longest_word = len(word)

    for i in range(len(str)):
        if not dp[i]: # because we did dp = len(str)+1 dp[i] corresponds to the character before the current
            continue   

        for j in range(i+1, min(i+longest_word+1, len(str)+1)): 
            if str[i:j] in dictionary:
                dp[j] = 1

    return dp[len(str)]

# This problem took me around an hour

# Test Cases
test1 = wordBreak(["leet", "code"], "leetcode")
print(test1)

test2 = wordBreak(["apple", "pen"], "applepenapple")
print(test2)

test3 = wordBreak(["cats", "dog", "sand", "and", "cat"], "catsandog")
print(test3)

test4 = wordBreak(["a", "aa", "aaa"], "aaaaaa")
print(test4)
     
