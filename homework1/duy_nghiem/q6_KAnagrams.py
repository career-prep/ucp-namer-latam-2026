"""
Technique: Once directional running computation/total
Time Complexity: O(n)
Space Complexity: O(n)
"""


"""
Approach:
track the occurance of the characters of the 2 string into 2 different hashmap
after that, we gonna loop through the key of hashmap1, there will be 2 case:
1: char in hashmap1 does not appear in hashmap2 => k-=hashmap1[c]
2: char in hashmap1 occurs more than char in hashmap2 => k-= hashmap1[c] - hashmap2[c]

(if hashmap1 has a char that have more occurance than itself in hashmap2 
=> it means that there might be some other char in hashmap1 occur less compare to hashmap2
=> dont need to check or it will be duplicate )

finally, if the change is more than k (k<0) => it must be false; otherwises, it is true

"""
def k_anagrams(s1,s2,k):
    if len(s1)!= len(s2):
        return False

    hashmap1={}
    hashmap2={}

    for c1 in s1:
        if c1 in hashmap1:
            hashmap1[c1]+=1
        else:
            hashmap1[c1]=1
    
    for c2 in s2:
        if c2 in hashmap2:
            hashmap2[c2]+=1
        else:
            hashmap2[c2]=1 
    
    for c in hashmap1:
        if c not in hashmap2: #exist in s1 but not in s2
            k-= hashmap1[c]

        elif hashmap1[c]>hashmap2[c]: #exist in s1 and s2
            k-= hashmap1[c]-hashmap2[c]
    
    return k>=0

print(k_anagrams("apple","peach",1))
print(k_anagrams("apple","peach",2))
print(k_anagrams("cat","dog",3))
print(k_anagrams("debit curd","bad credit",1))
print(k_anagrams("baseball","basketball",2))







