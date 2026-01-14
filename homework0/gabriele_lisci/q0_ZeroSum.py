#Time Complexity: O(n)
#Space Complexity: O(n)
def zero_sum(numbers):
    result = []
    partner = {}

    for num in numbers:
        if (-num in partner):
            result.append([num, -num])
        else:
            partner[num] = 1
    return len(result)


# #Test Case 1
print(zero_sum([1,10,8,3,2,5,7,2,-2,-1]) == 2)
# #Test Case 2
print(zero_sum([1,10,8,-2,2,5,7,2,-2,-1]) == 3)
# #Test Case 3
print(zero_sum([4,3,3,5,7,0,2,3,8,6]) == 0)
# #Test Case 4
print(zero_sum([4,3,3,5,7,0,2,3,8,0]) == 1)

#Spent 17 minutes

#---------------------------------------------------------------------------------------------------------

#ZeroSum Follow-up Question

#Time Complexity: O(n)
#Space Complexity: O(n)
def zero_sum(numbers):
    result = []
    partner = {}

    for num in numbers:
        if num not in partner:
            partner[num] = 1
        else:
            partner[num] +=1
        if (-num in partner and num != 0):
            multiplicity = partner[-num]
            for i in range(multiplicity):
                result.append([num, -num])
        elif (num==0):
            multiplicity = partner[num] // 2
            for i in range(multiplicity):
                result.append([num, -num])
            

    return len(result)

#Test Case 1
print(zero_sum([1,10,8,3,2,5,7,2,-2,-1]) == 3)
#Test Case 2
print(zero_sum([1,10,8,-2,2,5,7,2,-2,-1]) == 5)
#Test Case 3
print(zero_sum([4,3,3,5,7,0,2,3,8,6]) == 0)
#Test Case 4
print(zero_sum([4,3,3,5,7,0,2,3,8,0]) == 1)

#Spent 21 minutes