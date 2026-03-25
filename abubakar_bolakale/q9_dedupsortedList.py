class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        

def insert_at_front(head, val):
    new_node = Node(val)  
    new_node.next = head  
    return new_node

def dedupsorted(head):
    curr = head
    
    while curr and curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next
        
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


head = build_sorted_list([1, 2, 2, 4, 5, 5, 5, 10, 10])
print("Original List: ", end="")
display(head)
head = dedupsorted(head)
print("Sorted List With no duplicate: ", end="")
display(head)

print("\nEdge Case 1 (Empty List): ", end="")
head = build_sorted_list([])
display(dedupsorted(head))

print("Edge Case 2 (Single Node): ", end="")
head = build_sorted_list([7])
display(dedupsorted(head))

print("Edge Case 3 (All Duplicates): ", end="")
head = build_sorted_list([3, 3, 3, 3, 3])
display(dedupsorted(head))

print("Edge Case 4 (No Duplicates): ", end="")
head = build_sorted_list([1, 2, 3, 4, 5])
display(dedupsorted(head))

print("Edge Case 5 (Duplicates at Start/End): ", end="")
head = build_sorted_list([1, 1, 2, 3, 4, 5, 5])
display(dedupsorted(head))

# Technique: Linked List Reset/Catch-up Two-Pointer (Modified)
# Time Complexity: O(n)
# Space Complexity: O(1)
# Time Spent: 30 minutes