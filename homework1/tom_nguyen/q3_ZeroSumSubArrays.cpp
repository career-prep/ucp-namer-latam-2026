#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

//uses prefix sums and a hash map to count subarrays that sum to zero in O(n)
int zeroSumSubArrays(const vector<int>& arr) {
    unordered_map<int, int> prefixCount;
    prefixCount[0] = 1; //empty prefix
    int sum = 0, count = 0;
    for (int num : arr) {
        sum += num;
        if (prefixCount.contains(sum)) {
            count += prefixCount[sum];
        }
        ++prefixCount[sum];
    }
    return count;
}

int main() {
    vector<int> t1 = {4, 5, 2, -1, -3, -3, 4, 6, -7};
    cout << zeroSumSubArrays(t1) << endl; // 2

    vector<int> t2 = {1, 8, 7, 3, 11, 9};
    cout << zeroSumSubArrays(t2) << endl; // 0

    vector<int> t3 = {8, -5, 0, -2, 3, -4};
    cout << zeroSumSubArrays(t3) << endl; // 2

    return 0;
}

//time spent: 10 minute
