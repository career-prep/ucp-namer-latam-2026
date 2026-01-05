
def zeroSum(nums):
    counts = {}
    pairs = 0
    for number in nums:
        complement = number * -1
        if complement in counts and counts[complement] > 0:
            pairs += 1
            counts[complement] -= 1
        elif number in counts:
            counts[number] += 1
        else:
            counts[number] = 1
    
    return pairs
print(zeroSum([1,10,8,3,2,5,7,2,-2,-1,-2,0,0]))

def zeroSumContinued(nums):
    counts = set()
    pairs = 0
    for number in nums:
        if number not in counts:
            counts.add(number)
    
    for unique in counts:
        complement = unique * -1
        if complement in counts:
            pairs += 1        
    return pairs

print(zeroSumContinued([2,-2,2,-2]))

#40 minutes