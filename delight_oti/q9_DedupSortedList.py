# Technique: Simultaneous iteration two-pointer
# Time Complexity: O(n)
# Space Complexity: O(1)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def DedupSortedList(self):
        curr = self

        while curr and curr.next:
            if curr.data == curr.next.data:
                curr.next = curr.next.next
            else:
                curr = curr.next
        
        return self


# build list: 1 → 2 → 2 → 4 → 5 → 5
# head = Node(1)
# n2 = Node(2)
# n3 = Node(2)
# n4 = Node(4)
# n5 = Node(5)
# n6 = Node(5)

# head.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5
# n5.next = n6

# # run function
# head = head.DedupSortedList()

# # print result
# curr = head
# while curr:
#     print(curr.data, end=" → ")
#     curr = curr.next