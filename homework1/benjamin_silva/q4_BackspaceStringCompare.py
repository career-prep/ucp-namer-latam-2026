def backspaceCompare(s, t):
    S = len(s) - 1
    T = len(t) - 1
    skip_counterS = 0
    skip_counterT = 0
    while S >= 0 or T >= 0:
        while S >= 0 and s[S] == '#':
            skip_counterS += 1
            S -= 1
        while S >= 0 and skip_counterS > 0 and s[S] != '#':
            skip_counterS -= 1
            S -= 1
        while T >= 0 and t[T] == '#':
            skip_counterT += 1
            T -= 1
        while T >= 0 and skip_counterT > 0 and t[T] != '#':
            skip_counterT -= 1
            T -= 1
        if (S < 0 and T >= 0) or (S >= 0 and T < 0):
            return False
        if S < 0 and T < 0:
            return True
        if S >= 0 and T >= 0 and s[S] != t[T]:
            return False
        else:
            S -= 1
            T -= 1
    return True

def test_backspaceCompare():
    assert backspaceCompare("abcde", "abcde") == True, "Test 1 Failed"

    assert backspaceCompare("Uber Career Prep", "u#Uber Careee#r Prep") == True, "Test 2 Failed"

    assert backspaceCompare("abcdef###xyz", "abcw#xyz") == True, "Test 3 Failed"

    assert backspaceCompare("abcdef###xyz", "abcdefxyz###") == False, "Test 4 Failed"

if __name__ == "__main__":
    test_backspaceCompare()