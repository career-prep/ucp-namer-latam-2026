#include <iostream>
#include <vector>
#include <string>
#include <stdexcept>

using namespace std;

class PriorityQueue
{

private:
    // Using vector to allow dynamic resizing.
    // pair.first = element (string), pair.second = priority weight (int)
    vector<pair<string, int>> arr;

    // Helper functions to get indices of parent and children
    int getParent(int i) { return (i - 1) / 2; };
    int getLeftChild(int i) { return (2 * i + 1); };
    int getRightChild(int i) { return (2 * i + 2); };

    // Restore max heap property by bubbling up the element at index i
    void heapifyUp(int i)
    {
        while (i > 0 && arr[i].second > arr[getParent(i)].second)
        {
            swap(arr[i], arr[getParent(i)]);
            i = getParent(i);
        }
    }

    // Restore max heap property by bubbling down the element at index i
    void heapifyDown(int i)
    {
        int maxIndex = i;
        int leftChild = getLeftChild(i);
        int rightChild = getRightChild(i);
        int size = arr.size();

        // Get the largest among i, left child and right child
        if (leftChild < size && arr[leftChild].second > arr[maxIndex].second)
        {
            maxIndex = leftChild;
        }
        if (rightChild < size && arr[rightChild].second > arr[maxIndex].second)
        {
            maxIndex = rightChild;
        }
        // If i is not the largest, swap and continue heapifying
        if (maxIndex != i)
        {
            swap(arr[i], arr[maxIndex]);
            heapifyDown(maxIndex);
        }
    }

public:
    // Return the element with the highest priority (the root of the heap)
    string top()
    {
        if (arr.empty())
        {
            throw runtime_error("Priority Queue is empty");
        }
        return arr[0].first;
    }

    // Add an element with a given priority to the queue and maintain the max heap property
    void insert(string value, int priority)
    {
        arr.push_back({value, priority}); // Add the new element to the end of the vector
        heapifyUp(arr.size() - 1);        // Restore the max heap property by bubbling up the new element
    }

    // Remove the element with the highest priority from the queue and maintain the max heap property
    void remove()
    {
        if (arr.empty())
        {
            throw runtime_error("Priority Queue is empty");
        }
        arr[0] = arr.back(); // Replace the root with the last element
        arr.pop_back();      // Remove the last element
        if (!arr.empty())

        {
            heapifyDown(0); // Restore the max heap property by bubbling down the new root
        }
    }

    // Helper method
    bool isEmpty()
    {
        return arr.empty();
    }
};

// ---------------------------------------------------------
// Test Suite
// ---------------------------------------------------------
void drainQueue(PriorityQueue &pq, const string &label)
{
    cout << label << ": [ ";
    while (!pq.isEmpty())
    {
        cout << pq.top() << " ";
        pq.remove();
    }
    cout << "]\n";
}

int main()
{
    cout << "=== PRIORITY QUEUE TEST SUITE ===\n\n";

    // Test Case 1: Standard Usage
    cout << "--- TC1: Mixed Priorities ---\n";
    PriorityQueue pq1;
    pq1.insert("LowTask", 1);
    pq1.insert("UrgentTask", 100);
    pq1.insert("MediumTask", 50);
    pq1.insert("Emergency", 999);

    cout << "Top element should be 'Emergency': " << pq1.top() << "\n";
    drainQueue(pq1, "Expected order [Emergency UrgentTask MediumTask LowTask]");

    // Test Case 2: Duplicate Priorities
    // Should handle identical weights gracefully
    cout << "\n--- TC2: Duplicate Priorities ---\n";
    PriorityQueue pq2;
    pq2.insert("TaskA", 10);
    pq2.insert("TaskB", 10);
    pq2.insert("HighTask", 20);
    drainQueue(pq2, "Expected order [HighTask TaskA TaskB] (or TaskB TaskA)");

    // Test Case 3: Negative Priorities
    cout << "\n--- TC3: Negative Priorities ---\n";
    PriorityQueue pq3;
    pq3.insert("ZeroTask", 0);
    pq3.insert("SubZeroTask", -50);
    pq3.insert("PositiveTask", 5);
    drainQueue(pq3, "Expected order [PositiveTask ZeroTask SubZeroTask]");

    // Test Case 4: Exception Handling
    cout << "\n--- TC4: Empty Queue Exceptions ---\n";
    PriorityQueue pq4;
    try
    {
        pq4.top();
        cout << "FAIL: top() did not throw.\n";
    }
    catch (const out_of_range &e)
    {
        cout << "PASS: Caught exception on top() -> " << e.what() << "\n";
    }

    return 0;
}