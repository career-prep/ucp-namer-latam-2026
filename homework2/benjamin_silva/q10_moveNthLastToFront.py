# Technique: fixed distance two pointer
# Time Complexity: O(n)
# Space Complexity: O(1)
# Time spent: 30 minutes

from q1_singlyLinkedList import Node, insertAtBack

def move_nth_last_to_front(head, k):
    dummy = Node(0)
    dummy.next = head
    left = dummy
    right = head

    while k > 0 and right:
        right = right.next
        k -= 1
    
    while right:
        left = left.next
        right = right.next
    
    # if left.next is None:
    #     return dummy.next
    
    node_to_move = left.next

    left.next = node_to_move.next

    node_to_move.next = dummy.next

    dummy.next = node_to_move

    return dummy.next
 
 
 
def build_list(values):
    head = None
    for v in values:
        head = insertAtBack(head, v)
    return head
 
 
def to_list(head):
    result = []
    curr = head
    while curr:
        result.append(curr.data)
        curr = curr.next
    return result
 
 
head = build_list([15, 2, 8, 7, 20, 9, 11, 6, 19])
print(to_list(move_nth_last_to_front(head, 2)))  # expected [6, 15, 2, 8, 7, 20, 9, 11, 19]

head = build_list([15, 2, 8, 7, 20, 9, 11, 6, 19])
print(to_list(move_nth_last_to_front(head, 7)))  # expected [8, 15, 2, 7, 20, 9, 11, 6, 19]

head = build_list([1, 2, 3, 4, 5])
print(to_list(move_nth_last_to_front(head, 1)))  # expected [5, 1, 2, 3, 4]