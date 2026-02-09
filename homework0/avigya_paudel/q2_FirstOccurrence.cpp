#include <iostream>
#include <unordered_set>
using namespace std;

// TIME COMPLEXITY: O(N)
// SPACE COMPLEXITY: O(N)

string first_occ(string s){
    unordered_set<char> char_set;
    string ans;
    for (char c: s){
        if (char_set.count(c) <= 0){
            ans += c;
            char_set.insert(c);
        }
    }
    return ans;    
}

int main(){
    string s1 = "abcddefgabcd";
    string s2 = "Uber Career Prep";
    string s3 = "zzyzx";

    string res1 = first_occ(s1);
    string res2 = first_occ(s2);
    string res3 = first_occ(s3);

    cout << res1 << "\n";
    cout << res2 << "\n";
    cout << res3 << "\n";
    return 0;
}

// Time taken: ~8 minutes