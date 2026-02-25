#this is a two-pointer fixed size sliding window problem
#time and space complexity of O(n)
def main():
    test1 = maxMeanSubArray(3, [4,5,-3,2,6,1])
    print(test1)

    test2 = maxMeanSubArray(0, [4,5,-3,2,6,1])
    print(test2)

    test3 = maxMeanSubArray(2, [1])
    print(test3)

def maxMeanSubArray(k, nums):

    if k < 1:
        return "k > 1 must be true"
    
    if k >= len(nums):
        return "k is a subarray and must have length greater than array"
    
    if k < 1:
        return "k must be greater than or equal to one"
    

    greatest_sum = 0
    moving_sum = 0

    for i in range(k):
        moving_sum+=nums[i]

    greatest_sum = moving_sum

    for j in range(k, len(nums)):
        moving_sum -= nums[j-k]
        moving_sum += nums[j]
        greatest_sum = max(greatest_sum, moving_sum)

    return greatest_sum/k


main()

#this took me around 15 minutes to complete