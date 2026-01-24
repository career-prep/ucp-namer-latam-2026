#time complexity: O(n)
#space complexity: O(1)

def DedupArray(nums):
    i = 0
    while i < len(nums):
        current = nums[i]
        while i + 1 < len(nums) and nums[i+1] == current:
            del nums[i]
        i += 1
    
    return nums

test1 = [1,2,2,3,3,3,3,4,4,4,4]
test2 = [1,2,3,4,5]
test3 = [1,1,1,1,1,1]
test4 = []

print('test1: ', DedupArray(test1))
print('test2: ', DedupArray(test2))
print('test3: ', DedupArray(test3))
print('test4: ', DedupArray(test4)) 

#time spent: 15 mins