#given an array of int return the sum of unique elemrnts in the array
#seperate each element into a hash set and then add the diffrent hash set elements together

def unique_sum(arr):
    unique_elements = set() #hash set to store unique elements

    for num in arr:
        unique_elements.add(num) #add each element to the hash set

    return sum(unique_elements) #return the sum of unique elements


arr = [1, 10,8,3,2,5,7,2,-2,-1]
print(unique_sum(arr)) #prints 33

#time spent: 14 min
