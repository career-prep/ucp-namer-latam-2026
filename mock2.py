import collections
def possibilities(ingredients):
    q = collections.deque()
    q.append([])
    combs = []

    for ingredient in ingredients:
        for _ in range(len(q)):
            curr = q.popleft()
            combs.append(curr)
            q.append(curr + [ingredient])
    return list(q)

print(possibilities(["cheese", "onions", "peppers"]))
