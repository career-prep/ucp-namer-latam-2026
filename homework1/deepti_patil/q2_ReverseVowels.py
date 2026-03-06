def reverse_vowels(s: str) -> str:
    """
    Reverses only the vowels in the input string using two pointers.
    """

    vowels = set("aeiouAEIOU")
    chars = list(s)  # Strings are immutable, so convert to list

    left, right = 0, len(chars) - 1

    while left < right:
        # Move left pointer until it points to a vowel
        while left < right and chars[left] not in vowels:
            left += 1

        # Move right pointer until it points to a vowel
        while left < right and chars[right] not in vowels:
            right -= 1

        # Swap the two vowels
        chars[left], chars[right] = chars[right], chars[left]

        left += 1
        right -= 1

    return "".join(chars)


# Example usage
print(reverse_vowels("Uber Career Prep"))  # "eber Ceraer PrUp"
print(reverse_vowels("xyz"))               # "xyz"
print(reverse_vowels("flamingo"))          # "flominga"

"""
Time Complexity: O(n)
        - Each character is visited at most once by the left and right pointers.

    Space Complexity: O(n)
        - We convert the string to a list to allow in-place swaps
          (strings in Python are immutable).
"""
