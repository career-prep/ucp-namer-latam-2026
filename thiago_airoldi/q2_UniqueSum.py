# O(n) time complexity where n is the length of all elements in nums array
# O(n) space complexity because we create a set, which can contain all n elements of nums array the worst case

arr1 = [1, 10, 8, 3, 2, 5, 7, 2, -2, -1]
arr2 = [4, 3, 3, 5, 7, 0, 2, 3, 8, 6]

def UniqueSum(nums):
    sum = 0

    seen = set()

    for num in nums:

        if num not in seen:

            sum += num

            seen.add(num)

    return sum

print(UniqueSum(arr1))
print(UniqueSum(arr2))

# 5 minutes
