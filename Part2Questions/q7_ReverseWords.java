package Part2Questions;
public class q7_ReverseWords {
    /**
     * Topics: Two pointers & StringBuilder
     * My approach: I will use two pointers from the end of the words length. then each space i see i create a substring form left right
     * and i append it to the stringbuilder. 
     * things to keep in mind  : handle extra spaces , handle null inputs.
     * for extra spaces; what i need was ran a while loop that skips the spaces and i mannual add one space between each words in the output
     * assuming we dont need the ordering of the space also exact when reversing!
     * 
     * 
     */
    public static String reverseWords(String words){
    if(words == null || words.length()==0){
        return "";
    }
    StringBuilder finalString = new StringBuilder();
    int left=words.length()-1;
    int right = words.length()-1;
    while(left>0){
        if(words.charAt(left)==' '){
            if(finalString.isEmpty()){
                finalString.append(words.substring(left+1,right+1));
         }else{
            finalString.append(" "+ words.substring(left+1,right+1));
         }
         while(left>0 && words.charAt(left)==' '){
            left--;
         }
         right = left;
        }else{
            left--;
        }
        
    }
    if(finalString.isEmpty()){ //added this check so  testcase 5 can run correctly
        finalString.append(words.substring(left,right+1));
    }else{
        finalString.append(" "+words.substring(left,right+1));
    }
    
    return finalString.toString();
    }

    public static void main(String[] args){
        String test1 = "Uber Career Prep";
        System.out.println(reverseWords(test1));
         String test2 = "   Uber   Career   Prep";
        System.out.println(reverseWords(test2));
         String test3 = "I Live, In YORKW a b";
        System.out.println(reverseWords(test3));
        String test4 = "I Live, In YORKW a b   ";
        System.out.println(reverseWords(test4));
        String test5 = "123";// i can see extra space at the start when the input has no spaces.(fixed line 35)
        System.out.println(reverseWords(test5));
    }
    //time taken 35min
    //time compelxity : o(n) where n is the length of the words and space is o(n) because i use extrasapce for stringbuilder
    
}
