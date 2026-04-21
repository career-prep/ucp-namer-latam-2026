#include <iostream>
#include <vector>
using namespace std;

//uses the sum formula to find the missing integer in O(n)
int missingInteger(const vector<int>& arr, int n) {
    int expectedSum = n * (n + 1) / 2;
    int actualSum = 0;
    for (int num : arr) {
        actualSum += num;
    }
    return expectedSum - actualSum;
}

int main() {
    vector<int> t1 = {1, 2, 3, 4, 6, 7};
    cout << missingInteger(t1, 7) << endl; // 5

    vector<int> t2 = {1};
    cout << missingInteger(t2, 2) << endl; // 2

    vector<int> t3 = {1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12};
    cout << missingInteger(t3, 12) << endl; // 9

    return 0;
}

//time spent: 5 mins
