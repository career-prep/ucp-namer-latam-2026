# Maintain Two Heaps
# O(nlog(n)) Time complexity, where n is the number of elements in the stream
# O(n) Space Complexity
# You are given an array of numbers representing a stream received one by one. Return an array representing the median after each new number is received.


import heapq

def runningMedian(stream):


    # The intution behind this problem is maintaining two heaps.
    # Think of each heap like a left hand and a right hand.
    # The left hand is a max heap which stores values less than the current median.
    # the right hand is a min heap which stores values greater than the current median.
    # Both heap sizes must not differ by more than 1 element, so we might need to move elements around to different heaps to satisfy this.
    # If both heaps have the same size after insertion, the median is the mid point of the top elements from each heap.
    # If the heaps have different sizes after insertion, the median is the top element of whichever heap you just added an element to.
    
    if not stream:
        return []


    left = [] # maxheap, all values <= median
    right = [] # minheap, all values >= median

    res = [] # Stores the median at each point in time of the stream

    median = float('-inf')

    for i in range(len(stream)):

        num = stream[i] # Current number in the stream

        
        if len(left) == len(right): # Both heaps have the same size

            # Check if num is greater than or less than our most recent median
            if num > median:
                # If num > median, it must be put inside the right side heap (the min heap)
                heapq.heappush(right, num)

                median = right[0] # The new median is the value at the top of the heap we just added to
            else:
                # num <= median
                heapq.heappush(left, -1 * num)
                median = -1 * left[0] # We must multiply by -1 since heapq is a minheap, therefore in order to use it as a max heap, we needed to push negatives of
                                      # the real values, so now to extract the real values, we need to multiply the popped values by -1


        elif len(left) > len(right): # Left heap has 1 more element than right heap

            if num > median:
                # Num goes into right heap, and since len(right) < len(left), we do not need to move anything around
                heapq.heappush(right, num)

                # Now since both heaps have the same amount of elements, the median is the midpoint of the sum of the top values from each heap
                median = ((-1 * left[0]) + right[0]) / 2
            
            else:
                # num <= median
                # Num must go to the left heap, however since the left heap is already larger than the right heap, we need to move the left
                # heap's top element to the right heap
                moveElem = heapq.heappop(left)
                moveElem = -1 * moveElem # Revert this value back to its original value since it came from the left side (max heap)

                heapq.heappush(right, moveElem)

                # Now add num to the left heap (max heap)
                heapq.heappush(left, -1 * num)

                # Now since both heaps have the same amount of elements, the median is the midpoint of the sum of the top values from each heap
                median = ((-1 * left[0]) + right[0]) / 2

        elif len(left) < len(right):

            if num > median:
                # Num must go into the right heap, but since len(right) > len(left), we need to move the top element from right heap to the left heap,
                # then we can add num to the right heap
                moveElem = heapq.heappop(right)

                heapq.heappush(left, -1 * moveElem)

                # Now add num to right heap
                heapq.heappush(right, num)

                # Now since both heaps have the same amount of elements, the median is the midpoint of the sum of the top values from each heap
                median = ((-1 * left[0]) + right[0]) / 2

            else:
                # num <= median, so num must go into the left heap
                # since len(left) < len(right), we can add num to the left heap without having to move things around
                heapq.heappush(left, -1 * num)

                # Now since both heaps have the same amount of elements, the median is the midpoint of the sum of the top values from each heap
                median = ((-1 * left[0]) + right[0]) / 2


        
        res.append(median)



    return res




# 18 minutes


# Test Cases

stream1 = [1, 11, 4, 15, 12]
stream2 = []
stream3 = [-3, -2, 0, 2, 3]
stream4 = [3, 1, 8]


print(runningMedian(stream1))
print(runningMedian(stream2))
print(runningMedian(stream3))
print(runningMedian(stream4))