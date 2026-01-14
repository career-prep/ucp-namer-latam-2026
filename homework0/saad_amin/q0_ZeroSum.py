#Time Complexity O(N)
#Space Complexity O(N)

def ZeroSum(arr):
    count = 0
    freq = {}

    for num in arr:
        comp = -num

        if comp in freq and freq[comp] > 0:
            count += 1
            freq[comp] -= 1
        
        else:
            freq[num] = freq.get(num, 0) + 1

    return count

#Testing the function 
if __name__ == "__main__":
    print(ZeroSum([1, 10, 8, 3, 2, 5, 7, 2, -2, -1]))   # Given test case should be two pairs (1, -1) and (2, -2)
    print(ZeroSum([1, 1, -1, -1, 3, -3, 4, -4])) # Should be 4 pairs (1, -1) (2, -2) (3, -3) and (4, -4)
    print(ZeroSum([0, 0, 0, 0])) #Testing all zeros should be two pairs 
    print(ZeroSum([1, 2, 3, 4, 5]))  #No pairs

#Time Complexity O(N)
#Space Complexity O(N)
#Zero Sum follow Up
def ZeroSum2(arr):
    count = 0
    freq = {}

    for num in arr:
        comp = -num

        if comp in freq:
            count += freq.get(comp, 0)
        
        freq[num] = freq.get(num, 0) + 1

    return count

if __name__ == "__main__":
    print(ZeroSum2([1, 10, 8, 3, 2, 5, 7, 2, -2, -1])) #Should be 3 three given pairs (1, -1) (2, -2) and (2, -2)
    print(ZeroSum2([1, 2, -1, -2, 2, 2, 1])) # Should be 5 pairs 2*(1, -1) and 3*(2, -2) pairs
    print(ZeroSum2([0, 0, 0, 0])) # should be 6 pairs

#Time Spent 35 min
