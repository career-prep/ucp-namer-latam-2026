def backspace_string_compare(s: str, t: str) -> bool:
    """
    Determines if two strings are equal after applying backspaces (#).

    Time Complexity: O(n)
        - Each pointer moves left across its string once.

    Space Complexity: O(1)
        - No extra data structures are used.
    """

    i, j = len(s) - 1, len(t) - 1

    while i >= 0 or j >= 0:
        # Find next valid character in s
        skip = 0
        while i >= 0:
            if s[i] == '#':
                skip += 1
                i -= 1
            elif skip > 0:
                skip -= 1
                i -= 1
            else:
                break

        # Find next valid character in t
        skip = 0
        while j >= 0:
            if t[j] == '#':
                skip += 1
                j -= 1
            elif skip > 0:
                skip -= 1
                j -= 1
            else:
                break

        # Compare current valid characters
        if i >= 0 and j >= 0:
            if s[i] != t[j]:
                return False
        elif i >= 0 or j >= 0:
            # One string has characters left, the other doesn't
            return False

        i -= 1
        j -= 1

    return True

