def reverseVowels(s):
    L = 0
    R = len(s) - 1
    s = list(s)

    while L < R:
        if (s[L].lower() == 'a' or s[L].lower() == 'e' or s[L].lower() == 'i' or s[L].lower() == 'o' or s[L].lower() == 'u') and (s[R].lower() == 'a' or s[R].lower() == 'e' or s[R].lower() == 'i' or s[R].lower() == 'o' or s[R].lower() == 'u'):
            temp = s[L]
            s[L] = s[R]
            s[R] = temp
            L += 1
            R -= 1
        while L < R and (s[L].lower() != 'a' and s[L].lower() != 'e' and s[L].lower() != 'i' and s[L].lower() != 'o' and s[L].lower() != 'u'):
            L += 1
        while  L< R and (s[R].lower() != 'a' and s[R].lower() != 'e' and s[R].lower() != 'i' and s[R].lower() != 'o' and s[R].lower() != 'u'):
            R -= 1
    ret = "".join(s)
    return  ret
    

def test_reverseVowels():
    assert reverseVowels("Uber Career Prep") == "eber Cerear PrUp", "Test Case 1 Failed"

    assert reverseVowels("xyz") == "xyz", "Test Case 2 Failed"

    assert reverseVowels("flamingo") == "flominga", "Test Case 3 Failed"