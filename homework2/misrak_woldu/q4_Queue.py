# Technique: Queue using linked list
# Time Complexity:
# - enqueue: O(1)
# - dequeue: O(1)
# - peek: O(1)
# - is_empty: O(1)
# - size: O(1)
#
# Space Complexity:
# - O(n) to store n elements in the queue
# - O(1) extra space for each operation


class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        # front_node points to the first item in the queue
        self.front_node = None

        # back_node points to the last item in the queue
        self.back_node = None

        # track how many items are currently in the queue
        self.item_count = 0

    def is_empty(self) -> bool:
    
        return self.front_node is None

    def size(self) -> int:
        
        return self.item_count

    def enqueue(self, value: int) -> None:
       
        new_node = Node(value)

        if self.back_node is None:
            self.front_node = new_node
            self.back_node = new_node
        else:
            self.back_node.next = new_node
            self.back_node = new_node

        self.item_count += 1

    def dequeue(self) -> int:
        
        if self.front_node is None:
            raise ValueError("Queue is empty")

        removed_value = self.front_node.value
        self.front_node = self.front_node.next
        self.item_count -= 1

        # If queue becomes empty after dequeue update back_node too
        if self.front_node is None:
            self.back_node = None

        return removed_value

    def peek(self) -> int:
        
        if self.front_node is None:
            raise ValueError("Queue is empty")

        return self.front_node.value

    def to_list(self) -> list[int]:
        
        values = []
        current_node = self.front_node

        while current_node is not None:
            values.append(current_node.value)
            current_node = current_node.next

        return values


def run_tests() -> None:
    queue = Queue()

    # empty queue checks
    assert queue.is_empty() is True
    assert queue.size() == 0
    assert queue.to_list() == []

    # enqueue elements
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    assert queue.is_empty() is False
    assert queue.size() == 3
    assert queue.to_list() == [10, 20, 30]
    assert queue.peek() == 10

    # dequeue should remove from the front (FIFO)
    assert queue.dequeue() == 10
    assert queue.to_list() == [20, 30]
    assert queue.size() == 2
    assert queue.peek() == 20

    assert queue.dequeue() == 20
    assert queue.to_list() == [30]
    assert queue.size() == 1
    assert queue.peek() == 30

    assert queue.dequeue() == 30
    assert queue.to_list() == []
    assert queue.size() == 0
    assert queue.is_empty() is True

    # error checks
    try:
        queue.dequeue()
        assert False
    except ValueError:
        pass

    try:
        queue.peek()
        assert False
    except ValueError:
        pass

    print("All tests passed")


if __name__ == "__main__":
    run_tests()