def first_occurence(s):
    '''
    I create a set to store characters that have been seen and a list to append the first occurence of a character in the order they appear

    I then build a string using the .join function from the ret list, this is a string that holds only the first instances of the input string

    Finally I return the new string
    '''
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