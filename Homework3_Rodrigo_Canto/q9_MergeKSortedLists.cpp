//Time Complexity: O(N * log(k)).
//Space Complexity: O(K).
//Technique: Min-Heap

//N is the number of elements
//K is the number of lists.

#include "bits/stdc++.h"
using namespace std;

#include <iostream>
#include <vector>
#include <string>
#include <utility>
#include <algorithm>

using namespace std;

class Heap {
private:
    vector<pair<int, pair<int,int>>> arr;

    void relocate_Up(int index) {

        //For min-heap

        //If the index is not the root and my father is greater than me,
        //we swap values to mantain the structure of the tree.
        while (index > 0 && arr[(index - 1) / 2] > arr[index]) {
            swap(arr[index], arr[(index - 1) / 2]);
            index = (index - 1) / 2;
        }
    }

    //To handle removals in the heap
    void relocate_Down(int index) {
        int minIndex = index;
        int leftChild = 2 * index + 1;
        int rightChild = 2 * index + 2;

        //Compare left child.
        if (leftChild < arr.size() && arr[leftChild] < arr[minIndex]) {
            minIndex = leftChild;
        }
        // Compare right child
        if (rightChild < arr.size() && arr[rightChild] < arr[minIndex]) {
            minIndex = rightChild;
        }

        //If there is a change, we keep going down into the tree.
        if (index != minIndex) {
            swap(arr[index], arr[minIndex]);
            relocate_Down(minIndex);
        }
    }

public:

    //This function must not be called if the heap is empty.
    pair<int, pair<int,int>> top() {
        return arr[0];
    }

    //Put the element at the end of the heap, and relocate it if necessary.
    void insert(pair<int, pair<int,int>> x) {
        arr.push_back(x);
        relocate_Up(arr.size() - 1);
    }

    void remove() {
        if (arr.empty()) return;

        //We move the last element to the root and relocate its value if necessary.
        arr[0] = arr.back();
        arr.pop_back();

        if (!arr.empty()) {
            relocate_Down(0);
        }
    }

    bool empty() {
        return arr.empty();
    }
};


vector<int> solveMergeKSortedArrays(int k, vector<vector<int>> &arrays){

    vector<int> answer;
    Heap heap;

    //We start with the first element for every list.
    for(int i = 0; i < k; ++i){
        heap.insert({arrays[i][0], {0, i}});
    }

    /*
        When we process the minimum element, we check its position in its corresponding list.
        The heap will retrieved those values.
        If there is a next value in that list we push that value into the heap.

        The size of our heap will be at most k.
    */

    while(!heap.empty()){

        auto curr = heap.top();
        heap.remove();

        int value = curr.first;
        int idx = curr.second.first;
        int list_idx = curr.second.second;

        answer.push_back(value);

        if(idx + 1 < arrays[list_idx].size()){
            heap.insert({arrays[list_idx][idx + 1], {idx + 1, list_idx}});
        }
    }

    return answer;
}

int main() {

    //int k = 2;

    /*
    vector<vector<int>> arrays = {
        {1, 2, 3, 4, 5},
        {1, 3, 5, 7, 9}
    };
    */

    int k = 3;
    
    vector<vector<int>> arrays = {
        {1, 4, 7, 9},
        {2, 6, 7, 10, 11, 13, 15},
        {3, 8, 12, 13, 16}
    };

    for(int value : solveMergeKSortedArrays(k, arrays)){
        cout << value << " ";
    }

    return 0;
}

//Time Spent: 22 minutes