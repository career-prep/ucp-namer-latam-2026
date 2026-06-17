# Time complexity: O(n)
# Space complexity: O(1)

# Technique: Reset/catch-up two pointer

def DedupArray(arr):
    if not arr:
        return []
    
    write = 1

    for read in range(1, len(arr)):
        if arr[read] != arr[read - 1]:
            arr[write] = arr[read]
            write += 1

    return arr[:write]
        
if __name__ == '__main__':
    inputArr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    # inputArr = []
    # inputArr = [1, 1, 1]
    print("Input Array:", inputArr)
    print("Output:", DedupArray(inputArr))

# ~ time spent: 15 minutes