#Time: O(n)
#Space: O(n), where n is the number of items in arr 

from typing import List 

def zero_sum(arr: List[int]) -> int:

    count_dict = {}
    pair_count = 0

    for i in arr:
        if i not in count_dict:
            count_dict[i] = 1
        else:
            count_dict[i] += 1
    
    for i in arr:
        val = -i 
        if val == i and count_dict[val] > 1:
            pair_count += 1
            count_dict[val] -= 2
        elif val in count_dict and count_dict[val] > 0 and count_dict[i] > 0 and val != i :
            pair_count += 1
            count_dict[val] -= 1
            count_dict[i] -= 1
    return pair_count

def main():
    test_cases = [
        ([0,1,2,3,4,5,6,7,8], 0),
        ([], 0),
        ([0,2,3,7,-2,5,0,-7,-3], 4),
        ([3, -3, 3, -3, 5, -5], 3)
    ]

    for input_text, expected in test_cases:
        assert zero_sum(input_text) == expected

    print("All test cases passed!")

if __name__ == "__main__":
    main()

#Time_taken: 40 minutes 
#Follow-up was not completed 


