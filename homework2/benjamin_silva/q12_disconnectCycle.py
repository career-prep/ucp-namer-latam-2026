# Technique: fast-slow two-pointer
# Time Complexity: O(n)
# Space Complexity: O(1)
# Time spent: 40 min
 
from q1_singlyLinkedList import Node, insertAtBack
 
 
def disconnect_cycle(head):
    if head is None:
        return head

    has_cycle = False
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            has_cycle = True
            break
    
    if not has_cycle:
        return head
        
    
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    tail = slow
    while tail.next != slow:
        tail = tail.next

    tail.next = None

    return head
 
 
def build_list_with_cycle(values, cycle_pos=-1):
    if not values:
        return None
    head = None
    nodes = []
    for v in values:
        head = insertAtBack(head, v)
    curr = head
    while curr:
        nodes.append(curr)
        curr = curr.next
    if cycle_pos >= 0:
        nodes[-1].next = nodes[cycle_pos]
    return head
 
 
def to_list_safe(head, limit=20):
    result = []
    curr = head
    while curr and len(result) < limit:
        result.append(curr.data)
        curr = curr.next
    return result
 
 
head = build_list_with_cycle([10, 18, 12, 9, 11, 4], cycle_pos=-1)
disconnect_cycle(head)
print(to_list_safe(head))  # expected [10, 18, 12, 9, 11, 4]

head = build_list_with_cycle([1, 2, 3, 4, 5], cycle_pos=0)
disconnect_cycle(head)
print(to_list_safe(head))  # expected [1, 2, 3, 4, 5]

head = build_list_with_cycle([42], cycle_pos=-1)
disconnect_cycle(head)
print(to_list_safe(head))  # expected [42]

head = build_list_with_cycle([42], cycle_pos=0)
disconnect_cycle(head)
print(to_list_safe(head))  # expected [42]