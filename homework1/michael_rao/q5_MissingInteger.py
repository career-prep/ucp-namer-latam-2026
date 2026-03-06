# method: binary search
# time: O(log(n))
# space: O(1)

def missingInteger(arr, n):
    l = 0
    r = len(arr)-1

    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == mid+1:
            l = mid + 1
        else:
            r = mid - 1
        
    return l+1

def checkSolution(arr, n, correct):
    print("Input Array:", arr)
    print("Input n:", n)
    print("Correct:", correct)
    print("Output: ", missingInteger(arr,n))
    print()

checkSolution([1,2,3,4,6,7],7,5)
checkSolution([1],2,2)
checkSolution([1,2,3,4,5,6,7,8,10,11,12],12,9)

# time taken: 10 min