def zeroSumSubarrays(nums):
    res = 0
    cur_sum = 0
    prefix_sums = {0:1}

    for n in nums:
        cur_sum += n
        
        res += prefix_sums.get(cur_sum, 0)
        prefix_sums[cur_sum] = 1 + prefix_sums.get(cur_sum,0)

    return res

def test_zeroSumSubarrays():
    assert zeroSumSubarrays([4,5,2,-1,-3,-3,4,6,-7]) == 2, "Test 1 Failed"

    assert zeroSumSubarrays([1, 8, 7, 3, 11, 9]) == 0, "Test 2 Failed"

    assert zeroSumSubarrays([8, -5, 0, -2, 3, -4]), "Test 3 Failed"

if __name__ == "__main__":
    test_zeroSumSubarrays()