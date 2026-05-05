from collections import deque

# Data Structure: Queue
# Algorithm: Breadth-First Generation
# Time Complexity: O(k)
# Space Complexity: O(k)

def first_k_binary_numbers(k: int) -> list[str]:
    if k <= 0:
        return []

    binary_numbers = []
    number_queue = deque(["1"])

    while len(binary_numbers) < k:
        current_binary = number_queue.popleft()
        binary_numbers.append(current_binary)

        number_queue.append(current_binary + "0")
        number_queue.append(current_binary + "1")

    return binary_numbers


def run_tests() -> None:
    assert first_k_binary_numbers(0) == []
    assert first_k_binary_numbers(-3) == []
    assert first_k_binary_numbers(1) == ["1"]
    assert first_k_binary_numbers(2) == ["1", "10"]
    assert first_k_binary_numbers(5) == ["1", "10", "11", "100", "101"]
    assert first_k_binary_numbers(10) == [
        "1", "10", "11", "100", "101",
        "110", "111", "1000", "1001", "1010"
    ]

    print("All tests passed")


if __name__ == "__main__":
    run_tests()
