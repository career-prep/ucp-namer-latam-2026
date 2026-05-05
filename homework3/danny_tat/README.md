# ucp-namer-latam-2026

## UCP Career Prep: Homework 2 Submission - Danny Tat

---

## Question 1: Singly Linked List

- **Problem Type:** Linked List
- **Time Spent:** [35 mins]
- **Complexity Analysis:**
  - insertAtFront — Time and Space: O(1)
  - insertAtBack — Time: O(n) and Space: O(1)
  - insertAfter — Time and Space: O(1)
  - insertBefore — Time: O(n) and Space: O(1)
  - deleteFront — Time and Space: O(1)
  - deleteBack — Time: O(n) and Space: O(1)
  - deleteNode — Time: O(n) and Space: O(1)
  - length — Time: O(n) and Space: O(1)
  - reverseIterative — Time: O(n) and Space: O(1)
  - reverseRecursive — Time: O(n) and Space: O(n) — recursion stack depth is n --

---

## Question 2: Doubly Linked List

- **Problem Type:** Linked List
- **Time Spent:** [20 mins]
- **Complexity Analysis:**
  - insertAtFront — Time and Space: O(1)
  - insertAtBack — Time and Space: O(1)
  - insertAfter — Time and Space: O(1)
  - insertBefore — Time and Space: O(1)
  - deleteFront — Time and Space: O(1)
  - deleteBack — Time and Space: O(1)
  - deleteNode — Time and Space: O(1)
  - length — Time: O(n) and Space: O(1)
  - reverseIterative — Time: O(n) and Space: O(1)
  - reverseRecursive — Time: O(n) and Space: O(n) — recursion stack depth is n --

---

## Question 3: Binary Search Tree

- **Problem Type:** Binary Search Tree
- **Time Spent:** [40 mins]
- **Complexity Analysis:**
  - min — Time: O(log n) avg, O(n) worst and Space: O(1)
  - max — Time: O(log n) avg, O(n) worst and Space: O(1)
  - contains — Time: O(log n) avg, O(n) worst and Space: O(1)
  - insert — Time: O(log n) avg, O(n) worst and Space: O(1)
  - delete — Time: O(log n) avg, O(n) worst and Space: O(log n) — recursion stack --

---

## Question 4: Queue

- **Problem Type:** Queue (backed by Singly Linked List)
- **Time Spent:** [20 mins]
- **Complexity Analysis:**
  - peek — Time and Space: O(1)
  - enqueue — Time and Space: O(1)
  - dequeue — Time and Space: O(1)
  - isEmpty — Time and Space: O(1) --

---

## Question 5: Stack

- **Problem Type:** Stack (backed by Singly Linked List)
- **Time Spent:** [20 mins]
- **Complexity Analysis:**
  - top — Time and Space: O(1)
  - push — Time and Space: O(1)
  - pop — Time and Space: O(1)
  - isEmpty — Time and Space: O(1) --

---

## Question 6: Deque

- **Problem Type:** Deque (backed by Doubly Linked List)
- **Time Spent:** [25 mins]
- **Complexity Analysis:**
  - front — Time and Space: O(1)
  - back — Time and Space: O(1)
  - pushBack — Time and Space: O(1)
  - pushFront — Time and Space: O(1)
  - popFront — Time and Space: O(1)
  - popBack — Time and Space: O(1)
  - isEmpty — Time and Space: O(1) --

---

## Question 7: CopyTree

- **Technique:** Depth-first traversal (Pre-order)
- **Problem Type:** Binary Tree / Recursion
- **Time Spent:** [15 mins]
- **Complexity Analysis:**
  - Time Complexity: O(n) — visit every node once
  - Space Complexity: O(n) — recursion stack + new tree of n nodes --

---

## Question 8: IsBST

- **Technique:** Search Binary Search Tree (BST)
- **Problem Type:** Binary Search Tree / Recursion
- **Time Spent:** [20 mins]
- **Complexity Analysis:**
  - Time Complexity: O(n) — visit every node once
  - Space Complexity: O(n) — recursion stack depth is n in worst case --

---

## Question 9: DedupSortedList

- **Technique:** Linked list fixed-distance two-pointer
- **Problem Type:** Linked List
- **Time Spent:** [13 mins]
- **Complexity Analysis:**
  - Time Complexity: O(n) — single pass through the list
  - Space Complexity: O(1) — modify list in place --

---

## Question 10: MoveNthLastToFront

- **Technique:** Linked list fixed-distance two-pointer
- **Problem Type:** Linked List
- **Time Spent:** [28 mins]
- **Complexity Analysis:**
  - Time Complexity: O(n) — two passes through the list
  - Space Complexity: O(1) — rearrange pointers in place --

---

## Question 11: IsPalindrome

- **Technique:** Doubly linked list forward-backward two-pointer
- **Problem Type:** Doubly Linked List
- **Time Spent:** [22 mins]
- **Complexity Analysis:**
  - Time Complexity: O(n) — traverse from both ends toward the middle
  - Space Complexity: O(1) — use existing prev pointers --

---

## Question 12: DisconnectCycle

- **Technique:** Linked list fast-slow two-pointer
- **Problem Type:** Linked List / Floyd's Cycle Detection
- **Time Spent:** [32 mins]
- **Complexity Analysis:**
  - Time Complexity: O(n) — Floyd's algorithm with two pointers
  - Space Complexity: O(1) — no extra data structures --

---

## Question 13: LeftView

- **Technique:** Level-order (breadth-first) traversal
- **Problem Type:** Binary Tree / BFS
- **Time Spent:** [35 mins]
- **Complexity Analysis:**
  - Time Complexity: O(n) — visit every node once via level-order traversal
  - Space Complexity: O(n) — queue holds up to one level of nodes --

---

## Question 14: FloorInBST

- **Technique:** Search Binary Search Tree (BST)
- **Problem Type:** Binary Search Tree
- **Time Spent:** [36 mins]
- **Complexity Analysis:**
  - Time Complexity: O(log n) avg, O(n) worst — traverse one path down the tree
  - Space Complexity: O(1) — iterative approach with no extra storage