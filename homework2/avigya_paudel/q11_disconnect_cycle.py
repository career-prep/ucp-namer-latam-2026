# Technique: Linked List Fast and Slow Pointer 

# Time Complexity: O(N)
# Space Complexity: O(1)

# Time taken: 35 minutes

from q0_singly_linked_list import Node, insertAtBack, display

def disconnect_cycle(head):
    if not head:
        return head

    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return head

    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    entry = slow

    cur = entry
    while cur.next != entry:
        cur = cur.next
    cur.next = None

    return head

# (Very fun problem -> I did this in leetcode before, 
# if i didnt know the idea before I would definitely not be able to solve this :)
if __name__ == "__main__":
    # build: 10 -> 18 -> 12 -> 9 -> 11 -> 4 -> (back to 12)
    head = Node(10)
    insertAtBack(head, 18)
    insertAtBack(head, 12)
    insertAtBack(head, 9)
    insertAtBack(head, 11)
    insertAtBack(head, 4)

    # manually create the cycle: find node 4 and node 12, point 4 back to 12
    node_12 = head.next.next       # 10 -> 18 -> 12
    node_4  = head.next.next.next.next.next  # 10 -> 18 -> 12 -> 9 -> 11 -> 4
    node_4.next = node_12          # create the cycle


    head = disconnect_cycle(head)

    display(head)   # expected: 10 -> 18 -> 12 -> 9 -> 11 -> 4 -> None

    # test 2: no cycle at all
    head2 = Node(1)
    insertAtBack(head2, 2)
    insertAtBack(head2, 3)
    print("\nNo cycle list:")
    display(head2)
    head2 = disconnect_cycle(head2)

    display(head2)  # expected: 1 -> 2 -> 3 -> None

    # test 3: cycle at the very last node pointing to itself
    head3 = Node(5)
    insertAtBack(head3, 10)
    insertAtBack(head3, 15)
    node_15 = head3.next.next
    node_15.next = node_15         
    print("\nSelf-loop on last node:")
    head3 = disconnect_cycle(head3)
    display(head3)  # expected: 5 -> 10 -> 15 -> None