# Base Conversion
# O(klog(k)) Time Complexity. We iterate over k numbers, and in each iteration, we convert the current number into its binary representaion by repeatedly dividing by 2,
# meaning each base conversion is O(log(k)) time. We do base conversion k times so the time complexity is O(klog(k)).
# O(klog(k)) Space Complexity because we store k binary strings, and each binary string stores up to log(k) characters.
# Given a number k, return an array of the first k binary numbers, represented as strings.

def fistKBinaryNumbers(k):

    # If k == 0, you cannot return an array of the first k binary numbers UP TO zero... so return an empty array
    if k == 0:
        return []
    
    # I'm noticing that for any number k, the result array needs to be of size k, and the elements inside the result array are in the range 0 to k-1...
    # that means the first element at index 0 is "0", and the last element (if k > 1), should be the binary representation of the number k-1

    # My intuition to solve this problem is to use a for loop, for each iteration we are on, convert the iteration number to its binary representation,
    # and add that binary representation (as a string) to the result array

    # I will convert each number past 0 into its binary representation using base conversion from decimal (base 10) to binary (base 2)
    result = []

    for num in range(k):

        if num == 0:
            result.append("0")
        else:
            # Use Base conversion to convert the number into its binary representation
            # 1. Compute the quotient of n // 2 and n % 2.
            # 2. add the result of n % 2 to an array which will store bits
            # 3. save n as (n // 2) <--- Integer Division
            # repeat until n == 0
            # the binary representation of n is the reverse of the bits array

            bits = []

            n = num

            while n > 0:
                bits.append(str(n % 2))

                n = n // 2

            result.append("".join(reversed(bits)))


    return result




# 36 minutes


# Test Cases

k1 = 5
k2 = 10
k3 = 0
k4 = 1

print(fistKBinaryNumbers(k1))
print(fistKBinaryNumbers(k2))

# My Added Test Cases
print(fistKBinaryNumbers(k3))
print(fistKBinaryNumbers(k4))







