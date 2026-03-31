# Technique: Linked list fast-slow two-pointer (Floyd's cycle detection)
# Time Complexity: O(n) - detection O(n), finding cycle start O(n)
# Space Complexity: O(1) - no extra storage
 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
 
def disconnect_cycle(head):
    if head is None or head.next is None:
        return head
 
    slow = head
    fast = head
 
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            break
    else:
        return head 
 
    slow = head
    while slow is not fast:
        slow = slow.next
        fast = fast.next
    cycle_start = slow
 
    prev = cycle_start
    while prev.next is not cycle_start:
        prev = prev.next
 
    prev.next = None
    return head

def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False

def list_to_array(head):
    result, seen = [], set()
    while head and id(head) not in seen:
        seen.add(id(head))
        result.append(head.data)
        head = head.next
    return result
 
 
n1 = [Node(v) for v in [10, 18, 12, 9, 11, 4]]
for i in range(len(n1) - 1): n1[i].next = n1[i + 1]
n1[5].next = n1[2]
disconnect_cycle(n1[0])
print(has_cycle(n1[0]))     
print(list_to_array(n1[0]))   
 
n2 = [Node(v) for v in [1, 2, 3, 4]]
for i in range(len(n2) - 1): n2[i].next = n2[i + 1]
n2[3].next = n2[3]
disconnect_cycle(n2[0])
print(has_cycle(n2[0]))     
print(list_to_array(n2[0]))    
 
n3 = [Node(v) for v in [1, 2, 3]]
for i in range(len(n3) - 1): n3[i].next = n3[i + 1]
disconnect_cycle(n3[0])
print(has_cycle(n3[0]))         
print(list_to_array(n3[0]))    
 
print(disconnect_cycle(None))   