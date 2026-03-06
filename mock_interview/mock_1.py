# Isomorphic Strings
# Two strings are considered isomorphic if the characters in one string can be replaced to get the characters in the other string.
#  No two distinct characters can be replaced by the same character, but a character can be replaced with itself.
# Example
# Input: “egg”, “add”
# Output: True
# Input: “foo”, “bar”
# Output: False

"""
ideas:
first need to check if the length =; if not then false 

we gonna use 2 hashmap, the hashmap1 store s1 character with its replacement in s2:
ex: e:a , g:d
we do the same with hashmap2:
ex: a:e, d:g

we loop through s1, add the character to hashmap, do the same with s2.
afterwards, check if it match, if not => false

"""

#foo bar ; f:b b:f; 
def iso_strings(s1,s2):
    if len(s1)!=len(s2):
        return False
    
    hashmap1={}
    hashmap2={}

    for i in range(len(s1)):
        char1=s1[i]
        char2=s2[i]

        if char1 not in hashmap1:
            hashmap1[char1]=char2
            print("char 1: "+ str(char1)+":"+str(hashmap1[char1]))

        if char2 not in hashmap2:
            hashmap2[char2]=char1
        print("char 2: "+ str(char2)+":"+str(hashmap2[char2]))
        
        if char2 != hashmap1[char1] or char1 != hashmap2[char2]:
            return False
    
    return True

print(iso_strings("egg","add"))
print(iso_strings("foo","bag"))
print(iso_strings("bag","foo"))


    