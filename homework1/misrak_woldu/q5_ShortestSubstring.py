# ============================================================
# Technique: Variable-size (shrinking/growing) sliding window
# Time: O(n)
# Space: O(m) where m = number of unique chars in required
# ============================================================

from typing import Dict
from collections import Counter, defaultdict

def shortest_substring_length(text: str, required: str) -> int:
    if not required or not text:
        return 0

    required_counts: Dict[str, int] = Counter(required)
    window_counts: Dict[str, int] = defaultdict(int)

    required_unique_count = len(required_counts)
    satisfied_unique_count = 0

    left_index = 0
    best_length = float("inf")

    for right_index, right_char in enumerate(text):
        window_counts[right_char] += 1

        if right_char in required_counts and window_counts[right_char] == required_counts[right_char]:
            satisfied_unique_count += 1

        while satisfied_unique_count == required_unique_count:
            window_length = right_index - left_index + 1
            if window_length < best_length:
                best_length = window_length

            left_char = text[left_index]
            window_counts[left_char] -= 1

            if left_char in required_counts and window_counts[left_char] < required_counts[left_char]:
                satisfied_unique_count -= 1

            left_index += 1

    return 0 if best_length == float("inf") else best_length


def run_tests() -> None:
    # examples from prompt
    assert shortest_substring_length("abracadabra", "abc") == 4
    assert shortest_substring_length("dog", "god") == 3
    assert shortest_substring_length("zxycbaabcdwxyzzyxwdcbxyzabccbazxy", "zzyzx") == 11

    # edge cases
    assert shortest_substring_length("", "abc") == 0
    assert shortest_substring_length("abc", "") == 0
    assert shortest_substring_length("abc", "dddd") == 0
    assert shortest_substring_length("aaaaa", "aa") == 2
    assert shortest_substring_length("a", "aa") == 0

    print("All tests passed")


if __name__ == "__main__":
    run_tests()
