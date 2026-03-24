# Technique: Linked list reset/catch-up two-pointer

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def dedupSortedList(head): # Time, Space Complexities: O(n), O(1)
    #1. Handle empty list or single node
    if head is None:
        return None
    
    current = head
    #2. Traverse the list comparing current node with the next node
    while current.next is not None:
        #3. If data is identical, skip the next node (catch-up technique)
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            #4. Only move the pointer forward if no duplicate was found
            current = current.next
            
    return head

#playing w class test instead of func test
class TestDedup:
    def run_tests(self):
        #1. Test multiple duplicates
        # 1 -> 2 -> 2 -> 4 -> 5 -> 5 -> 5 -> 10 -> 10
        n1 = Node(1)
        n1.next = Node(2); n1.next.next = Node(2)
        n1.next.next.next = Node(4)
        n1.next.next.next.next = Node(5); n1.next.next.next.next.next = Node(5); n1.next.next.next.next.next.next = Node(5)
        n1.next.next.next.next.next.next.next = Node(10); n1.next.next.next.next.next.next.next.next = Node(10)
        
        res1 = dedupSortedList(n1)
        assert res1.data == 1
        assert res1.next.data == 2
        assert res1.next.next.data == 4
        assert res1.next.next.next.data == 5
        assert res1.next.next.next.next.data == 10
        assert res1.next.next.next.next.next is None
        
        #2. Test all identical values
        # 8 -> 8 -> 8 -> 8
        n2 = Node(8); n2.next = Node(8); n2.next.next = Node(8); n2.next.next.next = Node(8)
        res2 = dedupSortedList(n2)
        assert res2.data == 8
        assert res2.next is None

        print("All tests passed")

if __name__ == "__main__":
    tester = TestDedup()
    tester.run_tests()