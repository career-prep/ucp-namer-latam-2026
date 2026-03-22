# Homework 2 — Samaksh Arora

---

## Part 1: Data Structure Implementations

### Q1 — Singly Linked List
Implement a singly linked list with the following operations: `insertAtFront`, `insertAtBack`, `insertAfter`, `insertBefore`, `deleteFront`, `deleteBack`, `deleteNode`, `length`, `reverseIterative`, `reverseRecursive`.

**insertAtFront**
Time Complexity = O(1)
Space Complexity = O(1)

**insertAtBack**
Time Complexity = O(n)
Space Complexity = O(1)

**insertAfter** (given a node reference)
Time Complexity = O(1)
Space Complexity = O(1)

**insertBefore**
Time Complexity = O(n)
Space Complexity = O(1)

**deleteFront**
Time Complexity = O(1)
Space Complexity = O(1)

**deleteBack**
Time Complexity = O(n)
Space Complexity = O(1)

**deleteNode**
Time Complexity = O(n)
Space Complexity = O(1)

**length**
Time Complexity = O(n)
Space Complexity = O(1)

**reverseIterative**
Time Complexity = O(n)
Space Complexity = O(1)

**reverseRecursive**
Time Complexity = O(n)
Space Complexity = O(n)

---

### Q2 — Doubly Linked List
Implement a doubly linked list with the same operations as above. Because each node holds a `prev` pointer, some operations improve to O(1).

**insertAtFront**
Time Complexity = O(1)
Space Complexity = O(1)

**insertAtBack**
Time Complexity = O(n)
Space Complexity = O(1)

**insertAfter** (given a node reference)
Time Complexity = O(1)
Space Complexity = O(1)

**insertBefore** (given a node reference)
Time Complexity = O(1)
Space Complexity = O(1)

**deleteFront**
Time Complexity = O(1)
Space Complexity = O(1)

**deleteBack** (given tail reference)
Time Complexity = O(1)
Space Complexity = O(1)

**deleteNode**
Time Complexity = O(1)
Space Complexity = O(1)

**length**
Time Complexity = O(n)
Space Complexity = O(1)

**reverseIterative**
Time Complexity = O(n)
Space Complexity = O(1)

**reverseRecursive**
Time Complexity = O(n)
Space Complexity = O(n)

---

### Q3 — Stack
Implement a stack (LIFO) using a linked list with operations: `push`, `pop`, `top`, `isEmpty`.

**push**
Time Complexity = O(1)
Space Complexity = O(1)

**pop**
Time Complexity = O(1)
Space Complexity = O(1)

**top**
Time Complexity = O(1)
Space Complexity = O(1)

**isEmpty**
Time Complexity = O(1)
Space Complexity = O(1)

---

### Q4 — Queue
Implement a queue (FIFO) using a linked list with operations: `enqueue`, `dequeue`, `peek`, `isEmpty`.

**enqueue**
Time Complexity = O(1)
Space Complexity = O(1)

**dequeue**
Time Complexity = O(1)
Space Complexity = O(1)

**peek**
Time Complexity = O(1)
Space Complexity = O(1)

**isEmpty**
Time Complexity = O(1)
Space Complexity = O(1)

---

### Q5 — Deque (Double-Ended Queue)
Implement a double-ended queue using a doubly linked list with operations: `pushFront`, `pushBack`, `popFront`, `popBack`, `front`, `back`, `isEmpty`.

**pushFront**
Time Complexity = O(1)
Space Complexity = O(1)

**pushBack**
Time Complexity = O(1)
Space Complexity = O(1)

**popFront**
Time Complexity = O(1)
Space Complexity = O(1)

**popBack**
Time Complexity = O(1)
Space Complexity = O(1)

**front / back**
Time Complexity = O(1)
Space Complexity = O(1)

**isEmpty**
Time Complexity = O(1)
Space Complexity = O(1)

---

### Q6 — Binary Search Tree
Implement a BST with operations: `insert`, `delete`, `contain`, `min`, `max`.

**insert**
Time Complexity = O(h)
Space Complexity = O(1)

**delete**
Time Complexity = O(h)
Space Complexity = O(1)

