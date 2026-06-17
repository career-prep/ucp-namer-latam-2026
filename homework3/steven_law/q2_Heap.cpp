// Time spent: 36 mins 22 seconds

#include <iostream>
#include <vector>
using namespace std;

class Heap {
private:
    vector<int> arr;

    // bubble up at index i
    void bubbleUp(int i){
        while(i > 0){
            int parent = (i - 1) / 2;
            if(arr[i] < arr[parent]){
                swap(arr[i], arr[parent]);
                i = parent;
            } else {
                break;
            }
        }
    }

    // bubble down from index i
    void bubbleDown(int i){
        int n = arr.size();
        while(true){
            int left = 2*i + 1;
            int right = 2*i + 2;
            int smallest = i;

            if(left < n && arr[left] < arr[smallest]) smallest = left;
            if(right < n && arr[right] < arr[smallest]) smallest = right;

            if(smallest == i) break;
            swap(arr[i], arr[smallest]);
            i = smallest;
        }
    }

public:
    // returns the min (top) element in the heap
    int top(){
        if(arr.empty()) return -1;
        return arr[0];
    }

    // adds int x to the heap in the appropriate position
    void insert(int x){
        arr.push_back(x);
        bubbleUp(arr.size() - 1);
    }

    // removes the min (top) element in the heap
    void remove(){
        if(arr.empty()) return;
        arr[0] = arr.back();
        arr.pop_back();
        if(!arr.empty()) bubbleDown(0);
    }
};

int main(){
    Heap h;
    h.insert(5);
    h.insert(3);
    h.insert(8);
    h.insert(1);
    h.insert(9);
    h.insert(2);

    cout << "Top: " << h.top() << " (Expected: 1)" << endl;
    h.remove();
    cout << "Top after remove: " << h.top() << " (Expected: 2)" << endl;
    h.remove();
    cout << "Top after remove: " << h.top() << " (Expected: 3)" << endl;
    h.insert(0);
    cout << "Top after insert 0: " << h.top() << " (Expected: 0)" << endl;

    return 0;
}
