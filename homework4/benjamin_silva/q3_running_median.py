import heapq

def running_median(stream):
    max_heap = []  
    min_heap = []  

    result = []

    for num in stream:
        heapq.heappush(max_heap, -num)

        if min_heap and (-max_heap[0]) > min_heap[0]:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))

        if len(max_heap) > len(min_heap) + 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        elif len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))
        
        if len(max_heap) == len(min_heap):
            result.append((-max_heap[0] + min_heap[0]) / 2)
        else:
            result.append(float(-max_heap[0]))

    return result


if __name__ == "__main__":
    print(running_median([1, 11, 4, 15, 12]))  # [1, 6.0, 4, 7.5, 11]
    print(running_median([5]))                  # [5]
    print(running_median([3, 3, 3]))            # [3, 3, 3]
    print(running_median([10, 1]))              # [10, 5.5]

    # Time spent: 40 minutes