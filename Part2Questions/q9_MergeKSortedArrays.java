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

   public class Node{
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
        PriorityQueue<Node> priorityQueue = new PriorityQueue<>();

            
    
    }
}
