#include <iostream>
#include <vector>
using namespace std;

//uses a sliding window to find the maximum mean of a subarray of size k in O(n)
double maxMeanSubArray(const vector<int>& arr, int k) {
    double windowSum = 0;
    for (int i = 0; i < k; ++i) {
        windowSum += arr[i];
    }
    double maxSum = windowSum;
    for (int i = k; i < (int)arr.size(); ++i) {
        windowSum += arr[i] - arr[i - k];
        if (windowSum > maxSum) {
            maxSum = windowSum;
        }
    }
    return maxSum / k;
}

int main() {
    vector<int> t1 = {4, 5, -3, 2, 6, 1};
    cout << maxMeanSubArray(t1, 2) << endl; // 4.5

    vector<int> t2 = {4, 5, -3, 2, 6, 1};
    cout << maxMeanSubArray(t2, 3) << endl; // 3

    vector<int> t3 = {1, 1, 1, 1, -1, -1, 2, -1, -1};
    cout << maxMeanSubArray(t3, 3) << endl; // 1

    vector<int> t4 = {1, 1, 1, 1, -1, -1, 2, -1, -1, 6};
    cout << maxMeanSubArray(t4, 5) << endl; // 1

    return 0;
}

//time spent: 8 minutes
