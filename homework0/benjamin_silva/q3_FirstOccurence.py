def first_occurence(s):
    seen = set()
    ret = []
    for c in s:
        if c not in seen:
            seen.add(c)
            ret.append(c)
    first = "".join(ret)
    return first

def test_first_occurrence():
    assert first_occurence("abracadabra") == "abrcd", "Test 1 Failed"
    assert first_occurence("Uber Career Prep") == "Uber CaPp", "Test 2 Failed"
    assert first_occurence("zzyzx") == "zyx", "Test 3 Failed"

if __name__ == "__main__":
    test_first_occurrence()

# This problem took me 12 minutes