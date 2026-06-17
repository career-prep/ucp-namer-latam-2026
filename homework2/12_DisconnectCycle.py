# Technique: Linked list fast-slow two-pointer
# Time: O(n)
# Space: O(1)
# Time Spent: 30 minutes


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def disconnectCycle(head):
    if not head:
        return head

    slow = head
    fast = head

    has_cycle = False

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            has_cycle = True
            break

    if not has_cycle:
        return head

    slow = head
    prev = None

    while slow != fast:
        prev = fast
        slow = slow.next
        fast = fast.next

    while fast.next != slow:
        fast = fast.next

    fast.next = None

    return head


def printList(head, limit=20):
    curr = head
    count = 0
    while curr and count < limit:
        print(curr.data, end=" -> ")
        curr = curr.next
        count += 1
    print("None")


head = Node(10)
n2 = Node(18)
n3 = Node(12)
n4 = Node(9)
n5 = Node(11)
n6 = Node(4)

head.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n3

head = disconnectCycle(head)
printList(head)


head2 = Node(10)
m2 = Node(18)
m3 = Node(12)
m4 = Node(9)
m5 = Node(11)
m6 = Node(4)

head2.next = m2
m2.next = m3
m3.next = m4
m4.next = m5
m5.next = m6
m6.next = m6

head2 = disconnectCycle(head2)
printList(head2)