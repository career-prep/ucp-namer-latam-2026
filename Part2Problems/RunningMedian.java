package Part2Problems;
import java.util.*;
//dsa used heaps!
//one thing i found out was:
//// PriorityQueue is minHeap by default.
// Collections.reverseOrder() makes it behave like a maxHeap.

//time spent 28min
//time complexity o(n log n) because each insertion is log of n
//space o(n)
public class RunningMedian {
    PriorityQueue<Integer> minHeap;
        PriorityQueue<Integer> maxHeap;
        double[] finalArr;
        int arrIndex=0;
    public double[] runningMedian(int[] arr){
        if(arr==null || arr.length==0){
            return new double[]{};//reutrning empty array
        }
        finalArr = new double[arr.length];
        minHeap = new PriorityQueue<>();
        maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        for(int num: arr){
            addNum(num);
        }
        return finalArr;
 
    }
    private void addNum(int num){
        if(maxHeap.isEmpty() || maxHeap.peek() >= num ){
            maxHeap.add(num);
        }else{
            minHeap.add(num);
        }
        //balancing both heap size difference can not be more then 1
        if(maxHeap.size() > minHeap.size()+1){
            minHeap.add(maxHeap.poll());
        }else if(minHeap.size() > maxHeap.size()+1){
            maxHeap.add(minHeap.poll());
        }
        findMedian();
    }
    private void findMedian(){
        if(minHeap.size() == maxHeap.size()){
             finalArr[arrIndex] = ((minHeap.peek() + maxHeap.peek())/2.0); 
        }else if(minHeap.size() > maxHeap.size()){
            finalArr[arrIndex] = minHeap.peek();
        }else if(maxHeap.size() > minHeap.size()){
            finalArr[arrIndex] = maxHeap.peek();
        }
        arrIndex++;
    }
  


    public static void main(String[] args) {
        RunningMedian rm = new RunningMedian();

        int[] arr = {1, 11, 4, 15, 12};
        int[] arr1 = {};

        double[] result = rm.runningMedian(arr);

        System.out.print("Output: ");
        for (double num : result) {
            System.out.print(num + " ");
        }
    
}

}
