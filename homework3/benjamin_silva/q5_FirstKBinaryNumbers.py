from collections import deque

def firstKBinaryNumbers(k):
    result = []
    queue = deque()

    if k > 0:
        result.append('0')
    queue.append('1')
    while len(result) < k and queue:
        curr = queue.popleft()
        result.append(curr)
        queue.append(curr + '0')
        queue.append(curr + '1')

    
    return result

if __name__ == "__main__":

    print("Test 1 (expect ['0', '1', '10', '11', '100']):")
    print(firstKBinaryNumbers(5))

    print("\nTest 2 (expect ['0', '1', '10', '11', '100', '101', '110', '111', '1000', '1001']):")
    print(firstKBinaryNumbers(10))