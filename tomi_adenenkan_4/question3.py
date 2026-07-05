

def main(lst):
    leng = len(lst)
    new = [None] * leng
    res = []

    for i in range(leng):
        j = 0
        while j < i and new[j] != None and new[j] < lst[i]:
            j += 1

        print(f"{i} == {j}")
        if i != j:
            new[j], new[i] = lst[i], new[j]
        else:
            new[i] = lst[i]
        print(new)
        val = i//2

        if i%2 == 0:
            res.append(new[val])
        else:
            total = (new[val] + new[val+1])/2
            res.append(total)



    return res


lstt = [1, 11, 4, 15, 12]
print(f"The ressult {main(lstt)}")
