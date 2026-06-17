# Technique: Linked List technique (not sure if it aligns with any)

# Time Complexity: O(N)
# Space Complexity: O(1)

# Time taken: 10 minutes

from q0_singly_linked_list import display, Node, insertAtBack

def dedup_sorted_list(head):
    # returns a singly linked list with no duplicate values,
    # given a sorted linked list with duplicate values   
    cur = head
    while cur and cur.next:
        if cur.data == cur.next.data:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head

if __name__ == "__main__":
    head = Node(1)
    insertAtBack(head, 2)
    insertAtBack(head, 2)
    insertAtBack(head, 4)
    insertAtBack(head, 5)
    insertAtBack(head, 5)
    insertAtBack(head, 5)
    insertAtBack(head, 6)
    insertAtBack(head, 7)
    insertAtBack(head, 10)
    insertAtBack(head, 10)
    insertAtBack(head, 10)
    display(head)
    head = dedup_sorted_list(head)
    display(head)

