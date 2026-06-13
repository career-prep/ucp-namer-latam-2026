package Part2Problems;
import java.util.*;
public class WordBreak {
    //time complexity o(n^2)
    // space o(n) seenSet;
    //timspennd 23 minute
    //dsa used dp array and hashset logic;
    
    
    public boolean wordBreak(List<String> dictionary , String input){
        Set<String> seenSet = new HashSet<>();
        for(String word : dictionary){
            seenSet.add(word.toLowerCase());
        }
        boolean[] dp = new boolean[input.length()+1];
        dp[0] = true;
        for(int i=1;i<=input.length();i++){
            for(int j=0;j<i;j++){
                String subString = input.substring(j,i);
                if(dp[j] && seenSet.contains(subString)){
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[dp.length-1];

    }
   public static void main(String[] args) {

        WordBreak wb = new WordBreak();

        List<String> currList = Arrays.asList(
                "Elf",
                "Go",
                "Golf",
                "Man",
                "Manatee",
                "Not",
                "Note",
                "Pig",
                "Quip",
                "Tee",
                "Teen"
        );

        System.out.println(wb.wordBreak(currList, "mangolf"));        // true
        System.out.println(wb.wordBreak(currList, "manateenotelf"));  // true
        System.out.println(wb.wordBreak(currList, "quipig"));         // false
    }
}
