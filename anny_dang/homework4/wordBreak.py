def breakWord(word, dictionary):
    """
    idea:
    - lowercase word and put all lowercase versions of all words in dictionary to a set 
    - create an dp list with len(word) + 1 in length and all values = False
    - set first value in dp = True (assume we have empty string)
    - create a parent list with len(word) in length and all values = -1 
    - outer loop walk through each character in word (i)
        - inner loop walk through from 0 to outer index (i + 1)
            - if dp[j] true and lowercase_word[j:i] in word set -> dp[i+1] = True, parent[j] = i break 
    
    - if not dp[n] -> return False, []
    - walk through each element in parent list 
        - if parent at that position != -1 -> add s[i:parent[i]] to ans list 
    - return True, ans list

    time: O(n^2)
    space: O(n)
    """
    s = word.lower()
    n = len(s)
    word_set = {word.lower() for word in dictionary}
    dp = [False]*(n + 1)
    dp[0] = True
    parent = [-1]*(n + 1)

    for i in range(n):
        for j in range(i + 1):
            if dp[j] and s[j:i + 1] in word_set:
                dp[i + 1] = True
                parent[i + 1] = j
                break 
    
    if not dp[n]:
        return False, []

    ans = []
    end = n
    while end > 0:
        start = parent[end]
        ans.append(s[start:end])
        end = start 
        
    ans.reverse()
    return True, ans

dictionary = [
    "Elf",
    "Go",
    "Golf",
    "Man",
    "Manatee",
    "Not",
    "Note",
    "Pig",
    "Quip",
    "Tee",
    "Teen",
]

print('Input: "mangolf" ->', breakWord("mangolf", dictionary))
print('Input: "manateenotelf" ->', breakWord("manateenotelf", dictionary))
print('Input: "quipig" ->', breakWord("quipig", dictionary))