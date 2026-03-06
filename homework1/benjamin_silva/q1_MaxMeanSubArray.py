def maxMeanSubArray(arr, k):
    L = 0
    max_mean = float('-inf')
    curr_mean = 0
    curr_sum = 0

    for R in range(len(arr)):
        curr_sum = curr_sum + arr[R]

        if R - L + 1 > k:
            curr_sum = curr_sum - arr[L]
            L += 1
        # curr_sum = curr_sum + arr[R]
        if R - L + 1 == k:
            curr_mean = curr_sum / k
            if curr_mean > max_mean:
                max_mean = curr_mean
    return max_mean
        

    

def test_maxMeanSubArray():
    assert maxMeanSubArray([4, 5, -3, 2, 6, 1], 2) == 4.5

    assert maxMeanSubArray([4, 5, -3, 2, 6, 1], 3) == 3

    assert maxMeanSubArray([1, 1, 1, 1, -1, -1, 2, -1, -1], 3) == 1

    assert maxMeanSubArray([1, 1, 1, 1, -1, -1, 2, -1, -1, 8], 5) == 1.4

    print("All tests passed")

if __name__ == "__main__":
    test_maxMeanSubArray()