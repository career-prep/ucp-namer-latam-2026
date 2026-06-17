def dedup_array(nums):
    """
    Given a sorted array of non-negative ints, remove duplicates in-place so each
    value appears once.

    If you need to keep the array the same length (static-array style),
    pad the leftover spots with -1.

    Time Complexity: O(n)
    Space Complexity: O(1) extra
    """

    if not nums:
        return nums

    # write points to where the next unique value should go
    write = 1

    # Since the array is sorted, duplicates will be next to each other.
    # So we can scan and only write when we see a "new" number.
    for read in range(1, len(nums)):
        if nums[read] != nums[read - 1]:
            nums[write] = nums[read]
            write += 1

    # Optional padding step (matches the prompt's "static array" note)
    for i in range(write, len(nums)):
        nums[i] = -1

    return nums


# Examples
a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(dedup_array(a))  # [1, 2, 3, 4, -1, -1, -1, -1, -1, -1]

b = [0, 0, 1, 4, 5, 5, 5, 8, 9, 9, 10, 11, 15, 15]
print(dedup_array(b))  # [0, 1, 4, 5, 8, 9, 10, 11, 15, -1, -1, -1, -1, -1]

c = [1, 3, 4, 8, 10, 12]
print(dedup_array(c))  # [1, 3, 4, 8, 10, 12]
