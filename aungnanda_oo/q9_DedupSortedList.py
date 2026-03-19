# Question 9: DedupSortedList

# Given a sorted singly linked list, remove any duplicates so that no value appears more than once.

# Time Complexity = O(n) — single pass through the list
# Space Complexity = O(1) — in-place pointer manipulation

# Examples:

# Input:  1->1->2->3->3->3->4->5->5
# Output: 1->2->3->4->5

# Input:  1->1->1->1
# Output: 1


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


def list_to_str(head):
    result = []
    cur = head
    while cur:
        result.append(str(cur.data))
        cur = cur.next
    return "->".join(result) if result else "[]"


def DedupSortedList(head):
    cur = head
    while cur and cur.next:
        if cur.data == cur.next.data:
            cur.next = cur.next.next  # skip duplicate
        else:
            cur = cur.next
    return head


# --- Tests ---

# Test 1: multiple duplicates
head = build_list([1, 1, 2, 3, 3, 3, 4, 5, 5])
print("Test 1 input: ", list_to_str(head))
print("Test 1 output:", list_to_str(DedupSortedList(head)))  # 1->2->3->4->5

# Test 2: all same
head = build_list([1, 1, 1, 1])
print("Test 2 input: ", list_to_str(head))
print("Test 2 output:", list_to_str(DedupSortedList(head)))  # 1

# Test 3: no duplicates
head = build_list([1, 2, 3, 4])
print("Test 3 input: ", list_to_str(head))
print("Test 3 output:", list_to_str(DedupSortedList(head)))  # 1->2->3->4

# Test 4: single element
head = build_list([7])
print("Test 4 input: ", list_to_str(head))
print("Test 4 output:", list_to_str(DedupSortedList(head)))  # 7

# Test 5: empty
print("Test 5 output:", list_to_str(DedupSortedList(None))) # []

# Spent a total of 15 mins on this question
