#Min Heap

class MinHeap:
    
    def __init__(self):
        self.heap_array = []

    def top(self):
        if len(self.heap_array) > 0:
            return self.heap_array[0]
        return None
    
    def insert(self, value):
        self.heap_array.append(value)
        self.sift_up(len(self.heap_array)-1)
    
    def remove(self):
        if len(self.heap_array) <= 1:
            return None
        
        self.heap_array[0] = self.heap_array[-1]
        self.heap_array.pop()
        self.sift_down(0)

    def sift_down(self, current_idx):
        heap_size = len(self.heap_array)

        while True:
            left_child_idx = 2 * current_idx + 1
            right_child_idx = 2 * current_idx + 2
            min_value_idx = current_idx

            if left_child_idx < heap_size and self.heap_array[left_child_idx] < self.heap_array[min_value_idx]:
                min_value_idx = left_child_idx
            
            if right_child_idx < heap_size and self.heap_array[right_child_idx] < self.heap_array[min_value_idx]:
                min_value_idx = right_child_idx
            
            if min_value_idx != current_idx:
                #swap
                self.heap_array[current_idx], self.heap_array[min_value_idx] = self.heap_array[min_value_idx], self.heap_array[current_idx]
                current_idx = min_value_idx
            else:
                break
    
    def sift_up(self, current_idx):
        while current_idx > 0:
            parent_idx = (current_idx - 1) // 2

            if self.heap_array[current_idx] < self.heap_array[parent_idx]:
                self.heap_array[current_idx], self.heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[current_idx]
                current_idx = parent_idx
            else:
                break