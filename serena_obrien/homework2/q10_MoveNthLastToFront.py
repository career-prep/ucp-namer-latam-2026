# Time complexity: O(n)
# Space complexity: O(1)

# Technique: Fixed distance two-pointer

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertAtFront(head, val):
    newNode = Node(val)
    newNode.next = head
    return newNode

def print_list(head):
    curr = head
    while curr:
        print(curr.data, end="->" if curr.next else "")
        curr = curr.next
    print()

def MoveNthLastToFront(head, n):
    fast = slow = head

    for i in range(n):
        if not fast:
            return head
        fast = fast.next

    prev = None
    while fast:
        fast = fast.next
        prev = slow
        slow = slow.next

    if not prev:
        return head
    
    prev.next = slow.next
    slow.next = head
    return slow

if __name__ == '__main__':
    head = Node(9)
    for val in [1,2,5,7,8,3]:
        head = insertAtFront(head, val)

    n = 20

    print_list(head)

    print(f"After moving {n}-th last to front:")

    head = MoveNthLastToFront(head, 3)
    print_list(head)
    
# ~ time spent: 35 minutes
