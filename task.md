Uber Career Prep Homework Assignment 4
Due: June 15, 2026
Trie & Repeated Computation Problem-Solving Techniques
These questions should be completed without Googling the answer, which in most cases is easily available on the internet. That would defeat the point of the assignment, which is for you to practice interviewing skills. You use your own knowledge as it stands. There are two exceptions to this rule. Firstly, if you are unsure of syntax (e.g., method names, constructor arguments, etc.), you may look it up. Secondly, if you do not know a term, you may look it up. In some cases, depending on your academic schedule, you may not yet have covered a data structure yet, in which case we encourage you to learn and study the general concepts before attempting the problem.
Some questions may seem vague. This is intentional, as interview questions are often vague. Avoid making unnecessary assumptions, including based on example input/output, which is not exhaustive. If you must make an assumption, state your assumption in a comment in your code.
Trie & Repeated Computation Problem-Solving Techniques
Part 1: Data Structure Implementation (~40 min)
Instructions
Question 1: Build a Trie
Part 2: “10%” Technique Problems (~5 hrs, 20 min)
Instructions
Question 2: Boggle
Question 3: RunningMedian
Question 4: Catalan Numbers
Question 5: MinCostStairClimbing
Question 6: WordBreak
Question 7: LargestSquareOf1s
Question 8: CoinChange
Question 9: AdoptAPet

Part 1: Data Structure Implementation (~40 min)
Instructions
If you are unfamiliar with tries, please read the following articles before attempting the problems. Read the descriptions of how the methods work, but stop before the implementation.
Trie: Overview
Trie: Insert & Search
Trie: Delete
You’re welcome to consult other internet resources on the definition and use cases of, but do not read any implementations before attempting these problems. (If you’ve seen or created implementations in the past, of course that’s okay, but do these problems without consulting them.)

If you are stuck when you reach the time limit, please get help from your mentor to complete it; you will need this implementation for the subsequent problems.
Question 1: Build a Trie
Implement a trie class, including the insert, search, and delete methods. Your class should adhere to the following API, adjusted appropriately for your language of choice.

struct TrieNode {
vector<struct TrieNode \*> children; // a (resizable or fixed size) array of size 26
bool validWord; // boolean to indicate if this node marks the end of a word
};

class Trie {
struct TrieNode\* root;

void insert(string word); // adds a word to the trie
bool isValidWord(string word); // returns a boolean indicating whether word is in the trie
void remove(string word); // removes word, from the trie & deletes unused nodes
}

Part 2: “10%” Technique Problems (~5 hrs, 20 min)
Instructions
For each problem, identify the appropriate array/string technique from Workshop 4. State the technique in a comment at the top of your file. As a reminder, the options are:
Trie as a parameter
Dynamic programming
Tabulation
Memoization
Multiple query techniques:
Save state
Pre-process: sort, then binary search
Maintain a queue
Regular
Priority
Double-ended (deque)
Maintain two heaps
Then, write a function to solve the problem and write test cases to check your function. When run, the file you submit should execute your function on your test cases (e.g., through a main method, if applicable in your language). State the time and space complexity of your solution in a comment at the top of your file.

Time how long you spend on each problem. You should actively work on each problem for a MAXIMUM of 40 minutes. Once 40 minutes has elapsed, submit whatever you have, regardless of whether you are finished. Please indicate in a comment at the bottom of your file how long you spent on the problem. It is important that you are honest about how long each problem took you as it will help your mentor help you!
Question 2: Boggle
Boggle is a word game in which players compete to find the most words on a square grid of random letters. Valid words must be at least three characters and formed from non-overlapping (i.e., a position on the board can only be used once in a word) adjacent (including diagonal) letters. Given a Boggle board and a dictionary of valid words, return all valid words on the board.

Example:
Dictionary:

Ace
Ape
Cape
Clap
Clay
Gape
Grape
Lace
Lap
Lay
Mace
Map
May
Pace
Pay
Race
Rap
Ray
Tap
Tape
Trace
Trap
Tray
Yap

