import heapq

# Time complexity: O(n log n)
# Space complexity: O(n)

# Technique: Multiple query problems: two heaps

def RunningMedian(stream):
    smaller, larger, = [], []
    res = []

    for num in stream:
        heapq.heappush(smaller, -num)

        heapq.heappush(larger, -heapq.heappop(smaller))

        if len(larger) > len(smaller):
            heapq.heappush(smaller, -heapq.heappop(larger))

        if len(larger) == len(smaller):
            median = (-smaller[0] + larger[0]) / 2
        else:
            median = -smaller[0]

        res.append(median)

    return res
            


if __name__ == "__main__":
    stream = [1, 11, 4, 15, 12]
    print(RunningMedian(stream))

    stream = []
    print(RunningMedian(stream))

# ~ time spent: ~30 minutes