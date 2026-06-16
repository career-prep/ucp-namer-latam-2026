# Technique: Dynamic Programming - Tabulation
# Data Structure: Array / Hash Set
# Time Complexity: O(n^2 * m), where n is the string length and m is substring slicing length
# Space Complexity: O(n + d), where d is the number of words in the dictionary


def word_break(input_string: str, dictionary: list[str]) -> bool:
    if input_string == "":
        return True

    word_set = set()

    for word in dictionary:
        word_set.add(word.lower())

    input_string = input_string.lower()

    can_break = [False] * (len(input_string) + 1)

    can_break[0] = True

    for end_index in range(1, len(input_string) + 1):
        for start_index in range(end_index):
            current_word = input_string[start_index:end_index]

            if can_break[start_index] and current_word in word_set:
                can_break[end_index] = True
                break

    return can_break[len(input_string)]


def run_tests() -> None:
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
        "Teen",
    ]

    assert word_break("mangolf", dictionary) is True

    assert word_break("manateenotelf", dictionary) is True

    assert word_break("quipig", dictionary) is False

    assert word_break("", dictionary) is True

    assert word_break("elf", dictionary) is True

    assert word_break("manatee", dictionary) is True

    assert word_break("unknown", dictionary) is False

    assert word_break("golfman", dictionary) is True

    assert word_break("notebook", dictionary) is False

    print("All tests passed")


if __name__ == "__main__":
    run_tests()