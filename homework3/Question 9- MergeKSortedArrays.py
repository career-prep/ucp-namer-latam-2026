# Time: 40 minutes
# Heap 

class Heap:
    def __init__(self):
        self.arr = []
    
    def top(self):
        return self.arr[0]
    
    def insert(self, x):
        self.arr.append(x)
        i = len(self.arr) - 1
        while i > 0:
            parent = (i-1) // 2
            if self.arr[i] < self.arr[parent]:
                self.arr[i], self.arr[parent] = self.arr[parent], self.arr[i]
                i = parent
            else:
                break
    
    def remove(self):
        self.arr[0] = self.arr[-1]  
        self.arr.pop()              
        i = 0
        while True:
            left = 2*i + 1
            right = 2*i + 2
            smallest = i
            
            if left < len(self.arr) and self.arr[left] < self.arr[smallest]:
                smallest = left
            if right < len(self.arr) and self.arr[right] < self.arr[smallest]:
                smallest = right
            
            if smallest != i:
                self.arr[i], self.arr[smallest] = self.arr[smallest], self.arr[i]
                i = smallest
            else:
                break

def MergeKSortedArrays(k, lists):

    h = Heap()
    for i in range(len(lists)):
        h.insert((lists[i][0], i, 0))

    result = []
    while h.arr:
        value, array_idx, element_idx = h.top()
        h.remove()
        result.append(value)
        
        if element_idx + 1 < len(lists[array_idx]):
            next_val = lists[array_idx][element_idx + 1]
            h.insert((next_val, array_idx, element_idx+1))

    return result

print(MergeKSortedArrays(2, [[1,2,3,4,5], [1,3,5,7,9]]))


