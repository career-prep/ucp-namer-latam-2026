#Time: O(n)
#Space: O(n), where n is the length of text 

def first_occurrence(text: str) -> str:
    seen = set()
    res = ""
    for i in text:
        if i not in seen:
            res += i
            seen.add(i)
        else:
            continue
    return res 

def main():
    
    test_cases = [
        ("Netherlands", "Nethrlands"),
        ("fghijk", "fghijk"),
        ("", ""),
        ("ccccc", "c"),
        ("k!g!$?k", "k!g$?")
    ]

    for input_text, expected in test_cases:
        assert first_occurrence(input_text) == expected

    print("All test cases passed!")

if __name__ == "__main__":
    main()
    
#Time taken: 15 minutes
