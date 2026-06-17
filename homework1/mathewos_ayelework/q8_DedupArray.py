# Technique used: Two pointer method
# removes all duplicates in the list
def dedupArray(nums: list[int]) -> list[int]:
    # Solution 1, Time complexity: O(n^2) worst case, Space complexity: O(1)
    # curr = len(nums) - 1
    # prev = curr - 1

    # while prev >= 0:
    #     if nums[prev] == nums[curr]:
    #         nums.pop(curr)
    #     prev -=1
    #     curr -=1
    # return nums
    
    
    # Solution 2
    if nums == []:
        return []

    p = 0
    c = 1

    uniqueEl = 1
    while c < len(nums):
        if nums[p] != nums[c]: 
            uniqueEl += 1
        p+= 1
        c+= 1

    p = 0
    c = 1
    while p <= uniqueEl and c < len(nums):
        while p <= uniqueEl and c < len(nums) and nums[p] == nums[c]:
            c+= 1
        
        if c < len(nums) and p <= uniqueEl and nums[p] != nums[c]:
            if c - p > 1:
                temp = nums[c]
                nums[c] = nums[p+1]
                nums[p+1] = temp

            p +=1
            c+= 1

    del nums[uniqueEl:]
    return nums
test_cases = [
            [1,2,2,3,3,3,4,4,4,4],
            [0,0,1,4,5,5,5,8,9,9,10,11,15,15],
            [1,3,4,8,10,12],
            [1,1,1,1],
            [10],
            []
              ]
for test_case in test_cases:
    print(dedupArray(test_case)) #Expected Output: [1,2,3,4], [0,1,4,5,8,9,10,11,15], [1,3,4,8,10,12], [1], [10], []
    
# Time Complexity: O(n)
# Space Complexity: O(1)
# Time Taken: 51 mins