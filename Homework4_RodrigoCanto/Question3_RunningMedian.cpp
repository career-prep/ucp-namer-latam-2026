//Time Complexity: O(n log n), where n is the number of elements
//Space Complexity: O(n)

//Technique: Two heaps

#include "bits/stdc++.h"
using namespace std;

void solve_running_median(vector<int> &array){

    /*
        For the median we only care about the elements at the middle, so we are going to divide the array
        in two halves. For both halves we are going to retrieve the elements in heaps.
        For the left half (smallest elements) we have a max-heap and for the right half (largest elements) we have a min-heap.
        We will mantain a balance in the size of the heaps so the top of both heaps will be the elements at the middle.

        When the number of elements is odd the left half will be greater in size.
    */

    priority_queue<int, vector<int>> left_part;
    priority_queue<int, vector<int>, greater<int>> right_part;

    int lenght = 0;

    for(int value : array){

        /*
            We push the element in the left half, grab the current maximum element in the left half (which is at the top of the heap) 
            of our array and push that element in the right half (the min heap).
            
            If the right half is greater in size, we push the minimum element (which is at the top) into the left part so the size stays balanced. 
            This way we mantain the invariant of the left half being greater in size when the number of elements is odd.
        */

        left_part.push(value);
        right_part.push(left_part.top());

        left_part.pop();
        lenght++;

        if((int)right_part.size() > left_part.size()){
            left_part.push(right_part.top());
            right_part.pop();
        }

        double median = 0;

        //Based on the parity of the number of elements we have so far, there is one element at the middle or two.

        if(lenght & 1){
            median = left_part.top();
        }
        else{
            median = (double)left_part.top() + (double)right_part.top();
            median = median / 2.0;
        }

        cout << fixed << setprecision(2) << median << " ";
    }
}

int main(){
    vector<int> array = {1, 11, 4, 15, 12};
    solve_running_median(array);

    return 0;
}

//Time Spent: 20 minutes.