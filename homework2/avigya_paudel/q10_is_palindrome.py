# Technique: Doubly Linked List forward backward two pointer

# Time Complexity: O(N)
# Space Complexity: O(1)

# Time taken: 25 minutes

from q1_doubly_linked_list import Node, display, insertAtFront

def is_palindrome(head):
    # Given a doubly linked list, determine if it is a palindrome.

    tail = get_tail(head)
    start, end = head, tail
    while start != end:
        if start.data != end.data:
            return False 
        start = start.next
        end = end.prev
    return True

def get_tail(head):
    # returns the pointer to the tail of the doubly linked list
    cur = head
    while cur and cur.next:
        cur = cur.next
    return cur

if __name__ == "__main__":
    head = Node(8)
    head = insertAtFront(head, 2)
    head = insertAtFront(head, 8)
    head = insertAtFront(head, 2)
    head = insertAtFront(head, 8)
    head = insertAtFront(head, 2)
    head = insertAtFront(head, 8)
    head = insertAtFront(head, 2)
    head = insertAtFront(head, 8)
    display(head)
    print(is_palindrome(head)) 
    