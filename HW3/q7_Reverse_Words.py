"""
    idea: using a stack
        - split each words and put in a list (consider it as a stack)
        - pop from stack, add to new list

"""

def reverse_words(s):
    #stack
    word_list= s.split(" ")
    revered_list=[]

    while word_list:
        revered_list.append(word_list.pop())
    
    return " ".join(revered_list)

