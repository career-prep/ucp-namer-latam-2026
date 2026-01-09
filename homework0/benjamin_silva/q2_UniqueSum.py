def uniquesum(arr):
    '''
    For this solution I use a set to get a list of the 
    unique elements in the input array. Once I've got the set
    I use the sum function to add all the elements in the set together.
    This results in a sum of all the unique elements in the arr.
    '''
    unique_set = set(arr)
    total_sum = sum(unique_set)

    return total_sum

def test_uniquesum():
    assert uniquesum([1,10,8,3,2,5,7,2,-2,-1]) == 33, "Test 1 Failed"
    assert uniquesum([4,3,3,5,7,0,2,3,8,6]) == 35, "Test 2 Failed"

if __name__ ==  "__main__":
    test_uniquesum()

# This problem took me 5 minutes