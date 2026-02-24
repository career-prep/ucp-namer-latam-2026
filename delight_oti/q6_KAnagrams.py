from collections import Counter
def KAnagrams(string1, string2, k):
    '''
    two arrays

    Time Complexity: O(n)
    Space Complexity: O(n)
    '''
    
    if len(string1) != len(string2):
        return False
    
    s = Counter(string1)
    t = Counter(string2)

    changes = 0

    for char in s:
        if s[char] != t.get(char,0):
            if s[char] > t.get(char,0):
                changes += s[char]-t.get(char,0)
    
    if changes <= k:
        return True
    
    return False


#Time Taken: 20mins 

# string1 = "apple"
# string2 = "peeeh"
# k= 2
# Output: False

# string1 = "apple"
# string2 = "peeeh"
# k = 3
# Output:True

# print (KAnagrams(string1,string2,k))