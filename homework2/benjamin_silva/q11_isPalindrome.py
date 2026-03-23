# Technique: doubly linked list forward backward 2 pointer
# Time Complexity: O(n)
# Space Complexity: O(1)
# Time spent: 20 minutes

from q2_doublyLinkedList import Node


def is_palindrome(head):
    if head is None or head.next is None:
        return True
    
    left = head
    right = head

    while right.next:
        right = right.next

    while left != right and left.prev != right:
        if left.data != right.data:
            return False
        left = left.next
        right = right.next
    
    return True


def build_dlist(values):
    if not values:
        return None
    head = Node(values[0])
    curr = head
    for v in values[1:]:
        new_node = Node(v)
        new_node.prev = curr
        curr.next = new_node
        curr = curr.next
    return head

head = build_dlist([9, 2, 4, 2, 9])
print(is_palindrome(head))  # expected True

head = build_dlist([9, 12, 4, 2, 9])
print(is_palindrome(head))  # expected False