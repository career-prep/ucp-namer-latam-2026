# Runtime: O(n)
# Space complexity: O(1)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def MoveNthLastToFront(head, n):
    if not head or n <= 0:
        return head

    dummy = Node(0)
    dummy.next = head

    fast = dummy
    slow = dummy

    for _ in range(n):
        if fast.next:
            fast = fast.next
        else:
            return head

    while fast.next:
        fast = fast.next
        slow = slow.next

    if slow == dummy:
        return head

    nth_node = slow.next
    slow.next = nth_node.next
    nth_node.next = dummy.next
    return nth_node

def toList(head):
    curr = head
    result = []
    while curr:
        result.append(curr.data)
        curr = curr.next
    return result

def run_tests():
    # 1. Test moving middle element to front (2nd from last)
    h1 = Node(1)
    h1.next = Node(2); h1.next.next = Node(3)
    h1.next.next.next = Node(4); h1.next.next.next.next = Node(5)
    h1 = MoveNthLastToFront(h1, 2)
    assert toList(h1) == [4, 1, 2, 3, 5]
    print("Middle element move passed")

    # 2. Test moving the last element to front (1st from last)
    h2 = Node(10)
    h2.next = Node(20); h2.next.next = Node(30)
    h2 = MoveNthLastToFront(h2, 1)
    assert toList(h2) == [30, 10, 20]
    print("Last element move passed")

    # 3. Test n equals list length (no change needed)
    h3 = Node(1)
    h3.next = Node(2); h3.next.next = Node(3)
    h3 = MoveNthLastToFront(h3, 3)
    assert toList(h3) == [1, 2, 3]
    print("Head element move (no-op) passed")

    # 4. Test n out of bounds (larger than length)
    h4 = Node(1)
    h4.next = Node(2)
    h4 = MoveNthLastToFront(h4, 5)
    assert toList(h4) == [1, 2]
    print("Out of bounds n passed")

    # 5. Test single node
    h5 = Node(100)
    h5 = MoveNthLastToFront(h5, 1)
    assert toList(h5) == [100]
    print("Single node test passed")

run_tests()

# Time spent: 40:00
