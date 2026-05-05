class Heap:
    def __init__(self):
        self.arr = []

    def top(self):
            if not self.arr:
                return None
            return self.arr[0]
        
    def insert(self, x):
        self.arr.append(x)
        i = len(self.arr) - 1

        while i > 0:
            parent = (i - 1) // 2

            if self.arr[parent] <= self.arr[i]:
                break

            temp = self.arr[parent]
            self.arr[parent] = self.arr[i]
            self.arr[i] = temp

            i = parent
        
    def remove(self):
        if len(self.arr) == 0:
            return None
            
        min_value = self.arr[0]
        last = self.arr.pop()

        if len(self.arr) > 0:
            self.arr[0] = last
            i = 0

            while True:
                left = 2 * i + 1
                right = 2 * i + 2
                smallest = i

                if left < len(self.arr) and self.arr[left] < self.arr[smallest]:
                    smallest = left

                if right < len(self.arr) and self.arr[right] < self.arr[smallest]:
                    smallest = right
                
                if smallest == i:
                    break

                temp = self.arr[i]
                self.arr[i] = self.arr[smallest]
                self.arr[smallest] = temp

                i = smallest

        return min_value

# h = Heap()

# h.insert(5)
# h.insert(3)
# h.insert(8)
# h.insert(1)

# print(h.arr)       
# Output: [1, 3, 8, 5]
# print(h.top())  
# Output: 1  
# print(h.remove()) 
# Output: 1 
# print(h.top())     
# Output: 3

# 40