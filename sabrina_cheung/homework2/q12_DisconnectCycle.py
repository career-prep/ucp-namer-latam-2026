'''
Method: Hashed Linked List
Time: 20 min
Time Complexity: O(n)
Space Complexity: O(n)

Intuition: Hash the nodes everytime you move next in the linked list. 
Check whether the pointer points to a node that has been hashed. If so, remove the pointer such that it points to None

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def DisconnectCycle(head):
    if not head:
        return None
    
    cur = head
    visited = set()
    prev = None
    while cur:
        if cur in visited:
            prev.next = None
            cur = prev
        visited.add(cur)
        prev = cur
        cur = cur.next
    return head

def print_list(head):
    linked_list = []
    while head:
        linked_list.append(head.data)
        head = head.next
    print(linked_list)

# Example 1
# Input (with cycle): 10 -> 18 -> 12 -> 9 -> 11 -> 4
# (4 points back to 12)
# Expected output: 10 -> 18 -> 12 -> 9 -> 11 -> 4 -> None
head1 = Node(10)
head1.next = Node(18)
head1.next.next = Node(12)
head1.next.next.next = Node(9)
head1.next.next.next.next = Node(11)
head1.next.next.next.next.next = Node(4)

node12_1 = head1.next.next
node4_1 = head1.next.next.next.next.next
node4_1.next = node12_1


# Example 2
# Input (with cycle): 10 -> 18 -> 12 -> 9 -> 11 -> 4
# (4 points to itself)
# Expected output: 10 -> 18 -> 12 -> 9 -> 11 -> 4 -> None
head2 = Node(10)
head2.next = Node(18)
head2.next.next = Node(12)
head2.next.next.next = Node(9)
head2.next.next.next.next = Node(11)
head2.next.next.next.next.next = Node(4)

node4_2 = head2.next.next.next.next.next
node4_2.next = node4_2

print_list(DisconnectCycle(head1))
print_list(DisconnectCycle(head2))