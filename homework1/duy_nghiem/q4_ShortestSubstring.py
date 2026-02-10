"""
Technique: Shrinking/Growing Sliding window
Time Complexity: O(n+m)
Space Complexity: O(m)
n is length of s1
m is length of s2
"""




"""
#we gonna create a hashmap to store the occurance of every character in s2 so that we can look up the char later

create a value to track the missing valuable in s2: missing_char_in_s2

use 2 pointer to represent the 2 limit of a valid subarray
l=the left limit 
r= right limit of the valid sub array

we gonna move the r ptr from 0-> len(s1)-1:
we check if s1[r] in hashmap, then decrease the occurance of the number in hashmap and the missing_char_in_s2 
in order to known that the substring already include all the neccessary char or not

after finding out the valid subarray, we gonna shrink it down (move the left pointer) to find the shortest valid substring 

keep doing that while tracking the min_substring

"""
#a'brac'ada => hashmap={a:-1,b:0,c:0}
def shortest_substring(s1,s2):
    hashmap={}

    for c in s2:
        if c in hashmap:
            hashmap[c]+=1
        else:
            hashmap[c]=1
    
    min_length=float('inf')
    l=0

    missing_char_in_s2=len(s2)

    for r in range(len(s1)):
        # track the missing char so that we can find a valid substring of s1 that include all char in s2
        if s1[r] in hashmap:
            if hashmap[s1[r]]>0:
                missing_char_in_s2-=1
            hashmap[s1[r]]-=1

        # moving the left ptr so that we can find the shortest valid substring
        while missing_char_in_s2==0:
            min_length=min(min_length,r-l+1) 
            if s1[l] in hashmap:
                if hashmap[s1[l]]==0:
                    hashmap[s1[l]]+=1
                    missing_char_in_s2+=1

                elif hashmap[s1[l]]<0:
                    hashmap[s1[l]]+=1

            l+=1
        
    
    if min_length == float('inf'):
        return 0
    else:
        return min_length


    

print(shortest_substring("abracadabra","abc"))
print(shortest_substring("zxycbaabcdwxyzzxwdcbxyzabccbazyx","zzyzx"))
print(shortest_substring("dog","god"))

                

    



     
        


