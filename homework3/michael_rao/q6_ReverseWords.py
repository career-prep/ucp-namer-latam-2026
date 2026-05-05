# Data structure: Array 
# Time: O(n) 
# Space: O(n) 


def reverse_words(s):
    words = s.split()
    words.reverse()
    return " ".join(words)


print("Correct:", "Prep Career Uber")
print("Output: ", reverse_words("Uber Career Prep"))
print()

print("Correct:", "York. New Brooklyn, in lives Emma")
print("Output: ", reverse_words("Emma lives in Brooklyn, New York."))
print()

print("Correct:", "")
print("Output: ", reverse_words(""))
print()

# time taken: 5 min
