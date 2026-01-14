"""
Q3: 
Given a string, return a string that contains only the first occurrence of each char
"""

def FirstOccurrence(str):
    #1. Same algo as before, only this time keeping track of characters and
    #   concatenating to a string
    seen = set()
    new_string = ""

    for char in str:
        if char in seen:
            continue
        else:
            new_string += char
            seen.add(char)
    
    return new_string
# Time Complexity: O(n)
# Space Complexity: O(n)



if __name__ == "__main__":
    input_string_1 = "abracadabra"
    input_string_2 = "Uber Career Prep"
    input_string_3 = "zzyzx"

    print(FirstOccurrence(input_string_1))
    print(FirstOccurrence(input_string_2))
    print(FirstOccurrence(input_string_3))

# Time spent: ~ 5 mins