class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def dedupSortedList(head):
    """
    Given a sorted singly linked list, remove duplicates
    so that each value appears at most once.
    Return the head of the list.

    Time: O(n)
    Space: O(1)
    """
    if not head or not head.next:
        return head
    
    prev = head
    cur = head.next

    while cur:
        if prev.data == cur.data:
            prev.next = cur.next
            cur = cur.next   
        else: 
            prev = cur
            cur = cur.next

    return head


# Example 1
# Input: 1 -> 2 -> 2 -> 4 -> 5 -> 5 -> 5 -> 10 -> 10
# Expected Output: 1 -> 2 -> 4 -> 5 -> 10
head1 = Node(1)
head1.next = Node(2)
head1.next.next = Node(2)
head1.next.next.next = Node(4)
head1.next.next.next.next = Node(5)
head1.next.next.next.next.next = Node(5)
head1.next.next.next.next.next.next = Node(5)
head1.next.next.next.next.next.next.next = Node(10)
head1.next.next.next.next.next.next.next.next = Node(10)


# Example 2
# Input: 8 -> 8 -> 8 -> 8
# Expected Output: 8
head2 = Node(8)
head2.next = Node(8)
head2.next.next = Node(8)
head2.next.next.next = Node(8)

def printList(head):
    cur = head
    vals = []
    while cur:
        vals.append(str(cur.data))
        cur = cur.next
    print(" -> ".join(vals) if vals else "empty")


printList(dedupSortedList(head1))
printList(dedupSortedList(head2))