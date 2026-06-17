class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def insertAtFront(head, val):
        new_node = Node(val)
        new_node.next = head
        return new_node
 
    def insertAtBack(head, val):
        new_node = Node(val)
        if head is None:
            return new_node
        curr = head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        return head
    
    def insertAfter(head, val, loc):
        new_node = Node(val)
        new_node.next = loc.next
        loc.next = new_node
        return head
    
    def insertBefore(head, val, loc):
        new_node = Node(val)
        if head is loc:
            new_node.next = head
            return new_node
        curr = head
        while curr and curr.next is not loc:
            curr = curr.next
        if curr:
            new_node.next = loc
            curr.next = new_node
        return head
    
    def deleteFront(head):
        if head is None:
            return None
        return head.next
    
    def deleteBack(head):
        if head is None:
            return None
        if head.next is None:
            return None
        curr = head
        while curr.next.next:
            curr = curr.next
        curr.next = None
        return head
    
    def deleteNode(head, loc):
        if head is loc:
            return head.next
        curr = head
        while curr and curr.next is not loc:
            curr = curr.next
        if curr:
            curr.next = loc.next
        return head
    
    def length(head):
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        return count
    
    def reverseIterative(head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    
    def reverseRecursiveHelper(curr, prev):
        # O(n) time
        if curr is None:
            return prev
        nxt = curr.next
        curr.next = prev
        return Node.reverseRecursiveHelper(nxt, curr)
    
    def reverseRecursive(head):
        # O(n) time
        return Node.reverseRecursiveHelper(head, None)
    
    def toList(head):
        result = []
        curr = head
        while curr:
            result.append(curr.data)
            curr = curr.next
        return result
    
    def fromList(lst):
        head = None
        for val in reversed(lst):
            head = Node.insertAtFront(head, val)
        return head
