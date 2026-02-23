"""
Q2: First Occurrence
Given a string, return a new string containing only the first occurrence of each character.
"""

def first_occurrence(s):
    """
    Build string with only first occurrence of each character.
    
    Algorithm:
    - Track characters we've already included using a set
    - Build result string by appending characters we haven't seen
    - Skip characters that are already in our tracking set
    """
    visited = set()
    result = []  # Using list for efficient string building
    
    for character in s:
        # Only add if this character hasn't appeared yet
        if character not in visited:
            result.append(character)
            visited.add(character)
    
    # Join list into final string
    return ''.join(result)

# Time Complexity: O(n) - process each character once
# Space Complexity: O(n) - set and list storage


if __name__ == "__main__":
    string1 = "abracadabra"
    string2 = "Uber Career Prep"
    string3 = "zzyzx"
    
    print("First occurrence result:", first_occurrence(string1))
    print("First occurrence result:", first_occurrence(string2))
    print("First occurrence result:", first_occurrence(string3))

# Time spent: 8 minutes
