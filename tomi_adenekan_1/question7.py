"""
two pointer
40 miinutes
time complexity = O(n)
space complexity = O(n)

"""
def main(str1, str2, k):
    l1 = sorted(list(str1))
    l2 = sorted(list(str2))

    i = 0
    j = 0
    count = 0
    while i < len(l1) and j < len(l2):
        if l1[i] == l2[j]:
            count += 1
            i += 1
            j += 1
        elif l1[i] < l2[j]:
            i += 1
        else:
            j += 1

       
    val = max(len(l1), len(l2))

    return count + k == val

str1 = "debit curd"
str2 = "bad credit"

k = 1
print(main(str1, str2, k))