**contain**
Time Complexity = O(h)
Space Complexity = O(1)

**min / max**
Time Complexity = O(h)
Space Complexity = O(1)

---

## Part 2: Algorithm Questions

### Q7 — Copy Tree
Given a binary tree, create and return a deep copy with the same structure and values. Uses recursive pre-order traversal.

**Algorithm:** For each node, create a new node with the same value, then recursively do the same for the left and right children. Return `None` when a null node is hit.

Time Complexity = O(n), where n is the number of nodes in the tree (visits every node once)
Space Complexity = O(h), where h is the height of the tree (call stack); O(log n) on average, O(n) worst case for a skewed tree

---

### Q8 — Is BST
Given a binary tree, determine whether it is a valid Binary Search Tree. Uses recursive validation with a running `[low, high]` range for each node.

**Algorithm:** Recursively check each node against a valid range. Going left tightens the upper bound, going right tightens the lower bound. If any node falls outside its range, return `False`.

Time Complexity = O(n), where n is the number of nodes in the tree (visits every node once)
Space Complexity = O(h), where h is the height of the tree (call stack); O(log n) on average, O(n) worst case for a skewed tree

---

### Q9 — Dedup Sorted List
Given a sorted singly linked list, remove all duplicate nodes so each value appears at most once.

**Algorithm:** Walk the list with two pointers `prev` and `curr`. If `curr` has the same value as `prev`, skip it by setting `prev.next = curr.next`. Otherwise move `prev` forward. Since the list is sorted, duplicates are always adjacent.

Time Complexity = O(n), where n is the number of nodes in the list (single pass)
Space Complexity = O(1)

---

### Q10 — Move Nth Last Node to Front
Given a singly linked list and integer `n`, move the nth-to-last node to the front of the list.

**Algorithm:** Use two pointers. Advance `curr` by `n` steps, then move both `prev` and `curr` together until `curr` hits the end. `prev` is now just before the target node. Detach the target, point it to the head, and make it the new head.

Time Complexity = O(n), where n is the length of the list (two-pointer single pass)
Space Complexity = O(1)

---

### Q11 — Is Palindrome
Given a doubly linked list with head and tail pointers, determine whether the list is a palindrome by comparing values from both ends moving inward.

**Algorithm:** Use two pointers, `front` at the head and `back` at the tail. Compare their values and move them toward the middle. If any values differ, return `False`. Stop when the pointers meet or cross.

Time Complexity = O(n), where n is the length of the list (at most n/2 comparisons, which simplifies to O(n))
Space Complexity = O(1)

---

### Q12 — Disconnect Cycle
Given a singly linked list that may contain a cycle, detect and remove the cycle using Floyd's cycle detection algorithm.

**Algorithm:** Move `slow` one step and `fast` two steps — if they meet, there is a cycle. Reset `slow` to the head and advance both one step at a time until they meet again at the cycle entry. Then walk `fast` around the cycle until `fast.next == slow`, and set `fast.next = None` to break it.

Time Complexity = O(3n), where n is the length of the list (three passes: detect, find cycle entry, find tail), which simplifies to O(n)
Space Complexity = O(1)

---

### Q13 — Left View of Binary Tree
Given a binary tree, return a list of the first (leftmost) node visible at each level when viewed from the left side. Uses BFS level-order traversal.

**Algorithm:** Use a queue to go through the tree level by level. At each level, add the first node's value to the result. Then add all children to the queue for the next level.

Time Complexity = O(2n), where n is the number of nodes in the tree (every node is enqueued and dequeued once), which simplifies to O(n)
Space Complexity = O(n/2) + O(h), where n is the number of nodes in the tree (queue holds up to n/2 nodes at the widest level) and h is the height of the tree (result list), which simplifies to O(n)

---

### Q14 — Floor in BST
Given a BST and a target value, return the largest value in the BST that is less than or equal to the target (the floor).

**Algorithm:** Walk the BST. If the current node equals the target, return it. If it is too big, go left. If it is smaller, save it as a candidate and go right to look for a closer value. Return the last saved candidate.

Time Complexity = O(h), where h is the height of the tree
Space Complexity = O(1)
