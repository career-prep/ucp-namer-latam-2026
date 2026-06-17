# this is a binary search problem
# this solution had O(log(n)) time complexity and O(1) space complexity 


def main():
    test1 = missingInteger([1,2,3,4,6,7], 7)
    print(test1)

    test2 = missingInteger([1,2,3,4,5,6,7,8,10,11,12],12)
    print(test2)

    test3 = missingInteger([1],2)
    print(test3)

def missingInteger(nums,n):
    low = 0
    high = n-2

    if n not in set(nums):
        return n
    
    if nums[0] != 1 or n<2:
        return "Invalid inputs"

    while low <= high:
        mid = int((high-low)/2+low)

        high_num = nums[high]
        low_num = nums[low]
        mid_num = nums[mid]

        mid_val = int((high_num-low_num)/2+low_num)

        if mid_num <= mid_val:
            low = mid+1
        else:
            high = mid

        # print(low)
        # print(mid)
        # print(high)
    return low


main()

# this took me 16 minutes to solve