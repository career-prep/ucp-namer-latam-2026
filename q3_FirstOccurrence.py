# Time complexity - O(n)
# Space complexity - O(n)

def first_occurrence(s):
    out = "" # output string
    seen = set() # tracks visited letters
    
    for char in s: # loop through input string
        if char not in seen: # first occurence
            seen.add(char)
            out += char
    
    return out




if __name__ == "__main__":
    input_str = input("Enter a string: ")
    first_occurrence_str = first_occurrence(input_str)
    print(first_occurrence_str)
    
# Spent 15 minutes
