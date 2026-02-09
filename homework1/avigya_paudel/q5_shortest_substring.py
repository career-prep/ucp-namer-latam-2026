# TIME COMPLEXITY: O(N) 
# SPACE COMPEXITY: O(N)
# TIME TAKEN: ~5 minutes
# TECHNIQUE: Not sure if it aligns with any but reset catchup pointer might work 
from collections import defaultdict
from collections import Counter

def shortest_substring(str1, str2):
    """
    given str1 and a second string str2 representing required characters,
    return the length of the shortest substring containing all required characters
    """
    n_target = len(str2)
    target_map = Counter(str2)
    cur_shortest = float("inf")
    
    l = r = 0
    while r < len(str1):
        if (str1[r] in target_map):
            n_target -= 1
            if n_target == 0:
                cur_shortest = min(cur_shortest, r-l+1)
                while l < len(str1) and (str1[l] not in target_map or target_map[str1[l]] == ):
                    l += 1
                l += 1
                n_target += 1
        r += 1

    return cur_shortest


if __name__ == "__main__":
    print(shortest_substring("abracadabra", "abc")) 
    print(shortest_substring("zxycbaabcdwxyzzxwdcbxyzabccbazyx", "zzyzx"))
