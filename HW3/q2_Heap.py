class Heap:
    def __init__(self):
        self.arr = []
    
    def top(self) -> int:
        if len(self.arr)==0:
            return None
        return self.arr[0]
    

    """
    heap: parent must be smaller than child
    child must be filled from left to right (aka balance)

    ideas: add to the end and arrange it to the correct position

        - keep comparing the elem x with its parent:
            if x >= parent => append
            elif x< parent => swap position
    """
    
    def insert(self, x: int):
        self.arr.append(x)

        #track the elem so that we can move the x from that postion to the right place (it start from last elem and go up)
        idx_track= len(self.arr)-1

        #check if parent > x => swap
        while idx_track >0 and self.arr[(idx_track-1)//2] > self.arr[idx_track]:
            #swap parent with x
            temp= self.arr[(idx_track-1)//2]
            self.arr[(idx_track-1)//2]= self.arr[idx_track]
            self.arr[idx_track]= temp

            idx_track= (idx_track-1)//2
    
        return 

    
    """
    remove the min item (aka the root) of the heap
    idea: 
        - take the last elem and swap with the first elem (move it to index 0)
        - remove the last elem

        - if the swapped elem is too big -> swap with its childs:
            + if only have 1 child -> swap with it
            + if has 2 childs => swap with smaller one
    """
    def remove(self):
        # empty heap
        if len(self.arr)==0:
            return 

        # 1 elem in heap
        if len(self.arr)==1:
            self.arr.pop()
            return 
        
        #replace root with last elem
        self.arr[0]= self.arr[-1] 
        #delete last elem
        self.arr.pop()

        #move the swapped elem if it > children

        #start with root
        idx_track=0

        while True:
            #left child
            left_child_idx= 2*idx_track+1

            #right child
            right_child_idx= 2*idx_track+2

            #track min elem
            min_elem_idx= idx_track

            if left_child_idx< len(self.arr) and self.arr[left_child_idx] < self.arr[min_elem_idx]:
                min_elem_idx= left_child_idx
            
            if right_child_idx < len(self.arr) and self.arr[right_child_idx] < self.arr[min_elem_idx]:
                min_elem_idx= right_child_idx
            
            #if its already the smallest (nothing change) => return
            if min_elem_idx == idx_track:
                return 
            
            #swap with the smaller child
            temp = self.arr[idx_track]
            self.arr[idx_track] = self.arr[min_elem_idx]
            self.arr[min_elem_idx]= temp

            idx_track= min_elem_idx


        

        

        

        



        

    


