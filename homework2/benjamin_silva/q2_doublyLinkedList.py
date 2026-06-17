class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def insertAtFront(head, val):
    new_node = Node(val)

    new_node.next = head

    if head is not None:
        head.prev = new_node

    return new_node
    


def insertAtBack(head, tail, val):
    new_node = Node(val)
    if head is None:
        new_node.next = head
    else:
        curr = head
        while curr.next is not None:
            curr = curr.next
        
        curr.next = new_node

        new_node.prev = curr
    
    return head


def insertAfter(head, val, loc):
    curr = head

    while curr is not None:
        if curr == loc:
            new_node = Node(val)

            new_node.next = curr.next
            
            new_node.prev = curr
            if curr.next is not None:
                curr.next.prev = new_node
            curr.next = new_node
            return head
        curr = curr.next
    return head
    


def insertBefore(head, val, loc):
    if head is None:
        return head
    
    if head == loc:
        new_node = Node(val)
        new_node.next = head
        head.prev = new_node
        return new_node
    
    curr = head
    while curr is not None:
        if curr == loc:
            new_node = Node(val)
            new_node.next = curr
            new_node.prev = curr.prev
            curr.prev.next = new_node
            curr.prev = new_node
            return head
        curr = curr.next
    return head
    


def deleteFront(head):
    if head is None:
        return None
    
    temp = head

    head = head.next

    if head is not None:
        head.prev = None

    return head
    


def deleteBack(head, tail):
    if head is None:
        return None
    if head.next is None:
        return None
    
    curr = head
    while curr.next is not None:
        curr = curr.next

    if curr.prev is not None:
        curr.prev.next = None
    
    return head


def deleteNode(head, loc):
    if head is None:
        return head
    
    curr = head

    for i in range(1, loc):
        if curr is None:
            return head
        curr = curr.next

    if curr is None:
        return head
    
    if curr.prev is not None:
        curr.prev.next = curr.next
    
    if curr.next is not None:
        curr.next.prev = curr.prev
    
    if head == curr:
        head = curr.next
    
    return head
    


def length(head):
    count = 0
    curr = head
    while curr is not None:
        count += 1
        curr = curr.next
    return count
    


def reverseIterative(head):
    curr = head
    temp = None

    while curr is not None:
        temp = curr.prev

        curr.prev = curr.next

        curr.next = temp

        curr = curr.prev
    
    if temp is not None:
        head = temp.prev
    return head


def _reverseRecursiveHelper(node):
    temp = node.prev
    node.prev = node.next
    node.next = temp
    
    if node.prev is None:
        return node
    
    return _reverseRecursiveHelper(node.prev)


def reverseRecursive(head):
    if head is None:
        return None
    return _reverseRecursiveHelper(head)


def printList(head):
    result = []
    curr = head
    while curr:
        result.append(str(curr.data))
        curr = curr.next
    print(" <-> ".join(result))


if __name__ == "__main__":
    head = None
    tail = None

    head = insertAtFront(head, 3)
    head = insertAtFront(head, 2)
    head = insertAtFront(head, 1)
    printList(head)

    head = insertAtBack(head, tail, 4)
    head = insertAtBack(head, tail, 5)
    printList(head)

    print(length(head))

    head = deleteFront(head)
    printList(head)

    head = deleteBack(head, tail)
    printList(head)

    head = reverseIterative(head)
    printList(head)

    head = reverseRecursive(head)
    printList(head)