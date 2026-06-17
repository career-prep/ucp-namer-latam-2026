def first_occ(s):
    """
    create a set to check membership faster
    go through each character in string 
    if that character not in a set -> add it into a set and ans
    else -> continue
    
    """
    seen = set()
    ans = []
    for ch in s:
        if ch not in seen:
            seen.add(ch)
            ans.append(ch)
        
    return "".join(ans)

ex1 = "abracadabra"
expected_ans1 = "abrcd"
print(first_occ(ex1) == expected_ans1)

ex2 = "Uber Career Prep"
expected_ans2 = "Uber CaPp"
print(first_occ(ex2) == expected_ans2)

ex3 = "zzyzx"
expected_ans3 = "zyx"
print(first_occ(ex3) == expected_ans3)