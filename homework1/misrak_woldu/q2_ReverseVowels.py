
# =======================
# Technique: Forward / Backward Two-Pointer
# Time Complexity: O(n)
# Space Complexity: O(n)
# =======================

def reverse_vowels(input_string: str) -> str:
    """
    Given a string, reverse the order of the vowels in the string.
    All non-vowel characters stay in the same position.
    """
    vowels = set("aeiouAEIOU")

    characters = list(input_string)

    left_index = 0

    right_index = len(characters) - 1

    while left_index < right_index:

        while left_index < right_index and characters[left_index] not in vowels:
            left_index += 1

        while left_index < right_index and characters[right_index] not in vowels:
            right_index -= 1

        if left_index < right_index:
            characters[left_index], characters[right_index] = (
                characters[right_index],
                characters[left_index],
            )

            left_index += 1
            right_index -= 1

    return "".join(characters)

def run_tests() -> None:
    # Provided examples
    assert reverse_vowels("Uber Career Prep") == "eber Ceraer PrUp"
    assert reverse_vowels("xyz") == "xyz"
    assert reverse_vowels("flamingo") == "flominga"

    # Edge cases
    assert reverse_vowels("") == ""
    assert reverse_vowels("aeiou") == "uoiea"
    assert reverse_vowels("AEIOU") == "UOIEA"
    assert reverse_vowels("bcdfg") == "bcdfg"
    assert reverse_vowels("a") == "a"

    print("All tests passed")


if __name__ == "__main__":
    run_tests()