Board:

A
D
E
R
C
P
L
A
Y

Ouput:

Ace
Race
Pace
Lace
Pay
Lay
Clay
Ray
Lap
Rap
Clap
Ape
Cape
Yap

Question 3: RunningMedian
You are given an array of numbers representing a stream received one by one. Return an array representing the median after each new number is received.

Example:
Input: 1, 11, 4, 15, 12
Output: 1, 6, 4, 7.5, 11

Question 4: Catalan Numbers
The Catalan numbers are a mathematical sequence of numbers. The nth Catalan number is defined as (2n)! / (n+1)!n!. Given a non-negative integer n, return the Catalan numbers 0-n.

Examples:
Input: 1
Output: 1, 1

Input: 5
Output: 1, 1, 2, 5, 14, 42

Question 5: MinCostStairClimbing
A staircase on a hiking trail implements a rather unusual toll system to cover trail maintenance costs. Each stair in the staircase has a different toll which you only have to pay if you step on that stair. Due to the height of the stairs, you can only climb one or two stairs at once. This means that from the ground you must initially step on either stair 0 or stair 1 and that, if there are n stairs, the last stair you step on can be either stair n-1 or n-2. Given an array representing the costs per stair, what is the minimum possible toll you can pay to climb the staircase?

Examples:
Input: [4, 1, 6, 3, 5, 8]
Output: 9 (step on stairs 1, 3, 4 for a cost of 1+3+5)

Input: [11, 8, 3, 4, 9, 13, 10]
Output: 25 (step on stairs 1, 3, 5 for a cost of 8+4+13)

Question 6: WordBreak
Given a string of characters without spaces and a dictionary of valid words, determine if it can be broken into a list of valid words by adding spaces.

Dictionary:

Elf
Go
Golf
Man
Manatee
Not
Note
Pig
Quip
Tee
Teen

Input: mangolf
Output: True ("man", "golf")

Input: manateenotelf
Output: True ("manatee", "not", "elf")

Input: quipig
Output: False

Question 7: LargestSquareOf1s
Given a square matrix of 0s and 1s, find the dimension of the largest square consisting only of 1s.

Examples: (squares corresponding to output are highlighted for readability)
Input:

0
1
0
1
0
0
1
1
0
1
1
1
0
0
1
1

Output: 2

Input:

0
1
0
1
1
0
0
1
1
1
1
1
1
1
1
1
1
1
1
1
0
1
1
0
0

Output: 3

Question 8: CoinChange
Given a list of coin denominations and a target sum k, return the number of possible ways to make change for that sum.

Examples:
Input:
Coins: [2, 5, 10]

Sum: 20
Output: 6 (Options are: 10 2s; 4 5s; 2 10s; 5 2s & 2 5s; 5 2s & 1 10; 2 5s & 1 10)

Sum: 15
Output: 3 (Options are: 5 2s & 1 5; 1 5 & 1 10; 3 5s)

Question 9: AdoptAPet
An animal shelter that houses cats and dogs wants to ensure no pet has to wait too long for a forever home. Therefore, anyone who comes to adopt a pet can pick the species (cat or dog) but not the specific animal; they are assigned the animal of that species that has been in the shelter longest. If there are no animals available of the desired species, they must take the other species. You are given a list of pets in the shelter with their names, species, and time in the shelter at the start of a week. You receive a sequence of incoming people (to adopt pets) and animals (new additions to the shelter) one at a time. Print the names and species of the pets as they are adopted out.

Example (input and output forms one sequence of sample input):
Initial Input:
Sadie, dog, 4 days
Woof, cat, 7 days
Chirpy, dog, 2 days
Lola, dog, 1 day

Input: Bob, person, dog
Output: Sadie, dog

Input: Floofy, cat
Output:

Input: Sally, person, cat
Output: Woof, cat

Input: Ji, person, cat
Output: Floofy, cat

Input: Ali, person, cat
Output: Chirpy, dog
