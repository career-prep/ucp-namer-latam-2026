from typing import List, Dict

def zero_sum(nums: List[int]) -> int:
    """Count number of pairs that sum to 0, where each index can be used at most once"""

    available: Dict[int, int] = {}
    pairs = 0

    for x in nums:
        complement = -x
        if available.get(complement, 0) > 0:
            pairs += 1
            available[complement] -= 1 # so the complement can't be used again
        else:
            available[x] = available.get(x,0) + 1 #to store x as unpaired
    
    return pairs

def run_tests() -> None:
    assert zero_sum([1, 10, 8, 3, 2, 5, 7, 2, -2, -1]) == 2 
    assert zero_sum([1, 10, 8, 3, -2, 2, 5, 2, -2, -1]) == 3
    assert zero_sum([4, 3, 3, 5, 7, 0, 2, 3, 8, 6]) == 0
    assert zero_sum([4, 3, 3, 5, 7, 0, 2, 3, 8, 0]) == 1

    # edge cases
    assert zero_sum([]) == 0 
    assert zero_sum([0]) == 0
    assert zero_sum([0, 0]) == 1
    assert zero_sum([0, 0, 0, 0]) == 2
    assert zero_sum([2, 2, -2, -2]) == 2

    print("All tests passed")

if __name__ == "__main__":
    run_tests()    