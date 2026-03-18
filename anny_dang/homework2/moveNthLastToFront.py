class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def moveNthLastToFront(head, n):
    """
    Given a singly linked list, move the nth-from-last node
    to the front of the list.
    Return the head.

    Time: O(n)
    Space: O(1)
    """

    "assume that n always <= length of head"

    if not head or not head.next:
        return head

    length = 0
    cur = head
    while cur:
        length += 1
        cur = cur.next

    idx = length - n + 1
    if idx == 1:
        return head

    prev = None
    cur = head
    i = 1
    while i < idx:
        prev = cur
        cur = cur.next
        i += 1

    prev.next = cur.next
    cur.next = head
    return cur


# Example 1
# Input: k = 2
# 15 -> 2 -> 8 -> 7 -> 20 -> 9 -> 11 -> 6 -> 19
# Expected Output:
# 6 -> 15 -> 2 -> 8 -> 7 -> 20 -> 9 -> 11 -> 19
k1 = 2
head1 = Node(15)
head1.next = Node(2)
head1.next.next = Node(8)
head1.next.next.next = Node(7)
head1.next.next.next.next = Node(20)
head1.next.next.next.next.next = Node(9)
head1.next.next.next.next.next.next = Node(11)
head1.next.next.next.next.next.next.next = Node(6)
head1.next.next.next.next.next.next.next.next = Node(19)


# Example 2
# Input: k = 7
# 15 -> 2 -> 8 -> 7 -> 20 -> 9 -> 11 -> 6 -> 19
# Expected Output:
# 8 -> 15 -> 2 -> 7 -> 20 -> 9 -> 11 -> 6 -> 19
k2 = 7
head2 = Node(15)
head2.next = Node(2)
head2.next.next = Node(8)
head2.next.next.next = Node(7)
head2.next.next.next.next = Node(20)
head2.next.next.next.next.next = Node(9)
head2.next.next.next.next.next.next = Node(11)
head2.next.next.next.next.next.next.next = Node(6)
head2.next.next.next.next.next.next.next.next = Node(19)

def printList(head):
    cur = head
    vals = []
    while cur:
        vals.append(str(cur.data))
        cur = cur.next
    print(" -> ".join(vals) if vals else "empty")

printList(moveNthLastToFront(head1, k1))
printList(moveNthLastToFront(head2, k2))
