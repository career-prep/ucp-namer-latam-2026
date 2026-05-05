# Data Structure: String / List
# Algorithm: String Manipulation
# Time Complexity: O(N) where N is the length of the string
# Space Complexity: O(N) to store the result

def reverseWords(s):
    words = s.split()
    return " ".join(words[::-1])

def main():
    input1 = "Uber Career Prep"
    print(f"Test Case 1 - Input: '{input1}', Result: '{reverseWords(input1)}'")

    input2 = "Emma lives in Brooklyn, New York."
    print(f"Test Case 2 - Input: '{input2}', Result: '{reverseWords(input2)}'")

    input3 = "Hello"
    print(f"Test Case 3 - Input: '{input3}', Result: '{reverseWords(input3)}'")

if __name__ == "__main__":
    main()

# Time Spent: 10 minutes