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

class MaxHeap:
    def __init__(self):
        self.arr = []

    def top(self):
        return self.arr[0]

    def insert(self, x):
        self.arr.append(x)
        i = len(self.arr) - 1
        while i > 0:
            parent = (i-1) // 2
            if self.arr[i] > self.arr[parent]:
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
            largest = i
            
            if left < len(self.arr) and self.arr[left] > self.arr[largest]:
                largest = left
            if right < len(self.arr) and self.arr[right] > self.arr[largest]:
                largest = right
            
            if largest != i:
                self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
                i = largest
            else:
                break