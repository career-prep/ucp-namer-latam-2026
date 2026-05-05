## Question 1: Graph Algorithms

### Question Type  
Graph / Traversal / Topological Sort

### Description  
Implemented core graph algorithms including:
- Building an adjacency set
- Breadth-First Search (BFS) for traversal and target search
- Depth-First Search (DFS) for traversal and target search
- Topological Sort using Kahn’s Algorithm (BFS)
- Topological Sort using DFS with cycle detection

### Time Spent  
75 minutes

### Approach 

I represented the graph using an adjacency set where each node maps to a set of its neighbors.

For searching a target node:
- I used BFS with a queue to explore nodes level by level  
- I used DFS with recursion to explore paths more deeply  

For topological sort:
- I used Kahn’s algorithm where I calculate in-degrees and process nodes with 0 in-degree using a queue  
- I also implemented a DFS-based version that detects cycles using a visiting set  

If a cycle is detected, I return an empty list because a valid topological ordering does not exist.

### Edge Cases  
- Empty graph  
- Graph with cycles (topological sort should return empty)  
- Disconnected graph  
- Target node not present in graph  
- Graph with no edges  

### Time & Space Complexity  

- Time: O(V + E)  
  Because each node and each edge is processed at most once during traversal and topological sorting  

- Space: O(V + E)  
  Because we store the graph and use additional structures like visited sets, recursion stack, and queues  


### Completion Status  
Finished implementation and all tests passed.

## Question 2: Heap

### Question Type  
Heap / Priority Queue (Min Heap)


### Description  
Implemented a Min Heap data structure supporting:
- Insert
- Peek (get minimum element)
- Delete Min (remove minimum element)
- Size and is_empty checks


### Time Spent  
45 minutes

### Approach  

I implemented a Min Heap using a list where the smallest element is always at the root (index 0).

For insertion:
- I add the new value at the end of the list  
- Then I perform heapify-up to restore the heap property by comparing with its parent and swapping if needed  

For deletion (delete_min):
- I remove the root (minimum value)  
- Replace it with the last element  
- Then perform heapify-down by comparing with its children and swapping with the smaller child  

This ensures the heap property is maintained after every operation.

### Edge Cases  
- Empty heap (peek or delete should raise an error)  
- Single element heap  
- Duplicate values  
- Inserting into empty heap  
- Removing last element  


### Time & Space Complexity  

- Insert: O(log n)  
  Because in the worst case the element moves up the height of the heap  

- Delete Min: O(log n)  
  Because the root may move down the height of the heap  

- Peek: O(1)  
  Because we directly access the root  

- Space: O(n)  
  Because we store all elements in the heap array  


### Completion Status  
Finished implementation and all tests passed.

## Question 3: Priority Queue

### Question Type  
Heap / Priority Queue (Min Heap implementation)


### Description  
Implemented a Priority Queue using a Min Heap structure, supporting:
- Enqueue (insert element)
- Dequeue (remove element with highest priority / smallest value)
- Peek (view highest priority element)
- Size and is_empty checks


### Time Spent  
35 minutes

### Approach  

I implemented a Priority Queue using a Min Heap, where the smallest element represents the highest priority.

For enqueue:
- I add the new value to the end of the heap list  
- Then I perform heapify-up to maintain the heap property  

For dequeue:
- I remove the root element (smallest value)  
- Replace it with the last element in the heap  
- Then perform heapify-down to restore the heap structure  

For peek:
- I return the root element directly since it is always the minimum  

This ensures that the highest priority element is always accessible in O(1) time.


### Edge Cases  
- Empty priority queue (peek or dequeue should raise an error)  
- Single element queue  
- Duplicate values  
- Enqueue into empty queue  
- Removing the last element  


### Time & Space Complexity  

- Enqueue: O(log n)  
  Because the element may move up the height of the heap  

- Dequeue: O(log n)  
  Because the root may move down the height of the heap  

- Peek: O(1)  
  Because we directly access the root  

- Space: O(n)  
  Because all elements are stored in the heap  


### Completion Status  
Finished implementation and all tests passed.

## Question 4: Number of Islands

### Question Type  
Graph / Matrix Traversal (DFS)

### Description  
Given a 2D grid of 0s (water) and 1s (land), count the number of islands.  
An island is formed by connecting adjacent land cells (up, down, left, right).


### Time Spent  
30 minutes


### Approach  

