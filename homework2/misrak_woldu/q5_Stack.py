# Technique: Stack using linked list
# Time Complexity:
# - push: O(1)
# - pop: O(1)
# - peek: O(1)
# - is_empty: O(1)
# - size: O(1)
#
# Space Complexity:
# - O(n) to store n elements in the stack
# - O(1) extra space for each operation


class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        # top_node represents the top of the stack
        self.top_node = None

        # track number of elements
        self.item_count = 0

    def is_empty(self) -> bool:
        
        return self.top_node is None

    def size(self) -> int:
        
        return self.item_count

    def push(self, value: int) -> None:
        
        new_node = Node(value)

        new_node.next = self.top_node
        self.top_node = new_node

        self.item_count += 1

    def pop(self) -> int:
        
        if self.top_node is None:
            raise ValueError("Stack is empty")

        removed_value = self.top_node.value
        self.top_node = self.top_node.next
        self.item_count -= 1

        return removed_value

    def peek(self) -> int:
        
        if self.top_node is None:
            raise ValueError("Stack is empty")

        return self.top_node.value

    def to_list(self) -> list[int]:
        
        values = []
        current_node = self.top_node

        while current_node is not None:
            values.append(current_node.value)
            current_node = current_node.next

        return values


def run_tests() -> None:
    stack = Stack()

    # empty stack checks
    assert stack.is_empty() is True
    assert stack.size() == 0
    assert stack.to_list() == []

    # push elements
    stack.push(10)
    stack.push(20)
    stack.push(30)

    assert stack.is_empty() is False
    assert stack.size() == 3
    assert stack.to_list() == [30, 20, 10]  # LIFO
    assert stack.peek() == 30

    # pop elements
    assert stack.pop() == 30
    assert stack.to_list() == [20, 10]
    assert stack.size() == 2
    assert stack.peek() == 20

    assert stack.pop() == 20
    assert stack.to_list() == [10]
    assert stack.size() == 1
    assert stack.peek() == 10

    assert stack.pop() == 10
    assert stack.to_list() == []
    assert stack.size() == 0
    assert stack.is_empty() is True

    # error checks
    try:
        stack.pop()
        assert False
    except ValueError:
        pass

    try:
        stack.peek()
        assert False
    except ValueError:
        pass

    print("All tests passed")


if __name__ == "__main__":
    run_tests()