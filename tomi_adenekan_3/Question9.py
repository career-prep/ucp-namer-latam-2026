"""
Input: 2, [[1, 2, 3, 4, 5], [1, 3, 5, 7, 9]]
Output: [1, 1, 2, 3, 3, 4, 5, 5, 7, 9]

Input: 3, [[1, 4, 7, 9], [2, 6, 7, 10, 11, 13, 15], [3, 8, 12, 13, 16]]
Output: [1, 2, 3, 4, 6, 7, 7, 8, 9, 10, 11, 12, 13, 13, 15, 16]

time = nlogn
space = n

"""
import heapq

def sorted_k(input, n):
    if n <= 1:
        return input[-1]

    heap = []
    for i in range(n):
        heapq.heappush(heap, (input[i][0], i, 0))

    res = []
    while heap:
        val, typ, idx = heapq.heappop(heap)
        if idx < len(input[typ])-1:
            idx += 1
            heapq.heappush(heap, (input[typ][idx], typ, idx))
        
        res.append(val)
    return res

input = [[1, 2, 3, 4, 5], [1, 3, 5, 7, 9]]
print(sorted_k(input, 2))

out = [[1, 4, 7, 9], [2, 6, 7, 10, 11, 13, 15], [3, 8, 12, 13, 16]]
print(sorted_k(out, 3))
    
