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

// Helper function to print vectors cleanly
void printVector(const vector<string> &vec)
{
    cout << "[";
    for (size_t i = 0; i < vec.size(); ++i)
    {
        cout << "\"" << vec[i] << "\"";
        if (i < vec.size() - 1)
            cout << ", ";
    }
    cout << "]";
}

// Helper function to run standard insertion/drain tests
void runTest(int testNum, const string &description, const vector<pair<string, int>> &inputs, const vector<string> &expected)
{
    PriorityQueue pq;

    // Insert all items
    for (const auto &item : inputs)
    {
        pq.insert(item.first, item.second);
    }

    // Drain the queue to get the actual order
    vector<string> result;
    while (!pq.isEmpty())
    {
        result.push_back(pq.top());
        pq.remove();
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
    cout << "\n";
    cout << "  Actual:   ";
    printVector(result);
}

// Helper function specifically for exception testing
void runExceptionTest(int testNum, const string &description)
{
    PriorityQueue pq;
    cout << "Test " << testNum << " (" << description << "): ";

    try
    {
        pq.top(); // This should trigger the exception
        cout << "FAIL\n";
        cout << "  Expected: Exception to be thrown\n";
        cout << "  Actual:   No exception was thrown\n";
    }
    catch (const runtime_error &e) // Note: Fixed to catch runtime_error to match your class logic
    {
        cout << "PASS\n";
        cout << "  Output: Caught exception -> \"" << e.what() << "\"\n";
    }
    catch (...)
    {
        cout << "FAIL\n";
        cout << "  Expected: std::runtime_error\n";
        cout << "  Actual:   Unknown exception thrown\n";
    }
}

int main()
{
    cout << "--- Running Priority Queue Test Suite ---\n\n";

    runTest(1, "Mixed Priorities",
            {{"LowTask", 1}, {"UrgentTask", 100}, {"MediumTask", 50}, {"Emergency", 999}},
            {"Emergency", "UrgentTask", "MediumTask", "LowTask"});

    runTest(2, "Duplicate Priorities",
            {{"TaskA", 10}, {"TaskB", 10}, {"HighTask", 20}},
            {"HighTask", "TaskA", "TaskB"});

    runTest(3, "Negative Priorities",
            {{"ZeroTask", 0}, {"SubZeroTask", -50}, {"PositiveTask", 5}},
            {"PositiveTask", "ZeroTask", "SubZeroTask"});

    // Note: I updated the catch block inside this helper function to look for `runtime_error`
    // instead of `out_of_range`, because your PriorityQueue class explicitly throws `runtime_error`.
    runExceptionTest(4, "Empty Queue Exceptions");

    return 0;
}