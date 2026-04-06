# Technique: Linked list fixed-distance two-pointer
# Time: O(n)
# Space: O(1)
# Time Spent: 30 minutes


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def moveNthLastToFront(head, k):
    if not head or k <= 0:
        return head

    fast = head
    slow = head

    for _ in range(k):
        if not fast:
            return head
        fast = fast.next

    prev = None
    while fast:
        fast = fast.next
        prev = slow
        slow = slow.next

    if not slow or slow == head:
        return head

    prev.next = slow.next
    slow.next = head

    return slow


def printList(head):
    curr = head
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("None")


head = Node(15)
head.next = Node(2)
head.next.next = Node(8)
head.next.next.next = Node(7)
head.next.next.next.next = Node(20)
head.next.next.next.next.next = Node(9)
head.next.next.next.next.next.next = Node(11)
head.next.next.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next.next.next = Node(19)

head = moveNthLastToFront(head, 2)
printList(head)

head = moveNthLastToFront(head, 7)
printList(head)