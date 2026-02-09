def dedupArray(nums):
    set_nums = set(nums)
    set_nums = list(set_nums)
    return set_nums
    

def test_dedupArray():
    assert dedupArray([1,2,2,3,3,3,4,4,4,4]) == [1,2,3,4], "Test Case 1 Failed"

    assert dedupArray([0,0,1,4,5,5,5,8,9,9,9,10,11,15,15]) == [0,1,4,5,8,9,10,11,15], "Test Case 2 Failed"

    assert dedupArray([1,3,4,8,10,12]) == [1,3,4,8,10,12], "Test Case 3 Failed"

if __name__ == "__main__":
    test_dedupArray()