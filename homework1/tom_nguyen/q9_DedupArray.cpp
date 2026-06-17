#include <iostream>
#include <vector>
using namespace std;

//uses two pointers to remove duplicates in-place from a sorted array in O(n)
void dedupArray(vector<int>& arr) {
    if (arr.empty()) {
        return;
    }
    int write = 1;
    for (int read = 1; read < (int)arr.size(); ++read) {
        if (arr[read] == arr[read - 1]) {
            continue;
        }
        arr[write] = arr[read];
        ++write;
    }
    arr.resize(write);
}

void print(const vector<int>& arr) {
    cout << "[";
    for (int i = 0; i < (int)arr.size(); ++i) {
        if (i > 0) cout << ", ";
        cout << arr[i];
    }
    cout << "]" << endl;
}

int main() {
    vector<int> t1 = {1, 2, 2, 3, 3, 3, 4, 4, 4, 4};
    dedupArray(t1);
    print(t1); // [1, 2, 3, 4]

    vector<int> t2 = {0, 0, 1, 4, 5, 5, 5, 8, 9, 9, 10, 11, 15, 15};
    dedupArray(t2);
    print(t2); // [0, 1, 4, 5, 8, 9, 10, 11, 15]

    vector<int> t3 = {1, 3, 4, 8, 10, 12};
    dedupArray(t3);
    print(t3); // [1, 3, 4, 8, 10, 12]

    return 0;
}

//time spent: 25 minutes
