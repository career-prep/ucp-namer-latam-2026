# A priority queue functions like a queue except that elements are removed in order
# of priority rather than insertion. This is typically implemented as a max heap that
# stores pairs of elements and numeric weights, with the weights used as the values in the heap.
# Implement a priority queue according to the following API using a heap as the underlying data structure. 
# For simplicity, you can assume the priority queue stores string elements with integer priorities. 
# Start by copy-pasting your heap implementation from question 2 and making modifications.


# implementing as a max heap, each element in the array will be a tuple that look like: (string, weight)
class PriorityQueue():
    # private:
    #   array<pair<string, int>> arr; // the underlying array

    # public:
    #   int top(); // returns the highest priority (first) element in the PQ
    #   void insert(string x, int weight); // adds string x to the PQ with priority weight
    #   void remove(); // removes the highest priority (first) element in the PQ

    def __init__(self, queue):
        self.arr = queue

    # assumption: when returning the top it should retunr the string not the weight
    def top(self):
        if len(self.arr) == 0:
            return "Max heap is empty"
        
        return self.arr[0][0]
    
    def insert(self, x, weight):
        n = len(self.arr)
        self.arr.append((x, weight))

        # now we have the array with new element in the end of the array 

        # Its time to heapify, or fix the heap

        while n > 0 and self.arr[n][1] > self.arr[(n-1)//2][1]:
            self.arr[n], self.arr[(n-1)//2] = self.arr[(n-1)//2], self.arr[n]
            n = (n-1)//2
    

    def remove(self):
        if len(self.arr) == 0:
            return "the Max Heap is empty"
        
        if len(self.arr) == 1:
            node = self.arr.pop()
            return node[0]
        
        node = self.arr[0]
        self.arr[0] = self.arr.pop()

        # now we have a structure where the first element (with max priority is removed)
        # and we replace it by the last elemnt in the arr or heap

        # now we need to max heapify the strucutre to maintain the max heap property
        i = 0
        n = len(self.arr)
        while True:   
            left = (2*i) + 1
            right = (2*i) + 2
            priority = i

            if left < n and self.arr[left][1] > self.arr[priority][1]:
                priority = left

            if right < n and self.arr[right][1] > self.arr[priority][1]:
                priority = right

            if priority == i:
                break

            self.arr[priority], self.arr[i] = self.arr[i], self.arr[priority]
            i = priority

        return node