package homework1.nitaimahat;
import java.util.*;
public class q8_MergeIntervals {
    //time o(n logn n) because of sorting and space complexitty is o(n) 
    public static int[][] mergeInterval(int[][] inputArray){
        //wrote functions in short
        Arrays.sort(inputArray, (a,b) -> Integer.compare(a[0],b[0]));//lambdas
        
        int[][] ans = new int[inputArray.length][2];
        int currentStart = inputArray[0][0];
        int currentEnd = inputArray[0][1];

        int idx = 0;
        int left = 1;
        while(left < inputArray.length){
            int nextStart = inputArray[left][0];
            int nextEnd = inputArray[left][1];

            if(currentEnd >= nextStart){
                currentEnd = Math.max(currentEnd,nextEnd);
            }else{
                ans[idx][0] = currentStart;
                ans[idx][1] = currentEnd;
                idx++;
                currentStart = nextStart;
                currentEnd = nextEnd;
            }
            left++;

        }
        //need to run one more loop since last interval is not accoounteed for above
        //as nextstart will be empty and will not populate the ans

        ans[idx][0] = currentStart;
        ans[idx][1] = currentEnd;
        idx++;
        return Arrays.copyOf(ans,idx);

    }
    //time took 38 min
    //for printing purpose
    private static void printIntervals(int[][] arr) {
    for (int[] interval : arr) {
        System.out.print("[" + interval[0] + ", " + interval[1] + "] ");
    }
    System.out.println();
}

    public static void main(String[] args) {
    int[][] test1 = {{2,3},{4,8},{1,2},{5,7},{9,12}};
    int[][] test2 = {{5,8},{6,10},{2,4},{3,6}};
    int[][] test3 = {{10,12},{5,6},{7,9},{1,3}};
    

    printIntervals(mergeInterval(test1));
    printIntervals(mergeInterval(test2));
    printIntervals(mergeInterval(test3));
    
}

}
