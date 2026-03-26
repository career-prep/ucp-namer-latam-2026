#technique: two pointer fast and slow
#time complexity: O(n)
#space complexity: O(1)
class Node: 
    def __init__ (self,data):
        self.val = data
        self.next = None 

def MoveNthLastToFront(head, n):
    if head is None or head.next is None:
        return head
    
    fast = head
    slow = head
    for i in range(n):
        if fast is None:
            return head
        fast = fast.next

    if fast is None:
        return head
    while fast.next:
        fast = fast.next
        slow = slow.next 

    target = slow.next
    slow.next = target.next
    target.next = head
    head = target

    return head

def printList(head):
    elements = []
    current = head
    while current:
        elements.append(current.val)
        current = current.next

    print(', '.join(str(i) for i in elements))

head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print('test1: ')
head = MoveNthLastToFront(head, 2)
printList(head)
    
#time spent: 20min