#given: 
# integer N, 
# sorted array of INTEGERS: size N - 1
# this array contains all int but one in range(1,N)

# to do:
# find the missing integer

#timetaken: 12mins
# method used: dictionaries
# time and Space complexity: O(n)

#solution
def missingInteger(n, arr):
    # dict1 = {}
    # for i in range(1, n+1):
    #     dict1[i] = 0
    
    # for num in arr:
    #     if num in dict1:
    #         dict1[num] += 1

    # for key, value in dict1.items():
    #     if value == 0:
    #         return key

    lst =[]

    for i in range(1, n+1):
        lst.append(i)

    for num in lst:
        if num not in arr:
            return num


        
print(missingInteger(7, [1, 2, 3, 4, 6, 7]))
print(missingInteger(2, [1]))
print(missingInteger(12, [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12]))