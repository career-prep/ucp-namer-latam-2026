// Time spent: 18 mins 47 seconds

#include <iostream>
#include <vector>
#include <string>
using namespace std;

class PriorityQueue {
private:
    vector<pair<string, int>> arr;

    // bubble up at index i
    void bubbleUp(int i){
        while(i > 0){
            int parent = (i - 1) / 2;
            if(arr[i].second > arr[parent].second){ // max heap so flipped from heap impl
                swap(arr[i], arr[parent]);
                i = parent;
            } else {
                break;
            }
        }
    }

    // bubble down from index i. 
    void bubbleDown(int i){
        int n = arr.size();
        while(true){
            int left = 2*i + 1;
            int right = 2*i + 2;
            int largest = i;

            if(left < n && arr[left].second > arr[largest].second) largest = left;
            if(right < n && arr[right].second > arr[largest].second) largest = right;

            if(largest == i) break;
            swap(arr[i], arr[largest]);
            i = largest;
        }
    }

public:
    // returns the highest priority (first) element in the PQ
    int top(){
        if(arr.empty()) return -1;
        return arr[0].second;
    }

    // helper to grab the string since top() returns the weight
    string topElement(){
        if(arr.empty()) return "";
        return arr[0].first;
    }

    // adds string x to the PQ with priority weight
    void insert(string x, int weight){
        arr.push_back({x, weight});
        bubbleUp(arr.size() - 1);
    }

    // removes the highest priority (first) element in the PQ
    void remove(){
        if(arr.empty()) return;
        arr[0] = arr.back();
        arr.pop_back();
        if(!arr.empty()) bubbleDown(0);
    }
};

int main(){
    PriorityQueue pq;
    pq.insert("low", 1);
    pq.insert("high", 10);
    pq.insert("mid", 5);
    pq.insert("highest", 20);

    cout << "Top: " << pq.topElement() << " priority " << pq.top() << " (Expected: highest 20)" << endl;
    pq.remove();
    cout << "After remove: " << pq.topElement() << " priority " << pq.top() << " (Expected: high 10)" << endl;
    pq.remove();
    cout << "After remove: " << pq.topElement() << " priority " << pq.top() << " (Expected: mid 5)" << endl;

    return 0;
}
