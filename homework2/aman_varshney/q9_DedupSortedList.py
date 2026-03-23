# spent 10 minutes
# Time complexity - O(n)
# Space complexity - O(n)

class Node:
    """Node struct in python"""
    def __init__(self, data: int, next: Node = None) -> None:
        self.data = data
        self.next = next 
        
        
def dedupLinkedList(ll):
    """Removes duplicates from a linked list"""
    if not ll:
        return None
    
    first = ll
    curr = first.next
    while curr:
        if first.data == curr.data: # duplicate so remove
            first.next = curr.next
            curr = curr.next
        else: # move pointers by 1
            first = curr
            curr = curr.next
        
    return ll
    
    
    
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
        
        
        
    # make list1
    ll1 = Node(1)
    insert(ll1, 2)
    insert(ll1, 2)
    insert(ll1, 4)
    insert(ll1, 5)
    insert(ll1, 5)
    insert(ll1, 5)
    insert(ll1, 10)
    insert(ll1, 10)
    print("Original: ")
    printll(ll1)
    # remove duplicates
    dedupLinkedList(ll1)
    # print
    print("After Dedup")
    printll(ll1)
    
    print()
    
    # make list2
    ll2 = Node(8)
    insert(ll2, 8)
    insert(ll2, 8)
    insert(ll2, 8)
    printll(ll2)
    # remove duplicates
    dedupLinkedList(ll2)
    # print
    print("After Dedup")
    printll(ll2)
    
    