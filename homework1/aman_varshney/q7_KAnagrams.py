# spent 30 min
# two strings increment/decrement hashmap counts
# Time Complexity - O(n)
# Space Complexity - O(n)


def KAnagrams(s1, s2, k):
    # null cases
    if k < 0: return False
    if len(s1) != len(s2): return False # must be same size

    freq1 = {} # freq map for s1
    freq2 = {} # freq map for s2
    for char in s1:
        freq1[char] = freq1.get(char, 0) + 1
    for char in s2:
        freq2[char] = freq2.get(char, 0) + 1
        
    # try to turn freq2 into freq1
    # modify until same or run out of changes 
    for key in freq1:
        if key not in freq2: # add letters to freq2
            amt = freq1[key]
            freq2[key] = amt
            k -= amt/2 # half moves (bc only modifying one array, not swapping)
        elif freq1[key] > freq2[key]: # increase count in freq2
            amt = freq1[key] - freq2[key]
            freq2[key] += amt
            k -= amt/2
        elif freq1[key] < freq2[key]: # decrease count in freq2
            amt = freq2[key] - freq1[key]
            freq2[key] -= amt
            k -= amt/2
        else: # equal -> fine
            continue
        
        # ensure that there are more changes or else failed
        if k <= 0:
            return False
        
    return True




if __name__ == "__main__":
    input_strings = [
        ("apple", "peach"),
        ("apple", "peach"),
        ("cat", "dog"), 
        ("debit curd", "bad credit"),
        ("baseball", "basketball")
    ]
    input_ks = [
        1,
        2,
        3,
        1,
        2
    ]
    expected = [
        False,
        True,
        True,
        True,
        False
    ]
    
    for i in range(len(input_strings)):
        print("strings: ", input_strings[i][0], ", ", input_strings[i][1])
        print("k: ", input_ks[i])
        print("expected: ", expected[i])
        print("actual: ", KAnagrams(input_strings[i][0], input_strings[i][1], input_ks[i]))
        print()
        
        