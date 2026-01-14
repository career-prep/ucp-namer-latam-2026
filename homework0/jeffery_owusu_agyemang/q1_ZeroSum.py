# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)


def ZeroSum(arr):
    freq = {}
    
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    count = 0

    for num in freq:
        if num > 0 and -num in freq:
            count += min(freq[num], freq[-num])
        elif num == 0:
            count += freq[0] // 2

    return count

if __name__ == "__main__":
    print(ZeroSum([1, 10, 8, 3, 2, 5, 7, 2, -2, -1]))   #  2
    print(ZeroSum([1, 10, 8, -2, 2, 5, 7, 2, -2, -1])) # 3
    print(ZeroSum([4, 3, 3, 5, 7, 0, 2, 3, 8, 6]))     # 0
    print(ZeroSum([4, 3, 3, 5, 7, 0, 2, 3, 8, 0]))     # 1


# QUESTION 1: FOLLOW UP

def ZeroSumFollowUp(arr):
    freq = {}

    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    count = 0

    for num in freq:
        if num > 0 and -num in freq:
            count += freq[num] * freq[-num]
        elif num == 0:
            count += freq[0] * (freq[0] - 1) // 2

    return count


if __name__ == "__main__":
    print(ZeroSumFollowUp([1, 10, 8, 3, 2, 5, 7, 2, -2, -1]))   #  3
    print(ZeroSumFollowUp([4, 3, 3, 5, 7, 0, 2, 3, 8, 0])) # 1
   
