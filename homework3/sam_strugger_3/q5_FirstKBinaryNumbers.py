# I think this is O(nlogn) time complexity and O(n) space

def binaryNumbers(k):
    res = []

    def intToBinary(num):
        if num == 0: 
            return "0"
        result = []
        q = num
        while q > 0:
            result.append(str(q%2))
            q = q // 2
        return "".join(result[::-1])

    for i in range(k):
        bin = intToBinary(i)
        res.append(bin)

    return res

test1 = binaryNumbers(5)
print(test1)

from collections import deque

def binaryNumbers2(k):
    result = ["0"]

    queue = deque()
    queue.append("1")

    for i in range(1,k):
        top = queue.popleft()
        result.append(top)

        queue.append(top+"0")
        queue.append(top+"1")

    return result

test1 = binaryNumbers2(5)
print(test1)


# both solutions together took me 50 minutes 
