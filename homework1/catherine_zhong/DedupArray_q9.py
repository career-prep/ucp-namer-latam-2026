#time complexity: O(n)
#space complexity: O(1)

def DedupArray(nums):
    #checks for empty array
    if not nums:
        return nums

    write = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[write-1]:
            nums[write] = nums[i]
            write += 1
    
    #trims array till last nonduplicate element
    return nums[:write]

test1 = [1,2,2,3,3,3,3,4,4,4,4]
test2 = [1,2,3,4,5]
test3 = [1,1,1,1,1,1]
test4 = []

print('test1: ', DedupArray(test1))
print('test2: ', DedupArray(test2))
print('test3: ', DedupArray(test3))
print('test4: ', DedupArray(test4)) 

#time spent: 15 mins