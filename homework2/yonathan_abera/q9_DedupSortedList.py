# Technique: Linked list reset/catch-up two-pointer
# Time Complexity: O(n) - single pass through list
# Space Complexity: O(1) - in-place, no extra storage
 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
 
def dedup_sorted_list(head):
    current = head
    while current and current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
    return head

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
 
 
print(list_to_array(dedup_sorted_list(make_list([1, 2, 2, 4, 5, 5, 5, 10, 10]))))
print(list_to_array(dedup_sorted_list(make_list([8, 8, 8, 8]))))                
print(list_to_array(dedup_sorted_list(make_list([1, 2, 3, 4]))))                
print(list_to_array(dedup_sorted_list(make_list([3, 3]))))                      
print(list_to_array(dedup_sorted_list(make_list([7]))))                     
print(list_to_array(dedup_sorted_list(make_list([]))))