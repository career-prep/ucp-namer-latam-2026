import heapq

def get_running_median(stream: list[int]) -> list[float]:
    max_heap = []
    min_heap = []
    medians = []

    for num in stream:
        if not max_heap or num <= -max_heap[0]:
            heapq.heappush(max_heap, -num)
        else:
            heapq.heappush(min_heap, num)

        if len(max_heap) > len(min_heap) + 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        elif len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))

        if len(max_heap) == len(min_heap):
            medians.append((-max_heap[0] + min_heap[0]) / 2.0)
        else:
            medians.append(float(-max_heap[0]))
            
    return medians


if __name__ == "__main__":
    assert get_running_median([1, 11, 4, 15, 12]) == [1.0, 6.0, 4.0, 7.5, 11.0]
    assert get_running_median([]) == []
    assert get_running_median([5]) == [5.0]

    assert get_running_median([3, 1]) == [3.0, 2.0]
    assert get_running_median([2, 2, 2, 2]) == [2.0, 2.0, 2.0, 2.0]
    assert get_running_median([10, 1, 2, 3, 4, 5]) == [10.0, 5.5, 2.0, 2.5, 3.0, 3.5]
    assert get_running_median([100]) == [100.0]

    print("All RunningMedian tests passed!")
