#Disconnect Cycle
#Time Complexity: O(3n) which simplifies to O(n) where n is the length of the list
#Space Complexity: O(1)
#Technique: Linked List Fast-Slow Two-Pointer + Linked List Reset/Catch-Up Two-Pointer
#Time Spent: >40 minutes

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
def disconnectCycle(head):
    slow = fast = head
    hasCycle = False
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            hasCycle = True
            break
    
    if not hasCycle:
        return head
    
    slow = head
    while slow!=fast:
        slow = slow.next
        fast = fast.next

    while fast.next != slow:
        fast = fast.next
    
    fast.next = None

    return head




def print_list(head):
    curr = head
    while curr:
        print(curr.data, end=" -> " if curr.next else "\n")
        curr = curr.next


#Test Case 1

head = Node(10)
head.next = Node(18)
head.next.next = Node(12)
head.next.next.next = Node(9)
head.next.next.next.next = Node(11)
head.next.next.next.next.next = Node(4)

node = head.next.next
lastNode = head.next.next.next.next.next
lastNode.next = node

disconnectCycle(head)
print_list(head)

#Test Case 2

head2 = Node(10)
head2.next = Node(18)
head2.next.next = Node(12)
head2.next.next.next = Node(9)
head2.next.next.next.next = Node(11)
head2.next.next.next.next.next = Node(4)

lastNode2 = head2.next.next.next.next.next
lastNode2.next = lastNode2

disconnectCycle(head)
print_list(head)
