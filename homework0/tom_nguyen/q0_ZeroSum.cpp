#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

int zeroSumPairs(vector<int>& arr) {
    unordered_map<int, int> count;
    for (int num : arr) {
        ++count[num];
    }

    int pairs = 0;
    for (auto& p : count) {
        int num = p.first;
        int cnt = p.second;
        if (num == 0) {
            pairs += cnt / 2;
            count[0] = cnt % 2;
        } else if (num > 0 && count.count(-num)) {
            int match = min(cnt, count[-num]);
            pairs += match;
            count[num] -= match;
            count[-num] -= match;
        }
    }
    return pairs;
}

int zeroSumPairsReuse(vector<int>& arr) {
    unordered_map<int, int> count;
    for (int num : arr) count[num]++;

    int pairs = 0;
    for (auto& p : count) {
        int num = p.first;
        int cnt = p.second;
        if (num == 0) {
            pairs += (cnt * (cnt - 1)) / 2;
            count[0] = 0;
        } else if (num > 0 && count.count(-num)) {
            pairs += cnt * count[-num];
            count[num] = 0;
            count[-num] = 0;
        }
    }
    return pairs;
}

int main() {
    cout << "Part 1:" << endl;
    vector<int> t1 = {1, 10, 8, 3, 2, 5, 7, 2, -2, -1};
    cout << zeroSumPairs(t1) << endl;

    vector<int> t2 = {1, 10, 8, -2, 2, 5, 7, 2, -2, -1};
    cout << zeroSumPairs(t2) << endl;

    vector<int> t3 = {4, 3, 3, 5, 7, 0, 2, 3, 8, 6};
    cout << zeroSumPairs(t3) << endl;

    vector<int> t4 = {4, 3, 3, 5, 7, 0, 2, 3, 8, 0};
    cout << zeroSumPairs(t4) << endl;

    cout << "\nFollow-up:" << endl;
    vector<int> t5 = {1, 10, 8, 3, 2, 5, 7, 2, -2, -1};
    cout << zeroSumPairsReuse(t5) << endl;

    vector<int> t6 = {1, 10, 8, -2, 2, 5, 7, 2, -2, -1};
    cout << zeroSumPairsReuse(t6) << endl;

    vector<int> t7 = {4, 3, 3, 5, 7, 0, 2, 3, 8, 6};
    cout << zeroSumPairsReuse(t7) << endl;

    vector<int> t8 = {4, 3, 3, 5, 7, 0, 2, 3, 8, 0};
    cout << zeroSumPairsReuse(t8) << endl;

    return 0;
}

// Time spent: 30 minutes