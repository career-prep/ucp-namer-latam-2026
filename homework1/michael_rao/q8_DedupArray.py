# method: reset catch-up two pointer
# time: O(n)
# space: O(1)

def dedupArray(arr):
    replace = 1
    for i in range(1,len(arr)):
        if arr[i] != arr[replace-1]:
            arr[replace] = arr[i]
            replace += 1
    
    return arr[:replace]

def checkSolution(arr, correct):
    print("Input Array:", arr)
    print("Correct:", correct)
    print("Output: ", dedupArray(arr))
    print()

checkSolution([1,2,2,3,3,3,4,4,4,4],[1,2,3,4])
checkSolution([0,0,1,4,5,5,8,9,9,10,11,15,15],[0,1,4,5,8,9,10,11,15])
checkSolution([1,3,4,8,10,12],[1,3,4,8,10,12])

# time taken: 10 min