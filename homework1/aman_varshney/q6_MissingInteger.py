# spent < 10 min
# one directional running computation
# Time Complexity - O(n) 
# Space Complexity - O(1)


def missingInteger(arr, n):
    count = 1
    for num in arr:
        if num != count:
            return count
        count += 1
    return n
    
    
    
    
if __name__ == "__main__":
    input_arrs = [
        [1,2,3,4],
        [1,2,3,4,6,7],
        [1],
        [1,2,3,4,5,6,7,8,10,11,12]
    ]
    input_ns = [
        5,
        7,
        2,
        12
    ]
    expected = [
        5,
        5,
        2,
        9
    ]
    
    for i in range(len(input_arrs)):
        print("expected:", expected[i])
        print("actual:", missingInteger(input_arrs[i], input_ns[i]))
        print()