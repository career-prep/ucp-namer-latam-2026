# ucp-namer-latam-2026 HW0


## Q1: Zero Sum
**Problem Type:** Set 
**Time Spent:** 10 minutes
**Approach:** 
- Initialize a visited set to track which numbers we have seen already
- Initialize a variable to count the number of valid pairs
- Iterate through the array
    - Multiply number by -1 to get its negative form
    - If the number is in the visited set, remove it from the set and increment the counter
    - If the number is not in the visited set, add it
- Return the counter
**Time Complexity:** O(n)
**Space Complexity:** O(n)


## Q1: Zero Sum Followup
**Problem Type:** Set 
**Time Spent:** 5 minutes
**Approach:** 
- Initialize a visited set to track which numbers we have seen already
- Initialize a variable to count the number of valid pairs
- Iterate through the array
    - Add the number to the visited set
    - Multiply the number by -1 
    - If the number is in the visited set, increment the counter
- Return the counter
**Time Complexity:** O(n)
**Space Complexity:** O(n)


## Q2: Unique Sum
**Problem Type:** Set 
**Time Spent:** 20 minutes
**Approach:** 
- Initialize a frequency hashmap to track which numbers in array we have seen already and how many times we have seen them
- Initialize a variable to track the unique sum
- Iterate through the numbers in the array
    - If the number is not a key in the hashmap, it is unique so far so add it to the sum and initialize it in the map with a value of 1
    - Else If the number's value in the hashmap is 1, then increment its value and subtract the number amount from the unique sum variable
- Return the unique sum variable
**Time Complexity:** O(n)
**Space Complexity:** O(n)


## Q3: First Occurrence
**Problem Type:** Set 
**Time Spent:** 15 minutes
**Approach:** 
- Initialize a visited set to track which letters we have seen already
- Initialize an empty string
- Iterate through each character of the input string
    - If the character is not in the visited set, then add it to the end of the string and to the visited set
- Return the counter
**Time Complexity:** O(n)
**Space Complexity:** O(n)
