#SPACE COMPLEXITY: 0(N) TIME COMPLEXITY: 0(N)

def uniquesum(arr):
    unique = set(arr)
    count = 0
    for number in unique:
        count += number
        
    return count
    
def test_cases():
    assert uniquesum([]) == 0
    assert uniquesum([10]) == 10
    assert uniquesum([1, 2, 3, 4]) == 10
    assert uniquesum([1, 1, 2, 2, 3, 3, 4]) == 10
    assert uniquesum([-1, -1, 2, -2, 3]) == 2
    
if __name__ == "__main__":
    test_cases()
    print("All test cases passed successfully!")
    
#TIME SPENT = 23 minutes
            
    