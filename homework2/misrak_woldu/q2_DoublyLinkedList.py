# Technique: Doubly Linked List Basics
# Time Complexity: Depends on method
# Space Complexity: O(1) extra space for most methods


class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def to_list(self) -> list[int]:
        values = []
        current_node = self.head

        while current_node is not None:
            values.append(current_node.value)
            current_node = current_node.next

        return values
    
    def insert_at_front(self, value: int) -> None:
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insert_at_back(self, value: int) -> None:
        new_node = Node(value)

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def insert_after(self, location_node: Node, value: int) -> None:
        if location_node is None:
            return

        new_node = Node(value)
        new_node.prev = location_node
        new_node.next = location_node.next

        if location_node.next is not None:
            location_node.next.prev = new_node
        else:
            self.tail = new_node

        location_node.next = new_node

    def insert_before(self, location_node: Node, value: int) -> None:
        if location_node is None:
            return

        if location_node == self.head:
            self.insert_at_front(value)
            return

        new_node = Node(value)
        previous_node = location_node.prev

        new_node.next = location_node
        new_node.prev = previous_node

        previous_node.next = new_node
        location_node.prev = new_node

    def delete_front(self) -> None:
        if self.head is None:
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
            return

        self.head = self.head.next
        self.head.prev = None

    def delete_back(self) -> None:
        if self.tail is None:
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
            return

        self.tail = self.tail.prev
        self.tail.next = None

    def delete_node(self, location_node: Node) -> None:
        if location_node is None:
            return

        if location_node == self.head:
            self.delete_front()
            return

        if location_node == self.tail:
            self.delete_back()
            return

        previous_node = location_node.prev
        next_node = location_node.next

        previous_node.next = next_node
        next_node.prev = previous_node

    def length(self) -> int:
        current_node = self.head
        node_count = 0

        while current_node is not None:
            node_count += 1
            current_node = current_node.next

        return node_count

    def reverse_iterative(self) -> None:
        current_node = self.head
        self.head, self.tail = self.tail, self.head

        while current_node is not None:
            current_node.prev, current_node.next = current_node.next, current_node.prev
            current_node = current_node.prev

    def reverse_recursive(self) -> None:
        self.head, self.tail = self.tail, self.head
        self._reverse_recursive_helper(self.tail)

    def _reverse_recursive_helper(self, current_node: Node) -> None:
        if current_node is None:
            return

        current_node.prev, current_node.next = current_node.next, current_node.prev
        self._reverse_recursive_helper(current_node.prev)

def run_tests() -> None:
    linked_list = DoublyLinkedList()

    linked_list.insert_at_front(10)
    linked_list.insert_at_front(5)
    assert linked_list.to_list() == [5, 10]

    linked_list.insert_at_back(20)
    linked_list.insert_at_back(30)
    assert linked_list.to_list() == [5, 10, 20, 30]

    linked_list.insert_after(linked_list.head.next, 15)  # after 10
    assert linked_list.to_list() == [5, 10, 15, 20, 30]

    linked_list.insert_before(linked_list.tail, 25)  # before 30
    assert linked_list.to_list() == [5, 10, 15, 20, 25, 30]

    assert linked_list.length() == 6

    linked_list.delete_front()
    assert linked_list.to_list() == [10, 15, 20, 25, 30]

    linked_list.delete_back()
    assert linked_list.to_list() == [10, 15, 20, 25]

    middle_node = linked_list.head.next  # 15
    linked_list.delete_node(middle_node)
    assert linked_list.to_list() == [10, 20, 25]

    linked_list.reverse_iterative()
    assert linked_list.to_list() == [25, 20, 10]

    linked_list.reverse_recursive()
    assert linked_list.to_list() == [10, 20, 25]

    empty_list = DoublyLinkedList()
    assert empty_list.to_list() == []
    assert empty_list.length() == 0

    print("All tests passed")


if __name__ == "__main__":
    run_tests()