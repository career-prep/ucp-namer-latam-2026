#one-directional running computation/total
#time complexity: O(n)
#space complexity: O(n)
#24 minutes

def zero_sum_sub_arrays(arr):
    count = 0
    current_sum = 0
    sum_counts = {0: 1} #O(n) space, not forget about the zero
    for num in arr:
        current_sum += num #summing as we go like a happy little bee counting flowers
        if current_sum in sum_counts: #this means that there is a "sum-zero" in between
            count += sum_counts[current_sum] #add the number of times we've seen this sum before
            sum_counts[current_sum] += 1
        else:
            sum_counts[current_sum] = 1
    return count

#test cases

array1 = [4,5,2,-1,-3,-3,4,6,-7]
assert(zero_sum_sub_arrays(array1) == 2)

array2 = [1,8,7,3,11,9]
assert(zero_sum_sub_arrays(array2) == 0)

array3 = [8,-5,0,-2,3,-4]
assert(zero_sum_sub_arrays(array3) == 2)

print("yipee")