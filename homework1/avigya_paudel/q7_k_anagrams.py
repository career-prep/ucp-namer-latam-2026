# TIME COMPLEXITY: O(N) 
# SPACE COMPEXITY: O(N)
# TIME TAKEN: ~7 minutes
# TECHNIQUE: One-directional running computation/total
from collections import Counter 

def is_anagrams(str1, str2, k):
    """
    returns True if str1 and str2 are anagrams by subsituting at most k characters 
                else returns False
    """
    n1, n2 = len(str1), len(str2)
    if n1 != n2: return False

    c1_count = Counter(str1) 
    for c in str2:
        if (c not in c1_count) or (c in c1_count and c1_count[c] <= 0): 
            if k > 0:
                k -= 1
            else:
                return False
            c1_count[c] -= 1
    return True


if __name__ == "__main__":
    print(is_anagrams("apple","peach",1))            # Expected: False
    print(is_anagrams("apple","peach",2))            # Expected: True
    print(is_anagrams("cat","dog",3))                # Expected: True
    print(is_anagrams("cat","dog",2))                # Expected: False
    print(is_anagrams("debit curd","bad credit",1))  # Expected: True
    print(is_anagrams("baseball","basketball",2))    # Expected: False
