#Is Palindrome
#Time complexity: O(n) where n is the length of the list
#Space Complexity: O(1)
#Technique: Doubly Linked List Forward-Backward Two-Pointer
#Time Spent: 5 minutes


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def IsPalindrome(head, tail):
    if not head or head==tail:
        return True
    
    front = head
    back = tail

    while front.prev != back and front!=back:
        if front.data != back.data:
            return False
        front = front.next
        back = back.prev
    
    return True
     
#Test Cases

# Helper to build a doubly linked list and return (head, tail)
def buildList(values):
    head = Node(values[0])
    curr = head
    for val in values[1:]:
        newNode = Node(val)
        newNode.prev = curr
        curr.next = newNode
        curr = newNode
    return head, curr

#Test case 1
# 1 <-> 2 <-> 3 <-> 2 <-> 1
head1, tail1 = buildList([9, 2, 4, 2, 9])

#Test case 2
# 1 <-> 2 <-> 3 <-> 4 <-> 5
head2, tail2 = buildList([9, 12, 4, 2, 9])

print(IsPalindrome(head1, tail1))
print(IsPalindrome(head2, tail2))