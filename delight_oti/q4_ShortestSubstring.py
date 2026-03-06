from collections import Counter

def ShortestSubstring(string1, string2):
    '''
    Growing/Sliding window + hashmap

    Time Complexity: O(n)
    Space Complexity: O(n)
    '''

    need= Counter(string2)

    left= 0
    have= {}
    required = len(need)
    min_len = len(string1)
    found = 0

    for index, char in enumerate(string1):
        have[char] = have.get(char,0) + 1
    
        if char in need and have[char] == need[char]:
            found+=1
        
        while found == required:
            window_size = (index-left) + 1
            min_len= min(window_size, min_len)

            left_char = string1[left]
            have[left_char]-=1

            if left_char in need and have[left_char] < need[left_char]:
                found-=1

            left+=1
    
    return min_len

# TIme taken: 40mins

# print(ShortestSubstring("dog", "god"))
# Output: 3

# print(ShortestSubstring("abracadabra", "abc")) 
# Output: 4