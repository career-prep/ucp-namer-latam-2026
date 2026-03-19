# Question 2: Doubly Linked List

# Copy-paste and modify the singly linked list. The Node struct has an additional prev reference.

# Examples:

# insertAtFront([1<->2<->3], 0) -> [0<->1<->2<->3]
# insertAtBack([1<->2<->3], tail, 4) -> [1<->2<->3<->4]
# insertAfter([1<->2<->3], 99, node_2) -> [1<->2<->99<->3]
# insertBefore([1<->2<->3], 99, node_2) -> [1<->99<->2<->3]
# deleteFront([1<->2<->3]) -> [2<->3]
# deleteBack([1<->2<->3], tail) -> [1<->2]
# deleteNode([1<->2<->3], node_2) -> [1<->3]
# length([1<->2<->3]) -> 3
# reverseIterative([1<->2<->3]) -> [3<->2<->1]
# reverseRecursive([1<->2<->3]) -> [3<->2<->1]


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# Helper to build a doubly linked list; returns (head, tail)
def build_list(vals):
    if not vals:
        return None, None
    head = Node(vals[0])
    cur = head
    for v in vals[1:]:
        new_node = Node(v)
        new_node.prev = cur
        cur.next = new_node
        cur = cur.next
    return head, cur


# Helper to print list forward
def list_to_str(head):
    result = []
    cur = head
    while cur:
        result.append(str(cur.data))
        cur = cur.next
    return "<->".join(result) if result else "[]"


def insertAtFront(head, val):
    new_node = Node(val)
    if head:
        new_node.next = head
        head.prev = new_node
    return new_node
# Time Complexity = O(1), Space Complexity = O(1)


def insertAtBack(head, tail, val):
    new_node = Node(val)
    if not tail:
        return new_node, new_node
    tail.next = new_node
    new_node.prev = tail
    return head, new_node
# Time Complexity = O(1), Space Complexity = O(1)


def insertAfter(head, val, loc):
    new_node = Node(val)
    new_node.next = loc.next
    new_node.prev = loc
    if loc.next:
        loc.next.prev = new_node
    loc.next = new_node
    return head
# Time Complexity = O(1), Space Complexity = O(1)


def insertBefore(head, val, loc):
    new_node = Node(val)
    new_node.next = loc
    new_node.prev = loc.prev
    if loc.prev:
        loc.prev.next = new_node
    else:
        head = new_node
    loc.prev = new_node
    return head
# Time Complexity = O(1), Space Complexity = O(1)


def deleteFront(head):
    if not head:
        return None
    head = head.next
    if head:
        head.prev = None
    return head
# Time Complexity = O(1), Space Complexity = O(1)


def deleteBack(head, tail):
    if not tail:
        return None, None
    if not tail.prev:
        return None, None
    new_tail = tail.prev
    new_tail.next = None
    return head, new_tail
# Time Complexity = O(1), Space Complexity = O(1)


def deleteNode(head, loc):
    if loc.prev:
        loc.prev.next = loc.next
    else:
        head = loc.next
    if loc.next:
        loc.next.prev = loc.prev
    return head
# Time Complexity = O(1), Space Complexity = O(1)


def length(head):
    count = 0
    cur = head
    while cur:
        count += 1
        cur = cur.next
    return count
# Time Complexity = O(n), Space Complexity = O(1)


def reverseIterative(head):
    cur = head
    new_head = None
    while cur:
        cur.prev, cur.next = cur.next, cur.prev
        new_head = cur
        cur = cur.prev  # prev now points to what was next
    return new_head
# Time Complexity = O(n), Space Complexity = O(1)


def reverseRecursive(head):
    def helper(cur):
        if not cur:
            return None
        cur.prev, cur.next = cur.next, cur.prev
        if not cur.prev:  # prev now points to original next
            return cur
        return helper(cur.prev)
    return helper(head)
# Time Complexity = O(n), Space Complexity = O(n) call stack


# --- Tests ---

head, tail = build_list([1, 2, 3])
print("Original:", list_to_str(head))

head = insertAtFront(head, 0)
print("insertAtFront(0):", list_to_str(head))           # 0<->1<->2<->3

head, tail = insertAtBack(head, tail, 4)
print("insertAtBack(4):", list_to_str(head))             # 0<->1<->2<->3<->4

# insertAfter node with value 2
cur = head
while cur.data != 2:
    cur = cur.next
head = insertAfter(head, 99, cur)
print("insertAfter(99, node_2):", list_to_str(head))     # 0<->1<->2<->99<->3<->4

# insertBefore node with value 1
cur = head
while cur.data != 1:
    cur = cur.next
head = insertBefore(head, 88, cur)
print("insertBefore(88, node_1):", list_to_str(head))    # 0<->88<->1<->2<->99<->3<->4

head = deleteFront(head)
print("deleteFront:", list_to_str(head))                 # 88<->1<->2<->99<->3<->4

# rebuild tail reference
cur = head
while cur.next:
    cur = cur.next
tail = cur
head, tail = deleteBack(head, tail)
print("deleteBack:", list_to_str(head))                  # 88<->1<->2<->99<->3

# deleteNode node with value 99
cur = head
while cur.data != 99:
    cur = cur.next
head = deleteNode(head, cur)
print("deleteNode(99):", list_to_str(head))              # 88<->1<->2<->3

print("length:", length(head))                           # 4

head = reverseIterative(head)
print("reverseIterative:", list_to_str(head))            # 3<->2<->1<->88

head = reverseRecursive(head)
print("reverseRecursive:", list_to_str(head))            # 88<->1<->2<->3

# Spent a total of 20 mins on this question
