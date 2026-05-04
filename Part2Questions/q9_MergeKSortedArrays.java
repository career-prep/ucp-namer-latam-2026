package Part2Questions;

import java.util.*;

public class q9_MergeKSortedArrays {
    /**
     Brute force:
    * Loop through all arrays, store every value in one array, then sort it using Arrays.sort().
    *
    * My approach:
    * Since each array is already sorted, I can use a min heap / PriorityQueue.
    * I will first compare the first value from each array.
    * Then I repeatedly remove the smallest value and add the next value
    * from the same array.
    *
    * To do this, I will create a Node class that stores:
    * - value
    * - arrayIndex
    * - valueIndex
    */

   static class Node{
        int value;
        int arrayIndex;
        int valueIndex;
        Node(int value,int arrayIndex,int valueIndex){
            this.value = value;
            this.arrayIndex = arrayIndex;
            this.valueIndex = valueIndex;

        }
   }
    public static int[] mergeKSortedArrays(int numArr, int[][] sortedArr){
        if(sortedArr == null || sortedArr.length==0){
            return new int[] {};
        }
        PriorityQueue<Node> priorityQueue = new PriorityQueue<>(
            (a, b) -> Integer.compare(a.value,b.value) // minHeap;
        );
        for(int i=0;i<sortedArr.length;i++){
            if(sortedArr[i].length >0){
                Node newNode = new Node(sortedArr[i][0],i,0);
                priorityQueue.add(newNode);
            }
        }
        int totalSize = 0;
        for(int i=0;i<sortedArr.length;i++){
            totalSize += sortedArr[i].length;

        }
        int[] result = new int[totalSize];
        int currResultIndex = 0;
        while(!priorityQueue.isEmpty()){
            Node minElement = priorityQueue.poll();
            result[currResultIndex] = minElement.value;
            currResultIndex++;
            int nextIndex = minElement.valueIndex+1;
            if(nextIndex < sortedArr[minElement.arrayIndex].length){
                Node tempNode = new Node(sortedArr[minElement.arrayIndex][nextIndex],minElement.arrayIndex,nextIndex); 
                priorityQueue.add(tempNode);
            }

        }
        return result;
            
    
    }
    public static void main(String[] args) {
    int[][] arr = {
        {1, 2, 3, 4, 5},
        {1, 3, 5, 7, 9},
        
    };
     int[][] arr1 = {
        {1, 4, 7, 9},
        {2, 6, 7, 10, 11, 13, 15},
        {3, 8, 12, 13, 16}
        
    };
    int[][] arr2 = {
        {}
        
    };

    System.out.println(Arrays.toString(mergeKSortedArrays(2,arr)));
    System.out.println(Arrays.toString(mergeKSortedArrays(3,arr1)));
    System.out.println(Arrays.toString(mergeKSortedArrays(3,arr2)));
}
}
//time taken 40 min
//time complexity o(n log k) wehre k is num of arrays and n is total number of elemts in each array 
// space is o(n) 
