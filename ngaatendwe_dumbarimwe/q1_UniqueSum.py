#Time: O(n)
#Space: O(1)

from typing import List

def unique_sum(arr: List[int]) -> int:
    if not arr:
        return 0
    return sum(set(arr))

def main():

    test_cases = [
        ([1,2,3,4,5,6,7,8,9,10], 55),
        ([], 0),
        ([2,2,2,2,2,2,2,2,2,2], 2),
        ([4,1,2,2,3,4,4,5,5,5,2], 15)
    ]

    for input_text, expected in test_cases:
        assert unique_sum(input_text) == expected

    print("All test cases passed!")


if __name__ == "__main__":
    main()

#Time taken: 15 minutes