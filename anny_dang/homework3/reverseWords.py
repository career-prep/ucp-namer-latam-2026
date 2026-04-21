def reverseWords(string):
    """
    Idea:
    Split the string into a list of words, then treat that list like a stack.
    Pop words from the end one by one and add them to a result list.
    Finally, join the result list with spaces to build the reversed sentence.

    Time complexity: O(n)
    Space complexity: O(n)
    """
    stack = string.split(" ")
    res = []
    while stack:
        res.append(stack.pop())
    return " ".join(res)


if __name__ == "__main__":
    example1 = "Uber Career Prep"
    example2 = "Emma lives in Brooklyn, New York."

    print(reverseWords(example1))  # Expected: Prep Career Uber
    print(reverseWords(example2))  # Expected: York. New Brooklyn, in lives Emma
