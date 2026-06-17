# Time complexity: O(n)
# Space complexity: O(n)

# Technique: I wasn't exactly sure what there were looking for with this one from the techniques given, you could use a stack I guess?

def ReverseWords(str):
    return " ".join(str.split()[::-1])

if __name__ == "__main__":
    strs = [
        "Uber Career Prep",
        "Emma lives in Brooklyn, New York."
    ]

    for str in strs:
        print(f"Original string: {str}")
        print(f"Reversed words string: {ReverseWords(str)}\n")

# ~ time spent: 10 minutes