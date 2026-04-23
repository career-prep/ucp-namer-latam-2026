class Node:
    def __init__(self, data: int):
        self.data = data
        self.next: Node | None = None
        self.prev: Node | None = None


def insertAtFront(head: Node, val: int): 
    # creates new Node with data val at front; returns head. O(1) time.
    new_node = Node(val)

    if not head: return new_node
    
    new_node.next = head
    head.prev = new_node
    head = new_node
    return head

def insertAtBack(head, tail, val): 
    # creates new Node with data val at end; returns head. O(1) time.
    new_node = Node(val)

    if not tail: return new_node

    tail.next = new_node
    new_node.prev = tail
    tail = new_node

    return head
    

def insertAfter(head, val, loc): 
    #  creates new Node with data val after Node loc; returns head. O(1) time.
    #  some edges cases: if loc == None or loc is not in linked list, then linked list doesn't add the new node

    if not loc:
        return head

    new_node = Node(val)
    
    nxt = loc.next # type: ignore

    if nxt is None:
        return insertAtBack(head, loc, val)
    
    loc.next = new_node
    new_node.prev = loc

    new_node.next = nxt
    nxt.prev = new_node

    return head


def insertBefore(head: Node, val: int, loc: Node | None): 
    # creates new Node with data val before Node loc; returns head. O(1) time.
    #  some edges cases: if loc == None or loc is not in linked list, then linked list doesn't add the new node

    if not loc:
        return head 
    
    new_node = Node(val)

    if loc == head:
        return insertAtFront(head, val)

    pre_node = loc.prev

    pre_node.next = new_node # type: ignore
    new_node.prev = pre_node

    new_node.next = loc
    loc.prev = new_node
    
    return head


def deleteFront(head):
    # removes first Node; returns head. O(1) time.

    if not head: return None
    if not head.next: return None  

    head = head.next
    head.prev = None

    return head

def deleteBack(head, tail): 
    # removes last Node; returns head. O(1) time.
    
    if not tail: return None
    if not tail.prev: return None 
    
    second_last_node = tail.prev
    second_last_node.next = None
    tail.prev = None
    tail = second_last_node

    return head

def deleteNode(head, loc): 
    # deletes Node loc; returns head. O(n) time.
    
    if head == loc: return deleteFront(head)

    runner = head.next

    while runner:
        if runner == loc:
            pre = runner.prev
            nxt = runner.next
            pre.next = nxt
            if nxt: nxt.prev = pre 
        runner = runner.next
    
    return head

def length(head): 
    # returns length of the list. O(n) time.
    count = 0
    runner = head
    while runner:
        runner = runner.next
        count += 1

    return count

def reverseIterative(head):
    # reverses the linked list iteratively. O(n) time.
    if not head: return None
    
    runner = head
    prev = None

    while runner:
        nxt = runner.next
        runner.next = prev 
        runner.prev = nxt
        prev = runner
        runner = nxt 
    return prev

def reverseRecursive(head): 
    # reverses the linked list recursively (Hint: you will need a helper function.) O(n) time.
    def reverse(head, pre):
        if not head: return pre

        nxt = head.next
        head.next = pre
        head.prev = nxt
        return reverse(nxt, head)

    return reverse(head, None)


def display(head):
    # extra function to visualization and testing purpose
    runner = head
    res = ""
    while runner:
        res += str(runner.data)
        res += " -> "
        runner = runner.next
    res += "None"
    print(res)

if __name__ == "__main__":
    head = Node(1)
    display(head)
    head = insertAtFront(head,2)
    display(head)
    head = insertAtBack(head, head.next, 3)
    display(head)
    head = insertAfter(head, 4, head.next.next) # type: ignore
    display(head)
    head = insertBefore(head, 5, head.next)
    display(head)
    head = deleteFront(head)
    display(head)
    print("Delete back")
    head = deleteBack(head, head.next.next.next) #type: ignore
    display(head)
    head = deleteNode(head, head.next) # type: ignore
    display(head)
    print(length(head))
    head = insertAtFront(head, 0) #type: ignore
    head = insertAtFront(head, -1)
    display(head)
    head = reverseIterative(head)
    display(head)
    head = reverseRecursive(head)
    display(head)