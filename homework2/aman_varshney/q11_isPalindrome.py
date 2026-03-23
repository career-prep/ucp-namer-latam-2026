# spent 25 minutes
# Time complexity - O(n)
# Space complexity - O(1)
# Linked list forward backward pointer

class Node:
    """Node struct in python"""
    def __init__(self, data: int, next: Node = None, prev: Node = None) -> None:
        self.data = data
        self.next = next 
        self.prev = prev
        
        
def isPalindrome(dll):
    if not dll:
        return True
    
    front = dll # front pointer
    back = dll # back pointer
    while back.next:
        back = back.next
        
    while front != back and front.prev != back:
        if front.data != back.data:
            return False
        front = front.next
        back = back.prev
        
    return True



if __name__ == '__main__':
    # helper to build list
    def insert(dll, val):
        new_node = Node(val)
        curr = dll
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr
    # helper to print ll
    def printll(dll):
        s = ""
        curr = dll
        while curr:
            s += str(curr.data) + " "
            curr = curr.next
        print(s)
        
        
    # list 1 
    dll1 = Node(9)
    insert(dll1, 2)
    insert(dll1, 4)
    insert(dll1, 2)
    insert(dll1, 9)
    print("Linked list (doubly)")
    printll(dll1)
    print("isPalindrome actual: ", isPalindrome(dll1))
    print("isPalindrom expected:, True")
    
    # list 2
    dll2 = Node(9)
    insert(dll2, 12)
    insert(dll2, 4)
    insert(dll2, 2)
    insert(dll2, 9)
    print("Linked list (doubly)")
    printll(dll2)
    print("isPalindrome actual: ", isPalindrome(dll2))
    print("isPalindrom expected:, False")
    