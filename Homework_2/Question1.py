# Implement a singly linked list with the following methods:
# insertAtFront, insertAtBack, insertAfter, insertBefore,
# deleteFront, deleteBack, deleteNode, length,
# reverseIterative, reverseRecursive.
# Use a Node struct with data and next fields.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insert_at_front(head, val):
    new_node = Node(val)
    new_node.next = head
    return new_node


def insert_at_back(head, val):
    new_node = Node(val)
    if head is None:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head


def insert_after(head, val, loc):
    new_node = Node(val)
    new_node.next = loc.next
    loc.next = new_node
    return head


def insert_before(head, val, loc):
    new_node = Node(val)
    if head is loc:
        new_node.next = head
        return new_node
    current = head
    while current.next is not loc:
        current = current.next
    new_node.next = loc
    current.next = new_node
    return head


def delete_front(head):
    if head is None:
        return None
    return head.next


def delete_back(head):
    if head is None:
        return None
    if head.next is None:
        return None
    current = head
    while current.next.next:
        current = current.next
    current.next = None
    return head


def delete_node(head, loc):
    if head is loc:
        return head.next
    current = head
    while current.next is not loc:
        current = current.next
    current.next = loc.next
    return head


def length(head):
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    return count


def reverse_iterative(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


def reverse_recursive(head):
    def helper(node, prev):
        if node is None:
            return prev
        next_node = node.next
        node.next = prev
        return helper(next_node, node)
    return helper(head, None)


def to_list(head):
    result = []
    current = head
    while current:
        result.append(current.data)
        current = current.next
    return result


head = None
head = insert_at_front(head, 3)
head = insert_at_front(head, 2)
head = insert_at_front(head, 1)
print(to_list(head))

head = insert_at_back(head, 4)
print(to_list(head))

loc = head.next
head = insert_after(head, 10, loc)
print(to_list(head))

head = insert_before(head, 0, head)
print(to_list(head))

head = delete_front(head)
print(to_list(head))

head = delete_back(head)
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
# insertAtBack: O(n)
# insertAfter: O(1)
# insertBefore: O(n)
# deleteFront: O(1)
# deleteBack: O(n)
# deleteNode: O(n)
# length: O(n)
# reverseIterative: O(n)
# reverseRecursive: O(n)
# Spent 40 mins
