class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def disconnectCycle(head):
    """
    Given a singly linked list, disconnect the cycle if one exists.
    Return the head.

    Time: O(n)
    Space: O(1)
    """
    slow, fast = head, head
    hasCycle = False
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            hasCycle = True
            break
    
    if not hasCycle:
        return head

    start = head 
    while start != slow:
        start = start.next
        slow = slow.next

    prev = start
    while prev.next != start:
        prev = prev.next
    
    prev.next = None

    return head
    
# Example 1
# Input (with cycle): 10 -> 18 -> 12 -> 9 -> 11 -> 4
# (4 points back to 12)
# Expected output: 10 -> 18 -> 12 -> 9 -> 11 -> 4 -> None
head1 = Node(10)
head1.next = Node(18)
head1.next.next = Node(12)
head1.next.next.next = Node(9)
head1.next.next.next.next = Node(11)
head1.next.next.next.next.next = Node(4)

node12_1 = head1.next.next
node4_1 = head1.next.next.next.next.next
node4_1.next = node12_1


# Example 2
# Input (with cycle): 10 -> 18 -> 12 -> 9 -> 11 -> 4
# (4 points to itself)
# Expected output: 10 -> 18 -> 12 -> 9 -> 11 -> 4 -> None
head2 = Node(10)
head2.next = Node(18)
head2.next.next = Node(12)
head2.next.next.next = Node(9)
head2.next.next.next.next = Node(11)
head2.next.next.next.next.next = Node(4)

node4_2 = head2.next.next.next.next.next
node4_2.next = node4_2


def printList(head):
    cur = head
    vals = []
    while cur:
        vals.append(str(cur.data))
        cur = cur.next
    print(" -> ".join(vals) if vals else "empty")

printList(disconnectCycle(head1))
printList(disconnectCycle(head2))