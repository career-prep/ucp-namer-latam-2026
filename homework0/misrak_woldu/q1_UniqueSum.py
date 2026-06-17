from typing import List, Set

def unique_sum(nums: List[int]) -> int:
    """Return the sum of unique elements in the array"""

    seen: Set[int] = set()
    total = 0 

    for x in nums:
        if x not in seen:
            total += x
            seen.add(x)

    return total

def run_tests() -> None:
      assert unique_sum([1, 10, 8, 3, 2, 5, 7, 2, -2, -1]) == 33
      assert unique_sum([4, 3, 3, 5, 7, 0, 2, 3, 8, 6]) == 35

    #edge cases
      assert unique_sum([]) == 0 
      assert unique_sum([5]) == 5
      assert unique_sum([0, 0, 0]) == 0
      assert unique_sum([-1, -1, 1]) == 0

      print("All tests passed")

if __name__ == "__main__":
     run_tests()           
