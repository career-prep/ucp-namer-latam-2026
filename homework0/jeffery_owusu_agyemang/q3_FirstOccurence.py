# TIME COMPLEXITY: O(n)
# SPACE COMPLEXITY: O(n)

def first_occurence(word):
    check_set = set()
    result = []
    
    for char in word:
        if char in check_set:
            continue
        check_set.add(char)
        result.append(char)
        
    return ''.join(result)



if __name__ == "__main__":
    print(first_occurence("abracadabra"))     #  abrcd
    print(first_occurence("Uber Career Prep")) # Uber CaP
    print(first_occurence("zzyzx"))           #  zyx
    print(first_occurence(""))                # ""
