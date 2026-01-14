def FirstOccurrence(string):
    my_set=set()
    appear=[]

    for i in string:
        if i not in my_set:
            my_set.add(i)
            appear.append(i)
    rtn="".join(appear)
    return rtn
# 20mins
