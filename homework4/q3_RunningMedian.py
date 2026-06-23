# Array/String Technique:  Maintain two heaps
# Time Complexity: O(N log N) 
# Space Complexity: O(N) 

import heapq

class MedianFinder:
    def __init__(self):
        self.small = []  
        self.large = []  

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0

if __name__ == "__main__":
    finder = MedianFinder()
    stream = [1, 11, 4, 15, 12]
    medians = []
    for num in stream:
        finder.addNum(num)
        medians.append(finder.findMedian())
    print("Stream Medians:", medians)

# Time Spent: 20 minutes