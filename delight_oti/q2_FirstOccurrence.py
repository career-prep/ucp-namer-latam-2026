def FirstOccurrence(string):
    '''
    Read the String
    Create a set to store unique characters as they appear

    iterate over the input string
        if character not in set
            add it to set
    join set to empty string result

    return result
    '''

    seen=set()
    unique_chars=[]

    for char in string:
        if char not in seen:
            seen.add(char)
            unique_chars.append(char)
    result="".join(unique_chars)
    return result

# Testcase1
# string="banana"
# Output="ban"

# Testcase2
# string2="abca"
# Output="abc"
