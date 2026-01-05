def zeroSum(nums):
    freqMap = {}
    count = 0
    usedSet = set()

    for num in nums:
        if num in freqMap:
            freqMap[num] +=1
        else:
            freqMap[num] = 1

    for num in nums:
        diff = -1 * num
        if num == 0 and num not in usedSet:
            count += freqMap[num] // 2
            usedSet.add(num)
            continue
        
        if freqMap.get(diff) and num not in usedSet and diff not in usedSet:
            count += min(freqMap[num],freqMap[diff])
            usedSet.add(num)
            usedSet.add(diff)

    return count           

# Time Complexity: O(n), Space Complexity: O(n)
# Total time taken: 47 mins

def zeroSumReuse(nums):
    freqMap = {}
    count = 0
    usedSet = set()

    for num in nums:
        if num in freqMap:
            freqMap[num] +=1
        else:
            freqMap[num] = 1

    for num in nums:
        diff = -1 * num
        if num == 0 and num not in usedSet:
            temp = 1
            while temp < freqMap[num]:
                count += freqMap[num]  - temp
                temp += 1
            
            usedSet.add(num)
            continue

        if freqMap.get(diff) and num not in usedSet and diff not in usedSet:
            count += freqMap[num] * freqMap[diff]
            usedSet.add(num)
            usedSet.add(diff)

    return count           


# Time Complexity: O(n), Space Complexity: O(n)
# Total time taken: 31 mins