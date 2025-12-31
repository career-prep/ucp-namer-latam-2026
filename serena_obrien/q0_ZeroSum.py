# Time complexity: O(n)
# Space complexity: O(n)

def ZeroSum(arr):
    nums = {}
    count = 0
    for num in arr:
        if -num in nums:
            nums.pop(-num)
            count += 1
        else:
            nums[num] = 0
    return count

def ZeroSumRepeats(arr):
    nums = {}
    count = 0
    for num in arr:
        if -num in nums:
            count += nums[-num]
            nums[num] = nums.get(num, 0) + 1
        else:
            nums[num] = nums.get(num, 0) + 1
    return count

if __name__ == '__main__':
    inputArr = [1, 10, 8, 3, 2, 5, 7, 2, -2, -1]
    #inputArr = [1, 10, 8, -2, 2, 5, 7, 2, -2, -1]
    #inputArr = [4, 3, 3, 5, 7, 0, 2, 3, 8, 6]
    #inputArr = [4, 3, 3, 5, 7, 0, 2, 3, 8, 0]
    #inputArr = [0]
    print("Input Array:", inputArr)
    print("Output (no repeats):", ZeroSum(inputArr))
    print("Output (with repeats):", ZeroSumRepeats(inputArr))

# ~ time spent: 25 minutes