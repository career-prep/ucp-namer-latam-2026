/*Data Structure: array (dp table)
Algorithm: tabulation using the Catalan convolution recurrence
Technique: dynamic programming (tabulation)
Time Complexity: O(n^2)
Space Complexity: O(n)
Time Taken: 18 mins 47 seconds
*/

#include<iostream>
#include<vector>

using namespace std;

/*
1. dont touch factorials (overflow + recompute). use the recurrence.
2. C[0] = 1.
3. C[k+1] = sum over i=0..k of C[i] * C[k-i].
4. return C[0..n].
*/

vector<long long> CatalanNumbers(int n){
    vector<long long> C(n + 1, 0);
    C[0] = 1;
    for(int k = 0; k < n; k++){
        for(int i = 0; i <= k; i++){
            C[k+1] += C[i] * C[k-i];
        }
    }
    return C;
}

int main(){
    for(int n : {1, 5}){
        vector<long long> output = CatalanNumbers(n);
        cout << "Actual result (n=" << n << "): ";
        for(size_t i = 0; i < output.size(); i++) cout << output[i] << (i+1 < output.size() ? ", " : "");
        cout << endl;
    }
    cout << "Expected result: n=1 -> 1, 1   |   n=5 -> 1, 1, 2, 5, 14, 42" << endl;
}

/* psudocode/thoughts/logic
goal: return catalan numbers 0..n
restraints: the (2n)!/((n+1)!n!) formula blows up fast and recomputing factorials is wasteful

strategy: classic dp. the recurrence C(k+1) = sum C(i)*C(k-i) builds each number from the ones
before it, no factorials, no overflow until the numbers themselves get huge (long long buys room).
its O(n^2) because the inner convolution grows with k. could also do the O(n) closed-form
C(n)=C(n-1)*2(2n-1)/(n+1) but the convolution is the cleaner "dp" answer for the technique.
*/
