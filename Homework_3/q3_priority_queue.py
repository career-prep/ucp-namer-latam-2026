# Question 3: Build a Priority Queue
#
# A priority queue functions like a queue except that elements are removed
# in order of priority rather than insertion order.
# This is typically implemented as a max heap that stores pairs of elements
# and numeric weights, with the weights used as the values in the heap.
#
# Implement a priority queue according to the following API using a heap
# as the underlying data structure.
# For simplicity, assume the priority queue stores string elements with integer priorities.
# Start by copy-pasting your heap implementation from question 2 and making modifications.
#
# class PriorityQueue:
#     arr = []                            # underlying array
#
#     def top(self)                      -> returns the highest priority element
#     def insert(self, val, priority)    -> adds val with given priority
#     def remove(self)                   -> removes the highest priority element

class PriorityQueue:
    def __init__(self):
        self.arr=[]

    def top(self):
        return self.arr[0][1]
    
    def insert(self,val,priority):
        self.arr.append((priority,val))
        self.push_up(len(self.arr)-1)

    def remove(self):
        self.arr[0]=self.arr[-1]
        self.arr.pop()
        self.push_down(0)

    def push_up(self,i):
        parent_node=(i-1)//2
        if i>0 and self.arr[i]<self.arr[parent_node]:
            self.arr[i],self.arr[parent_node]=self.arr[parent_node],self.arr[i]
            self.push_up(parent_node)

    def push_down(self,i):
        node=i
        left=(2*i)+1
        right=(2*i)+2
        if left<len(self.arr) and self.arr[left]<self.arr[node]:
            node=left
        if right<len(self.arr) and self.arr[right]<self.arr[node]:
            node=right
        if node!= i: 
            self.arr[i],self.arr[node]=self.arr[node],self.arr[i] 
            self.push_down(node)

heap = PriorityQueue()
for n in [5, 3, 8, 1, 2, 7, 4]:
    heap.insert(n)
print(heap.top()) 
heap.remove()
print(heap.top())  
heap.insert(10)
print(heap.top())


#Time Complexity: O(logn) except for top with O(1)
#Space Complexity: O(n)

#Spent 30 mins
