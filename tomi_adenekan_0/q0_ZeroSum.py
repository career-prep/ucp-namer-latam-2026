"""
Time Cmplexity = O(n)
Space Complexity = O(n)
Time used = 40 minutes

"""

def main(array):
    dic = {}
    for each in array:
        if each in dic:
            dic[each] += 1
        else:
            dic[each] = 1
    res = 0
    for key, value in dic.items():
        if  key > 0 and -key in dic:
            val = min(value, dic[-key])
            res += val

    return res

def zeroSUM(lst):
    dic = {}
    for each in lst:
        if each not in dic:
            dic[each] = 1
        else:
            dic[each] += 1

    total = 0
    for key, val in dic.items():
        if key < 0 and -key in dic:
            total += (val * dic[-key])
        if key == 0:
            total += (val * (val -1)) // 2


    return total


lis = [1, 10, 8, 3, 2, 5, 7, 2, -2, -1, 0,0,0]
print(zeroSUM(lis))

lst = [1, 10, 8, -2, 2, 5, 7, 2, -2, -1]
print(main(lst))

lst = [1, 10, 8, 3, 2, 5, 7, 2, -2, -1]
print(main(lst))

