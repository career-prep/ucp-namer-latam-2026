class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
 
 
def is_palindrome(head):
    if head is None:
        return True
 
    tail = head
    while tail.next is not None:
        tail = tail.next
 
    left = head
    right = tail
 
    while left != right and left.prev != right:
        if left.data != right.data:
            return False
        left = left.next
        right = right.prev
 
    return True

def make_list(values):
    if not values:
        return None
    head = Node(values[0])
    cur = head
    for v in values[1:]:
        node = Node(v)
        node.prev = cur
        cur.next = node
        cur = node
    return head
 
 
print(is_palindrome(make_list([9, 2, 4, 2, 9]))) 
print(is_palindrome(make_list([9, 12, 4, 2, 9])))  
print(is_palindrome(make_list([1, 2, 2, 1])))   
print(is_palindrome(make_list([5, 5, 5, 5])))      
print(is_palindrome(make_list([3, 4])))             
print(is_palindrome(make_list([7])))               
print(is_palindrome(None))                         