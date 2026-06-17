#fixed-size sliding window
# time complexity: O(n)
# space complexity: O(1)
#10 minutes

def max_mean_sub_array(arr, k):
    if k > len(arr) or k == 0: #edge cases
        return None
    window_sum = sum(arr[:k]) #first sum
    max_sum = window_sum
    for i in range(k, len(arr)): #slide the window
        window_sum += arr[i] - arr[i - k] #update sum, then max_sum
        max_sum = max(max_sum, window_sum)
    return max_sum / k

#test cases
array1 = [4,5,-3,2,6,1]
k1 = 2
assert max_mean_sub_array(array1, k1) == 4.5

array2 = [4,5,-3,2,6,1]
k2 = 3
assert max_mean_sub_array(array2, k2) == 3

array3 = [1,1,1,1,-1,-1,2,-1,-1]
k3 = 3
assert max_mean_sub_array(array3, k3) == 1

array4 = [1,1,1,1,-1,-1,2,-1,-1,6]
k4 = 5
assert max_mean_sub_array(array4, k4) == 1

print("yay!!")