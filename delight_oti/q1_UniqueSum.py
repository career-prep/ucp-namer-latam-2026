def UniqueSum(arr):
    sum=0
    my_set=set()

    for i in arr:
        if i not in my_set:
            my_set.add(i)
            sum+=i
    return sum
# 10 mins
