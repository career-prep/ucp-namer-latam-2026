#Technique Used: Fixed-size sliding window

def max_mean_sub_array(array, k):
    if not array or k > len(array) or k == 0:
        return 0
     
    max_mean = float('-inf')
    num_sum = sum(array[:k])
    max_mean = max(max_mean, (num_sum / k))
    
    for l in range(1, len(array) - k + 1):
        r = k + l - 1
        num_sum -= array[l - 1]
        num_sum += array[r]
        max_mean = max(max_mean, (num_sum / k))
   
    return max_mean
        



def test_cases():
    assert max_mean_sub_array([], 3) == 0
    assert max_mean_sub_array([4, 5, -3, 2, 6, 1], 2) == 4.5
    assert max_mean_sub_array([4, 5, -3, 2, 6, 1], 3) == 3
    assert max_mean_sub_array([1, 1, 1, 1, -1, 2, -1, -1], 3) == 1
    assert max_mean_sub_array([1, 1, 1, 1, -1, -1, 2, -1, -1, 6], 5) == 1
    
if __name__ == "__main__":
    test_cases()
    print("All test cases passed successfully!")

#Time Spent: 29 mins
