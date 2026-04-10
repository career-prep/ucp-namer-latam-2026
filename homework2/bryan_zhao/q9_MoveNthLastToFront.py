# Technique: Linked list fixed distance two pointer because both 
# fast and slow pointers increment the same distance once fast
# gets their headstart.
# Time Complexity: O(n) because the list is traversed only once.
# Space Complexity: O(1) because nothing new is being created.

from typing import Optional

class Node:
    def __init__(self, data):
        self.data = data
        self.next: Optional[Node] = None

def MoveNthLastToFront(head: Optional[Node], k: int) -> Optional[Node]:
    if not head or not head.next or k <= 0:
        return head
    
    temp = Node(0)
    temp.next = head

    fast = temp
    slow = temp

    for _ in range(k):
        if fast.next:
            fast = fast.next
        else:
            return head
    
    while fast.next:
        fast = fast.next
        slow = slow.next
    
    target = slow.next
    slow.next = target.next
    
    target.next = temp.next
    temp.next = target

    return temp.next

def LinkedListPrint(head: Optional[Node]):
    values = []
    curr = head
    while curr:
        values.append(str(curr.data))
        curr = curr.next
    print(" -> ".join(values))

def TestCase():
    values = [15,2,8,7,20,9,11,6,19]
    head = Node(values[0])
    curr = head

    for val in values[1:]:
        curr.next = Node(val)
        curr = curr.next
    
    LinkedListPrint(head)
    
    new_head = MoveNthLastToFront(head, 2)
    LinkedListPrint(new_head)

TestCase()

# Time Spent: 31 minutes