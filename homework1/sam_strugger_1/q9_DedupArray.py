#Two pointer problem
#Time complexity of O(n) and a space complexity of O(1)
def main():
    test1 = debupArray([1,2,2,3,3,3,4,4,4,4,5])
    print(test1)

def debupArray(arr):
    j = 1
    for i in range(1,len(arr)):
        if arr[i] != arr[i-1]:
            arr[j] = arr[i]
            j+=1
    return arr[:j]


main()

# this took me 35 minutes to solve. 
# It took me awhile to find the right logic to solve