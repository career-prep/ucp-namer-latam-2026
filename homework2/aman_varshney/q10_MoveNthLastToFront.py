# spent 30 minutes
# Time complexity - O(n)
# Space complexity - O(1) 
# Linked list fast slow pointers


class Node:
    """Node struct in python"""
    def __init__(self, data: int, next: Node = None) -> None:
        self.data = data
        self.next = next 
        
        
def moveNth(ll, k):
    assert ll is not None, "empty linked list" # empty case
    assert k >= 1, "k must be greater than 0" # edge case
    
    fast = ll
    for _ in range(k):
        assert fast is not None, "k is out of bounds"
        fast = fast.next
        
    # if fast == None -> k == length 
    if fast is None:
        return ll
    
    slow = ll
    while fast.next: # slow will be at node before kth
        slow = slow.next
        fast = fast.next
        
    # remove node
    kth = slow.next
    slow.next = kth.next
    # add to front
    kth.next = ll
    return kth
    
       
       
       
if __name__ == "__main__":
    # helper to build ll
    def insert(ll, val):
        curr = ll
        while curr.next:
            curr = curr.next
        new_node = Node(val)
        curr.next = new_node
        
    # helper to print ll
    def printll(ll):
        s = ""
        curr = ll
        while curr:
            s += str(curr.data) + " "
            curr = curr.next
        print(s) 
        
        
    # test 1
    ll1 = Node(15)
    insert(ll1, 2)
    insert(ll1, 8)
    insert(ll1, 7)
    insert(ll1, 20)
    insert(ll1, 9)
    insert(ll1, 11)
    insert(ll1, 6)
    insert(ll1, 19)
    print("Original ")
    printll(ll1)
    print("After moving (k = 2)")
    ll_moved1 = moveNth(ll1, 2)
    printll(ll_moved1)
    
    print()
    
    # test 2
    ll1 = Node(15)
    insert(ll1, 2)
    insert(ll1, 8)
    insert(ll1, 7)
    insert(ll1, 20)
    insert(ll1, 9)
    insert(ll1, 11)
    insert(ll1, 6)
    insert(ll1, 19)
    print("Original ")
    printll(ll1)
    print("after moving (k = 7) ")
    ll_moved2 = moveNth(ll1, 7)
    printll(ll_moved2)
    
    
        