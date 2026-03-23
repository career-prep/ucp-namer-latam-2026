class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    #implemented this using linked list that is why we dont need size to chekc if this stack is full before adding
    def __init__(self):       #stack looks something like this
        self.top = None       # self.top
                              #    |
    def returnTop(self):      #    V
        return self.top.data  #   node
                              #    |
    def push(self, x):        #    V
        newNode = Node(x)     #   node
                              #    |
                              #    V
                              #   none

        newNode.next = self.top 
        self.top = newNode

    def pop(self):
        if self.top is not None:
            topNode = self.top
            self.top = self.top.next
            return topNode.data
        return None
    
    def isEmpty(self):
        return self.top is None

