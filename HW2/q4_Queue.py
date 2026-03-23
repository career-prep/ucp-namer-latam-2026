class Node:
    def __init__(self, data=None, next=None):
        self.data=data
        self.next=next
    

class Queue:
    def __init__(self):
        self.front=None
        self.back=None
    
    def peek(self): #return first item
        if self.front==None:
            return None
        
        return self.front.data
    
    def enqueue(self,x): #append x to the back of the queue
        node=Node(x)
        if self.front==None and self.back==None:
            self.front=node
            self.back=node
            return 
        
        if self.back!=None:
            self.back.next=node
            self.back=node
    
        return 
        
    def dequeue(self):
        if self.front==None or self.back==None:
            return None
        
        returned_data=self.front.data
        self.front= self.front.next

        #handle the case when the queue is empty after remove elem
        if self.front==None:
            self.back=None
        
        return returned_data

    def isEmpty(self):
        if self.front==None or self.back==None:
            return True
        return False
    


    



            
    

    

    

