# Data Structure: Priority Queue (Min Heap)
# Algorithm: Heapify Up and Heapify Down
# Time Complexity:
# - enqueue: O(log n)
# - dequeue: O(log n)
# - peek: O(1)
# Space Complexity: O(n)


class PriorityQueue:
    def __init__(self):
        self.heap = []

    def size(self) -> int:
        return len(self.heap)

    def is_empty(self) -> bool:
        return len(self.heap) == 0

    def peek(self) -> int:
        if self.is_empty():
            raise ValueError("Priority Queue is empty")

        return self.heap[0]

    def enqueue(self, value: int) -> None:
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def dequeue(self) -> int:
        if self.is_empty():
            raise ValueError("Priority Queue is empty")

        min_value = self.heap[0]
        last_value = self.heap.pop()

        if not self.is_empty():
            self.heap[0] = last_value
            self._heapify_down(0)

        return min_value

    def _heapify_up(self, current_index: int) -> None:
        while current_index > 0:
            parent_index = (current_index - 1) // 2

            if self.heap[parent_index] <= self.heap[current_index]:
                break

            self.heap[parent_index], self.heap[current_index] = (
                self.heap[current_index],
                self.heap[parent_index],
            )

            current_index = parent_index

    def _heapify_down(self, current_index: int) -> None:
        heap_size = len(self.heap)

        while True:
            left_child_index = 2 * current_index + 1
            right_child_index = 2 * current_index + 2
            smallest_index = current_index

            if (
                left_child_index < heap_size
                and self.heap[left_child_index] < self.heap[smallest_index]
            ):
                smallest_index = left_child_index

            if (
                right_child_index < heap_size
                and self.heap[right_child_index] < self.heap[smallest_index]
            ):
                smallest_index = right_child_index

            if smallest_index == current_index:
                break

            self.heap[current_index], self.heap[smallest_index] = (
                self.heap[smallest_index],
                self.heap[current_index],
            )

            current_index = smallest_index


def run_tests() -> None:
    pq = PriorityQueue()

    assert pq.is_empty() is True
    assert pq.size() == 0

    pq.enqueue(10)
    pq.enqueue(5)
    pq.enqueue(20)
    pq.enqueue(1)

    assert pq.peek() == 1
    assert pq.size() == 4

    assert pq.dequeue() == 1
    assert pq.dequeue() == 5
    assert pq.dequeue() == 10
    assert pq.dequeue() == 20

    assert pq.is_empty() is True

    # test duplicates
    pq.enqueue(3)
    pq.enqueue(3)
    pq.enqueue(2)
    pq.enqueue(2)

    assert pq.dequeue() == 2
    assert pq.dequeue() == 2
    assert pq.dequeue() == 3
    assert pq.dequeue() == 3

    # test single element
    pq.enqueue(100)
    assert pq.peek() == 100
    assert pq.dequeue() == 100

    try:
        pq.peek()
        assert False
    except ValueError:
        pass

    try:
        pq.dequeue()
        assert False
    except ValueError:
        pass

    print("All tests passed")


if __name__ == "__main__":
    run_tests()
