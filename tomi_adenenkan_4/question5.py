def main(num):
    res = []
    if len(num) == 0:
        return 0
    if len(num) <= 2:
        return min(num)

    res.append(num[0])
    res.append(num[1])

    for n in num[2:]:
        val = min(res[-1] + n, res[-2] + n)
       
        res.append(val)

    return min(res[-1], res[-2])

lst = [11,8,3,4,9,13,10]
 
