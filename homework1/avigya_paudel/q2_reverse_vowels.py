# TIME COMPLEXITY: O(N) 
# SPACE COMPEXITY: O(1)
# TIME TAKEN: ~7 minutes
# TECHNIQUE: Forward backward two pointer

from turtle import left


def reverse_vowels(input_str):
    """
    returns a string with everything the same as input_str
    except index of vowels are reversed
    """
    vowels = set("AEIOUaeiou")
    input_str = list(input_str)
    left, right = 0, len(input_str)-1

    while left < right:
        if input_str[left] not in vowels:
            left += 1
        elif input_str[right] not in vowels:
            right -= 1
        else:
            input_str[left], input_str[right] = input_str[right], input_str[left]
            left += 1
            right -= 1
    
    return "".join(input_str)


if __name__ == "__main__":
    print(reverse_vowels("Uber Career Prep")) # expected: eber Ceraer PrUp
    print(reverse_vowels("xyz")) # xyz
    print(reverse_vowels("flamingo")) # flominga
    