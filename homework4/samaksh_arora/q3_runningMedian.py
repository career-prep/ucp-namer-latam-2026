#Samaksh Arora
#Question 3 - Running Median
#Maintain two heaps
#Time Complexity:
#Space Complexity:
#Time Spent:



def getRunningMedian(stream):
    import heapq

    min_heap = []  # To store the larger half of the numbers
    max_heap = []  # To store the smaller half of the numbers
    medians = []

    for number in stream:
        if not max_heap or number <= -max_heap[0]:
            heapq.heappush(max_heap, -number)  # Push negative to simulate max heap
        else:
            heapq.heappush(min_heap, number)

        # Balance the heaps
        if len(max_heap) > len(min_heap) + 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        elif len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))

        # Calculate median
        if len(max_heap) == len(min_heap):
            median = (-max_heap[0] + min_heap[0]) / 2
        else:
            median = float(-max_heap[0])

        medians.append(median)

    return medians

#Test Cases
# input_stream = [1, 11, 4, 15, 12]
# expected_output = [1, 6, 4, 7.5, 11]
# assert getRunningMedian(input_stream) == expected_output

# Extra: input_stream = [5, 15, 1, 3]
# expected_output = [5, 10, 5, 4]
# assert getRunningMedian(input_stream) == expected_output
