class Node:
    def __init__(self,data=None,prev=None,next=None):
        self.data=data
        self.prev=prev
        self.next=next
    

class Deque:
    def __init__(self):
        self.front_node=None
        self.back_node=None
    

    def front(self):
        if self.front_node==None or self.back_node==None:
            return None
        return self.front_node.data
    
    
    def back(self):
        if self.front_node==None or self.back_node==None:
            return None
        return self.back_node.data
    

    def pushBack(self,x): #add x to the back of queue
        node=Node(x)
        if self.front_node==None or self.back_node==None:
            self.front_node= node
            self.back_node= node
            return 
        
        # if there exist >=1 node
        self.back_node.next=node
        node.prev= self.back_node
        self.back_node= node
        return 
    
    def pushFront(self,x):
        node=Node(x)
        if self.front_node==None or self.back_node==None:
            self.front_node= node
            self.back_node= node
            return 
        
        #if there exist >=1
        self.front_node.prev=node
        node.next=self.front_node
        self.front_node=node
        return

    def popFront(self): #rm and return the data of first elem
        if self.front_node==None or self.back_node==None:
            return None
        
        returned_data= self.front_node.data
        self.front_node=self.front_node.next

        #handle case when there is 1 node only
        if self.front_node==None:
            self.back_node=None
            return returned_data
        
        #if there exists >=2 nodes
        return returned_data
    

    def popBack(self):
        if self.front_node==None or self.back_node==None:
            return None
        
        returned_data= self.back_node.data
        self.back_node=self.back_node.prev

        #handle case when there is 1 node only
        if self.back_node==None:
            self.front_node=None
            return returned_data
        
        #if there exists >=2 nodes
        return returned_data
    
    def isEmpty(self): #bool
        if self.front_node==None or self.back_node==None:
            return True
        return False

    

        


        

