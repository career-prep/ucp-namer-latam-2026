# Time: 12 minutes and 14 seconds
# Technique: One-directional running computation

def ZeroSumSubArrays(number):
    prefix_sum = 0
    seen = {0:1}
    count = 0

    for i in range(len(number)):
        prefix_sum += number[i]
        count += seen.get(prefix_sum, 0)
        seen[prefix_sum] = seen.get(prefix_sum, 0) + 1
    return count

print(ZeroSumSubArrays([4,5,2,-1,-3,-3,4,6,-7]))
print(ZeroSumSubArrays([1,8,7,3,11,9]))
print(ZeroSumSubArrays([8,-5,0,-2,3,-4]))


