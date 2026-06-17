# Technique: Linked list fixed-distance two-pointer
# Time Complexity: O(n) - single pass to find the node, O(1) to move it
# Space Complexity: O(1) - in-place
 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
 
def move_nth_last_to_front(head, k):
    if head is None or head.next is None:
        return head
 
    dummy = Node(0)
    dummy.next = head
 
    fast = dummy
    for _ in range(k):
        fast = fast.next

    slow = dummy
    while fast.next is not None:
        slow = slow.next
        fast = fast.next
 
    target = slow.next

    slow.next = target.next
 
    target.next = dummy.next
    dummy.next = target
 
    return dummy.next

def make_list(values):
    if not values:
        return None
    head = Node(values[0])
    cur = head
    for v in values[1:]:
        cur.next = Node(v)
        cur = cur.next
    return head
 
 
def list_to_array(head):
    result = []
    while head:
        result.append(head.data)
        head = head.next
    return result
 
 
print(list_to_array(move_nth_last_to_front(make_list([15, 2, 8, 7, 20, 9, 11, 6, 19]), 2))) 
print(list_to_array(move_nth_last_to_front(make_list([15, 2, 8, 7, 20, 9, 11, 6, 19]), 7)))  
print(list_to_array(move_nth_last_to_front(make_list([1, 2, 3, 4, 5]), 1)))                 
print(list_to_array(move_nth_last_to_front(make_list([1, 2, 3, 4, 5]), 5)))                  
print(list_to_array(move_nth_last_to_front(make_list([10, 20]), 2)))                         
print(list_to_array(move_nth_last_to_front(make_list([42]), 1)))                            
 