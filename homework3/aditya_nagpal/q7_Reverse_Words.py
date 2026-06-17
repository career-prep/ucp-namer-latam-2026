#time Taken: 10 Mins
#Time complexity: O(n), where n is the number of words in string
# Given a string, return the string with the order of the space-separated words reversed.

#eg 
# Input: "Emma lives in Brooklyn, New York."
# Output: "York. New Brooklyn, in lives Emma"

"""inital approach that comes to mind is to split the sentece based off of
spaces and add them into an array,  reverse the array and then join the arr
"""

def reverseWords(input):
    arr = input.split(" ")
    res = []
    for _ in range(len(arr)):
        removed_word = arr.pop()
        res.append(removed_word)

    res_str = " ".join(res)

    return res_str


print(reverseWords("Emma lives in Brooklyn, New York."))