#include "bits/stdc++.h"

using namespace std;

class PriorityQueue {
private:
    
    vector<pair<string, int>> arr;

    void relocate_Up(int index) {

        //For min-heap

        //If the index is not the root and my father is greater than me,
        //we swap values to mantain the structure of the tree.

        //In this case, we compare the second value because that gives us the priority for the elements.
        while (index > 0 && arr[(index - 1) / 2].second < arr[index].second) {
            swap(arr[index], arr[(index - 1) / 2]);
            index = (index - 1) / 2;
        }
    }

    //To handle removals in the tree.
    void relocate_Down(int index) {
        int maxIndex = index;
        int left = 2 * index + 1;
        int right = 2 * index + 2;

        //Compare left child.
        if (left < arr.size() && arr[left].second > arr[maxIndex].second) {
            maxIndex = left;
        }

        //Compare right child.
        if (right < arr.size() && arr[right].second > arr[maxIndex].second) {
            maxIndex = right;
        }

        //If there is a change, we keep going down into the tree.
        if (index != maxIndex) {
            swap(arr[index], arr[maxIndex]);
            relocate_Down(maxIndex);
        }
    }

public:

    //This function must not be called if the heap is empty.
    string top() {
        return arr[0].first; 
    }   

    //Put the element at the end of the heap, and relocate it if necessary.
    void insert(string x, int weight) {
        arr.push_back({x, weight});
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