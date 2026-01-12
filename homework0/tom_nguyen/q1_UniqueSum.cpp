#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

int uniqueSum(vector<int>& arr) {
    unordered_set<int> seen;
    int sum = 0;
    for (int num : arr) {
        if (!seen.count(num)) {
            sum += num;
            seen.insert(num);
        }
    }
    return sum;
}

int main() {
    vector<int> t1 = {1, 10, 8, 3, 2, 5, 7, 2, -2, -1};
    cout << uniqueSum(t1) << endl;

    vector<int> t2 = {4, 3, 3, 5, 7, 0, 2, 3, 8, 6};
    cout << uniqueSum(t2) << endl;

    return 0;
}

// Time spent: 12 minutes
