# Time complexity: O(n)
# Space complexity: O(n)

def UniqueSum(arr):
    nums = {}
    sum = 0
    for num in arr:
        nums[num] = nums.get(num, 0) + 1
        sum += num if nums[num] == 1 else 0
    return sum

if __name__ == "__main__":
    #inputArr = [1, 10, 8, 3, 2, 5, 7, 2, -2, -1]
    #inputArr = [4, 3, 3, 5, 7, 0, 2, 3, 8, 6]
    inputArr = [0, 0]
    print("Output:", UniqueSum(inputArr))

# ~ time spent: 10 minutes