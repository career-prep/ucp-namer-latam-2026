#Samaksh Arora
#Shortest Substring
#Time Complexity: O(n^2 * m)
#Space Complexity: O(m)
#Optimal Solution: Dynamic Sliding Window | This Solution: Brute Force

def ShortestSubstring(string1, string2):
    required = {}
    for char in string2:
        required[char] = required.get(char, 0) + 1

    result = ""
    for i in range(len(string1)):
        curr_window = {}
        for j in range(i, len(string1)):
            curr_char = string1[j]
            curr_window[curr_char] = curr_window.get(curr_char, 0) + 1
            check = True
            for letter in required:
                if curr_window.get(letter, 0) < required[letter]:
                    check = False
                    break
            if check:
                substring = string1[i:j+1]
                if result == "" or len(substring) < len(result):
                    result = substring
                break

    return len(result)

test = "abracadabra"
string2 = "abc"
print(ShortestSubstring(test,string2)) #output = 4

test = "dog"
string2 = "god"

print(ShortestSubstring(test,string2)) #output = 3
   
#Time Spent: >40 minutes





        

    

