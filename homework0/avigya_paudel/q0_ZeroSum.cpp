#include <iostream>
#include <unordered_map>
#include <algorithm>
using namespace std;

// TIME COMPLEXITY: O(N)
// SPACE COMPLEXITY: O(N)

unsigned long long fact(unsigned int n) {
    unsigned long long result = 1;
    for (unsigned int i = 1; i <= n; ++i) {
        result *= i;
    }
    return result;
}

int zero_sum(int arr[], int n){
    // count occurence of each integer : num -> occ
    unordered_map<int,int> num_count;
    for (int i = 0; i < n; i++) {
        num_count[arr[i]] += 1;
    }

    int res = 0;
    int complement;
    for (int i=0; i < n; i++){
        complement = -arr[i];
        if (num_count.count(complement) && num_count[complement] > 0){
            res++;
            num_count[arr[i]] -= 1;
            num_count[complement] -= 1;
        }
    }

    return res;
}

int zero_sum_followup(int arr[], int n){
    // count occurence of each integer : num -> occ
    unordered_map<int,int> num_count;
    for (int i = 0; i < n; i++) {
        num_count[arr[i]] += 1;
    }

    int res = 0;
    int complement;
    for (int i=0; i < n; i++){
        complement = -arr[i];
        if (num_count.count(complement) && num_count[complement] > 0 && complement != 0){
            res += num_count[arr[i]] * num_count[complement];
            num_count[arr[i]] = 0;
            num_count[complement] = 0;
        } else if (num_count[complement] >= 2 && complement == 0) {
            res += fact(num_count[complement])/(fact(num_count[complement]-2)*fact(2));
            num_count[complement] = 0;
        }
    }

    return res;
}

int main(){
    int arr1[] =  {1,10,8,3,2,-2,-2,2,-1};
    int arr2[] = {1,5,7,0,0,0};
    int arr3[] = {4,3,3,5,7,8,9};
    int res1 = zero_sum(arr1, sizeof(arr1)/sizeof(arr1[0]));
    int res2 = zero_sum(arr2, sizeof(arr2)/sizeof(arr2[0]));
    int res3 = zero_sum(arr3, sizeof(arr3)/sizeof(arr3[0]));
    cout << res1 << "\n";
    cout << res2 << "\n";
    cout << res3 << "\n";

    int res1_followup = zero_sum_followup(arr1, sizeof(arr1)/sizeof(arr1[0]));
    int res2_followup = zero_sum_followup(arr2, sizeof(arr2)/sizeof(arr2[0]));
    int res3_followup = zero_sum_followup(arr3, sizeof(arr3)/sizeof(arr3[0]));
    cout << res1_followup << "\n";
    cout << res2_followup << "\n";
    cout << res3_followup << "\n";
    return 0;
}

// TIME SPENT: ~30 minutes