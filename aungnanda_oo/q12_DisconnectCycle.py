# Question 12: DisconnectCycle

# Given a singly linked list, disconnect the cycle if one exists.
# If there is no cycle, do nothing.

# Time Complexity = O(n) — Floyd's cycle detection (fast/slow pointers)
# Space Complexity = O(1) — only pointer variables

# Examples:

# Input:  1->2->3->4->5->3 (cycle: 5 points back to 3)
# Output: 1->2->3->4->5 (5.next = None, cycle disconnected)

# Input:  1->2->3->4->5 (no cycle)
# Output: 1->2->3->4->5 (unchanged)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def build_list(vals):
    if not vals:
        return None
    head = Node(vals[0])
    cur = head
    for v in vals[1:]:
        cur.next = Node(v)
        cur = cur.next
    return head


def list_to_str(head, limit=20):
    result = []
    cur = head
    count = 0
    while cur and count < limit:
        result.append(str(cur.data))
        cur = cur.next
        count += 1
    return "->".join(result) if result else "[]"


def DisconnectCycle(head):
    if not head or not head.next:
        return head

    # Phase 1: detect cycle using Floyd's algorithm
    slow = head
    fast = head
    has_cycle = False

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            has_cycle = True
            break

    if not has_cycle:
        return head

    # Phase 2: find the start of the cycle
    # Reset slow to head; advance both one step at a time
    slow = head
    while slow is not fast:
        slow = slow.next
        fast = fast.next
    # slow (== fast) is now at the cycle start node

    # Phase 3: find the node just before the cycle start (the tail of the cycle)
    # Walk from cycle start until next == cycle start
    cycle_start = slow
    tail = cycle_start
    while tail.next is not cycle_start:
        tail = tail.next

    # Disconnect the cycle
    tail.next = None

    return head


# --- Tests ---

# Test 1: cycle at node 3 (index 2)
head = build_list([1, 2, 3, 4, 5])
cycle_node = head.next.next  # node with value 3
tail = head
while tail.next:
    tail = tail.next
tail.next = cycle_node  # 5 -> 3, creates cycle
DisconnectCycle(head)
print("Test 1 output:", list_to_str(head))  # 1->2->3->4->5

# Test 2: no cycle
head = build_list([1, 2, 3, 4, 5])
DisconnectCycle(head)
print("Test 2 output:", list_to_str(head))  # 1->2->3->4->5

# Test 3: cycle at head (tail points to head)
head = build_list([1, 2, 3])
tail = head
while tail.next:
    tail = tail.next
tail.next = head  # 3 -> 1, whole list is a cycle
DisconnectCycle(head)
print("Test 3 output:", list_to_str(head))  # 1->2->3

# Test 4: single node, no cycle
head = build_list([42])
DisconnectCycle(head)
print("Test 4 output:", list_to_str(head))  # 42

# Test 5: two nodes cycle
head = build_list([1, 2])
head.next.next = head  # 2 -> 1
DisconnectCycle(head)
print("Test 5 output:", list_to_str(head))  # 1->2

# Spent a total of 30 mins on this question
