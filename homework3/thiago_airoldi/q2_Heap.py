# Min heap
class Heap:
    def __init__(self):
        self.heap = [] # 0-based indexing


    # Returns the min (top) element in the heap. O(1) Time Complexity.
    def top(self):
        if len(self.heap) > 0:
            return self.heap[0]
        else:
            return None


    # Adds 'val' into the heap in the appropriate position. O(log(n)) Time Complexity.
    def insert(self, val):

        # Store the index of the value we are about to insert
        idx = len(self.heap)

        # Add value to the heap
        self.heap.append(val)

        # Percolate the value up to fix the heap property
        self.percolateUp(idx)


    # Removes the min (top) element in the heap. O(log(n)) Time Complexity.
    def remove(self):

        # We can only remove an element if the heap has elements
        if len(self.heap) > 0:

            # Copy the last value into the root
            self.heap[0] = self.heap[len(self.heap) - 1]

            # Remove that last value we just copied to avoid duplicates
            self.heap.pop()

            # Start percolating down from the root because the value we just copied into the root is almost certainly in the wrong spot
            if len(self.heap) > 0:
                self.percolateDown(0)


    # Moves a node up to the correct position after insertion. O(log(n)) Time Complexity.
    def percolateUp(self, idx):
        
        if idx > 0: # Because we cannot percolate up past the root

            # Check if our current node is smaller in value than its parent node
            parentIdx = (idx-1)//2
            if self.heap[idx] < self.heap[parentIdx]:

                # Move our current node up one level
                self.swap(idx, parentIdx)

                # Recursive call to see if our current node still needs to keep percolating up
                self.percolateUp(parentIdx) # We pass in parentIdx because after the swap, our current node is at the parent's old position




    # Moves a node down to correct position after we remove the top. O(log(n)) Time Complexity.
    def percolateDown(self, idx):
        
        # Only percolate down locations that are inside the heap

        # First check if current node has two children. We only need to check if the right child exists because we should be following shape property
        rightIdx = (2*idx) + 2
        leftIdx = (2*idx) + 1

        if rightIdx < len(self.heap):

            # Find the index of the minimum value of the two children of our current node
            minIdx = self.minIndex(leftIdx, rightIdx)

            # If 'minIdx' value we got above is less than our current node, then our current node needs to percolate down
            if self.heap[minIdx] < self.heap[idx]:

                self.swap(idx, minIdx)

                # Recursive call to check if our current node needs to keep percolating down
                self.percolateDown(minIdx)


        elif leftIdx < len(self.heap): # If we arrive here, then the current node has ONLY a left child because we should be following shape property.
            
            # Here we only compare the current node to its only child, and no recursive call is needed because if we ONLY have a left child, then that child must be a leaf
            if self.heap[leftIdx] < self.heap[idx]:
                
                self.swap(idx, leftIdx)





    # Swaps two values in the heap. O(1) Time Complexity.
    def swap(self, idx1, idx2):
        temp = self.heap[idx1]
        self.heap[idx1] = self.heap[idx2]
        self.heap[idx2] = temp


    # Returns the index of the smaller value. O(1) Time Complexity.
    # Assumes idx1 and idx2 are valid positions in the heap.
    def minIndex(self, idx1, idx2):

        val1 = self.heap[idx1]
        val2 = self.heap[idx2]
        
        if val1 < val2:
            return idx1
        else:
            return idx2
        

