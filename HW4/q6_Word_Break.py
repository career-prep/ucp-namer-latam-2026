"""
idea:
    we can use dp
    the ultimate goal is to check if the last char be True or False



"""
def word_break(word, dictionary):
    words = set(dictionary)

    n = len(word)

    # dp[i] check if the first i chars or the string be broken into valid word in dict
    dp = [False] * (n+1)

    #base case: empty string is true (first 0 char => true)
    dp[0] = True

    #try every ending postion
    for i in range(1, n+1):
        #try every possible split point 
        for j in range(i):

            #left part must already be valid
            if dp[j]:
                curr_word = word[j:i]

                if curr_word in word:
                    dp[i] = True
                    break

    
    return dp[n]

print(word_break("mangolf", ["elf", "go", "golf", "man", "manatee", "not", "note", "pig", "quip", "tee", "teen"]))

