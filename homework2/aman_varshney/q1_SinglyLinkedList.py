# spent 40 minutes

# Node struct in py
class Node:
    def __init__(self, data: int, next: Node = None) -> None:
        self.data = data
        self.next = next 
    
    
class SinglyLinkedList:
    def __init__(self, head: Node) -> None:
        self.head = head
        
    def insertAtFront(self, val: int) -> Node:
        """Creates a new node with `val` data and links it at the head of the list. O(1) """
        return Node(val, self.head)
    
    def insertAtBack(self, val: int) -> Node:
        """Creates a new node with `val` data and links it at the end of the list. O(n)"""
        new_node = Node(val, None)
        curr = self.head
        # traverse to end
        while curr.next:
            curr = curr.next
        # link
        curr.next = new_node
        
    def insertAfter(self, val: int, loc: Node) -> Node:
        """Creates a new node with `val` data after Node `loc` and then returns the head. O(1)"""
        # create new node
        new_node = Node(val, None)
        # link
        temp = loc.next
        new_node.next = temp
        loc.next = new_node
        return self.head
    
    def insertBefore(self, val: int, loc: Node) -> Node:
        """Creates a new node with `val` data before `loc` and then returns the head. O(n)"""
        # check head case
        if (loc == self.head):
            return Node(val, loc)
        
        # find the node before loc    
        curr = self.head
        while (curr.next and curr.next != loc):
            curr = curr.next
        if not curr.next: # loc not found
            return None
            
        # create node
        new_node = Node(val, None)
        # link
        curr.next = new_node 
        new_node.next = loc
        return self.head
    
    def deleteFront(self) -> Node:
        """Removes the first node and returns the new head. O(1)"""
        if not self.head: # empty case
            return None
        return self.head.next
    
    def deleteBack(self) -> Node:
        """Removes the last node and returns head. O(n)"""
        if not self.head: # empty case
            return None
        
        # iterate to the 2nd to last node
        curr = self.head
        while curr.next:
            curr = curr.next
            
        # unlink last node
        curr.next = None
        return self.head
    
    def deleteNode(self, loc: Node) -> Node:
        """deletes the node `loc` and returns head. O(n)"""
        if not self.head: # empty case
            return None
        
        # check head case
        if (loc == self.head):
            return loc.next
        
        # find the node before loc
        curr = self.head
        while (curr.next and curr.next != loc):
            curr = curr.next
        if not curr.next: # loc not found
            return None
        
        # unlink loc
        curr.next = loc.next 
        return self.head
    
    def length(self) -> int:
        """Returns length of linked list. O(n)"""
        counter = 0
        curr = self.head
        while curr:
            curr = curr.next
            counter += 1
        return counter
    
    def reverseIterative(self) -> Node:
        """reverses the linked list iteratively. O(n)"""
        prev = None
        curr = self.head 

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
           
        self.head = prev 
        return self.head
        
    def reverseRecursive(self) -> Node:
        """Reverses the linked list recursively with a helper. O(n)"""
        # empty + base case
        if not self.head or self.head.next:
            return self.head
        
        # go to end and unravel
        new_head = self.reverseRecursive(self.head.next) 
        # reverse pointer
        self.head.next.next = self.head
        self.head.next = None
        
        return new_head