# Technique: Linked list fixed-distance two-pointer
# Time Complexity: O(n)
# Space Complexity: O(1)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def moveNthLastToFront(self, k):
        if not self or not self.next:
            return self

        fast = self
        slow = self


        for _ in range(k):
            if not fast:
                return self
            fast = fast.next

        if not fast:
            return self

        while fast.next:
            slow = slow.next
            fast = fast.next

        target = slow.next
        if not target:
            return self

        slow.next = target.next

        target.next = self
        return target



# build list: 1 → 2 → 3 → 4 → 5
# head = Node(1)
# n2 = Node(2)
# n3 = Node(3)
# n4 = Node(4)
# n5 = Node(5)

# head.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5

# head = head.moveNthLastToFront(2)

# # print result
# curr = head
# while curr:
#     print(curr.data, end=" → ")
#     curr = curr.next