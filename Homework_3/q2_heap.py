# Write a MinHeap class using an array as the underlying data structure.
# For simplicity, assume the heap holds integers only.
#
# Implement the following;

# class MinHeap:
#     arr = []
#
# def top(self)        -> returns the min element
# def insert(self, x)  -> adds x to the heap in the correct position
# def remove(self)     -> removes the min element from the heap


class MinHeap:
    def __init__(self):
        self.arr=[]

    def top(self):
        return self.arr[0]
    
    def insert(self,val):
        self.arr.append(val)
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

heap = MinHeap()
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
