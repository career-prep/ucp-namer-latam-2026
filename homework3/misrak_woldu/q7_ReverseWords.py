# Data Structure: String / List
# Algorithm: Split + Reverse + Join
# Time Complexity: O(n)
# Space Complexity: O(n)


def reverse_words(sentence: str) -> str:
    if not sentence:
        return ""

    words = sentence.split()

    left_index = 0
    right_index = len(words) - 1

    while left_index < right_index:
        words[left_index], words[right_index] = (
            words[right_index],
            words[left_index],
        )

        left_index += 1
        right_index -= 1

    return " ".join(words)


def run_tests() -> None:
    assert reverse_words("hello world") == "world hello"
    assert reverse_words("the sky is blue") == "blue is sky the"
    assert reverse_words("a b c") == "c b a"
    assert reverse_words("single") == "single"
    assert reverse_words("") == ""
    assert reverse_words("   hello   world   ") == "world hello"

    print("All tests passed")


if __name__ == "__main__":
    run_tests()
