# Implement a doubly linked list with the following methods:
# insertAtFront, insertAtBack, insertAfter, insertBefore,
# deleteFront, deleteBack, deleteNode, length,
# reverseIterative, reverseRecursive.
# Use a Node struct with data, next, and prev fields.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def insert_at_front(head, val):
    new_node = Node(val)
    new_node.next = head
    if head:
        head.prev = new_node
    return new_node


def insert_at_back(head, tail, val):
    new_node = Node(val)
    if tail is None:
        return new_node
    tail.next = new_node
    new_node.prev = tail
    return head


def insert_after(head, val, loc):
    new_node = Node(val)
    new_node.next = loc.next
    new_node.prev = loc
    if loc.next:
        loc.next.prev = new_node
    loc.next = new_node
    return head


def insert_before(head, val, loc):
    new_node = Node(val)
    new_node.next = loc
    new_node.prev = loc.prev
    if loc.prev:
        loc.prev.next = new_node
    else:
        head = new_node
    loc.prev = new_node
    return head


def delete_front(head):
    if head is None:
        return None
    new_head = head.next
    if new_head:
        new_head.prev = None
    return new_head


def delete_back(head, tail):
    if tail is None:
        return None
    if tail.prev is None:
        return None
    tail.prev.next = None
    return head


def delete_node(head, loc):
    if loc.prev:
        loc.prev.next = loc.next
    else:
        head = loc.next
    if loc.next:
        loc.next.prev = loc.prev
    return head


def length(head):
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    return count


def reverse_iterative(head):
    current = head
    while current:
        current.prev, current.next = current.next, current.prev
        if current.prev is None:
            head = current
        current = current.prev
    return head


def reverse_recursive(head):
    def helper(node):
        if node is None:
            return None
        node.prev, node.next = node.next, node.prev
        if node.prev is None:
            return node
        return helper(node.prev)
    return helper(head)


def to_list(head):
    result = []
    current = head
    while current:
        result.append(current.data)
        current = current.next
    return result


def get_tail(head):
    if head is None:
        return None
    current = head
    while current.next:
        current = current.next
    return current


head = Node(1)
head.next = Node(2)
head.next.prev = head
head.next.next = Node(3)
head.next.next.prev = head.next
tail = head.next.next
print(to_list(head))

head = insert_at_front(head, 0)
print(to_list(head))

tail = get_tail(head)
head = insert_at_back(head, tail, 4)
print(to_list(head))

loc = head.next.next
head = insert_after(head, 10, loc)
print(to_list(head))

loc = head.next.next.next
head = insert_before(head, 5, loc)
print(to_list(head))

head = delete_front(head)
print(to_list(head))

tail = get_tail(head)
head = delete_back(head, tail)
print(to_list(head))

loc = head.next.next
head = delete_node(head, loc)
print(to_list(head))

print(length(head))

head = reverse_iterative(head)
print(to_list(head))

head = reverse_recursive(head)
print(to_list(head))

# insertAtFront: O(1)
# insertAtBack: O(1)
# insertAfter: O(1)
# insertBefore: O(1)
# deleteFront: O(1)
# deleteBack: O(1)
# deleteNode: O(1)
# length: O(n)
# reverseIterative: O(n)
# reverseRecursive: O(n)
# Spent 35 mins
