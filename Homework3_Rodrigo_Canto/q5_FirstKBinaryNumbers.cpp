//Time Complexity: O(K * log(k)).
//Space Complexity: O(K * log(k)).
//Tecnhique: Math.

#include "bits/stdc++.h"
using namespace std;

vector<string> solveFirstKBinaryNumbers(int k){

    vector<string> answer;

    for(int i = 0; i < k; ++i){

        int number = i;

        string binary_representation = "";

        //Handle the special case (zero).
        if(number == 0){
            binary_representation = "0";
        }
        else{


            while(number != 0){

                //The AND operation allows us to process the last bit
                if(number & 1){
                    binary_representation.push_back('1');
                }
                else{
                    binary_representation.push_back('0');
                }

                //The right shift "eliminates" the last bit we just processed.
                number = number / 2;
            }
        }

        //We process the bits from right to left so we need to reverse the string.
        reverse(binary_representation.begin(), binary_representation.end());

        answer.push_back(binary_representation);
    }

    return answer;
}

int main() {

    int k; cin >> k;

    for(string binary_number : solveFirstKBinaryNumbers(k)){
        cout << binary_number << " ";
    }
}

//Time Spent: 10 minutes