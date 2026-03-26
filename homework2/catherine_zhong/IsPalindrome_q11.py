#technique: forward-backward two pointers 
#time complexity: O(n)
#space complexity: O(1)

class Node():
    def __init__(self, data):
        self.val = data
        self.next = None
        self.prev = None 

    
def IsPalindrome(head):

    if head is None or head.next is None:
        return True 

    end = head
    while end.next:
        end = end.next

    start = head
    while start != end:
        if start.val != end.val:
            return False
        start = start.next
        end = end.prev

    return True


head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(2)
node5 = Node(1)

head.next = node2
node2.prev = head
node2.next = node3
node3.prev = node2
node3.next = node4
node4.prev = node3
node4.next = node5
node5.prev= node4

print('test1: ')
print(IsPalindrome(head))

head.val = 9
node2.val = 12
node3.val = 4
node4.val = 2
node5.val = 9

print('test2: ')
print(IsPalindrome(head))
    

#time spent: 25min