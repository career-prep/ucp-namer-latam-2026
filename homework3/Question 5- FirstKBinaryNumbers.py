# Time: 12 minutes
# used bfs to expand on the tree 
def FirstKBinaryNumbers(x):
    result = ["0"]
    q = ["1"]

    while len(result) < x:
        current = q.pop(0)
        result.append(current)
        q.append(current + "0")
        q.append(current + "1")

    return result

print(FirstKBinaryNumbers(10))
print(FirstKBinaryNumbers(5))