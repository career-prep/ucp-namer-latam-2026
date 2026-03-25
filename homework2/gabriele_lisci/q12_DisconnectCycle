# Runtime: O(n)
# Space complexity: O(1)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def disconnectCycle(head):
    if not head or not head.next:
        return head

    slow = head
    fast = head
    has_cycle = False
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            has_cycle = True
            break
    if not has_cycle:
        return head

    slow = head

    if slow == fast:
        while fast.next != slow:
            fast = fast.next
    else:
        while slow.next != fast.next:
            slow = slow.next
            fast = fast.next

    fast.next = None

    return head

def toList(head):
    curr = head
    result = []
    while curr:
        result.append(curr.data)
        curr = curr.next
    return result

def run_tests():
    # 1. Test List with Cycle in middle
    h1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    h1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n2 # Cycle

    h1 = disconnectCycle(h1)
    assert toList(h1) == [1, 2, 3, 4]
    print("Middle cycle disconnection passed")

    # 2. Test List with Cycle at Head
    h2 = Node(1)
    h2.next = Node(2)
    h2.next.next = h2 # Cycle

    h2 = disconnectCycle(h2)
    assert toList(h2) == [1, 2]
    print("Head cycle disconnection passed")

    # 3. Test List with No Cycle
    h3 = Node(10)
    h3.next = Node(20)
    h3 = disconnectCycle(h3)
    assert toList(h3) == [10, 20]
    print("No cycle test passed")

    # 4. Test Single Node with self-cycle
    h4 = Node(5)
    h4.next = h4
    h4 = disconnectCycle(h4)
    assert toList(h4) == [5]
    print("Self-cycle test passed")


run_tests()

# Time spent: 40:00
