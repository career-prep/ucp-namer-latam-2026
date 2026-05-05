# Data Structure: Min Heap
# Algorithm: Heapify Up and Heapify Down
# Time Complexity:
# - peek: O(1)
# - insert: O(log n)
# - delete_min: O(log n)
# Space Complexity: O(n)

class MinHeap:
    def __init__(self):
        self.heap = []

    def size(self) -> int:
        return len(self.heap)

    def is_empty(self) -> bool:
        return len(self.heap) == 0

    def peek(self) -> int:
        if self.is_empty():
            raise ValueError("Heap is empty")

        return self.heap[0]

    def insert(self, value: int) -> None:
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def delete_min(self) -> int:
        if self.is_empty():
            raise ValueError("Heap is empty")

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
    min_heap = MinHeap()

    assert min_heap.is_empty() is True
    assert min_heap.size() == 0

    min_heap.insert(10)
    min_heap.insert(4)
    min_heap.insert(15)
    min_heap.insert(1)
    min_heap.insert(7)

    assert min_heap.is_empty() is False
    assert min_heap.size() == 5
    assert min_heap.peek() == 1

    assert min_heap.delete_min() == 1
    assert min_heap.peek() == 4

    assert min_heap.delete_min() == 4
    assert min_heap.delete_min() == 7
    assert min_heap.delete_min() == 10
    assert min_heap.delete_min() == 15

    assert min_heap.is_empty() is True
    assert min_heap.size() == 0

    duplicate_heap = MinHeap()
    duplicate_heap.insert(5)
    duplicate_heap.insert(5)
    duplicate_heap.insert(3)
    duplicate_heap.insert(3)

    assert duplicate_heap.delete_min() == 3
    assert duplicate_heap.delete_min() == 3
    assert duplicate_heap.delete_min() == 5
    assert duplicate_heap.delete_min() == 5

    single_heap = MinHeap()
    single_heap.insert(99)
    assert single_heap.peek() == 99
    assert single_heap.delete_min() == 99
    assert single_heap.is_empty() is True

    try:
        min_heap.peek()
        assert False
    except ValueError:
        pass

    try:
        min_heap.delete_min()
        assert False
    except ValueError:
        pass

    print("All tests passed")


if __name__ == "__main__":
    run_tests()