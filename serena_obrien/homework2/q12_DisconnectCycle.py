# Time complexity: O(n)
# Space complexity: O(1)

# Technique: Linked list reset/catch-up two-pointer (I think)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertAtFront(head, val):
    newNode = Node(val)
    newNode.next = head
    return newNode

def print_list(head, limit=20):
    curr = head
    count = 0
    while curr and count < limit:
        print(curr.data, end="->" if curr.next else "")
        curr = curr.next
        count += 1
    if curr:
        print("... (cycle detected)")
    else:
        print()

def disconnectCycle(head):
    slow = fast = head

    # detect cycle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return head

    slow = head
    prev = None
    while slow != fast:
        prev = fast
        slow = slow.next
        fast = fast.next

    prev.next = None
    return head
if __name__ == '__main__':
    # Build list: 1->2->3->4->5
    head = None
    for val in [5,4,3,2,1]:
        head = insertAtFront(head, val)
    
    # Print original list
    print("Original list:")
    print_list(head)

    # Create a cycle: 5.next -> 3
    tail = head
    while tail.next:
        tail = tail.next
    # tail is 5
    third_node = head.next.next  # node with value 3
    tail.next = third_node

    print("List with cycle (limited print):")
    print_list(head)

    # Disconnect cycle
    head = disconnectCycle(head)

    print("List after disconnecting cycle:")
    print_list(head)
    
# ~ time spent: 35 minutes
