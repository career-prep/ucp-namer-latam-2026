class PriorityQueue:
    """Priority queue class"""
    def __init__(self) -> None:
        self.arr = [] # (str, int)
        self.size = 0 
        
        
    def top(self) -> str:
        """Returns min in heap (first element); or None if empty"""
        return self.arr[0][0] if (self.size != 0) else None
    
    
    def insert(self, x: str, weight: int) -> None:
        """Inserts `x` in correct position."""
        # append x
        self.arr.append( (x, weight) )
        self.size += 1
        
        # bubble up
        i = self.size - 1
        while i > 0:
            parent = (i-1)//2
            if self.arr[parent][1] <= self.arr[i][1]:
                break
            # swap 
            self.arr[parent], self.arr[i] = self.arr[i], self.arr[parent]
            i = parent
            
        
    def remove(self) -> str: 
        """Pops minimum (top) element from heap. O(logn)"""
        if self.size == 0: # empty case
            return None
        elif self.size == 1:
            self.size -= 1
            return self.arr.pop()[0]
        
        # move last element to root
        res = self.arr[0][0]
        self.arr[0] = self.arr.pop()
        self.size -= 1
        
        # bubble down
        parent = 0
        while 1:
            left = 2*parent + 1
            right = 2*parent + 2
            smallest = parent
            
            # find smallest among parent, left child, right child
            if left < self.size and self.arr[left][1] < self.arr[smallest][1]:
                smallest = left
            if right < self.size and self.arr[right][1] < self.arr[smallest][1]:
                smallest = right
                
            if smallest == parent: # break if smallest is parent
                break
            
            # swap
            self.arr[parent], self.arr[smallest] = self.arr[smallest], self.arr[parent]
            parent = smallest
        
        return res
        
        
        
if __name__ == '__main__':
    pq = PriorityQueue()
    
    # empty
    print("Empty case test")
    print("Expected: None")
    print("Actual", pq.top())
    
    # insert nums
    nums = [ ("a",5), ("b",3), ("c",8), ("d",1), ("e",2), ("f",7) ]
    print("Inserting", nums)
    for s, w in nums:
        pq.insert(s, w)
        
    # top 
    print("Checking minimum")
    print("Expected: d")
    print("Actual:", pq.top())
    
     # remove elements
    print("Removing one by one")
    l = []
    for i in range(len(nums)):
        l.append(pq.remove())
    print("Removed", l)