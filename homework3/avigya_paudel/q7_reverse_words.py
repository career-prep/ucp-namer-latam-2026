# Time Taken: 15 minutes
# Time Complexity: O(N)
# Space Complexity: O(N)
# Algorithm: Stack 
# (I thought we can push it down to O(1) space by two pointers but two pointers 
# was not on the options of datastrcutres, so I pivoted to using stack)

def reverse_words(s):
    """
    Given a string, return the string with the order of the words reversed.
    """
    words = []
    word = ""
    for c in s:
        if c == " " and word.strip() != "":
            words.append(word)
            word = ""
        else:
            word += c
    words.append(word)
    new_word = ""

    while words:
        new_word += words.pop() + " "
    return new_word[:-1]
        



if __name__ == "__main__":
    print(reverse_words("Uber Career Prep"))  # Expected: "Prep Career Uber"
    print(reverse_words("Emma lives in Brooklyn, New York."))  # Expected: "York. New Brooklyn, in lives Emma"
