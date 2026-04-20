# Question 12: DisconnectCycle
# Technique: Linked list fast-slow two-pointer
# Time: O(n)
# Space: O(1)

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

    while slow != fast:
        slow = slow.next
        fast = fast.next

    cycle_start = slow
    current = cycle_start

    while current.next != cycle_start:
        current = current.next

    current.next = None
    return head


def print_list(head):
    result = []
    while head:
        result.append(head.data)
        head = head.next
    print(result)


# Example 1: 10→18→12→9→11→4, 4→12 (cycle)
# Expected: [10,18,12,9,11,4]
n1 = Node(10)
n2 = Node(18)
n3 = Node(12)
n4 = Node(9)
n5 = Node(11)
n6 = Node(4)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n3

disconnectCycle(n1)
print_list(n1)

# Example 2: 10→18→12→9→11→4, 4→4 (self-loop)
# Expected: [10,18,12,9,11,4]
m1 = Node(10)
m2 = Node(18)
m3 = Node(12)
m4 = Node(9)
m5 = Node(11)
m6 = Node(4)
m1.next = m2
m2.next = m3
m3.next = m4
m4.next = m5
m5.next = m6
m6.next = m6

disconnectCycle(m1)
print_list(m1)

# time: 32 minutes
