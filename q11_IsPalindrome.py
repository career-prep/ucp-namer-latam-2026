# Time: 23 minutes
# Technqiue: Doubly linked list forward-backward two-pointer
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def IsPalindrome(head, tail):

    left = head
    right = tail

    while left != right:
        if left.data != right.data:
            return False
        left = left.next
        right = right.prev
    
    return True

def building(values):
    if not values:
        return (None, None)

    head = Node(values[0])
    cur = head
    for v in values[1:]:
        nxt = Node(v)
        cur.next = nxt
        nxt.prev = cur
        cur = nxt
    tail = cur
    return (head, tail)

if __name__ == "__main__":
    head, tail = building([9, 2, 4, 2, 9])
    print(IsPalindrome(head, tail))

    head1, tail1 = building([9, 12, 4, 2, 9])
    print(IsPalindrome(head1, tail1))