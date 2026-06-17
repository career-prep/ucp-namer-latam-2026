#Samaksh Arora
#KAnagrams
#Time Complexity: O(n)
#Space Complexity: O(1) since we are bounded by the size of ASCII characters
#2 strings increment hashmap counts

def KAnagrams(string1, string2, k):
    string1_frequency = {}
    string2_frequency = {}
    if len(string1) != len(string2):
        return False
    
    for i in range(len(string1)):
        string1_char = string1[i]
        string2_char = string2[i]
        string1_frequency[string1_char] = string1_frequency.get(string1_char,0) + 1
        string2_frequency[string2_char] = string2_frequency.get(string2_char,0) + 1
    count = 0
    for val in string1_frequency:
        freq1 = string1_frequency[val]
        if val in string2_frequency:
            freq2 = string2_frequency[val]
        else:
            freq2 = 0
        if freq1 > freq2:
            count += (freq1-freq2)
    
    if count <= k:
        return True
    
    return False


string1 = "apple"
string2 = "peach"
k = 1
print(KAnagrams(string1, string2, k)) #output = False

string1 = "debit curd"
string2 = "bad credit"
k = 1
print(KAnagrams(string1, string2, k)) #output = True
 

#Time Spent: >40 Minutes