#Time Complexity: O(N) Space Complexity: O(N)
#Technique Used: Sort the array and solve

def merge_intervals(intervals):
    res = []
    intervals.sort(key=lambda x : x[0])
    print(intervals)
    
    interval = intervals[0]
    for i in range(1, len(intervals)):
        if interval[1] >= intervals[i][0]:
            interval = interval[0], max(intervals[i][1], interval[1])
        else:
            res.append(interval)
            interval = intervals[i]
    
    res.append(interval)       
    return res            
            
            
intervals = [(10,12), (5,6), (7,9), (1,3)]
print(merge_intervals(intervals))


def test_cases():
    assert merge_intervals([(2,3), (4,8), (1,2), (5,7), (9,12)]) == [(4,8), (1,3), (9,12)]
    assert merge_intervals([(5,8), (6,10), (2,4), (3,6)]) == [(2,10)]
    assert merge_intervals([(10,12), (5,6), (7,9), (1,3)]) == [(10,12), (5,6), (7,9), (1,3)]
    
if __name__ == "__main__":
    test_cases()
    print("All test cases passed successfully!")

#time spent: 34 mins