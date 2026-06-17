# Technique: Linked List technique (not sure if it aligns with any)

# Time Complexity: O(N)
# Space Complexity: O(1)

# Time taken: 21 minutes

from q0_singly_linked_list import display, length, Node, insertAtBack

def move_nth_last_to_front(head, k):
    # Given a singly linked list, move the nth from the last element to the front of the list.

    N = length(head)
    if k > N: return head

    target_N = N - k
    if N == k: return head

    start = 1
    cur = head
    while start < target_N:
        cur = cur.next
        start += 1
    val = cur.next
    cur.next = cur.next.next
    val.next = head
    head = val
    return head


if __name__ == "__main__":
    head = Node(15)
    insertAtBack(head, 2)
    insertAtBack(head, 8)
    insertAtBack(head, 7)
    insertAtBack(head, 20)
    insertAtBack(head, 9)
    insertAtBack(head, 11)
    insertAtBack(head, 6)
    insertAtBack(head, 19)
    display(head)
    head = move_nth_last_to_front(head, 7) 
    display(head)