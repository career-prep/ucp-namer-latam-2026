# dynamic sliding window
# spent 40 min
# Time complexity - O(n^2*k) 
# Space Complexity - O(n)

from math import inf


def shortestSubstring(s1, s2):
    # empty case
    if not s1 or not s2: 
        return -1
    
    # load frequency hashmap of required letters and get length
    target_freq = {} 
    len_s2 = 0 
    for char in s2:
        target_freq[char] = target_freq.get(char, 0) + 1
        len_s2 += 1
    
    # ensure s1 is equal/longer
    len_s1 = len(s1)
    if len_s1 < len_s2: 
        return -1
    
    shortest_len = inf # keeps track of shortest substring
    
    for left in range(len_s1-len_s2+1): # iterate through s1 with room for window of size s2
        if s1[left] not in target_freq: # will not be shortest
            continue
        
        window_freq = {s1[left] : 1} # window frequency map
        right = left + 1 # expands window
        while (window_freq != target_freq):
            if right == len_s1: # oob --> no more possible combos --> return shortest
                return -1 if shortest_len == inf else shortest_len
            
            if s1[right] in target_freq: # in target string -> add to window
                if s1[right] in window_freq:
                    if window_freq[s1[right]] != target_freq[s1[right]]: # make sure to not exceed value or else check will fail
                        window_freq[s1[right]] += 1
                else:
                    window_freq[s1[right]] = 1
            
            right += 1
            
        shortest_len = min(shortest_len, right-left) # update shortest
        
        if shortest_len == len_s2: # cannot be any shorter
            return shortest_len
        
    return -1 if shortest_len == inf else shortest_len # -1 if pattern not found 
        

    
        
    
if __name__ == "__main__":
    string1 = "abracadabraw"
    string2 = "braw"
    print(shortestSubstring(string1, string2))
    
    string3 = "zxycbaabcdwxyzzxwdcbxyzabccbazyx"
    string4 = "zzyzx"
    print(shortestSubstring(string3, string4))
        
    string5 = "dog"
    string6 = "god"
    print(shortestSubstring(string5, string6))
    
    string7 = "hi"
    string8 = "hii"
    print(shortestSubstring(string7, string8))
    