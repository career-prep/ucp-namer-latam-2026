# Data structure: Heap (min-heap)
# Algorithm: k-way merge


import heapq


def merge_k_sorted(arrays):
    h = []
    for i in range(len(arrays)):
        if arrays[i]:
            heapq.heappush(h, (arrays[i][0], i, 0))
    out = []
    while h:
        val, ai, ji = heapq.heappop(h)
        out.append(val)
        if ji + 1 < len(arrays[ai]):
            heapq.heappush(h, (arrays[ai][ji + 1], ai, ji + 1))
    return out


if __name__ == "__main__":
    print("=== Spec k=2 ===")
    print(
        " ",
        merge_k_sorted(
            [
                [1, 2, 3, 4, 5],
                [1, 3, 5, 7, 9],
            ]
        ),
    )

    print("=== Spec k=3 ===")
    print(
        " ",
        merge_k_sorted(
            [
                [1, 4, 7, 9],
                [2, 6, 7, 10, 11, 13, 15],
                [3, 8, 12, 13, 16],
            ]
        ),
    )

    print("=== Empty list of arrays ===")
    print(" ", merge_k_sorted([]))

    print("=== All empty inner arrays ===")
    print(" ", merge_k_sorted([[], [], []]))

    print("=== Single nonempty array ===")
    print(" ", merge_k_sorted([[1, 2, 3]]))

    print("=== Negatives ===")
    print(" ", merge_k_sorted([[-5, 0, 4], [-10, -3]]))

    print("=== Duplicates across arrays ===")
    print(" ", merge_k_sorted([[2, 2], [2, 3]]))


# Time complexity: O(N log k)
# Space complexity: O(N)
# Time spent: 40 minutes
