class max_heap:
    def __init__(self):
        self.array = []
        self.count = 0
    def top(self):
        if self.count == 0:
            return None
        return self.array[0]
    def insert(self, mes, val):
        """if self.count == 0:
            self.array.append(val)
            
        else:"""
        self.array.append([val,mes])
        idx = self.count 
        while idx > 0:
            parent = idx // 2
            
            if self.array[idx] [0]> self.array[parent][0]:
                self.array[idx], self.array[parent] = self.array[parent], self.array[idx]
                idx = parent
            else:
                break
        self.count += 1
    def remove(self):
        if self.count > 0:
            self.count -= 1
            self.array.pop(0)
