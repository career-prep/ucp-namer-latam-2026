package homework1.nitaimahat;
import java.util.*;
public class q9_DedupArray {
    //time o(n) space o(n)
    public static int[] dedupArray(int[] inputArray){
        int currentIndex = 0;
        Set<Integer> seenSet = new HashSet<>();

        for(int i=0;i<inputArray.length;i++){
            if(!seenSet.contains(inputArray[i])){
                seenSet.add(inputArray[i]);
                inputArray[currentIndex] = inputArray[i];
                currentIndex++;
            }
        }
        return Arrays.copyOf(inputArray,currentIndex);
    }
    //time spend: 10min


    //printng code
    private static void printArray(int[] arr) {
    System.out.print("[");
    for (int i = 0; i < arr.length; i++) {
        System.out.print(arr[i]);
        if (i < arr.length - 1) {
            System.out.print(", ");
        }
    }
    System.out.println("]");
}

    public static void main(String[] args) {

    int[] test1 = {1, 2, 2, 3, 3, 3, 4, 4, 4, 4};
    int[] test2 = {0, 0, 1, 4, 5, 5, 5, 8, 9, 9, 10, 11, 15, 15};
    int[] test3 = {1, 3, 4, 8, 10, 12};
   

    System.out.println("Test 1:");
    printArray(dedupArray(test1));

    System.out.println("Test 2:");
    printArray(dedupArray(test2));

    System.out.println("Test 3:");
    printArray(dedupArray(test3));

   
}

}
