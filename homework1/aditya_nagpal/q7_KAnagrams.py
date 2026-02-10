#given 
# two stirng
# an integer k

# need to find:
# if they are k anagrams: made into anagrams by changing at most k char

# solution:
# dic = {a: 1, p: 2, e: 1, l: 1      }  # vizualizing this in the start really helped me built a great approach
# dic = {a: 1, p: 1, e:1, , c:1, h: 1}

# dic = {c:1, a:1, t:1}
# dic = {d:1, o:1, g: 1}

# abs  = 1 in this case 
# if the keys are same sub the values and count the reaminder for each sub
# if they are diff add them doubling count, divide by 2 later

def KAnagrams(str1, str2, k):
    str1 = str1.strip()
    str2 = str2.strip()
    dic = {}
    for ch in str1:
        if ch not in dic:
            dic[ch] = 1
        else:
            dic[ch] += 1

    dic2 = {}
    for ch2 in str2:
        if ch2 not in dic2:
            dic2[ch2] = 1
        else:
            dic2[ch2] += 1

    total = 0
   
    all_keys = set(dic.keys()) | set(dic2.keys())


    for key in all_keys:
        if key in dic and key in dic2:
            total += abs(dic[key] - dic2[key])
        elif key in dic:
            total += abs(dic[key])
        else:
            total += abs(dic2[key])

    return total //2 == k
    # for(key1, val1), (key2, val2) in zip(dic.items(), dic2.items()):
    #     if key1 == key2:
    #         total += abs(val1 - val2)
    #     else:
    #         total2 += abs(val1-val2)

    
print(KAnagrams("apple", "peach", 1))
print(KAnagrams("apple", "peach", 2))
print(KAnagrams("cat", "dog", 3))
print(KAnagrams("debit curd", "bad credit", 1))
print(KAnagrams("baseball", "basketball", 2))     