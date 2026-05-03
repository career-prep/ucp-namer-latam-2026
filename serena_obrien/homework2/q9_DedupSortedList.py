# Time complexity: O(n)
# Space complexity: O(1)

# Technique: Simultaenous iteration two-pointer

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

def DedupSortedList(head):
    curr = head
    while curr and curr.next:
        if curr.data == curr.next.data:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head
        
if __name__ == '__main__':
    head = Node(9)
    for val in [8,7,7,7,7,6,3,2,2,1]:
        head = insertAtFront(head, val)

    print_list(head)

    print("After de-duplication")
    
    head = DedupSortedList(head)
    print_list(head)
    
# ~ time spent: 20 minutes