# This has a time and space complexity of O(n)
def main():
    test1 = firstOccurence("abracadabra")
    print(test1)

    test2 = firstOccurence("Uber Career Prep")
    print(test2)

def firstOccurence(string):
    seen = set()
    unique_word = ""
    for c in string:
        if c not in seen:
            seen.add(c)
            unique_word+=c
    return unique_word
    

main()

# This took me about 15 minutes 