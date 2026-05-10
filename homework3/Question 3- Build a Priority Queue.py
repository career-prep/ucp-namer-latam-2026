class PriorityQueue:
    def __init__(self):
        self.arr = []

    def top(self):
        return self.arr[0][0]

    def insert(self, element, weight):
        self.arr.append((element, weight))
        i = len(self.arr) - 1
        while i > 0:
            parent = (i-1) // 2
            if self.arr[i][1] > self.arr[parent][1]:
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
            
            if left < len(self.arr) and self.arr[left][1] > self.arr[largest][1]:
                largest = left
            if right < len(self.arr) and self.arr[right][1] > self.arr[largest][1]:
                largest = right
            
            if largest != i:
                self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
                i = largest
            else:
                break
