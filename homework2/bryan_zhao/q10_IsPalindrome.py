# Technique: Doubly linked list forward-backward two-pointer because
# palindromes need two pointers to converge from both sides of a list.
# Time Complexity: O(n) because a full iteration is needed to find the tail.
# Space Complexity: O(1) because nothing new is being made.

from typing import Optional

class Node:
    def __init__(self, data):
        self.data = data
        self.next: Optional[Node] = None
        self.prev: Optional[Node] = None

def IsPalindrome(head: Optional[Node]) -> bool:
    if not head or not head.next:
        return True
    
    left = head
    right = head
    while right.next:
        right = right.next
    
    while left != right and left.prev != right:
        if left.data != right.data:
            return False
        
        left = left.next
        right = right.prev
    
    return True

def LinkedListPrint(head: Optional[Node]):
    values = []
    curr = head
    while curr:
        values.append(str(curr.data))
        curr = curr.next
    print(" <-> ".join(values))

def TestCase():
    values = [9,2,4,2,9]
    head = Node(values[0])
    curr = head

    for val in values[1:]:
        curr.next = Node(val)
        curr = curr.next
    
    LinkedListPrint(head)
    
    print(IsPalindrome(head))

TestCase()

# Time Spent: 15 minutes