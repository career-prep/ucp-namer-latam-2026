# this is a shrinking/growing sliding window problem

# def main():

# def zeroSumSubArrays(nums):
#     sub_arrays = 0
#     running_sum = 0


#     r = 0
#     for i in range(len(nums)):
#         running_sum += nums[i]

#===========================================================
# I had to look up what strategy this problems needs, I spent ~20 minutes trying to get a sliding window to work
# Below is my code after finding the right strategy online

# this is actually a running computation/hash-map problem
# the solution has O(n) time and space complexity

def main():
    test1 = zeroSumSubArrays([4,5,2,-1,-3,-3,4,6,-7])
    print(test1)

    test2 = zeroSumSubArrays([1,8,7,3,11,9])
    print(test2)

    test3 = zeroSumSubArrays([8,-5,0,-2,3,-4,0,1,-1])
    print(test3)

def zeroSumSubArrays(nums):

    counts = {0:1}
    running_sum = 0
    total_found = 0

    for i in range(len(nums)):
        num = nums[i]
        running_sum+=num

        if running_sum in counts:
            counts[running_sum] +=1

        else:
            counts[running_sum] = 1

    for sum in counts:
            total_found+=counts[sum]-1

    return total_found

main()
# my solution only works when the answer is 2
# 40 minutes total, ran out of time