# spent 40 minutes

class Node:
    """Node struct in python"""
    def __init__(self, data: int, next: Node = None) -> None:
        self.data = data
        self.next = next 
        
        

def insertAtFront(head, val):
    """Creates a new node with `val` data and links it at the head of the list. O(1) """
    return Node(val, head)
    
    
def insertAtBack(head, val):
    """Creates a new node with `val` data and links it at the end of the list. O(n)"""
    if not head: # empty case
        return Node(val, None) 
    new_node = Node(val, None)
    curr = head
    # traverse to end
    while curr.next:
        curr = curr.next
    # link
    curr.next = new_node
    return head


def insertAfter(head, val, loc):
    """Creates a new node with `val` data after Node `loc` and then returns the head. O(1)"""
    if not head or not loc:
        return head
    # create new node
    new_node = Node(val, None)
    # link
    temp = loc.next
    new_node.next = temp
    loc.next = new_node
    return head


def insertBefore(head, val, loc):
    """Creates a new node with `val` data before `loc` and then returns the head. O(n)"""
    if not head or not loc:
        return head
    # check head case
    if (loc == head):
        return Node(val, loc)
    
    # find the node before loc    
    curr = head
    while (curr.next and curr.next != loc):
        curr = curr.next
    if not curr.next: # loc not found
        return head
        
    # create node
    new_node = Node(val, None)
    # link
    curr.next = new_node 
    new_node.next = loc
    return head
    
    
def deleteFront(head):
    """Removes the first node and returns the new head. O(1)"""
    if not head:
        return None
    return head.next


def deleteBack(head):
    """Removes the last node and returns head. O(n)"""
    if not head: # empty case
        return None
    if not head.next:
        return None
    # iterate to the 2nd to last node
    curr = head
    while curr.next.next:
        curr = curr.next
        
    # unlink last node
    curr.next = None
    return head


def deleteNode(head, loc):
    """deletes the node `loc` and returns head. O(n)"""
    if not head: # empty case
        return None
    if (loc == head): # head case
        return loc.next
    
    # find the node before loc
    curr = head
    while (curr.next and curr.next != loc):
        curr = curr.next
    if not curr.next: # loc not found
        return head
    
    # unlink loc
    curr.next = loc.next 
    return head


def length(head) -> int:
    """Returns length of linked list. O(n)"""
    counter = 0
    curr = head
    while curr:
        curr = curr.next
        counter += 1
    return counter


def reverseIterative(head):
    """reverses the linked list iteratively. O(n)"""
    prev = None
    curr = head 

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
        
    head = prev 
    return head
    
    
def reverseRecursive(head):
    """Reverses the linked list recursively with a helper. O(n)"""
    # empty + base case
    if not head or not head.next:
        return head
    
    # go to end and unravel
    new_head = reverseRecursive(head.next) 
    # reverse pointer
    head.next.next = head
    head.next = None
    
    return new_head



