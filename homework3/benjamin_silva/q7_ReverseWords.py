def reverseWords(s):
    words = s.split()
    stack = []

    for word in words:
        stack.append(word)
    
    ret = []

    while stack:
        ret.append(stack.pop())

    return " ".join(ret)


if __name__ == "__main__":

    print("Test 1 (expect 'Prep Career Uber'):")
    print(reverseWords("Uber Career Prep"))

    print("\nTest 2 (expect 'York. New Brooklyn, in lives Emma'):")
    print(reverseWords("Emma lives in Brooklyn, New York."))
