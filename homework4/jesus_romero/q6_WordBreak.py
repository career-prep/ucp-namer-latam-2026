# Runtime:
# Time: O(n^2)
# Space: O(n)
# Implementation time: 20 to 30 minutes


def word_break(text, dictionary):
    #1. Declare variables
    n = len(text)
    words = set(word.lower() for word in dictionary)

    dp = [False] * (n + 1)
    dp[0] = True

    previous = [-1] * (n + 1)

    #2. Build DP table
    for end in range(1, n + 1):
        for start in range(end):
            if dp[start] and text[start:end] in words:
                dp[end] = True
                previous[end] = start
                break

    #3. Check if solution exists
    if not dp[n]:
        return False, []

    #4. Reconstruct words
    result = []
    index = n

    while index > 0:
        start = previous[index]
        result.append(text[start:index])
        index = start

    result.reverse()

    #5. Return result
    return True, result


def Test_WordBreak():
    #1. Declare dictionayr
    dictionary = [
        "Elf",
        "Go",
        "Golf",
        "Man",
        "Manatee",
        "Not",
        "Note",
        "Pig",
        "Quip",
        "Tee",
        "Teen"
    ]

    #2. Declare test cases
    test_cases = [
        "mangolf",
        "manateenotelf",
        "quipig"
    ]

    #3. Run tests
    for text in test_cases:
        found, words = word_break(text, dictionary)
        print("Input:", text)
        print("Output:", found)

        if found:
            print("Words:", words)

        print()


if __name__ == "__main__":
    Test_WordBreak()