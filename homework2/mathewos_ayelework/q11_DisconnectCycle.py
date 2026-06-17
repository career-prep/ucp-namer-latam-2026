# Technique used: Linked list fast-slow two-pointer (Floyd's cycle detection)
# Time Complexity: O(n)
# Space Complexity: O(1)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def disconnectCycle(head):
    if not head or not head.next:
        return head

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    if not fast or not fast.next:
        return head

    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    cycle_start = slow

    curr = cycle_start
    while curr.next != cycle_start:
        curr = curr.next
    curr.next = None

    return head


def printList(head):
    result = []
    curr = head
    while curr:
        result.append(str(curr.data))
        curr = curr.next
    print(" -> ".join(result))


print("disconnectCycle Results:")

n1, n2, n3, n4, n5, n6 = Node(10), Node(18), Node(12), Node(9), Node(11), Node(4)
n1.next = n2; n2.next = n3; n3.next = n4; n4.next = n5; n5.next = n6; n6.next = n3
printList(disconnectCycle(n1))

m1, m2, m3, m4, m5, m6 = Node(10), Node(18), Node(12), Node(9), Node(11), Node(4)
m1.next = m2; m2.next = m3; m3.next = m4; m4.next = m5; m5.next = m6; m6.next = m6
printList(disconnectCycle(m1))

p1, p2, p3 = Node(1), Node(2), Node(3)
p1.next = p2; p2.next = p3
printList(disconnectCycle(p1))

# Time Taken: 37 mins
