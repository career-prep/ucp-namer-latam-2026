#time complexity: O(n)
#space complexity: O(n)

from collections import Counter

def main():
    test1 = [1, 10, 8, 3, 2, 5, 7, 2, -2, -1]
    test2 = [1, 10, 8, -2, 2, 5, 7, 2, -2, -1]
    test3 = [4, 3, 3, 5, 7, 0, 2, 3, 8, 6]
    test4 = [4, 3, 3, 5, 7, 0, 2, 3, 8, 0]
    test5 = [1,1,-1,-1]
    test6 = [1,-1,1,-1,0,0]

    print("test1: ", zerosum(test1))
    print("test2: ", zerosum(test2))
    print("test3: ", zerosum(test3))
    print("test4: ", zerosum(test4))
    print("test5: ", zerosum(test5))

    print("test1 (with duplicates): ", zerosumwrepeats(test1))
    print("test2 (with duplicates): ", zerosumwrepeats(test2))
    print("test3 (with duplicates): ", zerosumwrepeats(test3))
    print("test4 (with duplicates): ", zerosumwrepeats(test4))
    print("test6 (with duplicates): ", zerosumwrepeats(test6))

def zerosum (arr):
    nums = dict()
    count = 0
    for i in arr:
        if -i in nums and nums[-i] > 0:
            count += 1
            nums[-i] -= 1
        else:
            nums[i] = nums.get(i, 0) + 1
    return count

#using frequency maps
def zerosumwrepeats(arr):
    freq = Counter(arr)
    count = 0

    for i in freq:
        if i == 0:
            count += (freq[i] * (freq[i] -1))/2
        elif i > 0 and -i in freq:
            count += freq[i] * freq[-i]

    return int(count)
    
# def zerosumwrepeats (arr):
#     nums = dict()
#     count = 0

#     for i in range(len(arr)):
#         if nums.get(arr[i]*-1) != None:
#             count += nums.get(arr[i]*-1)
#         if nums.get(arr[i]) != None:
#             nums[arr[i]] += 1
#         else:
#             nums[arr[i]] = 1

#     return count
    

if __name__ == "__main__":
    main()

#time spent: 25 mins