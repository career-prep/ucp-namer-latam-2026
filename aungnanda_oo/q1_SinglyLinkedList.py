# Question 1: Singly Linked List

# Implement linked list operations using a Node struct representing the head of the list.
# Nodes store integers.

# Examples:

# insertAtFront([1->2->3], 0) -> [0->1->2->3]
# insertAtBack([1->2->3], 4) -> [1->2->3->4]
# insertAfter([1->2->3], 99, node_2) -> [1->2->99->3]
# insertBefore([1->2->3], 99, node_2) -> [1->99->2->3]
# deleteFront([1->2->3]) -> [2->3]
# deleteBack([1->2->3]) -> [1->2]
# deleteNode([1->2->3], node_2) -> [1->3]
# length([1->2->3]) -> 3
# reverseIterative([1->2->3]) -> [3->2->1]
# reverseRecursive([1->2->3]) -> [3->2->1]


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Helper to build a list from a Python list and return head
def build_list(vals):
    if not vals:
        return None
    head = Node(vals[0])
    cur = head
    for v in vals[1:]:
        cur.next = Node(v)
        cur = cur.next
    return head


# Helper to print a list as a string
def list_to_str(head):
    result = []
    cur = head
    while cur:
        result.append(str(cur.data))
        cur = cur.next
    return "->".join(result) if result else "[]"


def insertAtFront(head, val):
    new_node = Node(val)
    new_node.next = head
    return new_node
# Time Complexity = O(1), Space Complexity = O(1)


def insertAtBack(head, val):
    new_node = Node(val)
    if not head:
        return new_node
    cur = head
    while cur.next:
        cur = cur.next
    cur.next = new_node
    return head
# Time Complexity = O(n), Space Complexity = O(1)


def insertAfter(head, val, loc):
    new_node = Node(val)
    new_node.next = loc.next
    loc.next = new_node
    return head
# Time Complexity = O(1), Space Complexity = O(1)


def insertBefore(head, val, loc):
    new_node = Node(val)
    if head is loc:
        new_node.next = head
        return new_node
    cur = head
    while cur.next and cur.next is not loc:
        cur = cur.next
    new_node.next = cur.next
    cur.next = new_node
    return head
# Time Complexity = O(n), Space Complexity = O(1)


def deleteFront(head):
    if not head:
        return None
    return head.next
# Time Complexity = O(1), Space Complexity = O(1)


def deleteBack(head):
    if not head or not head.next:
        return None
    cur = head
    while cur.next.next:
        cur = cur.next
    cur.next = None
    return head
# Time Complexity = O(n), Space Complexity = O(1)


def deleteNode(head, loc):
    if head is loc:
        return head.next
    cur = head
    while cur.next and cur.next is not loc:
        cur = cur.next
    if cur.next:
        cur.next = cur.next.next
    return head
# Time Complexity = O(n), Space Complexity = O(1)


def length(head):
    count = 0
    cur = head
    while cur:
        count += 1
        cur = cur.next
    return count
# Time Complexity = O(n), Space Complexity = O(1)


def reverseIterative(head):
    prev = None
    cur = head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev
# Time Complexity = O(n), Space Complexity = O(1)


def reverseRecursive(head):
    def helper(cur, prev):
        if not cur:
            return prev
        nxt = cur.next
        cur.next = prev
        return helper(nxt, cur)
    return helper(head, None)
# Time Complexity = O(n), Space Complexity = O(n) call stack


# --- Tests ---

head = build_list([1, 2, 3])
print("Original:", list_to_str(head))

head = insertAtFront(head, 0)
print("insertAtFront(0):", list_to_str(head))         # 0->1->2->3

head = insertAtBack(head, 4)
print("insertAtBack(4):", list_to_str(head))           # 0->1->2->3->4

# insertAfter node with value 2
cur = head
while cur.data != 2:
    cur = cur.next
head = insertAfter(head, 99, cur)
print("insertAfter(99, node_2):", list_to_str(head))   # 0->1->2->99->3->4

# insertBefore node with value 1
cur = head
while cur.data != 1:
    cur = cur.next
head = insertBefore(head, 88, cur)
print("insertBefore(88, node_1):", list_to_str(head))  # 0->88->1->2->99->3->4

head = deleteFront(head)
print("deleteFront:", list_to_str(head))               # 88->1->2->99->3->4

head = deleteBack(head)
print("deleteBack:", list_to_str(head))                # 88->1->2->99->3

# deleteNode node with value 99
cur = head
while cur.data != 99:
    cur = cur.next
head = deleteNode(head, cur)
print("deleteNode(99):", list_to_str(head))            # 88->1->2->3

print("length:", length(head))                         # 4

head = reverseIterative(head)
print("reverseIterative:", list_to_str(head))          # 3->2->1->88

head = reverseRecursive(head)
print("reverseRecursive:", list_to_str(head))          # 88->1->2->3

# Spent a total of 40 mins on this question
