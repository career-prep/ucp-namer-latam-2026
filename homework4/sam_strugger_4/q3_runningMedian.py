import heapq
# I realize this is a very naive solution but I really wasn't sure what else to do

# [1 , 11, 4, 15, , 12]
def runningMedian(nums):

    result = [nums[0]]

    for i in range(1,len(nums)):

        if len(result) % 2 == 1:
            med_idx = i//2
            med = (nums[med_idx] + nums[med_idx+1]) / 2
            result.append(med)

        else:
            med_idx = i//2
            result.append(nums[med_idx])

    return result

test1 = runningMedian([1,11,4,15,12])
print(test1)

# I realized this isn't the median since the median needs to be taken from a sorted list

# I believe this needs to be solved with a min and max heap, if we split an array
# in half where the half with greater values is in a min heap and the half with smaller
# values is in a max heap then the top of one of those heaps will be the median OR 
# we can take the average of the two values at the top of the heap if the lengths of 
# the arrays are even

def runningMedian2(nums):
    result = []
    max_heap = []
    min_heap = []

    for num in nums:
        if not min_heap or num <= min_heap[0]:
            heapq.heappush(max_heap, -num)
        else:
            heapq.heappush(min_heap, num)

        min_count = len(min_heap)
        max_count = len(max_heap)

        if max(min_count, max_count) - min(min_count, max_count) == 2:
            if max(min_count, max_count) == min_count:
                n = heapq.heappop(min_heap)
                heapq.heappush(max_heap, -n)
            else:
                n = heapq.heappop(max_heap)
                heapq.heappush(min_heap, -n)

        if len(max_heap) == len(min_heap):
            result.append((-max_heap[0] + min_heap[0])/2)
        elif len(max_heap) > len(min_heap):
            result.append(-max_heap[0])
        else:
            result.append(min_heap[0])
    return result 

test1 = runningMedian2([1,11,4,15,12])
print(test1)
        

# This implementation has O(nlogn) time complexity and O(n) space complexity
# The two implementations together took me over an hour with this one taking me around 45 minutes. 
