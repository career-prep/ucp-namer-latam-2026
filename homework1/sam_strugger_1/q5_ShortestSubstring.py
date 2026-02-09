#this one is actually the shrinking/growing sliding window problem
# my solution has O(n+m) time and O(k) space complexity where k is the number of unique characters

# I had to use the internet a bit for this problem. 
# I correctly identified the type of problem but struggled figuring out how to compare dictionaries to see if the window should grow or shrink

# ===================================================
# # def main():

# def shortestSubstring(str1,str2):

#     requirements = Counter(str2)
#     moving_char_count = {}
#     min_length = float('inf')
#     needed_chars = len(str2)
#     left_pointer = 0

#     for i, c in enumerate(str1):
#         if c not in moving_char_count:
#             moving_char_count[c] = 1
#         else:
#             moving_char_count[c] += 1

#         if c in requirements and moving_char_count[c] == 

# ======== Above is what I completed in 40 minutes. I had a tough time combining dictionaries with the necessary technique 

from collections import Counter

def main():
    test1 = shortestSubstring("abracadabra", "abc")
    print(test1)
    test2 = shortestSubstring("zxycbaabcdwxyzzxwdcbxyzabccbazzyx", "zzyzx")
    print(test2)

def shortestSubstring(str1,str2):

    requirements = Counter(str2)
    moving_char_count = {}
    min_length = float('inf')
    needed_chars = len(requirements)
    left_pointer = 0
    needs_met = 0

    for right_pointer, c in enumerate(str1):
        if c not in moving_char_count:
            moving_char_count[c] = 1
        else:
            moving_char_count[c] += 1

        if c in requirements and moving_char_count[c] == requirements[c]:
            needs_met+=1

        while needs_met == needed_chars:
            min_length=min(right_pointer-left_pointer+1,min_length)

            c_left = str1[left_pointer] 
            moving_char_count[c_left] -= 1
            if c_left in requirements and moving_char_count[c_left]<requirements[c_left]:
                needs_met-=1

            left_pointer+=1

    return min_length
            

main()

# this solution took me an hour and 15 minutes with some help debugging from Gemini for those last 5 minutes