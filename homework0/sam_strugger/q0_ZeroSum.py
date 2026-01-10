# The first solution has a time complexity of O(n), the second has a time complexity of O(n^2)
# and I attempted a second solution with a time complexity of O(n).
#This is largely a hash map/dictionary problem. 


def main():
    test1 = zeroSum([1,10,8,3,2,5,7,2,-2,-1])
    print(test1)

    test2 = zeroSum([1,10,8,-2,2,5,7,2,-2,-1])
    print(test2) # <-- Had trouble getting the right answer for this test case within the 40 minutes

    test3 = zeroSum_follow_up([1,10,8,3,2,5,7,2,-2,-1])
    print(test3)

    test4 = zeroSum_follow_up([1,10,8,-2,2,5,7,2,-2,-1])
    print(test4)

    test5 = zeroSum_follow_up2([1,10,8,3,2,5,7,2,-2,-1])
    print(test5)

    test6 = zeroSum_follow_up2([1,10,8,-2,2,5,7,2,-2,-1])
    print(test6)



def zeroSum(arr):
    pairs = {}
    return_pairs = []
    for num in arr:
        need = 0 - num
        if need not in pairs:
            pairs[need] = 1
        else:
            pairs[need] +=1
             
        if num in pairs and pairs[need] > 0:
            return_pairs.append([need, num])
            pairs[need] -= 1

    return return_pairs




# Brute force solution to the follow up question
def zeroSum_follow_up(arr):
    pairs = 0
    for num in arr:
        need = 0 - num
        for num2 in arr:
            if num2 == need:
                pairs+=1

    return pairs

def zeroSum_follow_up2(arr): # Another attempt at a cleaner solution for the follow up
    pairs = 0
    for num in arr:
       need = 0 - num
       if need in arr:
           pairs+=1
    return pairs


main()

# I used the full 40 minutes to solve. 


