# sliding window
# Time complexity: O(n+m) 
# Space complexity: O(k) 
# where n is length of s1 and m is length of s2 and k is number of unique chars in s2


def shortestSubstring(s1, s2):
    # empty case
    if not s1 or not s2: 
        return -1

    # load frequency hashmap of required letters and get length
    target_freq = {}
    for char in s2:
        target_freq[char] = target_freq.get(char, 0) + 1
    len_s2 = len(s2)
    
    # ensure s1 is equal/longer
    len_s1 = len(s1)
    if len_s1 < len_s2:
        return -1
    
    # sliding window
    window_freq = {}
    have, need = 0, len(target_freq)
    shortest_len = float('inf')
    left = 0
    for right in range(len_s1):
        char = s1[right]
        if char in target_freq:
            window_freq[char] = window_freq.get(char, 0) + 1
            if window_freq[char] == target_freq[char]: # only increment when we accumulated enough of this char
                have += 1
        
        while have == need: # valid window
            shortest_len = min(shortest_len, right-left+1) # update shortest
            left_char = s1[left]
            if left_char in target_freq:
                window_freq[left_char] -= 1
                if window_freq[left_char] < target_freq[left_char]: # only decrement when we no longer have enough of this char
                    have -= 1
            left += 1
            
    return shortest_len if shortest_len != float('inf') else -1




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
    