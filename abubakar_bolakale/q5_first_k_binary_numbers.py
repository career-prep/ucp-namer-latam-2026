# Data structure: Deque (queue)
# Algorithm: Generate breadth-first over binary strings

from collections import deque


def first_k_binary(k):
    if k == 0:
        return []
    out = ["0"]
    if k == 1:
        return out
    q = deque(["1"])
    while len(out) < k:
        s = q.popleft()
        out.append(s)
        q.append(s + "0")
        q.append(s + "1")
    return out


if __name__ == "__main__":
    print("=== Spec k=5 ===")
    print(" ", first_k_binary(5))

    print("=== Spec k=10 ===")
    print(" ", first_k_binary(10))

    print("=== Edge k=0 ===")
    print(" ", first_k_binary(0))

    print("=== Edge k=1 ===")
    print(" ", first_k_binary(1))

    print("=== Edge k=2 ===")
    print(" ", first_k_binary(2))

    print("=== Length check k=15 ===")
    out = first_k_binary(15)
    print(" ", len(out), out[-1])


# Time complexity: O(k)
# Space complexity: O(k)
# Time spent: 30 minutes
