# Runtime: O(n)
# Space complexity: O(1)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def DedupSortedList(head):
    if not head:
        return None

    curr = head
    while curr and curr.next:
        if curr.data == curr.next.data:
            curr.next = curr.next.next
        else:
            curr = curr.next

    return head

def toList(head):
    curr = head
    result = []
    while curr:
        result.append(curr.data)
        curr = curr.next
    return result

def run_tests():
    # 1. Test standard duplicates
    h1 = Node(1)
    h1.next = Node(2); h1.next.next = Node(2)
    h1.next.next.next = Node(3); h1.next.next.next.next = Node(3); h1.next.next.next.next.next = Node(3)
    h1.next.next.next.next.next.next = Node(4)
    h1 = DedupSortedList(h1)
    assert toList(h1) == [1, 2, 3, 4]
    print("Standard duplicates test passed")

    # 2. Test all same values
    h2 = Node(1)
    h2.next = Node(1); h2.next.next = Node(1)
    h2 = DedupSortedList(h2)
    assert toList(h2) == [1]
    print("All duplicates test passed")

    # 3. Test no duplicates
    h3 = Node(1)
    h3.next = Node(2); h3.next.next = Node(3)
    h3 = DedupSortedList(h3)
    assert toList(h3) == [1, 2, 3]
    print("No duplicates test passed")

    # 4. Test empty list
    assert DedupSortedList(None) is None
    print("Empty list test passed")

    # 5. Test single node
    h5 = Node(10)
    h5 = DedupSortedList(h5)
    assert toList(h5) == [10]
    print("Single node test passed")

run_tests()

# Time spent: 20:20
