# TIME COMPLEXITY: O(N) 
# SPACE COMPEXITY: O(N)
# TIME TAKEN: ~5 minutes
# TECHNIQUE: 
from collections import defaultdict
from collections import Counter

def shortest_substring(str1, str2):
    """
    given str1 and a second string str2 representing required characters,
    return the length of the shortest substring containing all required characters

    "abracadabra"
         ^
    "abc"

    {a:-1, b:0, c:0}
    cnt = 3
    tar = 3
    """
    n_target = len(str2)
    cnt = 0
    target_map = Counter(str2)
    cur_shortest = float("inf")
    
    l = r = 0
    while r < len(str1):
        if (str1[r] in target_map):
            target_map[str1[r]] -= 1
            if target_map[str1[r]] >= 0:
                cnt += 1
                if cnt >= n_target:
                    cur_shortest = min(cur_shortest, r-l+1)
                    while cnt >= n_target:
                        if str1[l] in target_map:
                            target_map[str1[l]] += 1
                            if (target_map[str1[l]] >= 0):
                                cnt -= 1
                        l += 1
                    while (l <= r and str1[l] not in target_map):
                        l += 1
        r += 1
    
    while (l <= r and str1[l] not in target_map):
        l += 1
        cur_shortest = min(cur_shortest, r-l+1)

    return cur_shortest


if __name__ == "__main__":
    print(shortest_substring("abracadabra", "abc")) 
    print(shortest_substring("zxycbaabcdwxyzzxwdcbxyzabccbazyx", "zzyzx"))
    print(shortest_substring("god", "god"))
