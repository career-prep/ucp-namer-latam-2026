from collections import Counter

def are_k_anagrams(s1: str, s2: str, k: int) -> bool:
    """
    Return True if s1 and s2 are k-anagrams.

    Time Complexity: O(n)
        - Counting characters is linear in the string length.
    Space Complexity: O(1) / O(u)
        - O(u) for distinct characters (bounded by alphabet size in practice).
    """

    # Anagrams must be the same length
    if len(s1) != len(s2):
        return False

    count1 = Counter(s1)
    count2 = Counter(s2)

    # How many characters in s1 are "extra" compared to s2?
    # Each extra character requires one change in s1.
    changes_needed = 0
    for ch, freq in count1.items():
        if freq > count2.get(ch, 0):
            changes_needed += freq - count2.get(ch, 0)

    return changes_needed <= k


# Examples
print(are_k_anagrams("apple", "peach", 1))        # False
print(are_k_anagrams("apple", "peach", 2))        # True
print(are_k_anagrams("cat", "dog", 3))            # True
print(are_k_anagrams("debit curd", "bad credit", 1))  # True
print(are_k_anagrams("baseball", "basketball", 2))    # False
