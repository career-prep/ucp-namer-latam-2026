#O(n) time and O(n) space complexity
def firstOccurr(words):
    acc = ""
    counts = set()
    for word in words:
        counts.add(word)
    for word in words:
        if word in counts:
            acc = acc + word
            counts.remove(word)
    return acc

print(firstOccurr("Uber Career Prep"))

#10 minutes