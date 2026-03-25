class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def disconnectCycle(head):
    if not head or not head.next:
        return head

    slow = head
    fast = head
    has_cycle = False

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            has_cycle = True
            break

    if not has_cycle:
        return head

    slow = head
    if slow == fast:
        while fast.next != slow:
            fast = fast.next
        fast.next = None
        return head

    while slow.next != fast.next:
        slow = slow.next
        fast = fast.next

    fast.next = None
    
    return head

def display(head, limit=10):
    curr = head
    count = 0
    while curr and count < limit:
        print(curr.val, end=" -> ")
        curr = curr.next
        count += 1
    print("None" if count < limit else "(Cycle Detected/Limit Reached)")

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

print("Before Disconnect (Case 1):", end=" ")
display(node1)
disconnectCycle(node1)
print("After Disconnect (Case 1): ", end=" ")
display(node1)

h2 = Node(1)
h2.next = Node(2)
h2.next.next = h2

print("\nBefore Disconnect (Case 2):", end=" ")
display(h2)
disconnectCycle(h2)
print("After Disconnect (Case 2): ", end=" ")
display(h2)

h3 = Node(10)
h3.next = Node(20)
print("\nNo Cycle Test (Case 3):", end=" ")
display(h3)
disconnectCycle(h3)
display(h3)

# Technique: Linked list fast-slow two-pointer
# Time Complexity: O(n)
# Space Complexity: O(1)
# Time spent 40mins