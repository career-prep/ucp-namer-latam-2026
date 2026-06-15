[3,4,1,1,3,4,4,3,1]
from collections import Counter, deque
import heapq
def rearrange(nums):
    counts = Counter(nums)
    heap = [(-val, key) for key, val in counts.items()]
    heapq.heapify(heap)
    print(heap)

rearrange([3,4,1,1,3,4,4,3,1])
