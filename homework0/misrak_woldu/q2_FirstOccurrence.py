
from typing import Set

def first_occurrence(s: str) -> str:
    """Return a string containing only the first occurrence of each character in the input string"""

    seen: Set[str] = set()
    result = []

    for ch in s:
        if ch not in seen:
            seen.add(ch)
            result.append(ch)

    return "".join(result) 

def run_tests() -> None:
    assert first_occurrence("abracadabra") == "abrcd"
    assert first_occurrence("Uber Career Prep") == "Uber CaPp"
    assert first_occurrence("zzyzx") == "zyx"

    #edge cases
    assert first_occurrence("") == ""
    assert first_occurrence("aaaa") == "a"
    assert first_occurrence("AaA") == "Aa"

    print("All tests passed")

if __name__ == "__main__":
    run_tests()   