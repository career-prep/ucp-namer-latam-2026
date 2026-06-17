class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 

def insertAtFront(head,val):
    new_node = Node(val)
    new_node.next = head
    return new_node

def insertAtBack(head,val):
    if not head: return head
    new_node = Node(val)
    curr = head
    while curr.next:
        curr = curr.next    
    
    curr.next = new_node 
    return head

def insertAfter(head, val, loc):
    new_node = Node(val)
    curr = head
    
    while curr != loc and curr:
        curr = curr.next
    
    if not curr: return head

    new_node.next = curr.next 
    curr.next = new_node

    return head

def insertBefore(head, val, loc):
    new_node = Node(val)
    curr = head
    
    if curr == loc:
        new_node.next = curr
        return new_node
    
    while curr and curr.next != loc :
        curr = curr.next
    
    if not curr: return head
    
    new_node.next = curr.next
    curr.next = new_node
    return head


def deleteFront(head):
    if not head: return head
    return head.next

def deleteBack(head):
    prev = head
    if not prev: return None
    
    curr = prev.next
    if not curr: return None
    
    while curr.next:
        prev = prev.next
        curr = curr.next
    
    prev.next = None
    return head

def deleteNode(head, loc):  # O(n)
    if not head:
        return None
    if head == loc:
        return head.next
    curr = head
    while curr.next and curr.next != loc:
        curr = curr.next
    if curr.next:
        curr.next = curr.next.next
    return head

def length(head):
    curr = head
    count = 0
    while curr:
        count +=1
        curr = curr.next
    return count
        

def reverseIterative(head):
    prev = None
    curr = head

    while curr:
        temp_node = curr.next
        curr.next = prev
        prev = curr
        curr = temp_node
    return prev

    # arr = []
    # curr = head
    # while curr:
    #     arr.append(curr.data)
    #     curr = curr.next

    # arr.reverse()

    # curr = head

    # for num in arr:
    #     curr.data = num
    #     curr = curr.next
    # return head    

def reverseRecursive(head):  # O(n)
    def helper(node, prev):
        if not node:
            return prev
        next_node = node.next
        node.next = prev
        return helper(next_node, node)
    return helper(head, None)


def printList(head):
    result = []
    curr = head
    while curr:
        result.append(str(curr.data))
        curr = curr.next
    print(" -> ".join(result))


print("SinglyLinkedList Results:")

head = None
for v in [1, 2, 3, 4, 5]:
    head = insertAtBack(head, v)
printList(head)

head = insertAtFront(head, 0)
printList(head)

node2 = head.next.next
head = insertAfter(head, 99, node2)
printList(head)

head = insertBefore(head, 88, node2)
printList(head)

head = deleteFront(head)
printList(head)

head = deleteBack(head)
printList(head)

head = deleteNode(head, node2)
printList(head)

print(length(head))

head = reverseIterative(head)
printList(head)

head = reverseRecursive(head)
printList(head)
