#include <iostream>
#include <vector>
#include <stdexcept>

using namespace std;

class Heap
{
private:
    vector<int> arr; // Vector to store heap elements

    // Helper functions to get indices of parent and children
    int getParent(int i) { return (i - 1) / 2; };
    int getLeftChild(int i) { return (2 * i + 1); };
    int getRightChild(int i) { return (2 * i + 2); };

    // Restores the min heap property by bubbling up the element at index i
    void heapifyUp(int i)
    {
        // While the current index is greater than 0 and the current element is less than its parent
        while (i > 0 && arr[i] < arr[getParent(i)])
        {
            // Swap the current element with its parent
            swap(arr[i], arr[getParent(i)]);
            // Move up to the parent's index
            i = getParent(i);
        }
    }

    void heapifyDown(int i)
    {
        int minIndex = i;
        int leftChild = getLeftChild(i);
        int rightChild = getRightChild(i);
        int size = arr.size();

        // if the left child exists and is smaller than the current minimum index, update the minimum index
        if (leftChild < size && arr[leftChild] < arr[minIndex])
        {
            minIndex = leftChild;
        }

        // if the right child exists and is smaller than the current minimum index, update the minimum index
        if (rightChild < size && arr[rightChild] < arr[minIndex])
        {
            minIndex = rightChild;
        }

        // if the minimum index is not the current index, swap and continue heapifying down
        if (minIndex != i)
        {
            swap(arr[i], arr[minIndex]);
            heapifyDown(minIndex);
        }
    }

public:
    // Return the minimum element in the heap (the root of the heap)
    int top()
    {
        if (arr.empty())
        {
            throw runtime_error("Heap is empty");
        }
        return arr[0];
    }

    // Add int to the heap and maintain the min heap property
    void insert(int val)
    {
        arr.push_back(val);        // Add the new value to the end of the vector
        heapifyUp(arr.size() - 1); // Restore the min heap property by bubbling up the new element
    }

    // Remove the minimum element from the heap and maintain the min heap property
    void remove()
    {
        if (arr.empty())
        {
            throw runtime_error("Heap is empty");
        }
        arr[0] = arr.back(); // Replace the root with the last element
        arr.pop_back();      // Remove the last element

        if (!arr.empty())
        {
            heapifyDown(0); // Restore the min heap property
        }
    }

    // Return true if the heap is empty, false otherwise
    bool isEmpty()
    {
        return arr.empty();
    }
};

// Helper function to extract and print the entire heap
void drainHeap(Heap &h, const string &label)
{
    cout << label << ": ";
    while (!h.isEmpty())
    {
        cout << h.top() << " ";
        h.remove();
    }
    cout << "\n";
}

int main()
{
    cout << "=== HEAP TEST SUITE ===\n\n";

    // Test Case 1: Standard Mixed Input (Happy Path)
    cout << "--- TC1: Mixed Input ---\n";
    Heap h1;
    vector<int> mixed = {10, 4, 15, 20, 0, 8};
    for (int n : mixed)
        h1.insert(n);
    drainHeap(h1, "Expected [0 4 8 10 15 20]");

    // Test Case 2: Duplicate Elements
    // Heaps must correctly handle identical values.
    cout << "\n--- TC2: Duplicate Elements ---\n";
    Heap h2;
    vector<int> duplicates = {5, 1, 5, 5, 2, 1};
    for (int n : duplicates)
        h2.insert(n);
    drainHeap(h2, "Expected [1 1 2 5 5 5]");

    // Test Case 3: Negative Numbers
    // Ensures comparator logic holds for values below zero.
    cout << "\n--- TC3: Negative Numbers ---\n";
    Heap h3;
    vector<int> negatives = {-10, 5, 0, -20, -5};
    for (int n : negatives)
        h3.insert(n);
    drainHeap(h3, "Expected [-20 -10 -5 0 5]");

    // Test Case 4: Reverse Sorted Input (Worst Case Insert)
    // Forces maximum bubbling-up on every single insertion.
    cout << "\n--- TC4: Reverse Sorted Input ---\n";
    Heap h4;
    for (int i = 5; i >= 1; --i)
        h4.insert(i); // 5, 4, 3, 2, 1
    drainHeap(h4, "Expected [1 2 3 4 5]");

    // Test Case 5: Already Sorted Input (Best Case Insert)
    // Minimum bubbling required.
    cout << "\n--- TC5: Already Sorted Input ---\n";
    Heap h5;
    for (int i = 1; i <= 5; ++i)
        h5.insert(i); // 1, 2, 3, 4, 5
    drainHeap(h5, "Expected [1 2 3 4 5]");

    // Test Case 6: Interleaved Inserts and Removes
    // Tests if the tree remains strictly complete during dynamic use.
    cout << "\n--- TC6: Interleaved Operations ---\n";
    Heap h6;
    h6.insert(50);
    h6.insert(10);
    cout << "Extracted: " << h6.top() << " (Expected 10)\n";
    h6.remove(); // Removes 10
    h6.insert(5);
    h6.insert(30);
    cout << "Extracted: " << h6.top() << " (Expected 5)\n";
    h6.remove(); // Removes 5
    drainHeap(h6, "Remaining (Expected [30 50])");

    // Test Case 7: Single Element Heap
    // Edge case for array boundary logic (size = 1 -> size = 0).
    cout << "\n--- TC7: Single Element ---\n";
    Heap h7;
    h7.insert(42);
    cout << "Top is: " << h7.top() << " (Expected 42)\n";
    h7.remove();
    cout << "Heap is empty: " << (h7.isEmpty() ? "True" : "False") << " (Expected True)\n";

    // Test Case 8: Exception Handling (Empty Heap)
    // Attempting to read or delete from an empty structure.
    cout << "\n--- TC8: Empty Heap Exceptions ---\n";
    Heap h8;

    // Test top()
    try
    {
        h8.top();
        cout << "FAIL: top() did not throw an exception.\n";
    }
    catch (const out_of_range &e)
    {
        cout << "PASS: Caught exception on top() -> " << e.what() << "\n";
    }

    // Test remove()
    try
    {
        h8.remove();
        cout << "FAIL: remove() did not throw an exception.\n";
    }
    catch (const out_of_range &e)
    {
        cout << "PASS: Caught exception on remove() -> " << e.what() << "\n";
    }

    return 0;
}