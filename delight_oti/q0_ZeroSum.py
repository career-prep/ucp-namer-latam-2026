from collections import Counter

def ZeroSum(nums):

    '''
    Create an empty dictionary to store counts of numbers using Counter

    Iterate over the dictionary
        If the number is 0:
            Count how many pairs of zeros can be formed
            Add this to pairs

        If the number and its negative both exist in the dictionary:
            Use their frequencies to count how many zero-sum pairs can be formed
            Add this to pairs
    
    return dictionary
    '''

    freq=Counter(nums)
    pairs=0
    
    for num in freq:
        if num == 0:
            pairs += freq[num]//2

        elif num>0 and -num in freq:
            while freq[num]>0 and freq[-num]>0:
                freq[num]-=1
                freq[-num]-=1
                pairs+=1

    return pairs

# Test case
# nums= [1,10,8,3,2,5,7,2,-2,-1]
# output= 2

# nums= [0,0,0,0]
# output= 2


# Follow-up question
def zero_sum_reused(nums):

    '''
    Create an empty dictionary to store frequencies of numbers using Counter

    Iterate over the dictionary
        If the number is 0:
            Count all possible pairs of zeros using its frequency
            Add this to pairs

        If the number and its negative both exist in the dictionary:
            Multiply their frequencies to count all valid zero-sum pairs
            Add this to pairs

    Return pairs
    '''
    freq = Counter(nums)
    pairs = 0

    for num in freq:
        if num == 0:
            pairs += (freq[0]*(freq[0]-1))//2
        
        elif num>0 and -num in freq:
            pairs += freq[num]*freq[-num]
    
    return pairs

# test case
# nums=[2,2,-2,-2]
# output= 4

# nums=[0,0,0,0]
# output= 6
