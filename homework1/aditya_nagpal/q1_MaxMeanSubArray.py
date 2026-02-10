# Techniques to follow:
    ##state the technique on the top
    ## write the function to solve the problem
    ## write the test cases to check your function
    ## state the time and space complexity of the solution
    ## time taken

#p1
## time taken: 13mins + 15mins(brutforce and optimized) from start to end (incuding self explanations)
## time complexity: O(n)
## method used: sliding window

#given: 
     # an array of int
     # an integer k: size of the subarray
# question:
     # max mean of subarray of size k.

#solution:
# def maxxMeanSubArray(arr, k):
#     mean_arr = []

#     i = 0
#     j = k-1

#     while(j < len(arr)):
#         total = 0
#         for l in range(i, j+1):
#             total += arr[l]
#         mean_arr.append(total/k)
    
#         i += 1
#         j += 1
#     print(mean_arr)
#     print(max(mean_arr))

#testCases
# maxMeanSubArray([4, 5, -3, 2, 6, 1], 2)
# maxMeanSubArray([4, 5, -3, 2, 6, 1], 3)
# maxMeanSubArray([1, 1, 1, 1, -1, 2, -1, -1], 3)
# maxMeanSubArray([1, 1, 1, 1, -1, -1, 2, -1, -1, 6], 5)

#optimized approach

def maxMeanSubArray(arr, k):
    n = len(arr)
    window_sum = sum(arr[0:k])
    max_sum = window_sum

    for i in range(k, n):
        window_sum = (window_sum - arr[i-k]) + arr[i] # got stuck here on how to figure out the subtraction of the sum of the previous window
        max_sum = max(max_sum, window_sum)

    print(max_sum/k)


maxMeanSubArray([4, 5, -3, 2, 6, 1], 2)
maxMeanSubArray([4, 5, -3, 2, 6, 1], 3)
maxMeanSubArray([1, 1, 1, 1, -1, 2, -1, -1], 3)
maxMeanSubArray([1, 1, 1, 1, -1, -1, 2, -1, -1, 6], 5)