if __name__ == "__main__":
    # 1
    # test for insertatfront
    ll = None
    ll = insertAtFront(ll, 5)
    ll = insertAtFront(ll, 4)
    ll = insertAtFront(ll, 3)
    ll = insertAtFront(ll, 2)
    ll = insertAtFront(ll, 1)
    
    curr = ll
    arr = [1,2,3,4,5]
    for i in range(len(arr)):
        assert curr is not None, "InsertAtFront error1"
        assert curr.data == arr[i], "InsertAtFront error1"
        curr = curr.next
    assert curr is None, "InsertAtFront error3"
    
    
    # 2 
    # test for insertatback
    ll2 = None
    ll2 = insertAtBack(ll2, 1)
    ll2 = insertAtBack(ll2, 2)
    ll2 = insertAtBack(ll2, 3)
    ll2 = insertAtBack(ll2, 4)
    ll2 = insertAtBack(ll2, 5) 
    
    curr2 = ll2 
    arr2 = [1,2,3,4,5]
    for i in range(len(arr2)):
        assert curr2 is not None, "InsertAtBack error1"
        assert curr2.data == arr2[i], "InsertAtBack error2"
        curr2 = curr2.next
    assert curr2 is None, "InsertAtBack error3"
        
        
    # 3 
    # test for insertafter
    # create base list: 1 -> 2 -> 3
    base = None
    base = insertAtBack(base, 1)
    base = insertAtBack(base, 2)
    base = insertAtBack(base, 3)

    # get reference to node with value 2
    curr = base
    while curr and curr.data != 2:
        curr = curr.next

    base = insertAfter(base, 99, curr)  # 1 -> 2 -> 99 -> 3

    curr = base
    arr3 = [1,2,99,3]
    for i in range(len(arr3)):
        assert curr is not None, "InsertAfter error1"
        assert curr.data == arr3[i], "InsertAfter error2"
        curr = curr.next
    assert curr is None, "InsertAfter error3"
    
    # intentionally fails when nonexistent node is inputted to function to keep performance O(1)
    '''
    # test for node that doesnt exist in list
    nonexistent_node3 = Node(-1)
    base = insertAfter(base, 10, nonexistent_node3)
    curr = base
    for i in range(len(arr3)):
        assert curr is not None, "InsertAfter error4"
        assert curr.data == arr3[i], "InsertAfter error5"
        curr = curr.next
    assert curr is None, "InsertAfter error6"
    '''
    

    # 4
    # test for insertBefore
    # insert before node with value 99
    curr = base
    while curr and curr.data != 99:
        curr = curr.next

    base = insertBefore(base, 50, curr)  # 1 -> 2 -> 50 -> 99 -> 3

    curr = base
    arr4 = [1,2,50,99,3]
    for i in range(len(arr4)):
        assert curr is not None, "InsertBefore error1"
        assert curr.data == arr4[i], "InsertBefore error2"
        curr = curr.next
    assert curr is None, "InsertBefore error3"
    
    # test for node not in ll
    nonexistent_node4 = Node(-1)
    base = insertBefore(base, 10, nonexistent_node4)
    curr = base
    for i in range(len(arr4)):
        assert curr is not None, "InsertBefore error4"
        assert curr.data == arr4[i], "InsertBefore error5"
        curr = curr.next
    assert curr is None, "InsertBefore error6"


    # 5
    # test deleteFront
    base = deleteFront(base)  # remove 1

    curr = base
    arr5 = [2,50,99,3]
    for i in range(len(arr5)):
        assert curr is not None, "deleteFront error1"
        assert curr.data == arr5[i], "deleteFront error2"
        curr = curr.next
    assert curr is None, "deleteFront error3"


    # 6
    # test deleteBack
    base = deleteBack(base)  # remove 3

    curr = base
    arr6 = [2,50,99]
    for i in range(len(arr6)):
        assert curr is not None, "deleteBack error1"
        assert curr.data == arr6[i], "deleteBack error2"
        curr = curr.next
    assert curr is None, "deleteBack error3"


    # 7
    # test deleteNode (delete 50)
    curr = base
    while curr and curr.data != 50:
        curr = curr.next

    base = deleteNode(base, curr)

    curr = base
    arr7 = [2,99]
    for i in range(len(arr7)):
        assert curr is not None, "deleteNode error1"
        assert curr.data == arr7[i], "deleteNode error2"
        curr = curr.next
    assert curr is None, "deleteNode error3"
    
    # test for nonexistent node
    nonexistent_node7 = Node(-1)
    base = deleteNode(base, nonexistent_node7)
    curr = base
    for i in range(len(arr7)):
        assert curr is not None, "deleteNode error4"
        assert curr.data == arr7[i], "deleteNode error5"
        curr = curr.next
    assert curr is None, "deleteNode error6"
    

    # 8
    # test length
    assert length(base) == 2, "length error"


    # 9
    # test reverseIterative
    base = reverseIterative(base)  # [99, 2]

    curr = base
    arr9 = [99,2]
    for i in range(len(arr9)):
        assert curr is not None, "reverseIterative error1"
        assert curr.data == arr9[i], "reverseIterative error2"
        curr = curr.next
    assert curr is None, "reverseIterative error3"


    # 10
    # test reverseRecursive
    base = reverseRecursive(base)  # [2, 99]

    curr = base
    arr10 = [2,99]
    for i in range(len(arr10)):
        assert curr is not None, "reverseRecursive error1"
        assert curr.data == arr10[i], "reverseRecursive error2"
        curr = curr.next
    assert curr is None, "reverseRecursive error3"

    print("All tests passed")