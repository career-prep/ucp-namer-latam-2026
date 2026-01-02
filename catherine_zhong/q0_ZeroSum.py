#time complexity: O(n)
#space complexity: O(n)

def main():
    test1 = [1, 10, 8, 3, 2, 5, 7, 2, -2, -1]
    test2 = [1, 10, 8, -2, 2, 5, 7, 2, -2, -1]
    test3 = [4, 3, 3, 5, 7, 0, 2, 3, 8, 6]
    test4 = [4, 3, 3, 5, 7, 0, 2, 3, 8, 0]

    print("test1: ", zerosum(test1))
    print("test2: ", zerosum(test2))
    print("test3: ", zerosum(test3))
    print("test4: ", zerosum(test4))

    print("test1 (with duplicates): ", zerosumwrepeats(test1))
    print("test2 (with duplicates): ", zerosumwrepeats(test2))
    print("test3 (with duplicates): ", zerosumwrepeats(test3))
    print("test4 (with duplicates): ", zerosumwrepeats(test4))

def zerosum (arr):
    nums = set()
    ans = 0
    for i in range(len(arr)):
        if arr[i]*-1 in nums:
            ans += 1
            nums.remove(arr[i]*-1)
        else:
            nums.add(arr[i])
    return ans

def zerosumwrepeats (arr):
    nums = dict()
    ans = 0

    for i in range(len(arr)):
        if nums.get(arr[i]*-1) != None:
            ans += nums.get(arr[i]*-1)
        if nums.get(arr[i]) != None:
            nums[arr[i]] += 1
        else:
            nums[arr[i]] = 1

    return ans
    

if __name__ == "__main__":
    main()

#time spent: 25 mins