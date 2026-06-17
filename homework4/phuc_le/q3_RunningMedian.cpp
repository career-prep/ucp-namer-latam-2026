/*
    Technique:
    - Maintain two heaps

    - Use two heaps to keep track of the numbers seen so far.
        - Max Heap (left)
           - Stores the smaller half of the numbers.
        - Min Heap (right)
           - Stores the larger half of the numbers.
    - Every element in left <= every element in right.
    - The size difference between the heaps is at most 1.
    - If there is an odd number of elements, left stores one extra element.

    - Insert the new number into the appropriate heap.
    - Rebalance the heaps if their sizes differ by more than one.
    - Compute the median:
        - If both heaps have the same size,
            median = (left.top() + right.top()) / 2.0
        - Else,
          median = left.top()

    Time Complexity: O(log n): n = numbers of elements
    Space Complexity: O(n)

    Time spent: 40 minutes
*/

#include <iostream>
#include <vector>
#include <queue>

using namespace std;

class RunningMedian
{
private:
    // Max heap for smaller half
    priority_queue<int> left;

    // Min heap for larger half
    priority_queue<int, vector<int>, greater<int>> right;

public:
    double addNumber(int num)
    {
        // Insert into appropriate heap
        if (left.empty() || num <= left.top())
            left.push(num);
        else
            right.push(num);

        // Balance heaps
        if (left.size() > right.size() + 1)
        {
            right.push(left.top());
            left.pop();
        }
        else if (right.size() > left.size())
        {
            left.push(right.top());
            right.pop();
        }

        // Compute median
        if (left.size() == right.size())
        {
            return (left.top() + right.top()) / 2.0;
        }

        return left.top();
    }
};

int main()
{
    // Test 1: Example case
    {
        vector<int> nums = {1, 11, 4, 15, 12};

        RunningMedian rm;
        cout << "Test 1: ";
        for (int x : nums)
            cout << rm.addNumber(x) << " ";
        cout << "\n";
    }

    // Test 2: Single element
    {
        vector<int> nums = {5};

        RunningMedian rm;
        cout << "Test 2: ";
        for (int x : nums)
            cout << rm.addNumber(x) << " ";
        cout << "\n";
    }

    // Test 3: All same numbers
    {
        vector<int> nums = {7, 7, 7, 7, 7};

        RunningMedian rm;
        cout << "Test 3: ";
        for (int x : nums)
            cout << rm.addNumber(x) << " ";
        cout << "\n";
    }

    // Test 4: Increasing order
    {
        vector<int> nums = {1, 2, 3, 4, 5};

        RunningMedian rm;
        cout << "Test 4: ";
        for (int x : nums)
            cout << rm.addNumber(x) << " ";
        cout << "\n";
    }

    // Test 5: Decreasing order
    {
        vector<int> nums = {5, 4, 3, 2, 1};

        RunningMedian rm;
        cout << "Test 5: ";
        for (int x : nums)
            cout << rm.addNumber(x) << " ";
        cout << "\n";
    }

    // Test 6: Negative numbers
    {
        vector<int> nums = {-5, -1, -10, -3};

        RunningMedian rm;
        cout << "Test 6: ";
        for (int x : nums)
            cout << rm.addNumber(x) << " ";
        cout << "\n";
    }

    // Test 7: Mix of positive and negative
    {
        vector<int> nums = {-2, 10, -5, 8, 0};

        RunningMedian rm;
        cout << "Test 7: ";
        for (int x : nums)
            cout << rm.addNumber(x) << " ";
        cout << "\n";
    }

    // Test 8: Large values
    {
        vector<int> nums = {1000000, 2000000, 3000000};

        RunningMedian rm;
        cout << "Test 8: ";
        for (int x : nums)
            cout << rm.addNumber(x) << " ";
        cout << "\n";
    }

    return 0;
}