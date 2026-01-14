def ZeroSum(arr):
    tbr=[]
    used=set()

    for left in range(len(arr)):
        if left in used:
            continue

        vtf=0-arr[left]
        right=left+1
        while right<len(arr):
            if vtf==arr[right]:
                if right not in used and (left,right) not in tbr:
                    tbr.append((arr[left],arr[right]))
                    used.add(left)
                    used.add(right)
                    break
            right+=1
    return len(tbr)
  # 31mins
