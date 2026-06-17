# Technique: Simultaneous Iteration two-pointer because curr and
# curr.next are being inspected simultaneously
# Time Complexity: O(n) because each node is visited exactly once
# Space Complexity: O(1) because nothing new is being created.

from typing import Optional

class Node:
    def __init__(self, data):
        self.data = data
        self.next: Optional[Node] = None

def DedupSortedList(head: Optional[Node]) -> Optional[Node]:
    if not head:
        return None
    
    curr = head
    while curr.next:
        if curr.data == curr.next.data:
            curr.next = curr.next.next
        else:
            curr = curr.next
    
    return head

def LinkedListPrint(head: Optional[Node]):
    values = []
    curr = head
    while curr:
        values.append(str(curr.data))
        curr = curr.next
    print(" -> ".join(values))

def TestCase():
    values = [1,2,2,4,5,5,5,10,10]
    head = Node(values[0])
    curr = head

    for val in values[1:]:
        curr.next = Node(val)
        curr = curr.next
    
    LinkedListPrint(head)
    deduped_head = DedupSortedList(head)

    LinkedListPrint(deduped_head)    

TestCase()

# Time Spent: 5 minutes