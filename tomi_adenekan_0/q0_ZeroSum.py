def main(array):
    array.sort()
    dic = {}
    for each in array:
        if each in dic:
            dic[each] += 1
        else:
            dic[each] = 1
    res = 0
    for key, value in dic.items():
        if -key in dic and dic[key] == dic[-key]:
            res += (0.5  * value)

    return int(res)

lst = [1, 10, 8, 3, 2, 5, 7, 2, -2, -1]
print(main(lst))
