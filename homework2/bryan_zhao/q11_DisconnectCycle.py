# Technique: Linked list fast-slow two pointer because fast-slow is used to track cycles.
# Time Complexity: O(n) because a node isn't visited more than a constant number of times.
# Space Complexity: O(1) because nothing new is being created.

from typing import Optional

class Node:
    def __init__(self, data):
        self.data = data
        self.next: Optional[Node] = None

def DisconnectCycle(head: Optional[Node]) -> Optional[Node]:
    if not head or not head.next:
        return head
    
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return head
        
    slow = head

    if slow == fast:
        while fast.next != slow:
            fast = fast.next
    else:
        while slow.next != fast.next:
            slow = slow.next
            fast = fast.next
    
    fast.next = None

    return head

def TestCase():
    n10 = Node(10)
    n18 = Node(18)
    n12 = Node(12)
    n9 = Node(9)
    n11 = Node(11)
    n4 = Node(4)

    n10.next = n18
    n18.next = n12
    n12.next = n9
    n9.next = n11
    n11.next = n4

    n4.next = n12
    
    DisconnectCycle(n10)
    curr = n10
    path = []
    count = 0
    while curr and count < 10:
        path.append(str(curr.data))
        curr = curr.next
        count += 1
    
    print(" -> ". join(path))
    if count == 6:
        print("Cycle broken.")
    else:
        print("Cycle not broken.")

TestCase()

# Time Spent: 21 minutes