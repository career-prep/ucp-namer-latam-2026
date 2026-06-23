# Array/String Technique:  Dynamic programming - Tabulation
# Time Complexity: O(N^2) 
# Space Complexity: O(N + M) 

def wordBreak(s: str, wordDict: list[str]) -> bool:
    word_set = set(wordDict)
    dp = [False] * (len(s) + 1)
    dp[0] = True
    
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    return dp[len(s)]

if __name__ == "__main__":
    print("Word break 'leetcode':", wordBreak("leetcode", ["leet", "code"]))
    print("Word break 'applepenapple':", wordBreak("applepenapple", ["apple", "pen"]))

# Time Spent: 25 minutes