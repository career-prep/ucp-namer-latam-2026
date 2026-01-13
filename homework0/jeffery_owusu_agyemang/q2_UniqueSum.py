# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)

def unique_sum(arr):
    new_arr = set(arr)
    return sum(new_arr)



if __name__ == "__main__":
    print(unique_sum([1, 10, 8, 3, 2, 5, 7, 2, -2, -1]))  # 33
    print(unique_sum([4, 3, 3, 5, 7, 0, 2, 3, 8, 6]))    # 35
    print(unique_sum([]))                            # 0