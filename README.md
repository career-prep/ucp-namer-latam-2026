# Homework 0

---

## Problem 1: Zero Sum

### Approach
- 2 numbers can only add to 0 if they are the same number but opposite signs
- For every number in the list, we see if the negative of that number is in our hash map and if it isn't we add that number to the hash map with value 1. (Value here does not matter)
- If negative of the number is in the hash map, we inrement the result variable by 1 to keep count of total pairs.
- For Follow up, the frequency of the numbers in the list matters. So step 1 would be to create a frequecy hash map.
- Next step would be to iterate over the hash map, and see if the negative value exists in the same hash map (Same logic as before)
- If the value exists, we check if the value is positive (could work for negative as well) so that we do not re use pairs. 
- Then we add the result variable by the product of the frequencies of the positive value and the negative value to account for reusing values (not pairs)
- If the value = 0 then we add the result with the value gotten by this formula (num of zeros * (num of zeros -1)) // 2.

### Time Complexity
- **O(n)**

### Space Complexity
- **O(n)**

### Time Spent
- **30 minutes**
- **35 minutes** for follow up question

---

## Problem 2: Unique Sum

### Approach
- Since we need the result of unique numbers in the list, we convert the list to a set as our first step.
- Then we simply add all the items in the set and return the sum.

### Time Complexity
- **O(n)**

### Space Complexity
- **O(n)**

### Time Spent
- **5 minutes**

---

## Problem 3: First Occurence

### Approach
- Go through the list and for every time we add a string to a hash map, we also add it to the newString.
- If the string is already in the hash map, then we just continue and not perform any actions.
- Return the new string

### Time Complexity
- **O(n)**

### Space Complexity
- **O(n)**

### Time Spent
- **7 minutes**

---

## Notes

- Overall, Zero Sum was the hardest problem where I struggled with the follow up question the most. 
- Biggest Challenge was to handle the edge case of 0's and figuring out how to count how many pairs are there given the reusability of numbers.
