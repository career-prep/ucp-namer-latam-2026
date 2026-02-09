def missingInteger(nums, n):
    for i in range(len(nums) - 1):
        if nums[i + 1] != nums[i] + 1:
            return nums[i] + 1
    return n
    

def test_missingInteger():
    assert missingInteger([1,2,3,4,6,7], 7) == 5, "Test 1 Failed"

    assert missingInteger([1], 2) == 2, "Test 2 Failed"

    assert missingInteger([1,2,3,4,5,6,7,8,10,11,12], 12) == 9, "Test 3 Failed"

if __name__ == "__main__":
    test_missingInteger()