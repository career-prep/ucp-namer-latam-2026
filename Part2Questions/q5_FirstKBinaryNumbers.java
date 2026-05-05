package Part2Questions;
import java.util.*;
/**
 * Approach:
 * I use a queue to generate binary numbers in order.
 * Start with "1", then for each number, append "0" and "1"
 * and add them back to the queue. This ensures numbers are
 * generated level by level like BFS.
 *
 * DSA used: Queue 
 *
 * Time Complexity: O(n) → generate n binary numbers
 * Space Complexity: O(n) → queue + result array
 */
public class q5_FirstKBinaryNumbers {
    
    static String[] firstKBinaryNumbers(int n){
        if(n==0){
            return new String[] {"0"};
        }
        Queue<String> queue = new LinkedList<>();
        String[] finalArr = new String[n];
        finalArr[0] = "0";
        queue.add("1");
        for(int i=1;i<n;i++){
            
           
           
                String removedChar = queue.remove();
                queue.add(removedChar + "0");
                queue.add(removedChar + "1");
                finalArr[i] = removedChar;
                
            
          
            
        }
        return finalArr;
    }
    public static void main(String[] args){
        String[] result = firstKBinaryNumbers(10);
        System.out.println(Arrays.toString(result));
    }
}
