#Samaksh Arora
#Shortest Substring
#Time Complexity: O(n^2 * m)
#Space Complexity: O(m)
#Optimal Solution: Dynamic Sliding Window | This Solution: Brute Force

def ShortestSubstring(string1, string2):
    required = {}
    check = {}
    for char in string2:
        check.add(char)
        required[char] = required.get(char, 0) + 1

    left = 0
    right = 0
    satisfied = False
    while left<=right:
        while not satisfied:
            if string1[right] in required and string1[right] > 0:
                string1[right] -= 1
                if string1[right] in check and required[string1[right] == 0]:
                    check.remove(string1[right])
                    if not check:
                        satisfied = True
            if not satisfied:
                right += 1
        while satisfied:
            if string1[left] in required and string1[left]
        

            


    return len(result)

test = "abracadabra"
string2 = "abc"
print(ShortestSubstring(test,string2)) #output = 4

test = "dog"
string2 = "god"

print(ShortestSubstring(test,string2)) #output = 3
   
#Time Spent: >40 minutes





        

    

