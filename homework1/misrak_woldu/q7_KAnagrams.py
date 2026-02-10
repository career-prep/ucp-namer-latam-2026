# ============================================================
# Technique: Two arrays/strings increment/decrement hashmap counts (hashing)
# Time: O(n + m) where n = len(s1), m = len(s2)
# Space: O(u) where u = number of unique characters across both strings
# ============================================================

from typing import Dict
from collections import Counter

def k_anagrams(first_string: str, second_string: str, k: int) -> bool:
    """
    Return True if first_string and second_string are k-anagrams.
    Two strings are k-anagrams if we can change at most k characters in ONE string
    to make the two strings anagrams of each other.
    """

    if len(first_string) != len(second_string):
        return False

    first_counts: Dict[str, int] = Counter(first_string)

    second_counts: Dict[str, int] = Counter(second_string)

    changes_needed = 0

    for character_in_first, count_in_first in first_counts.items():
        count_in_second = second_counts.get(character_in_first, 0)

        if count_in_first > count_in_second:
            changes_needed += (count_in_first - count_in_second)

        if changes_needed > k:
            return False

    return changes_needed <= k

def run_tests() -> None:
    # examples from the prompt
    assert k_anagrams("apple", "peach", 1) is False
    assert k_anagrams("apple", "peach", 2) is True
    assert k_anagrams("cat", "dog", 3) is True
    assert k_anagrams("debit curd", "bad credit", 1) is True
    assert k_anagrams("baseball", "basketball", 2) is False

    # edge cases
    assert k_anagrams("", "", 0) is True
    assert k_anagrams("a", "a", 0) is True
    assert k_anagrams("a", "b", 0) is False
    assert k_anagrams("a", "b", 1) is True
    assert k_anagrams("ab", "abc", 5) is False  # different lengths

    # duplicates or frequency checks
    assert k_anagrams("aabb", "bbaa", 0) is True
    assert k_anagrams("aabb", "bbcc", 2) is True
    assert k_anagrams("aabb", "bbcc", 1) is False

    print("All tests passed")

if __name__ == "__main__":
    run_tests()
