//Time Complexity: O(n), where n is the number of catalan numbers to be calculated
//Space Complexity: O(n)

//Technique: DP (Tabulation)

#include "bits/stdc++.h"
using namespace std;

void solve_catalan_numbers(int n){
    
    vector<long long> fact(2 * n + 1);

    //Establish base cases.
    fact[0] = fact[1] = 1;
    
    //Calculate factorials using a bottom-up approach.
    for(int i = 2; i <= 2 * n; ++i) fact[i] = fact[i - 1] * i;

    //Apply formula to calculate the ith catalan number.
    for(int i = 0; i <= n; ++i){
        cout << fact[2 * i] / (fact[i + 1] * fact[i]) << " ";
    }
}

int main(){
    int n; cin >> n;
    solve_catalan_numbers(n);

    return 0;
}

//Time Spent: 10 minutes.