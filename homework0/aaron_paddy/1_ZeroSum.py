#SPACE COMPLEXITY: O(N) TIME COMPLEXITY: O(N)

from collections import defaultdict

def zerosum(arr):
    
    count = 0
    dict = defaultdict(int)
    for num in arr:
        if -(num) in dict:
            count += dict[-num]
        dict[num] += 1
    return count




def test_cases():
    assert zerosum([0]) == 0
    assert zerosum([0, 3, 4, 0]) == 1
    assert zerosum([1, 10, 8, -2, 2, 5, 7, 2, -2, -1]) == 5
    assert zerosum([]) == 0
    
if __name__ == "__main__":
    test_cases()
    print("All test cases passed")
    
#TIME SPENT: 36 minutes
            
        