I treated the grid like a graph where each cell is a node, and adjacent land cells are connected.

I used DFS to explore each island.

- I loop through every cell in the grid  
- When I find a cell with value 1 that hasn’t been visited, I start a DFS  
- The DFS explores all connected land cells and marks them as visited  
- After finishing DFS, I increment the island count  

This ensures that each island is counted exactly once.

### Edge Cases  
- Empty grid  
- Grid with no columns (`[[]]`)  
- Grid with all water (0s)  
- Grid with all land (1s)  
- Single cell grid  
- Multiple disconnected islands  

### Time & Space Complexity  

- Time: O(rows * cols)  
  Because each cell is visited at most once  

- Space: O(rows * cols)  
  Because of the visited set and recursion stack in the worst case  


### Completion Status  
Finished implementation and all tests passed.

## Question 5: First K Binary Numbers

### Question Type  
Queue / Breadth-First Generation

### Description  
Given an integer k, generate the first k binary numbers in order as strings.


### Time Spent  
30 minutes


### Approach  

I used a queue to generate binary numbers in order using a BFS-like approach.

- I start by putting "1" into the queue  
- Then I repeatedly:
  - remove the front element  
  - add it to the result list  
  - generate two new numbers by appending "0" and "1" to it  
  - add those back into the queue  

This works like level order traversal of a binary tree, where
- each node generates two children (current + "0", current + "1")  
This wll make sure the binary numbers are generated in the correct order.


### Edge Cases  
- k = 0 -> return empty list  
- k < 0 ->  return empty list  
- k = 1 ->  return ["1"]  
- Small values of k  
- Large values of k  


### Time & Space Complexity  

- Time: O(k)  
  Because we generate exactly k binary numbers  

- Space: O(k)  
  Because the queue and result list together store up to k elements  

### Completion Status  
Finished implementation and all tests passed.

## Question 6: Road Networks

### Question Type  
Graph / Connected Components (BFS)


### Description  
Given a list of cities and a list of roads connecting pairs of cities, determine the number of disconnected road networks.  
Each network represents a group of cities that are directly or indirectly connected.


### Time Spent  
40 minutes

### Approach  

I modeled the cities and roads as a graph using an adjacency list, where each city maps to its neighboring cities.

- I first build the graph by adding each road as a bidirectional connection  
- Then I use BFS to explore each connected component  

I loop through all cities, and:
- If a city hasn’t been visited, I start a BFS from that city  
- The BFS explores all cities connected to it and marks them as visited  
- After finishing BFS, I increment the network count  

This way, each BFS traversal represents one connected road network.

### Edge Cases  
- No cities ->  return 0  
- No roads ->  each city is its own network  
- Single city  
- Disconnected cities  
- Multiple separate networks  

### Time & Space Complexity  

- Time: O(cities + roads)  
  Because we visit each city and each road once during graph construction and BFS  

- Space: O(cities + roads)  
  Because we store the adjacency list and the visited set  


### Completion Status  
Finished implementation and all tests passed.

## Question 7: Reverse Words

### Question Type  
String / Two-Pointer Technique

### Description  
Given a string sentence, reverse the order of the words and return the new sentence.  
Words are separated by spaces and extra spaces should be ignored.


### Time Spent  
25 minutes


### Approach

I first split the sentence into a list of words using the built-in split function which automatically removes extra spaces.

Then I reversed the list of words using a two-pointer approach:
- One pointer starts at the beginning  
- The other pointer starts at the end  
- I swap the words until the pointers meet  

Finally I join the reversed list of words back into a string using spaces.


### Edge Cases  
- Empty string ->  return empty string  
- String with only spaces  
- Single word  
- Multiple spaces between words  
- Leading and trailing spaces  


### Time & Space Complexity  

- Time: O(n)  
  Because we process each character in the string when splitting, reversing, and joining  

- Space: O(n)  
  Because we store the list of words  

### Completion Status  
Finished implementation and all tests passed.

## Question 8: Alternating Path

### Question Type  
Graph / BFS (Shortest Path with State)


### Description  
Given a directed graph where each edge has a color (red or blue), find the length of the shortest path from an origin to a destination such that the edge colors strictly alternate.  
Return -1 if no such path exists.

### Time Spent  
50 minutes

### Approach 

I modeled the input as a graph using an adjacency list where each node stores its neighbors along with the color of the edge.

Since we need the shortest path, I used BFS. But because the edges must alternate in color, I also needed to track the previous edge color.

