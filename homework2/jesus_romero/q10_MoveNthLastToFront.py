# Technique: Linked list fixed-distance two-pointer

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def moveNthLastToFront(head, n): # Time, Space Complexities: O(n), O(1)
    #1. Handle edge cases: empty list or list with one node
    if head is None or head.next is None:
        return head
    
    #2. Use two pointers with a fixed distance of 'n' nodes
    fast = head
    slow = head
    
    #3. Move 'fast' pointer 'n' steps ahead
    for _ in range(n):
        if fast is None: # In case n is larger than the list length
            return head
        fast = fast.next
        
    #4. If fast is None after moving n steps, n equals list length (move head)
    if fast is None:
        return head

    #5. Move both pointers until fast reaches the last node
    # Note: We stop one node early so 'slow' is the node BEFORE the nth-last node
    while fast.next is not None:
        fast = fast.next
        slow = slow.next
        
    #6. Identify the nth-last node and its preceding node
    target = slow.next
    
    #7. Sever the target node from its current position
    slow.next = target.next
    
    #8. Move the target node to the front and update its next pointer
    target.next = head
    
    #9. Return the target node as the new head
    return target

#playing w class test instead of =func test
class TestMoveNth:
    def run_tests(self):
        #1. Test k=2: 15->2->8->7->20->9->11->6->19
        # Expected: 6 moves to front
        head = Node(15); curr = head
        vals = [2, 8, 7, 20, 9, 11, 6, 19]
        for v in vals:
            curr.next = Node(v)
            curr = curr.next
            
        new_head = moveNthLastToFront(head, 2)
        assert new_head.data == 6
        assert new_head.next.data == 15
        
        #2. Test k=7: 15->2->8->7->20->9->11->6->19
        
        head = Node(15); curr = head
        for v in vals:
            curr.next = Node(v)
            curr = curr.next
            
        new_head2 = moveNthLastToFront(head, 7)
        assert new_head2.data == 8
        assert new_head2.next.data == 15
        
        print("All tests passed")

if __name__ == "__main__":
    tester = TestMoveNth()
    tester.run_tests()