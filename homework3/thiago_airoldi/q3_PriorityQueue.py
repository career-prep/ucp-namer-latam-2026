class PriorityQueue:

    def __init__(self):
        self.PQ = [] # Holds tuples of (String, Weight), String being a string, and Weight being an integer
        # We will implement this as a max heap


    # Returns the max (top) element in the priority queue. O(1) Time Complexity. (The Assignment says this function should return an integer, but I believe that's wrong)
    # I believe this function should return string AND weight, not just weight. Since each element is a tuple of (string, weight)
    def top(self):
        if len(self.PQ) > 0:
            return self.PQ[0] # Return the first element
        else:
            return None


    # Adds (string, weight) into the priority queue in the appropriate position. O(log(n)) Time Complexity.
    def insert(self, string, weight):

        # Store the index of the element we are about to insert
        idx = len(self.PQ)

        # Add element to the priority queue
        self.PQ.append((string, weight))

        # Percolate the element up to fix the priority queue property
        self.percolateUp(idx)


    # Removes the max (top) element in the priority queue. O(log(n)) Time Complexity.
    def remove(self):

        # We can only remove an element if the priority queue has elements
        if len(self.PQ) > 0:

            # Copy the last value into the root
            self.PQ[0] = self.PQ[len(self.PQ) - 1]

            # Remove that last value we just copied to avoid duplicates
            self.PQ.pop()

            # Start percolating down from the root because the value we just copied into the root is almost certainly in the wrong spot
            if len(self.PQ) > 0:
                self.percolateDown(0)


    # Moves an element up to the correct position after insertion. O(log(n)) Time Complexity.
    def percolateUp(self, idx):
        
        if idx > 0: # Because we cannot percolate up past the root

            # Check if our current element's weight is larger in value than its parent element's weight
            parentIdx = (idx-1)//2
            if self.PQ[idx][1] > self.PQ[parentIdx][1]:

                # Move our current element up one level
                self.swap(idx, parentIdx)

                # Recursive call to see if our current element still needs to keep percolating up
                self.percolateUp(parentIdx) # We pass in parentIdx because after the swap, our current element is at the parent's old position




    # Moves a element down to correct position after we remove the top. O(log(n)) Time Complexity.
    def percolateDown(self, idx):
        
        # Only percolate down locations that are inside the priority queue

        # First check if current element has two children. We only need to check if the right child exists because we should be following shape property
        rightIdx = (2*idx) + 2
        leftIdx = (2*idx) + 1

        if rightIdx < len(self.PQ):

            # Find the index of the maximum weight of the two children of our current element
            maxIdx = self.maxIndex(leftIdx, rightIdx)

            # If 'maxIdx' weight we got above is greater than our current element, then our current element needs to percolate down
            if self.PQ[maxIdx][1] > self.PQ[idx][1]:

                self.swap(idx, maxIdx)

                # Recursive call to check if our current element needs to keep percolating down
                self.percolateDown(maxIdx)


        elif leftIdx < len(self.PQ): # If we arrive here, then the current element has ONLY a left child because we should be following shape property.
            
            # Here we only compare the current element to its only child, and no recursive call is needed because if we ONLY have a left child, then that child must be a leaf
            if self.PQ[leftIdx][1] > self.PQ[idx][1]:
                
                self.swap(idx, leftIdx)




    # Swaps two elements in the priority queue. O(1) Time Complexity.
    def swap(self, idx1, idx2):
        temp = self.PQ[idx1]
        self.PQ[idx1] = self.PQ[idx2]
        self.PQ[idx2] = temp


    # Returns the index of the larger weight. O(1) Time Complexity.
    # Assumes idx1 and idx2 are valid positions in the priority queue.
    def maxIndex(self, idx1, idx2):

        val1 = self.PQ[idx1][1]
        val2 = self.PQ[idx2][1]
        
        if val1 > val2:
            return idx1
        else:
            return idx2