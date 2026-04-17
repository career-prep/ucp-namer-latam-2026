# Technique: Hash linked list nodes

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def disconnectCycle(head): # Time, Space Complexities: O(n), O(n)
    #1. Handle empty list or single node
    if head is None or head.next is None:
        return head
    
    #2. Use a set to store visited nodes
    visited = set()
    current = head
    
    #3. Add head to the set
    visited.add(head)
    
    #4. Traverse and check if the next node has been seen before
    while current.next is not None:
        if current.next in visited:
            #5. Break the cycle by removing the link to the seen node
            current.next = None
            return head
        
        #6. Mark node as visited and move forward
        current = current.next
        visited.add(current)
        
    return head

def run_test():
    #1. Build list: 10 -> 18 -> 12 -> 9 -> 11 -> 4
    n1 = Node(10)
    n2 = Node(18)
    n3 = Node(12)
    n4 = Node(9)
    n5 = Node(11)
    n6 = Node(4)
    
    #2. Link nodes
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n6
    
    #3. Create cycle (4 points back to 12)
    n6.next = n3
    
    #4. Disconnect and verify
    disconnectCycle(n1)
    
    assert n6.next is None
    print("Test passed: Cycle disconnected.")

if __name__ == "__main__":
    run_test()