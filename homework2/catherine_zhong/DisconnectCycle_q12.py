#technique: 
#time complexity: O(n)
#space complexity: O(1)

class Node:
    def __init__(self, data):
        self.val = data
        self.next = None 

def DisconnectCycle(head):
    if head is None or head.next is None:
        return head

    fast = head
    slow = head 
    while True:
        if fast is None or fast.next is None:
            return head

        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            break

    slow = head
    while fast != slow:
        fast = fast.next
        slow = slow.next

    while fast.next != slow:
        fast = fast.next

    fast.next = None
    return head

def printList(head):
    elements = []
    while head:
        elements.append(head.val)
        head = head.next

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
node5.next = node3

print('test1: ')
head = DisconnectCycle(head)
printList(head)

#time spent: 30 min