# Data structure: List of tokens from string split
# Algorithm: Reverse word order


def reverse_words(s):
    return " ".join(s.split()[::-1])


if __name__ == "__main__":
    print("=== Spec ===")
    print(" ", reverse_words("Uber Career Prep"))
    print(" ", reverse_words("Emma lives in Brooklyn, New York."))

    print("=== Empty / whitespace ===")
    print(" ", repr(reverse_words("")))
    print(" ", repr(reverse_words("   ")))

    print("=== Single word ===")
    print(" ", reverse_words("hello"))

    print("=== Tabs and spaces ===")
    print(" ", reverse_words("a\tb  c"))

    print("=== One letter words ===")
    print(" ", reverse_words("a b c"))


# Time complexity: O(n)
# Space complexity: O(n)
# Time spent: 5 minutes
