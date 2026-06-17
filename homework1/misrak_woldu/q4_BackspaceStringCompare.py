# ============================================================
# Technique: Two-pointer with "catch-up" condition (scan from right to left)
# Time Complexity: O(n + m)
# Space Complexity: O(n + m)
# ============================================================

def backspace_string_compare(first_string: str, second_string: str) -> bool:
    """
    Return True if both strings are equal after applying backspaces (#).
    """

    def next_valid_index(text: str, start_index: int) -> int:
        
        backspace_count = 0
        current_index = start_index

        while current_index >= 0:
            if text[current_index] == "#":
                backspace_count += 1
                current_index -= 1
            elif backspace_count > 0:
                backspace_count -= 1
                current_index -= 1
            else:
                return current_index

        return -1

    first_index = len(first_string) - 1
    second_index = len(second_string) - 1

    while first_index >= 0 or second_index >= 0:
        first_index = next_valid_index(first_string, first_index)
        second_index = next_valid_index(second_string, second_index)

        if first_index == -1 and second_index == -1:
            return True

        if first_index == -1 or second_index == -1:
            return False

        if first_string[first_index] != second_string[second_index]:
            return False

        first_index -= 1
        second_index -= 1

    return True


def run_tests() -> None:
    # given examples
    assert backspace_string_compare("abcde", "abcde") is True
    assert backspace_string_compare("Uber Career Prep", "u#Uber Caree#er Prep") is True
    assert backspace_string_compare("abcdef###xyz", "abcw#xyz") is True
    assert backspace_string_compare("abcdef###xyz", "abcdefxyz####") is False

    # edge cases
    assert backspace_string_compare("", "") is True
    assert backspace_string_compare("#", "") is True
    assert backspace_string_compare("a#", "") is True
    assert backspace_string_compare("####", "") is True
    assert backspace_string_compare("a##b", "b") is True
    assert backspace_string_compare("bxj##tw", "bxo#j##tw") is True

    print("All tests passed")


if __name__ == "__main__":
    run_tests()

