# spent 15 minutes

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None
        

class Deque:
    def __init__(self) -> None:
        self._front = None
        self._back = None
    
    def front(self):
        """Returns first item. O(1)"""
        return self._front.data if self._front else None
        
    def back(self):
        """Returns last item. O(1)"""
        return self._back.data if self._back else None
        
    def pushBack(self, x):
        """Adds `x` to the back of the deque. O(1)"""
        if not self._front: # first element case
            new_node = Node(x) 
            self._front = new_node
            self._back = new_node
            return

        new_node = Node(x)
        new_node.prev = self._back
        self._back.next = new_node
        self._back = new_node
        
    def pushFront(self, x):
        """Adds `x` to the front. O(1)"""
        if not self._front: # first element case
            new_node = Node(x) 
            self._front = new_node
            self._back = new_node
            return
        
        new_node = Node(x)
        new_node.next = self._front
        self._front.prev = new_node
        self._front = new_node
        
    def popFront(self):
        """Removes and returns value at front of deque. O(1)"""
        if not self._front: # empty case
            return None
        
        if self._front == self._back: # one element case
            x = self._front.data
            self._front = None
            self._back = None
            return x    
        
        x = self._front.data
        self._front = self._front.next
        if self._front:
            self._front.prev = None
        return x
    
    def popBack(self):
        """Removes and returns value at back of deque. O(1)"""
        if not self._back: # empty case
            return None
        
        if self._front == self._back: # one element case
            x = self._front.data
            self._front = None
            self._back = None
            return x    
        
        x = self._back.data
        self._back = self._back.prev
        self._back.next = None
        return x
        
    def isEmpty(self):
        """True if deque is empty. O(1)"""
        return (self._front is None)


if __name__ == "__main__":
    # 1
    # empty deque
    d = Deque()
    assert d.isEmpty() is True, "empty isEmpty error"
    assert d.popFront() is None, "empty popFront error"
    assert d.popBack() is None, "empty popBack error"


    # 2
    # pushBack only —> order front to back
    d.pushBack(1)
    d.pushBack(2)
    d.pushBack(3)
    
    assert d.isEmpty() is False, "nonempty isEmpty error"
    assert d.front() == 1, "front error1"
    assert d.back() == 3, "back error1"
    assert d.popFront() == 1, "popFront error1"
    
    assert d.front() == 2, "front error2"
    assert d.back() == 3, "back error2"
    assert d.popBack() == 3, "popBack error2"
    
    assert d.front() == 2, "front error3"
    assert d.back() == 2, "back error3"
    assert d.popFront() == 2, "popFront error3"
    assert d.isEmpty() is True, "isEmpty error"
    assert d.front() is None, "error"
    assert d.back() is None, "error"


    # 3
    # pushFront / pushBack mix
    d2 = Deque()
    d2.pushBack(10)
    d2.pushFront(5)
    d2.pushBack(15)
    
    assert d2.front() == 5, "front error1"
    assert d2.back() == 15, "back error1"
    assert d2.popFront() == 5, "mix error1"
    
    assert d2.front() == 10, "front error2"
    assert d2.back() == 15, "back error3"
    assert d2.popBack() == 15, "mix error2"
    
    assert d2.front() == 10, "front error3"
    assert d2.back() == 10, "back error3"
    assert d2.popFront() == 10, "mix error3"
    
    assert d2.isEmpty() is True, "mix error"
    assert d2.front() is None, "mix error"
    assert d2.back() is None, "mix error"


    print("All tests passed")
