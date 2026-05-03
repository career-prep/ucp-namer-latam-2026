from collections import deque
def main(n):
    res = ["0"]
    if n == 0:
        return res
    count = 1
    queue = deque("1")

    while count < n :
        val = queue.popleft()

        res.append(val)
        queue.append(val+"0")
        queue.append(val+"1")
        count += 1

    return res
print(main(10))
  
