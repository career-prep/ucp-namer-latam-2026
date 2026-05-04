#time complexity: O(n)

def FirstKBinaryNumbers(k):
    if k <= 0:
        return None

    binary = ['0'] * k 

    for i in range(1, k):
        binary[i] = str(bin(int(binary[i-1],2) + 1))[2:]

    return binary

#test cases
k=0
print(f"k=0, {FirstKBinaryNumbers(k)}")
k=1
print(f"k=0, {FirstKBinaryNumbers(k)}")
k=5
print(f"k=0, {FirstKBinaryNumbers(k)}")
#time spent: 5min