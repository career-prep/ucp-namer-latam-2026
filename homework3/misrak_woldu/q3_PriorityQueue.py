# Data Structure: Priority Queue using Max Heap
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

    def peek(self) -> str:
        if self.is_empty():
            raise ValueError("Priority Queue is empty")

        return self.heap[0][0]

    def enqueue(self, data: str, priority: int) -> None:
        self.heap.append((data, priority))
        self._heapify_up(len(self.heap) - 1)

    def dequeue(self) -> str:
        if self.is_empty():
            raise ValueError("Priority Queue is empty")

        highest_priority_data = self.heap[0][0]
        last_item = self.heap.pop()

        if not self.is_empty():
            self.heap[0] = last_item
            self._heapify_down(0)

        return highest_priority_data

    def _heapify_up(self, current_index: int) -> None:
        while current_index > 0:
            parent_index = (current_index - 1) // 2

            if self.heap[parent_index][1] >= self.heap[current_index][1]:
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
            highest_priority_index = current_index

            if (
                left_child_index < heap_size
                and self.heap[left_child_index][1] > self.heap[highest_priority_index][1]
            ):
                highest_priority_index = left_child_index

            if (
                right_child_index < heap_size
                and self.heap[right_child_index][1] > self.heap[highest_priority_index][1]
            ):
                highest_priority_index = right_child_index

            if highest_priority_index == current_index:
                break

            self.heap[current_index], self.heap[highest_priority_index] = (
                self.heap[highest_priority_index],
                self.heap[current_index],
            )

            current_index = highest_priority_index


def run_tests() -> None:
    pq = PriorityQueue()

    assert pq.is_empty() is True
    assert pq.size() == 0

    pq.enqueue("send email", 5)
    pq.enqueue("fix bug", 10)
    pq.enqueue("write notes", 3)
    pq.enqueue("submit homework", 8)

    assert pq.peek() == "fix bug"
    assert pq.size() == 4

    assert pq.dequeue() == "fix bug"
    assert pq.dequeue() == "submit homework"
    assert pq.dequeue() == "send email"
    assert pq.dequeue() == "write notes"

    assert pq.is_empty() is True

    pq.enqueue("task one", 2)
    pq.enqueue("task two", 2)
    assert pq.dequeue() in {"task one", "task two"}
    assert pq.dequeue() in {"task one", "task two"}

    pq.enqueue("single task", 100)
    assert pq.peek() == "single task"
    assert pq.dequeue() == "single task"

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

# Time spent: 35 minutes