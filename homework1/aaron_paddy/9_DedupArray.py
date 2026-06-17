#Time Complexity: O(N)  Space Complexity: O(N)
#Technique Used: Decrement Hashmap Count

from collections import Counter

def dedup_array(array):
    count_nums = Counter(array)
    
    for num, count in count_nums.items():
        while count > 1:
            array.remove(num)
            count -= 1
            
    return array 


array = [0,0,1,4,5,5,5,8,9,9,10,11,15,15]
print(dedup_array(array))


def test_cases():
    assert dedup_array([0,0,1,4,5,5,5,8,9,9,10,11,15,15]) == [0, 1, 4, 5, 8, 9, 10, 11, 15]
    assert dedup_array([1,1,1,2,2,3,4,5,5,5]) == [1,2,3,4,5]
    assert dedup_array([1,2,3]) == [1,2,3]
    
if __name__ == "__main__":
    test_cases()
    print("All test cases passed successfully!")

#Time Spent: 11 mins
    
    
