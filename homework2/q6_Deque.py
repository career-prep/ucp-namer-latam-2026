class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class Deque:

    def __init__(self):
        self.frontNode = None
        self.backNode = None


    # Returns first item in the Deque. O(1) time.
    def front(self):
        if self.isEmpty():
            return None
        else:
            return self.frontNode.data
    
    # Returns the last item in the Deque. O(1) time.
    def back(self):
        if self.isEmpty():
            return None
        else:
            return self.backNode.data
    
    # Adds x to the back of the Deque. O(1) time.
    def pushBack(self, x):

        newItem = Node(x)

        # Empty Deque
        if self.isEmpty():
            self.frontNode = newItem
            self.backNode = newItem
            return

        # Normal Case (Works even when Deque only has 1 item)
        self.backNode.next = newItem

        newItem.prev = self.backNode

        self.backNode = newItem

    # Adds x to the front of the Deque. O(1) time.
    def pushFront(self, x):

        newItem = Node(x)

        # Empty Deque
        if self.isEmpty():
            self.frontNode = newItem
            self.backNode = newItem
            return


        # Normal Case (Works even when Deque only has 1 item)
        self.frontNode.prev = newItem

        newItem.next = self.frontNode

        self.frontNode = newItem


    # Removes and returns the first item in the Deque. O(1) time.
    def popFront(self):
        if self.isEmpty():
            return None
        
        saveVal = self.frontNode.data

        # One item in Deque
        if self.frontNode == self.backNode:
            self.frontNode = None
            self.backNode = None
            return saveVal

        # Normal Case
        newFrontNode = self.frontNode.next
        newFrontNode.prev = None
        self.frontNode.next = None
        self.frontNode = newFrontNode

        return saveVal
    

    # Removes and returns the last item in the Deque. O(1) time.
    def popBack(self):
        if self.isEmpty():
            return None
        
        saveVal = self.backNode.data

        # One item in Deque
        if self.frontNode == self.backNode:
            self.frontNode = None
            self.backNode = None
            return saveVal
        
        # Normal Case
        newBackNode = self.backNode.prev
        newBackNode.next = None
        self.backNode.prev = None
        self.backNode = newBackNode
        
        return saveVal

    # Returns a boolean indicating whether the Deque is empty. O(1) time.
    def isEmpty(self):
        if self.frontNode == None and self.backNode == None:
            return True
        else:
            return False