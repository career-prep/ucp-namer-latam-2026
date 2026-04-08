# I am honestly unsure of what type of problem this
# This solution has O(n) space complexity and O(nlogn) time complexity since the input is unsorted
def main():
    test1 =  mergeIntervals([[2,3],[4,8],[1,2],[5,7],[9,12]])
    print(test1)
    test2 =  mergeIntervals([[5,8],[6,10],[2,4],[3,6]])
    print(test2)

def mergeIntervals(intervals):
    sorted_intervals = sorted(intervals)
    new_intervals = [sorted_intervals[0]]
    j = 0

    for i in range(len(sorted_intervals)-1):
        next_interval = sorted_intervals[i+1]
        current_interval =  new_intervals[j]

        if current_interval[1] >= next_interval[0]:
            if current_interval[1] < next_interval[1]:
                current_interval[1] = next_interval[1]
            else:
                continue 
        else:
            new_intervals.append(next_interval)
            j+=1
    
    return new_intervals


main()

#this solution took me 35 minutes 