# Practice Assignment 2 – Part 1


## Question 1 – Singly Linked List

Implemented a singly linked list using a `Node` class containing:
- `int data`
- `Node next`

Implemented the following operations:

- `insertAtFront(head, val)` – Inserts a node at the front of the list.
- `insertAtBack(head, val)` – Inserts a node at the end of the list.
- `insertAfter(head, val, loc)` – Inserts a node after a given node.
- `insertBefore(head, val, loc)` – Inserts a node before a given node.
- `deleteFront(head)` – Removes the first node.
- `deleteBack(head)` – Removes the last node.
- `deleteNode(head, loc)` – Removes a specific node.
- `length(head)` – Returns the number of nodes in the list.
- `reverseIterative(head)` – Reverses the list iteratively.
- `reverseRecursive(head)` – Reverses the list recursively.

---

## Question 2 – Doubly Linked List

Implemented a doubly linked list using a `Node` class containing:
- `int data`
- `Node next`
- `Node prev`

Implemented the following operations:

- `insertAtFront(head, val)`
- `insertAtBack(head, tail, val)`
- `insertAfter(head, val, loc)`
- `insertBefore(head, val, loc)`
- `deleteFront(head)`
- `deleteBack(head, tail)`
- `deleteNode(head, loc)`
- `length(head)`
- `reverseIterative(head)`
- `reverseRecursive(head)`

---

## Question 3 – Binary Search Tree

Implemented a Binary Search Tree with the following operations:

- `min()` – Returns the minimum value in the tree.
- `max()` – Returns the maximum value in the tree.
- `contains(val)` – Checks whether a value exists in the tree.
- `insert(val)` – Inserts a new value while maintaining BST properties.
- `delete(val)` – Deletes a value from the tree if it exists.

---

## Question 4 – Queue

Implemented a queue using a linked list structure.

Operations implemented:

- `peek()` – Returns the first element in the queue.
- `enqueue(x)` – Adds an element to the back of the queue.
- `dequeue()` – Removes and returns the first element.
- `isEmpty()` – Checks if the queue is empty.

---

## Question 5 – Stack

Implemented a stack using a linked node structure.

Operations implemented:

- `top()` – Returns the element at the top of the stack.
- `push(x)` – Adds an element to the top of the stack.
- `pop()` – Removes and returns the top element.
- `isEmpty()` – Checks if the stack is empty.

---

## Question 6 – Deque

Implemented a double-ended queue (Deque) using a doubly linked list.

Operations implemented:

- `front()` – Returns the first element.
- `back()` – Returns the last element.
- `pushBack(x)` – Inserts an element at the back.
- `pushFront(x)` – Inserts an element at the front.
- `popFront()` – Removes and returns the front element.
- `popBack()` – Removes and returns the back element.
- `isEmpty()` – Checks if the deque is empty.

# Practice Assignment 2 – Part 2

## Question 7: CopyTree
**Problem:**  
Given a binary tree, create a deep copy. Return the root of the new tree.

**Time Complexity:** O(n)  
**Space Complexity:** O(h) where h is the height of the tree.


---

## Question 8: IsBST
**Problem:**  
Given a binary tree, determine if it is a binary search tree.

**Time Complexity:** O(n)  
**Space Complexity:** O(n)


---

## Question 9: DedupSortedList
**Problem:**  
Given a sorted singly linked list, remove any duplicates so that no value appears more than once.

**Time Complexity:** O(n)  
**Space Complexity:** O(1)


---

## Question 10: MoveNthLastToFront
**Problem:**  
Given a singly linked list, move the nth from the last element to the front of the list.

**Time Complexity:** O(n)  
**Space Complexity:** O(1)


---

## Question 11: IsPalindrome
**Problem:**  
Given a doubly linked list, determine if it is a palindrome.

**Time Complexity:** O(n)  
**Space Complexity:** O(1)


---

## Question 12: DisconnectCycle
**Problem:**  
Given a singly linked list, disconnect the cycle if one exists.

**Time Complexity:** O(n)  
**Space Complexity:** O(n)


---

## Question 13: LeftView
**Problem:**  
Given a binary tree, create an array of the left view (leftmost elements in each level) of the tree.

**Time Complexity:** O(n)  
**Space Complexity:** O(n)


---

## Question 14: FloorInBST
**Problem:**  
Given a target numeric value and a binary search tree, return the floor (greatest element less than or equal to the target) in the BST.

**Time Complexity:** O(log n) average, O(n) worst case  
**Space Complexity:** O(h) where h is the height of the tree.