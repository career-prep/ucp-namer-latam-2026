class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
def insert_at_front(head, val):
    new_node = Node(val) 
    if head is not None: 
        head.prev = new_node
        new_node.next = head 
    head = new_node 
    return new_node 

def display(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" <-> ")
        curr = curr.next
    print("None")

def IsPalindrome(head):
    if not head or not head.next:
        return True

    left = head
    right = head
    while right.next:
        right = right.next

    while left != right and left.prev != right:
        if left.data != right.data:
            return False
        left = left.next
        right = right.prev
        
    return True

def build_list(values):
    head = None
    for v in reversed(values):
        head = insert_at_front(head, v)
    return head

list1 = build_list([1, 2, 2, 1])
print("List 1: ", end="")
display(list1)
print(f"Is Palindrome? {IsPalindrome(list1)}")

list2 = build_list([1, 2, 3, 2, 1])
print("\nList 2: ", end="")
display(list2)
print(f"Is Palindrome? {IsPalindrome(list2)}")

list3 = build_list([1, 2, 3, 4])
print("\nList 3: ", end="")
display(list3)
print(f"Is Palindrome? {IsPalindrome(list3)}")

list4 = build_list([5])
print("\nList 4: ", end="")
display(list4)
print(f"Is Palindrome? {IsPalindrome(list4)}")

print("\nList 5 (Empty): ", end="")
display(None)
print(f"Is Palindrome? {IsPalindrome(None)}")

# Technique: Doubly linked list forward-backward two-pointer
# Time Complexity: O(n)
# Space Complexity: O(1) 
# Time Spent: 40 minutes