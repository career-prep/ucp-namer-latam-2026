# Technique: Linked List Basics
# Time Complexity: Depends on method
# Space Complexity: O(1) extra space for most methods

class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def to_list(self) -> list[int]:
        values = []
        current_node = self.head

        while current_node is not None:
            values.append(current_node.value)
            current_node = current_node.next

        return values
        
    def insert_at_end(self, value: int) -> None:
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = new_node

    def insert_at_end(self, value: int) -> None:
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = new_node

    def insert_at_front(self, value: int) -> None:
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def search(self, target_value: int) -> bool:
        current_node = self.head

        while current_node is not None:
            if current_node.value == target_value:
                return True
            current_node = current_node.next

        return False
    
    def delete_value(self, target_value: int) -> bool:
        if self.head is None:
            return False

        if self.head.value == target_value:
            self.head = self.head.next
            return True

        previous_node = self.head
        current_node = self.head.next

        while current_node is not None:
            if current_node.value == target_value:
                previous_node.next = current_node.next
                return True

            previous_node = current_node
            current_node = current_node.next

        return False
    
    #run tests 
def run_tests() -> None:
    linked_list = SinglyLinkedList()

    linked_list.insert_at_end(10)
    linked_list.insert_at_end(20)
    linked_list.insert_at_end(30)
    assert linked_list.to_list() == [10, 20, 30]

    linked_list.insert_at_front(5)
    assert linked_list.to_list() == [5, 10, 20, 30]

    assert linked_list.search(20) is True
    assert linked_list.search(99) is False

    assert linked_list.delete_value(20) is True
    assert linked_list.to_list() == [5, 10, 30]

    assert linked_list.delete_value(5) is True
    assert linked_list.to_list() == [10, 30]

    assert linked_list.delete_value(99) is False
    assert linked_list.to_list() == [10, 30]

    empty_list = SinglyLinkedList()
    assert empty_list.delete_value(1) is False
    assert empty_list.search(1) is False
    assert empty_list.to_list() == []

    print("All tests passed")

if __name__ == "__main__":
    run_tests()