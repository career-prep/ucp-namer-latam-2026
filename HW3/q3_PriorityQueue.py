class State:
    def __init__(self, name= None, priority=None):
        self.name= name
        self.priority=priority

class PriorityQueue:
    def __init__(self):
        self.arr= []
    

    def top(self):
        if len(self.arr)==0:
            return None
        return self.arr[0]
    
    """
    idea:
        insert to the end of the array, then swap
    """
    def insert(self, x:str, weight: int):
        state= State(x, weight)

        self.arr.append(state)

        idx_track= len(self.arr)-1
        while idx_track>0:
            parent_idx= (idx_track-1)//2

            #if the parent's prio >= current's prior => right place => return
            if self.arr[parent_idx].priority >= self.arr[idx_track].priority:
                return 
            #else => swap
            temp= self.arr[parent_idx]
            self.arr[parent_idx]= self.arr[idx_track]
            self.arr[idx_track]= temp

            idx_track= parent_idx
    

    def remove(self):
        #empty pqueue
        if len(self.arr)==0:
            return 
        
        #1 elem in pqueue
        if len(self.arr)==1:
            self.arr.pop()
            return 

        #replace the root with last elem
        self.arr[0]= self.arr[-1]
        self.arr.pop()

        idx_track=0
        while True:
            #left child
            left_child_idx= 2*idx_track+1

            #right child
            right_child_idx= 2*idx_track+2

            #track max elem
            max_elem_idx= idx_track

            if left_child_idx< len(self.arr) and self.arr[left_child_idx].priority > self.arr[max_elem_idx].priority:
                max_elem_idx= left_child_idx
            
            if right_child_idx < len(self.arr) and self.arr[right_child_idx].priority > self.arr[max_elem_idx].priority:
                max_elem_idx= right_child_idx
            
            #if its already the smallest (nothing change) => return
            if max_elem_idx == idx_track:
                return 
            
            #swap with the larger child
            temp = self.arr[idx_track]
            self.arr[idx_track] = self.arr[max_elem_idx]
            self.arr[max_elem_idx]= temp

            idx_track= max_elem_idx


        

        

        

        



        

    





            

            


