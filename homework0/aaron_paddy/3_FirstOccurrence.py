#SPACE COMPLEXITY: 0(N) TIME COMPLEXITY: 0(N)

from collections import defaultdict
def first_occurrence(word):
    dict = defaultdict(int)
    new_word = ""
    for n in word:
        dic[n] += 1
    for key in dic:
        new_word += key    
    return new_word


def test_cases():
    assert first_occurrence("") == ""
    assert first_occurrence("Banana banana") == "Ban b"
    assert first_occurrence("streets") == "stre"
    assert first_occurrence("s") == "s"
    
if __name__ == "__main__":
    test_cases()
    print("All test cases passed successfully")
    
#TIME SPENT = 18 minutes
    