class Heap:
    """Minheap class"""
    def __init__(self) -> None:
        self.arr = []
        self.size = 0 
        
        
    def top(self) -> int:
        """Returns min in heap (first element); or None if empty"""
        return self.arr[0] if (self.size != 0) else None
    
    
    def insert(self, x: int) -> None:
        """Inserts `x` in correct position."""
        # append x
        self.arr.append(x)
        self.size += 1
        
        # bubble up
        i = self.size - 1
        while i > 0:
            parent = (i-1)//2
            if self.arr[parent] <= self.arr[i]:
                break
            # swap 
            self.arr[parent], self.arr[i] = self.arr[i], self.arr[parent]
            i = parent
            
        
    def remove(self) -> int: 
        """Pops minimum (top) element from heap. O(logn)"""
        if self.size == 0: # empty case
            return None
        elif self.size == 1:
            self.size -= 1
            return self.arr.pop()
        
        # move last element to root
        res = self.arr[0]
        self.arr[0] = self.arr.pop()
        self.size -= 1
        
        # bubble down
        parent = 0
        while 1:
            left = 2*parent + 1
            right = 2*parent + 2
            smallest = parent
            
            # find smallest among parent, left child, right child
            if left < self.size and self.arr[left] < self.arr[smallest]:
                smallest = left
            if right < self.size and self.arr[right] < self.arr[smallest]:
                smallest = right
                
            if smallest == parent: # break if smallest is parent
                break
            
            # swap
            self.arr[parent], self.arr[smallest] = self.arr[smallest], self.arr[parent]
            parent = smallest
        
        return res
        
   
        
        
if __name__ == '__main__':
    minheap = Heap()
    
    # empty 
    print("Empty case test")
    print("Expected: None")
    print("Actual", minheap.top())
              
    # insert nums
    nums = [5,3,8,1,2,7]
    print("Inserting", nums)
    for num in nums:
        minheap.insert(num)
        
    # top 
    print("Checking minimum")
    print("Expected: 1")
    print("Actual:", minheap.top())
    
    # remove elements
    print("Removing one by one")
    l = []
    for i in range(len(nums)):
        l.append(minheap.remove())
    print("Removed", l)
        
        
    
    