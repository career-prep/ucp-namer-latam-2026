class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        

def insert_at_front(head, val):
    new_node = Node(val)  
    new_node.next = head  
    return new_node

def MoveNthLastToFront(head, k):
    if not head or not head.next or k <= 0:
        return head
    
    curr = head
    temp = head
    for i in range(k):
        if temp is None:
            return head
        temp = temp.next

    if temp is None:
        return head

    while temp.next is not None:
        temp = temp.next
        curr = curr.next
        
    target = curr.next
    curr.next = target.next
    target.next = head
    head = target
        
    return head

def display(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")    

def build_sorted_list(values):
    head = None
    for v in reversed(values):
        head = insert_at_front(head, v)
    return head


head = build_sorted_list([1, 2, 3, 4, 5])
print("Test 1 - Original List: ", end="")
display(head)
head = MoveNthLastToFront(head, 2)
print("Test 1 - After MoveNthLastToFront(k=2): ", end="")
display(head)

head = build_sorted_list([10, 20, 30, 40])
print("\nTest 2 - Original List: ", end="")
display(head)
head = MoveNthLastToFront(head, 1)
print("Test 2 - After MoveNthLastToFront(k=1, last to front): ", end="")
display(head)

print("\nEdge Case 1 (Empty List): ", end="")
head = build_sorted_list([])
display(MoveNthLastToFront(head, 1))

print("Edge Case 2 (Single Node): ", end="")
head = build_sorted_list([7])
display(MoveNthLastToFront(head, 1))

print("Edge Case 3 (k equals list length, no-op): ", end="")
head = build_sorted_list([1, 2, 3])
display(MoveNthLastToFront(head, 3))

print("Edge Case 4 (k larger than list, unchanged): ", end="")
head = build_sorted_list([1, 2, 3])
display(MoveNthLastToFront(head, 10))

print("Edge Case 5 (Two nodes, k=1): ", end="")
head = build_sorted_list([100, 200])
display(MoveNthLastToFront(head, 1))

# Technique: Fixed-distance two-pointer
# Time Complexity: O(n)
# Space Complexity: O(1)
# Time Spent: 30 minutes