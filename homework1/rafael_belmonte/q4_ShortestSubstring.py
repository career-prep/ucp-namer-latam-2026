#variable-size (shrinking/growing) sliding window
#assumption: return 0 if no valid substring found
#assumption: should match the quantity of repeated characters in constraint
#time complexity: O(n+m)
#space complexity: O(n+m)
#39 minutes


def shortest_substring(s, constraint):
    if not s or not constraint:
        return 0
    required_count = {} #map to count constraint characters O(m)
    for char in constraint:
        if char in required_count:
            required_count[char] += 1
        else:
            required_count[char] = 1
    required_unique = len(required_count) #number of unique characters to match O(m)
    window_count = {} #map to count window characters O(n)
    unique_count = 0
    l = 0
    min_len = float("inf")
    for r in range(len(s)): #expand right pointer
        char = s[r]
        if char in window_count:
            window_count[char] += 1
        else:
            window_count[char] = 1
        if char in required_count and window_count[char] == required_count[char]: #check constraint
            unique_count += 1
        while unique_count == required_unique: #shring left pointer
            current_len = r - l + 1
            if current_len < min_len:
                min_len = current_len
            left_char = s[l] #character to be removed from the window
            window_count[left_char] -= 1
            if left_char in required_count and window_count[left_char] < required_count[left_char]: #check constraint to stop shrinking
                unique_count -= 1
            l += 1
    return min_len if min_len != float("inf") else 0 

#test cases
string1 = "abracadabra"
constraint1 = "abc"
assert(shortest_substring(string1, constraint1) == 4) # "brac"

string2 = "zxycbaabcdwxyzzxwdcbxyzabcobazyx"
constraint2 = "zzyzx"
assert(shortest_substring(string2, constraint2) == 10) # "zzxwdcbxyz"

string3 = "dog"
constraint3 = "god"
assert(shortest_substring(string3, constraint3) == 3) # "dog"

print("wa")