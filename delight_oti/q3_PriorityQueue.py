class Heap:
    def __init__(self):
        self.arr = []

    def top(self):
            if not self.arr:
                return None
            return self.arr[0][0]
        
    def insert(self, x, weight):
        self.arr.append((x,weight))
        i = len(self.arr) - 1

        while i > 0:
            parent = (i - 1) // 2

            if self.arr[parent][1] >= self.arr[i][1]:
                break

            temp = self.arr[parent]
            self.arr[parent] = self.arr[i]
            self.arr[i] = temp

            i = parent
        
    def remove(self):
        if len(self.arr) == 0:
            return None
            
        max_value = self.arr[0][0]
        last = self.arr.pop()

        if len(self.arr) > 0:
            self.arr[0] = last
            i = 0

            while True:
                left = 2 * i + 1
                right = 2 * i + 2
                largest = i

                if left < len(self.arr) and self.arr[left][1] > self.arr[largest][1]:
                    largest = left

                if right < len(self.arr) and self.arr[right][1] > self.arr[largest][1]:
                    largest = right
                
                if largest == i:
                    break

                temp = self.arr[i]
                self.arr[i] = self.arr[largest]
                self.arr[largest] = temp

                i = largest

        return max_value

# h = Heap()

# h.insert("email", 5)
# h.insert("game", 3)
# h.insert("exam", 8)
# h.insert("run", 1)

# print(h.arr)       
# Output: [('exam', 8), ('game', 3), ('email', 5), ('run', 1)]
# print(h.top())  
# Output: "exam"
# print(h.remove()) 
# Output: "exam"
# print(h.top())     
# Output: "email"

# 40