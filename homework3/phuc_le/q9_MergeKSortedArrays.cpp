#include <iostream>
#include <vector>
#include <queue>

using namespace std;

struct Element
{
    int value;        // The value of the element
    int arrayIndex;   // The index of the array from which the element is taken
    int elementIndex; // The index of the element in its array

    // Create minHeap, default maxHeap in C++ priority_queue
    bool operator>(const Element &other) const
    {
        return value > other.value;
    }
};

vector<int> mergeKSortedArrays(int k, const vector<vector<int>> &arrays)
{
    // Priority queue (min-heap) to store the current smallest elements from each array
    priority_queue<Element, vector<Element>, greater<Element>> minHeap;
    vector<int> result;

    // Initialize the min-heap with the first element of each non-empty array
    for (int i = 0; i < k; i++)
    {
        if (!arrays[i].empty())
        {
            minHeap.push({arrays[i][0], i, 0});
        }
    }

    // Get the smallest element from the heap and add the next element from the same array to the heap
    while (!minHeap.empty())
    {
        // Get the top of the minHeap,
        Element current = minHeap.top();
        minHeap.pop();
        result.push_back(current.value);

        // If there is a next element in the same array, add it to the min-heap
        if (current.elementIndex + 1 < arrays[current.arrayIndex].size())
        {
            int nextElementIndex = current.elementIndex + 1;
            minHeap.push({arrays[current.arrayIndex][nextElementIndex], current.arrayIndex, nextElementIndex});
        }
    }
    return result;
};

// Helper function to print vectors cleanly
void printVector(const vector<int> &vec)
{
    cout << "[";
    for (size_t i = 0; i < vec.size(); ++i)
    {
        cout << vec[i] << (i < vec.size() - 1 ? ", " : "");
    }
    cout << "]";
}

// Helper function to run tests and format output
void runTest(int testNum, const string &description, int k, const vector<vector<int>> &input, const vector<int> &expected)
{
    vector<int> result = mergeKSortedArrays(k, input);

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
    cout << "\n\n";
}

int main()
{
    cout << "--- Running MergeKSortedArrays Test Suite ---\n\n";

    // 1. Example 1 from prompt
    runTest(1, "Prompt Example 1", 2,
            {{1, 2, 3, 4, 5}, {1, 3, 5, 7, 9}},
            {1, 1, 2, 3, 3, 4, 5, 5, 7, 9});

    // 2. Example 2 from prompt
    runTest(2, "Prompt Example 2", 3,
            {{1, 4, 7, 9}, {2, 6, 7, 10, 11, 13, 15}, {3, 8, 12, 13, 16}},
            {1, 2, 3, 4, 6, 7, 7, 8, 9, 10, 11, 12, 13, 13, 15, 16});

    // 3. Edge Case: Contains empty arrays
    runTest(3, "Contains Empty Arrays", 3,
            {{}, {1, 5, 6}, {}},
            {1, 5, 6});

    // 4. Edge Case: All arrays are empty
    runTest(4, "All Empty Arrays", 3,
            {{}, {}, {}},
            {});

    // 5. Edge Case: K is 0 (No arrays passed)
    runTest(5, "K = 0 (No input)", 0,
            {},
            {});

    // 6. Edge Case: Arrays of vastly different sizes
    runTest(6, "Different Sized Arrays", 3,
            {{1}, {2, 3, 4, 5, 6, 7}, {8, 9}},
            {1, 2, 3, 4, 5, 6, 7, 8, 9});

    return 0;
}