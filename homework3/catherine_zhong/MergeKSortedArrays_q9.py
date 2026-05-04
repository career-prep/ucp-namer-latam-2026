#time complexity: O(n)
#algorithm/DS = min heap

import heapq

def MergeKSortedArrays(k, arrs):
    nums = []
    
    if k <= 1:
        return arrs

    for i in range(k):
        heapq.heappush(nums, (arrs[i][0], i, 0))

    result = [] 
    while nums:
        num, arr, i = heapq.heappop(nums)
        result.append(num)
        if i+1 < len(arrs[arr]):
            heapq.heappush(nums, (arrs[arr][i+1], arr, i+1))

    return result

#test cases
k = 2
test = [[1, 2, 3, 4, 5], [1, 3, 5, 7, 9]]
print(f'test1: {MergeKSortedArrays(k, test)}')

k = 3
test = [[1, 4, 7, 9], [2, 6, 7, 10, 11, 13, 15], [3, 8, 12, 13, 16]]
print(f'test2: {MergeKSortedArrays(k, test)}')

k = 1
test = [1,2]
print(f'test3: {MergeKSortedArrays(k, test)}')

#time spent: 20 mins