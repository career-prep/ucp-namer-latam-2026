# Technique: Deque using doubly linked list
# Time Complexity:
# - add_front: O(1)
# - add_back: O(1)
# - remove_front: O(1)
# - remove_back: O(1)
# - peek_front: O(1)
# - peek_back: O(1)
# - is_empty: O(1)
# - size: O(1)
#
# Space Complexity:
# - O(n) to store n elements
# - O(1) extra space per operation


class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None
        self.prev = None


class Deque:
    def __init__(self):
        self.front_node = None
        self.back_node = None
        self.item_count = 0

    def is_empty(self) -> bool:
        
        return self.front_node is None

    def size(self) -> int:
        
        return self.item_count

    def add_front(self, value: int) -> None:
        
        new_node = Node(value)

        if self.front_node is None:
            self.front_node = new_node
            self.back_node = new_node
        else:
            new_node.next = self.front_node
            self.front_node.prev = new_node
            self.front_node = new_node

        self.item_count += 1

    def add_back(self, value: int) -> None:
       
        new_node = Node(value)

        if self.back_node is None:
            self.front_node = new_node
            self.back_node = new_node
        else:
            self.back_node.next = new_node
            new_node.prev = self.back_node
            self.back_node = new_node

        self.item_count += 1

    def remove_front(self) -> int:
        """
        Remove and return the front value.
        Raises ValueError if the deque is empty.
        """
        if self.front_node is None:
            raise ValueError("Deque is empty")

        removed_value = self.front_node.value
        self.front_node = self.front_node.next
        self.item_count -= 1

        if self.front_node is None:
            self.back_node = None
        else:
            self.front_node.prev = None

        return removed_value

    def remove_back(self) -> int:
        """
        Remove and return the back value.
        Raises ValueError if the deque is empty.
        """
        if self.back_node is None:
            raise ValueError("Deque is empty")

        removed_value = self.back_node.value
        self.back_node = self.back_node.prev
        self.item_count -= 1

        if self.back_node is None:
            self.front_node = None
        else:
            self.back_node.next = None

        return removed_value

    def peek_front(self) -> int:
        """
        Return the front value without removing it.
        Raises ValueError if the deque is empty.
        """
        if self.front_node is None:
            raise ValueError("Deque is empty")

        return self.front_node.value

    def peek_back(self) -> int:
        """
        Return the back value without removing it.
        Raises ValueError if the deque is empty.
        """
        if self.back_node is None:
            raise ValueError("Deque is empty")

        return self.back_node.value

    def to_list(self) -> list[int]:
        
        values = []
        current_node = self.front_node

        while current_node is not None:
            values.append(current_node.value)
            current_node = current_node.next

        return values


def run_tests() -> None:
    deque = Deque()

    # empty deque checks
    assert deque.is_empty() is True
    assert deque.size() == 0
    assert deque.to_list() == []

    # add to front and back
    deque.add_front(20)
    assert deque.to_list() == [20]
    assert deque.peek_front() == 20
    assert deque.peek_back() == 20

    deque.add_front(10)
    assert deque.to_list() == [10, 20]
    assert deque.peek_front() == 10
    assert deque.peek_back() == 20

    deque.add_back(30)
    assert deque.to_list() == [10, 20, 30]
    assert deque.peek_front() == 10
    assert deque.peek_back() == 30

    deque.add_back(40)
    assert deque.to_list() == [10, 20, 30, 40]
    assert deque.size() == 4

    # remove from front
    assert deque.remove_front() == 10
    assert deque.to_list() == [20, 30, 40]
    assert deque.peek_front() == 20
    assert deque.peek_back() == 40

    # remove from back
    assert deque.remove_back() == 40
    assert deque.to_list() == [20, 30]
    assert deque.peek_front() == 20
    assert deque.peek_back() == 30

    # continue removing
    assert deque.remove_front() == 20
    assert deque.to_list() == [30]

    assert deque.remove_back() == 30
    assert deque.to_list() == []
    assert deque.is_empty() is True
    assert deque.size() == 0

    # error checks
    try:
        deque.remove_front()
        assert False
    except ValueError:
        pass

    try:
        deque.remove_back()
        assert False
    except ValueError:
        pass

    try:
        deque.peek_front()
        assert False
    except ValueError:
        pass

    try:
        deque.peek_back()
        assert False
    except ValueError:
        pass

    print("All tests passed")


if __name__ == "__main__":
    run_tests()