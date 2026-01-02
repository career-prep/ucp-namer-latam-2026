#time complexity: O(n)
#space complexity: O(n)

def main():
    test1 = [1, 10, 8, 3, 2, 5, 7, 2, -2, -1]
    test2 = [4, 3, 3, 5, 7, 0, 2, 3, 8, 6]
    test3 = [1, 1, 1, 1, 1]
    test4 = [-1, -2, -3, 3, 4, 3]

    print("test1: ", uniquesum(test1))
    print("test2: ", uniquesum(test2))
    print("test3: ", uniquesum(test3))
    print("test4: ", uniquesum(test4))

def uniquesum(arr):
    nums = set()
    sum = 0
    for i in arr:
        if i not in nums:
            sum += i
            nums.add(i)
    
    return sum


if __name__ == "__main__":
    main()

#time spent:  10 mins