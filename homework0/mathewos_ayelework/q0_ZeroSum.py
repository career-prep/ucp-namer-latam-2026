from collections import Counter
# zeroSum returns the number of pairs of integers in the array that sum to 0. Note: you can only use the element at each index only once
def zeroSum(nums: list[int]) -> int:
    count = 0
    freqMap = Counter(nums)

    for num,freq in freqMap.items():
        if num == 0:
            count += (freq // 2)
            continue
        
        diff = -1 * num
        if freqMap.get(diff) and num > 0:
            count += min(freqMap[num], freqMap[diff])

    return count           

# Time Complexity: O(n), Space Complexity: O(n)
# Total time taken: 47 mins

# zeroSumReuse returns the number of pairs of integers in the array that sum to 0. Note: you can reuse elements at each index in different pairs
def zeroSumReuse(nums: list[int]) -> int:
    count = 0
    freqMap = Counter(nums)

    for num,freq in freqMap.items():
        diff = -1 * num
        if num == 0:
            temp = 1
            while temp < freq:
                count += freq  - temp
                temp += 1
            continue

        if num > 0:
            count += freq * freqMap.get(diff, 0) 

    return count           

print("zeroSum Results:")
test_cases = [[1,10,8,3,2,5,7,2,-2,-1], [1,10,8,-2,2,5,7,2,-2,-1], [4,3,3,5,7,0,2,3,8,6], [4,3,3,5,7,0,2,3,8,0],[],[1,-1,-1,-1]]
for test_case in test_cases:
    print(zeroSum(test_case)) # Expected Output: 2,3,0,1,0,1
    
print("zeroSumReuse Results:")
for test_case in test_cases:
    print(zeroSumReuse(test_case)) # Expected Output: 3,5,0,1,0,3
    

# Time Complexity: O(n), Space Complexity: O(n)
# Total time taken: 31 mins