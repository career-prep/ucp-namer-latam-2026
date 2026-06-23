# Array/String Technique: Dynamic programming - Tabulation
# Time Complexity: O(N^2) 
# Space Complexity: O(N) 

def numTrees(n: int) -> int:
    C = [0] * (n + 1)
    C[0] = 1
    for i in range(1, n + 1):
        for j in range(i):
            C[i] += C[j] * C[i - 1 - j]
    return C[n]

if __name__ == "__main__":
    print("Unique BST structures for N=3:", numTrees(3))
    print("Unique BST structures for N=4:", numTrees(4))

# Time Spent: 15 minutes