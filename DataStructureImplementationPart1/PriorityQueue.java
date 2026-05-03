package DataStructureImplementationPart1;
import java.util.*;
import java.util.ArrayList;

public class PriorityQueue {
    static class Pair{
        String value;
        int priority;
        Pair(String value,int priority){
            this.value = value;
            this.priority = priority; 
        }
    }
    private ArrayList<Pair> arr;

    public PriorityQueue(){
        arr = new ArrayList<>();
    }


    public String top(){
        if(arr.size() ==0){
           throw new IllegalStateException("heap empty");
        }
         return arr.get(0).value;
        
    }

    public void insert(String x, int weight){
        Pair tempPair = new Pair(x,weight);
        arr.add(tempPair);
        heapifyUp(arr.size()-1);
    }

    public void remove(){
        if (arr.size() == 0) {
            throw new IllegalStateException("heap empty");
        }
        arr.set(0,arr.get(arr.size()-1));
        arr.remove(arr.size()-1);
        if(arr.size()>0){
              heapifyDown(0);
        }
      
    }
    private void heapifyDown(int index){
        int left = 2 * index + 1;
        int right = 2 * index + 2;
        int largest = index;

    if (left < arr.size() && arr.get(left).priority > arr.get(largest).priority) {
        largest = left;
    }

    if (right < arr.size() && arr.get(right).priority > arr.get(largest).priority) {
        largest = right;
    }

    if (largest != index) {
        swap(index, largest);
        heapifyDown(largest);
    }
        
    }
    private void heapifyUp(int index){
        if(index==0){
            return;
        }
        int parent  = (index-1)/2;
        if(arr.get(parent).priority < arr.get(index).priority){
            swap(parent,index);
            heapifyUp(parent);
        }
    }
    
    private void swap(int index1, int index2){
        Pair temp = arr.get(index1);
        arr.set(index1,arr.get(index2));
        arr.set(index2,temp);
    }
}
