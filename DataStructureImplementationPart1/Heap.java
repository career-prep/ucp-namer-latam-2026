package DataStructureImplementationPart1;
import java.util.*;
public class Heap {
    private ArrayList<Integer> arr;

    public Heap(){
        arr = new ArrayList<>();
    }


    public int top(){
        if(arr.size() ==0){
           throw new IllegalStateException("heap empty");
        }
         return arr.get(0);
        
    }

    public void insert(int x){
        arr.add(x);
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
        int smallest = index;

    if (left < arr.size() && arr.get(left) < arr.get(smallest)) {
        smallest = left;
    }

    if (right < arr.size() && arr.get(right) < arr.get(smallest)) {
        smallest = right;
    }

    if (smallest != index) {
        swap(index, smallest);
        heapifyDown(smallest);
    }
        
    }
    private void heapifyUp(int index){
        if(index==0){
            return;
        }
        int parent  = (index-1)/2;
        if(arr.get(parent) > arr.get(index)){
            swap(parent,index);
            heapifyUp(parent);
        }
    }
    
    private void swap(int index1, int index2){
        int temp = arr.get(index1);
        arr.set(index1,arr.get(index2));
        arr.set(index2,temp);
    }

    
}
