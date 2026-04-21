#Time Complexity: O(N) Space Complexity: O(N)

def missing_interger(array, n):
    arr_set = set(array)

    for num in range(1, n + 1):
        if num not in arr_set:
            return num
           


def test_cases():
    assert missing_interger([1,2,3,4,5,6,7,8,10,11,12], 12) == 9
    assert missing_interger([2,3,4,5], 5) == 1
    assert missing_interger([1,2], 3) == 3
    
if __name__ == "__main__":
    test_cases()
    print("All test cases passed successfully!")


#Time Spent: 7 mins