- I used a queue where each entry stores (current node, previous color, distance)  
- I start from the origin with no previous color  
- For each step, I only move to neighbors whose edge color is different from the previous one  
- I also track visited states using (node, color) to avoid revisiting the same state  

As soon as I reach the destination, I return the distance.

If no valid alternating path exists, I return -1.

### Edge Cases  
- Origin equals destination ->  return 0  
- No valid alternating path exists  
- Graph missing origin or destination  
- Single edge path  
- Paths that exist but do not alternate  


### Time & Space Complexity  

- Time: O(V + E)  
  Because each node and edge is processed at most once in BFS  

- Space: O(V + E)  
  Because we store the graph and track visited states for (node, color)  


### Completion Status  
Finished implementation and all tests passed.

## Question 9: Merge K Sorted Arrays

### Question Type  
Heap / K-way Merge


### Description  
Given k sorted arrays, merge them into a single sorted array.

### Time Spent  
45 minutes

### Approach  

I used a min heap to efficiently merge all the sorted arrays.

- I first push the first element of each array into the heap (along with the array index and the element index)  

- Then I repeatedly:
  - remove the smallest element from the heap  
  - add it to the result list  
  - push the next element from the same array into the heap  

This way the heap always contains the next smallest possible elements across all arrays.

### Edge Cases  
- Empty input list ->  return empty list  
- Arrays that are empty  
- Single array  
- Arrays with duplicate values  
- Arrays with negative numbers  


### Time & Space Complexity  

- Time: O(n log k)  
  Where n is the total number of elements and k is the number of arrays  
  Because each insertion/removal from the heap takes O(log k)  

- Space: O(k)  
  Because the heap stores at most one element from each array at a time  


### Completion Status  
Finished implementation and all tests passed.

## Question 10: Prerequisite Courses

### Question Type  
Graph / Topological Sort (BFS - Kahn’s Algorithm)

### Description  
Given a list of courses and their prerequisites, determine a valid order to take the courses such that all prerequisites are satisfied.  
If no valid order exists (due to a cycle), return an empty list.


### Time Spent  
50 minutes

### Approach   

I modeled the courses and prerequisites as a directed graph using an adjacency list.

- Each prerequisite relationship forms a directed edge  
- I also track the in-degree of each course, which represents how many prerequisites it has  

Then I use Kahn’s Algorithm (BFS):

- I start by adding all courses with in-degree 0 (no prerequisites) to a queue  
- Then I process each course:
  - remove it from the queue  
  - add it to the result order  
  - reduce the in-degree of its dependent courses  
  - if any dependent course reaches in-degree 0, I add it to the queue  

At the end:
- If I processed all courses, I return the order  
- If not, it means there is a cycle, so I return an empty list  


### Edge Cases  
- No courses -> return empty list  
- No prerequisites ->  any order is valid  
- Cyclic dependencies ->  return empty list  
- Single course  
- Multiple valid orderings  


### Time & Space Complexity  

- Time: O(courses + prerequisites)  
  Because each course and each dependency is processed once  

- Space: O(courses + prerequisites)  
  Because we store the graph, in-degree map, and queue  


### Completion Status  
Finished implementation and all tests passed.

## Question 11: Vacation Destinations

### Question Type  
Graph / BFS (Shortest Path)

### Description  
Given a list of roads connecting cities, find the shortest path (minimum number of roads) between a start city and a destination city.  
Return -1 if no path exists.


### Time Spent  
40 minutes

### Approach  

I modeled the cities and roads as an undirected graph using an adjacency list.

Since all roads have equal weight, I used BFS to find the shortest path.

- I first build the graph by connecting each pair of cities in both directions  
- Then I use a queue to perform BFS starting from the start city  
- Each entry in the queue stores the current city and the distance from the start  

While traversing:
- I explore all neighboring cities  
- I keep track of visited cities to avoid revisiting  
- As soon as I reach the destination, I return the distance  

If the destination is never reached, I return -1.

### Edge Cases  
- Start equals destination ->  return 0  
- No roads ->  return -1  
- Disconnected graph  
- Start or destination not in graph  
- Single connection  

### Time & Space Complexity  

- Time: O(cities + roads)  
  Because we visit each city and each road at most once  

- Space: O(cities + roads)  
  Because we store the graph and use a queue and visited set  


### Completion Status  
Finished implementation and all tests passed.