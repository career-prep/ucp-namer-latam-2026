# spent 40 minutes
# Time complexity - O(n) 
# Space complexity - O(1)
# Linked list slow fast pointers



class Node:
    """Node struct in python"""
    def __init__(self, data: int, next: Node = None) -> None:
        self.data = data
        self.next = next 
        
        
def disconnectCycle(ll):
    if not ll:
        return None
    
    slow = ll
    fast = ll
    
    # detect cycle
    is_cycle = False
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast: # cycle detected
            is_cycle = True
            break
    if not is_cycle: # no cycle -> return
        return ll
    
    # find start 
    slow = ll 
    while slow != fast:
        slow = slow.next
        fast = fast.next
    start = slow
    
    # break next pointer creating cycle
    end = start
    while end.next != start:
        end = end.next
    end.next = None
    
    return ll

# example 1 -- 10 -> 18 -> 12 -> 9 -> 11 -> 4 -> 12 (cycle)
# example 2 -- 10 -> 18 -> 12 -> 9 -> 11 -> 4 -> 4 (cycle)


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
        counter = 20
        s = ""
        curr = ll
        while curr and counter != 0:
            s += str(curr.data) + " "
            curr = curr.next
            counter -= 1
        if counter == 0:
            s += "..."
        print(s)


    # test 1 
    ll1 = Node(10)
    insert(ll1, 18)
    insert(ll1, 12)
    insert(ll1, 9)
    insert(ll1, 11)
    insert(ll1, 4)
    curr = ll1
    ptr = None
    while curr:
        if curr.data == 12:
            ptr = curr
        if not curr.next:
            break
        curr = curr.next
    curr.next = ptr
    print("Original (test 1)")
    printll(ll1)
    ll1_disconnected = disconnectCycle(ll1)
    print("After disconnecting")
    printll(ll1_disconnected)
    print()
    
    
    # test 2 
    ll2 = Node(10)
    insert(ll2, 18)
    insert(ll2, 12)
    insert(ll2, 9)
    insert(ll2, 11)
    insert(ll2, 4)
    curr2 = ll2
    ptr2 = None
    while curr2:
        if curr2.data == 4:
            ptr2 = curr2
        if not curr2.next:
            break
        curr2 = curr2.next
    curr2.next = ptr2
    print("Original (test 2)")
    printll(ll2)
    print("After disconnecting")
    ll2_disconnected = disconnectCycle(ll2)
    printll(ll2_disconnected)
    