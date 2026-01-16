#include <iostream>
#include <unordered_map>
using namespace std;

// TIME COMPLEXITY: O(N)
// SPACE COMPLEXITY: O(N)

// Alternatively I could have used a set and summed it up

int unique_sum(int arr[], int n){
    unordered_map<int,int> num_cnt;
    for (int i = 0; i < n; i++){
        num_cnt[arr[i]] += 1;
    }
    int sum = 0;
    for (auto& p: num_cnt){
        if (p.second == 1) {
            sum += p.first;
        }
    }
    return sum;
}

int main(){
    int arr1[] =  {1,10,8,3,2,-2,-2,2,-1};
    int arr2[] = {1,5,7,0,0,0,-1};
    int arr3[] = {4,3,3,5,7,8,9};
    int res1 = unique_sum(arr1, sizeof(arr1)/sizeof(arr1[0]));
    int res2 = unique_sum(arr2, sizeof(arr2)/sizeof(arr2[0]));
    int res3 = unique_sum(arr3, sizeof(arr3)/sizeof(arr3[0]));
    cout << res1 << "\n";
    cout << res2 << "\n";
    cout << res3 << "\n";
    return 0;
}

// Time taken: ~5 minutes