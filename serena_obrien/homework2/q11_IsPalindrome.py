# Time complexity: O(n)
# Space complexity: O(1)

# Technique: Doubly linked list forward-backward two-pointer

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def insertAtFront(head, val):
    newNode = Node(val)

    if head:
        newNode.next = head
        head.prev = newNode

    return newNode

def print_list(head):
    curr = head
    while curr:
        print(curr.data, end="->" if curr.next else "")
        curr = curr.next
    print()

def IsPalindrome(head):
    if head is None:
        return True
    
    tail = head
    while tail.next:
        tail = tail.next

    while head != tail and head.prev != tail:
        if head.data != tail.data:
            return False
        head = head.next
        tail = tail.prev

    return True

if __name__ == '__main__':
    # Palindrome list: 1->2->3->2->1
    head = None
    for val in [1, 2, 3, 2, 1]:
        head = insertAtFront(head, val)
    
    print("List:")
    print_list(head)
    print("Is palindrome?", IsPalindrome(head))  # True

    # Non-palindrome list: 1->2->3
    head2 = None
    for val in [3, 2, 1]:
        head2 = insertAtFront(head2, val)
    
    print("List:")
    print_list(head2)
    print("Is palindrome?", IsPalindrome(head2))  # False

    # Single element
    head3 = Node(5)
    print("List:")
    print_list(head3)
    print("Is palindrome?", IsPalindrome(head3))  # True

    # Empty list
    print("List: None")
    print("Is palindrome?", IsPalindrome(None))  # True
    
# ~ time spent: 30 minutes
