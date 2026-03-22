#Dedup Sorted List
#Time Complexity: O(n) where n is the number of nodes
#Space Complexity: O(1)
#Technique: Linked List Fixed-Distance Two-Pointer
#Time Spent: 10 minutes

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def DedupSortedList(head):
    if not head or not head.next:
        return head
    
    prev = head
    curr = head.next
    while curr:
        if curr.data == prev.data:
            prev.next = curr.next
            curr = curr.next
        else:
            prev = curr
            curr = curr.next
    return head
            
    
#TEST CASES

head = Node(1)
head.next = Node(2)
head.next.next = Node(2)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(5)
head.next.next.next.next.next.next = Node(5)
head.next.next.next.next.next.next.next = Node(10)
head.next.next.next.next.next.next.next.next = Node(10)


def print_list(head):
    curr = head
    while curr:
        print(curr.data, end=" -> " if curr.next else "\n")
        curr = curr.next

DedupSortedList(head)
print_list(head)