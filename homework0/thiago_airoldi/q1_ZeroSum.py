# O(n) time complexity where n is the maximum number of elements in nums array
# O(n) space complexity because we create a set which in the worst case will contain all n elements from the nums array

arr1 = [1, 10, 8, 3, 2, 5, 7, 2, -2, -1]
arr2 = [1, 10, 8, -2, 2, 5, 7, 2, -2, -1]
arr3 = [4, 3, 3, 5, 7, 0, 2, 3, 8, 6]
arr4 = [4, 3, 3, 5, 7, 0, 2, 3, 8, 0]

def ZeroSum(nums):
    result = 0

    seen = set()

    for num in nums:

        needed = num * -1

        if needed in seen:
            result += 1
            seen.remove(needed)       
        else:
            seen.add(num)

    return result


print(ZeroSum(arr1))
print(ZeroSum(arr2))
print(ZeroSum(arr3))
print(ZeroSum(arr4))


# 19 minutes