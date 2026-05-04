#include "bits/stdc++.h";

using namespace std;

class Heap {
private:
    vector<int> arr;

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
    int top() {
        return arr[0];
    }

    //Put the element at the end of the heap, and relocate it if necessary.
    void insert(int x) {
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