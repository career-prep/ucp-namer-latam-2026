# Data Structure: Stack
#
# Walk the string and push each whitespace-separated word onto a stack, then
# pop them off to produce the reversed-order string.
#
# Assumption: words are separated by single spaces and the input has no leading
# or trailing whitespace (matches the examples). Multiple consecutive spaces
# would be collapsed by str.split() — note in comment.
#
# Time complexity:  O(n)
# Space complexity: O(n)


def reverse_words(s):
    stack = []
    for word in s.split(" "):
        stack.append(word)
    out = []
    while stack:
        out.append(stack.pop())
    return " ".join(out)


# test cases
if __name__ == "__main__":
    assert reverse_words("Uber Career Prep") == "Prep Career Uber"
    assert reverse_words("Emma lives in Brooklyn, New York.") == \
        "York. New Brooklyn, in lives Emma"
    assert reverse_words("hello") == "hello"
    assert reverse_words("") == ""

    print("yay!!")

# Time spent: ~5 minutes
