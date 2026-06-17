# Data Structure: Queue
#
# Generate binary strings in order by appending "0" / "1" suffixes to previously
# generated strings, BFS-style. Starting from "1", each dequeued string yields
# the next two by appending "0" and "1". We prepend "0" as the very first answer.
#
# Time complexity:  O(k * L), where L is the length of the longest binary string (~log k).
# Space complexity: O(k * L) for the result and queue.

from collections import deque


def first_k_binary_numbers(k):
    if k <= 0:
        return []
    result = ["0"]
    if k == 1:
        return result
    queue = deque(["1"])
    while len(result) < k:
        s = queue.popleft()
        result.append(s)
        if len(result) == k:
            break
        queue.append(s + "0")
        queue.append(s + "1")
    return result


# test cases
if __name__ == "__main__":
    assert first_k_binary_numbers(5) == ["0", "1", "10", "11", "100"]
    assert first_k_binary_numbers(10) == [
        "0", "1", "10", "11", "100", "101", "110", "111", "1000", "1001"
    ]
    assert first_k_binary_numbers(0) == []
    assert first_k_binary_numbers(1) == ["0"]
    assert first_k_binary_numbers(2) == ["0", "1"]

    print("yay!!")

# Time spent: ~15 minutes
