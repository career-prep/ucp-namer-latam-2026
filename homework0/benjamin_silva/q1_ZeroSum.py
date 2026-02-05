def zerosum(arr):
    d = {}
    count = 0
    for n in arr:
        if n in d:
            d[n] += 1
        else:
            d[n] = 1
    for key, value in d.items():
        target = 0 - key
        # if key == 0:
        if target in d and key > 0:
            count += min(value, d[target])
    return count

def test_zerosum():
    assert zerosum([1,10,8,3,2,5,7,2,-2,-1]) == 2, "Test 1 Failed"
    assert zerosum([1,10,8,-2,2,5,7,2,-2,-1]) == 3, "Test 2 Failed"
    assert zerosum([4,3,3,5,7,0,2,3,8,6]) == 0, "Test 3 Failed"
    assert zerosum([4,3,3,5,7,0,2,3,8,0]) == 1, "Test 4 Failed"

if __name__ == "__main__":
    test_zerosum()

# This problem took me the entire 40 minutes