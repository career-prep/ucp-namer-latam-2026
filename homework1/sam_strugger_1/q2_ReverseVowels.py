# this is a forward-backward two pointer problem
# time and space complexity of O(n)

def main():
    test1 = reverseVowels('Uber Career Prep')
    print(test1)

    test2 = reverseVowels('')
    print(test2)

    test3 = reverseVowels('rhythm')
    print(test3)

    test4 = reverseVowels('a')
    print(test4)


def reverseVowels(s):

    if s == '':
        return "Not a valid string"
    if len(s) <= 1:
        return s
            

    vowel_list = set(['a','e','i','o','u','A','E','I','O','U'])


    str_list = list(s)
    i = 0
    j = len(str_list)-1


    while i<j:
        if str_list[i] in vowel_list and str_list[j] in vowel_list:
            voweli = str_list[i]
            str_list[i] = str_list[j]
            str_list[j] = voweli
        elif str_list[j] in vowel_list:
            i+=1
            continue
        elif str_list[i] in vowel_list:
            j-=1
            continue
        i+=1
        j-=1

    return "".join(str_list)

main()

#this took me around 25 minutes