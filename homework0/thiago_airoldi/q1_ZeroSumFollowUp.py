# O(n) time complexity where n is the maximum number of elements in nums array

# O(n) space complexity because we create a hashmap stores the frequency of unique numbers. In the worst case, all n elements in nums array are unique and 
# must be stored in the hashmap

arr1 = [1, 10, 8, 3, 2, 5, 7, 2, -2, -1]
arr2 = [1, 10, 8, -2, 2, 5, 7, 2, -2, -1]
arr3 = [4, 3, 3, 5, 7, 0, 2, 3, 8, 6]
arr4 = [4, 3, 3, 5, 7, 0, 2, 3, 8, 0]

def ZeroSumFollowUp(nums):
    result = 0
    freq = {}

    for num in nums:
        needed = num * -1

        validPair = freq.get(needed, 0)

        result += validPair

        freq[num] = 1 + freq.get(num, 0)

    return result

print(ZeroSumFollowUp(arr1))
print(ZeroSumFollowUp(arr2))
print(ZeroSumFollowUp(arr3))
print(ZeroSumFollowUp(arr4))

# 36 minutes