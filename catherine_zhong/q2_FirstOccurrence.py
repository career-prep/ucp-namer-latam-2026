#time complexity: O(n)
#space complexity: O(n)

def main():
    test1 = "abracadabra"
    test2 = "Uber Career Prep"
    test3 = "zzyzx"
    test4 = "Billy Bobby Joe"

    print("test1: ", firstoccurrence(test1))
    print("test2: ", firstoccurrence(test2))
    print("test3: ", firstoccurrence(test3))
    print("test4: ", firstoccurrence(test4))

def firstoccurrence(str):
    result = ""
    for char in str:
        if char not in result:
            result += char
    
    return result

if __name__ == "__main__":
    main()

#time spent:  10 mins