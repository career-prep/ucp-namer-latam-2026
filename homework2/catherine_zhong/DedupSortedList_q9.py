#technique: linked list rest/catch-up two-pointer
#time complexity: O(n)
#space complexity: O(1)

class Node:
    def __init__ (self, data):
        self.val = data
        self.next = None

def printList(head):
    data = []
    current = head
    while current != None:
        data.append(current.val)
        current = current.next

    print(", ".join(str(item) for item in data))

def DedupSortedList(head):
    if head is None:
        return None

    start = head
    end = head.next

    while end:
        while end and end.val == start.val:
            end = end.next

        start.next = end
        start = end

    return head

head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print('list with no duplicates: ')
DedupSortedList(head)
printList(head)

print('list with one duplicate: ')
node5.next = Node(5)
DedupSortedList(head)
printList(head)

node2.val = 1
node3.val = 1
node3.next = None
print('list woth only duplicates: ')
DedupSortedList(head)
printList(head)


#time spent: 20 mins