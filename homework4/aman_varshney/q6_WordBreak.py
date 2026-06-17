# spent 45 min
# tabulation
# TC - O(n^2)
# SC - O(n)


def word_break(string: str, dictionary: set) -> bool:
    """Returns true if `string` can be formed from words in `dictionary` by only adding spaces."""
    n = len(string)
    if n == 0: # Empty case
        return False
    
    # dp = valid start indices
    # Only idx 0 initially
    dp = [False] * (n+1)
    dp[0] = True  
    
    # Iterate through each char
    for i in range(1, n+1):
        # Check each substring from a valid start idx 
        # to see if it forms a word in dictionary 
        for j in range(i): 
            if dp[j] and string[j:i] in dictionary:
                dp[i] = True
                break

    return dp[n]


def run_tests() -> None:
    print("Running tests")
    dictionary = {"elf", "manatee", "quip", "go", "not", "tee", "golf", "note", "teen", "man", "pig"}

    assert word_break("mangolf", dictionary) is True
    assert word_break("manateenotelf", dictionary) is True
    assert word_break("quipig", dictionary) is False

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
