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

// Helper function to print vectors cleanly
void printVector(const vector<int> &vec)
{
    cout << "[";
    for (size_t i = 0; i < vec.size(); ++i)
    {
        cout << vec[i];
        if (i < vec.size() - 1)
            cout << ", ";
    }
    cout << "]";
}

// Helper function to run standard insertion/drain tests
void runTest(int testNum, const string &description, const vector<int> &inputs, const vector<int> &expected)
{
    Heap h;
    for (int n : inputs)
    {
        h.insert(n);
    }

    vector<int> result;
    while (!h.isEmpty())
    {
        result.push_back(h.top());
        h.remove();
    }

    cout << "Test " << testNum << " (" << description << "): ";
    if (result == expected)
    {
        cout << "PASS\n";
    }
    else
    {
        cout << "FAIL\n";
    }
    cout << "  Expected: ";
    printVector(expected);
    cout << "  Actual:   ";
    printVector(result);
    cout << "\n\n";
}

// Custom helper for Interleaved Operations (TC6)
void runInterleavedTest(int testNum, const string &description)
{
    Heap h;
    vector<int> result;
    vector<int> expected = {10, 5, 30, 50};

    h.insert(50);
    h.insert(10);
    result.push_back(h.top()); // Should be 10
    h.remove();

    h.insert(5);
    h.insert(30);
    result.push_back(h.top()); // Should be 5
    h.remove();

    while (!h.isEmpty())
    {
        result.push_back(h.top()); // Should drain remaining: 30, 50
        h.remove();
    }

    cout << "Test " << testNum << " (" << description << "): ";
    if (result == expected)
    {
        cout << "PASS\n";
        cout << "  Output: ";
        printVector(result);
        cout << " (Order of extraction)\n\n";
    }
    else
    {
        cout << "FAIL\n";
        cout << "  Expected: ";
        printVector(expected);
        cout << "\n";
        cout << "  Actual:   ";
        printVector(result);
        cout << "\n\n";
    }
}

// Custom helper for Exception Testing (TC8)
void runExceptionTest(int testNum, const string &description)
{
    Heap h;
    cout << "Test " << testNum << " (" << description << "): ";

    bool topPassed = false;
    bool removePassed = false;
    string errorMessage = "";

    try
    {
        h.top();
    }
    catch (const runtime_error &e)
    { // Fixed from out_of_range
        topPassed = true;
        errorMessage = e.what();
    }

    try
    {
        h.remove();
    }
    catch (const runtime_error &e)
    { // Fixed from out_of_range
        removePassed = true;
    }

    if (topPassed && removePassed)
    {
        cout << "PASS\n";
        cout << "  Output: Caught exceptions -> \"" << errorMessage << "\"\n\n";
    }
    else
    {
        cout << "FAIL\n";
        cout << "  Expected: Exceptions to be thrown on empty top() and remove()\n";
        cout << "  Actual:   One or more methods failed to throw appropriately\n\n";
    }
}

int main()
{
    cout << "--- Running Heap Test Suite ---\n\n";

    runTest(1, "Mixed Input",
            {10, 4, 15, 20, 0, 8},
            {0, 4, 8, 10, 15, 20});

    runTest(2, "Duplicate Elements",
            {5, 1, 5, 5, 2, 1},
            {1, 1, 2, 5, 5, 5});

    runTest(3, "Negative Numbers",
            {-10, 5, 0, -20, -5},
            {-20, -10, -5, 0, 5});

    runTest(4, "Reverse Sorted Input (Worst Case)",
            {5, 4, 3, 2, 1},
            {1, 2, 3, 4, 5});

    runTest(5, "Already Sorted Input (Best Case)",
            {1, 2, 3, 4, 5},
            {1, 2, 3, 4, 5});

    runInterleavedTest(6, "Interleaved Operations");

    runTest(7, "Single Element Edge Case",
            {42},
            {42});

    runExceptionTest(8, "Empty Heap Exceptions");

    return 0;
}