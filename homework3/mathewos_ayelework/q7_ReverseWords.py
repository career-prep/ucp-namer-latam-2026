# Technique: split into words and two-pointer in-place reverse
# Time Complexity: O(n)
# Space Complexity: O(n)


def reverseWords(s):
    words = s.split(" ")
    left, right = 0, len(words) - 1
    while left < right:
        words[left], words[right] = words[right], words[left]
        left += 1
        right -= 1
    return " ".join(words)


print("ReverseWords Results:")

print(reverseWords("Uber Career Prep"))
print(reverseWords("Emma lives in Brooklyn, New York."))
print(reverseWords("hello"))
print(reverseWords(""))
print(reverseWords("a b c d e"))
