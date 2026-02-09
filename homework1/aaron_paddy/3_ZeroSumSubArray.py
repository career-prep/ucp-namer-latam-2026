#Time complexity: O(N^2), space complexity:  O(1)

def zero_sub_array(array):
    count = 0
    
    for i in range(len(array)):
        if array[i] == 0:
            count += 1
        for j in range(i + 1, len(array)):
            arr_sum = sum(array[i : j + 1])
            if arr_sum == 0:
                count += 1
            
    return count                    
        
        
def test_cases():
    assert zero_sub_array([0]) == 1
    assert zero_sub_array([4,5,2,-1,-3,-3,4,6,-7]) == 2
    assert zero_sub_array([1,8,7,3,11,9]) == 0
    assert zero_sub_array([8,-5,0,-2,3,-4]) == 2
    
if __name__ == "__main__":
    test_cases()
    print("All test cases passed successfully!")
        
#Time Spent: 18 mins
        