# 20 minutes
# I don't see a technique for this 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def DedupSortedList(head):
    current = head

    while current.data is not None and current.next is not None:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next

    return head

def _from_list(values):
    if not values:
        return None
    head = Node(values[0])
    cur = head
    for v in values[1:]:
        cur.next = Node(v)
        cur = cur.next
    return head

def _to_list(head):
    out = []
    cur = head
    while cur is not None:
        out.append(cur.data)
        cur = cur.next
    return out

if __name__ == "__main__":
    head = _from_list([1, 2, 2, 4, 5, 5, 5, 10, 10])
    head = DedupSortedList(head)
    print(_to_list(head))

    head1 = _from_list([8,8,8,8])
    head1 = DedupSortedList(head1)
    print(_to_list(head1))