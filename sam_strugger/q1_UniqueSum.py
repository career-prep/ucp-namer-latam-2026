# This solution has a time complexity of O(n) and a space complexity of O(n)

def main():
    test1 = uniqueSum([1,10,8,3,2,5,7,-2,2,-1])
    print(test1)


def uniqueSum(arr):
    return sum(set(arr))


main()

# This took me about two minutes