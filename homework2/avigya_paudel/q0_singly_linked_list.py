class Node:
    def __init__(self, data: int):
        self.data = data
        self.next: Node | None = None


def insertAtFront(head: Node, val: int): 
    # creates new Node with data val at front; returns head. O(1) time.
    new_node = Node(val)

    if not head: return new_node
    
    new_node.next = head
    head = new_node
    return head

def insertAtBack(head: Node, val: int): 
    # creates new Node with data val at end; returns head. O(n) time.
    new_node = Node(val)

    if not head: return new_node

    runner = head
    while runner:
        prev = runner
        runner = runner.next
    prev.next = new_node
    return head
    

def insertAfter(head: Node, val: int, loc: Node | None): 
    #  creates new Node with data val after Node loc; returns head. O(1) time.
    #  some edges cases: if loc == None, then linked list doesn't add the new node

    new_node = Node(val)
    if not loc: return head

    nxt = loc.next
    loc.next = new_node
    new_node.next = nxt

    return head


def insertBefore(head: Node, val: int, loc: Node | None): 
    # creates new Node with data val before Node loc; returns head. O(n) time.
    #  some edges cases: if loc == None or loc is not in linked list, then linked list doesn't add the new node

    new_node = Node(val)

    if loc == head:
        return insertAtFront(head, val)

    runner = head.next
    prev = head

    while runner:
        if runner == loc:
            prev.next = new_node
            new_node.next = runner
            return head
        prev = runner
        runner = runner.next
    
    return head


def deleteFront(head): 
    # removes first Node; returns head. O(1) time.

    if not head: return None

    head = head.next

    return head

def deleteBack(head): 
    # removes last Node; returns head. O(n) time.
    
    if not head: return None
    if not head.next: return None 

    runner = head
    while runner and runner.next:
        prev = runner
        runner = runner.next
    prev.next = None
    return head

def deleteNode(head, loc): 
    # deletes Node loc; returns head. O(n) time.
    
    if head == loc: return deleteFront(head)

    runner = head.next
    prev = head

    while runner:
        if runner == loc:
            prev.next = prev.next.next
            runner.next = None
            return head
        prev = runner
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
    prev = None
    cur = head

    while cur:
        nxt = cur.next
        cur.next = prev 
        prev = cur 
        cur = nxt

    return prev

def reverseRecursive(head): 
    # reverses the linked list recursively (Hint: you will need a helper function.) O(n) time.
    def reverse(head, prev):
        if not head:
            return prev
        nxt = head.next
        head.next = prev
        return reverse(nxt,head)
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
    head = insertAtBack(head, 3)
    display(head)
    head = insertAfter(head, 4, head.next.next) # type: ignore
    display(head)
    head = insertBefore(head, 5, head.next)
    display(head)
    head = deleteFront(head)
    display(head)
    head = deleteBack(head)
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


