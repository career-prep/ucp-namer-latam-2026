# Technique: Linked list fast-slow two-pointer (Floyd's cycle detection)
# time complexity: O(n)
# space complexity: O(1)
# 25 minutes

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def disconnectCycle(head):
    if not head or not head.next:
        return head

    slow = head
    fast = head

    # phase 1: detect cycle
    has_cycle = False
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            has_cycle = True
            break

    if not has_cycle:
        return head

    # phase 2: find cycle entry by resetting slow to head and advancing both one step at a time
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    cycle_entry = slow

    # phase 3: find the tail (node whose next points back to cycle entry)
    tail = cycle_entry
    while tail.next != cycle_entry:
        tail = tail.next

    tail.next = None
    return head

# helpers
def to_list(head):
    result = []
    visited = set()
    curr = head
    while curr and id(curr) not in visited:
        result.append(curr.data)
        visited.add(id(curr))
        curr = curr.next
    return result

# test cases

# cycle: 10 -> 18 -> 12 -> 9 -> 11 -> 4 -> (back to 12)
n0 = Node(10)
n1 = Node(18)
n2 = Node(12)
n3 = Node(9)
n4 = Node(11)
n5 = Node(4)
n0.next = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n2  # cycle to 12
result1 = disconnectCycle(n0)
assert to_list(result1) == [10, 18, 12, 9, 11, 4]
assert n5.next is None

# cycle: 10 -> 18 -> 12 -> 9 -> 11 -> 4 -> (back to 4, self-loop)
m0 = Node(10)
m1 = Node(18)
m2 = Node(12)
m3 = Node(9)
m4 = Node(11)
m5 = Node(4)
m0.next = m1
m1.next = m2
m2.next = m3
m3.next = m4
m4.next = m5
m5.next = m5  # self-loop
result2 = disconnectCycle(m0)
assert to_list(result2) == [10, 18, 12, 9, 11, 4]
assert m5.next is None

# no cycle
p0 = Node(1)
p1 = Node(2)
p2 = Node(3)
p0.next = p1
p1.next = p2
result3 = disconnectCycle(p0)
assert to_list(result3) == [1, 2, 3]

print("yay!!")
