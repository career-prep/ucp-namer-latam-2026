def kAnagrams(s, t, k):
    '''
    First check if both strings same length
    
    Remove spaces

    Create a frequency map to track character frequencies, 
    for example:
    "apple" = {a:1, p:2, l:1, e:1}, "peach" = {a:1, p:1, e:1, c:1, h:1}

    track matching characters

    find needed changes by matching characters - length

    if needed changes == k then return true else return false
    ''' 
    map_s = {}
    map_t = {}
    matching = 0
    

    s = "".join(s.split())
    t = "".join(t.split())

    if len(s) != len(t):
        return False
    
    for c in s:
        map_s[c] = map_s.get(c, 0) + 1
    for c in t:
        map_t[c] = map_t.get(c, 0) + 1
    
    for key, val in map_s.items():
        # if key in map_t and val == map_t[key]:
        #     length -= val
        matching += min(val, map_t.get(key, 0))
    length = len(s) - matching
    if length <= k:
        return True
    else:
        return False


def test_kAnagrams():
    assert kAnagrams("apple", "peach", 1) == False, "Test Case 1 Failed"

    assert kAnagrams("apple", "peach", 2) == True, "Test Case 2 Failed"

    assert kAnagrams("cat", "dog", 3) == True, "Test Case 3 Failed"

    assert kAnagrams("debit curd","bad credit", 1) == True, "Test Case 4 Failed"

    assert kAnagrams("baseball", "basketball", 2) == False, "Test Case 5 Failed"

if __name__ == "__main__":
    test_kAnagrams()