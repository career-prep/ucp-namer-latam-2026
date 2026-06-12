package Part2Problems;
import Part1DataStructureImplementation.Trie;
import java.util.*;

//time spend 35min 
//time and space i am not sure im confused, i think o(n) for both ik recursions tack is o(n)
public class Boggle {
    Trie trie = new Trie();
    public List<String> boggle(Set<String> dictionary, char[][] board){
       
        for(String word: dictionary){
            trie.insert(word.toLowerCase());
        }
        boolean[][] visited = new boolean[board.length][board[0].length];
        Set<String> currSet = new HashSet<>();
        for(int i=0;i<board.length;i++){
            for(int j=0;j<board[0].length;j++){
                
                dfs(board,visited,i,j,"" ,currSet);
                
            }
        }
        return new ArrayList<>(currSet);
    }
    private void dfs(char[][] board, boolean[][] visited,int row,int col,String currWord,Set<String> seenSet){
        if(row<0 || col <0 || row>= board.length || col >=board[0].length|| visited[row][col]){
            return;
        }
        currWord += Character.toLowerCase(board[row][col]);
        if(!trie.startsWith(currWord)){
            return;
        }
        if (trie.isValidWord(currWord)) {
    seenSet.add(currWord);
}

        visited[row][col] = true;
        dfs( board,  visited, row+1, col,currWord, seenSet);
        dfs( board,  visited, row-1, col,currWord, seenSet);
        dfs( board,  visited, row, col+1,currWord, seenSet);
        dfs( board,  visited, row, col-1,currWord, seenSet);
        dfs( board,  visited, row+1, col+1,currWord, seenSet);
        dfs( board,  visited, row-1, col-1,currWord, seenSet);
         dfs( board,  visited, row+1, col-1,currWord, seenSet);
          dfs( board,  visited, row-1, col+1,currWord, seenSet);
        visited[row][col] = false;
      
    }
    public static void main(String[] args) {
    Boggle boggle = new Boggle();

    Set<String> dictionary = new HashSet<>();

    dictionary.add("Ace");
    dictionary.add("Ape");
    dictionary.add("Cape");
    dictionary.add("Clap");
    dictionary.add("Clay");
    dictionary.add("Race");
    dictionary.add("Ray");
    dictionary.add("Tap");
    dictionary.add("Tape");
    dictionary.add("Trace");
    dictionary.add("Trap");
    dictionary.add("Tray");
    dictionary.add("Yap");

    char[][] board = {
        {'A', 'D', 'E'},
        {'R', 'C', 'P'},
        {'L', 'A', 'Y'}
    };

    List<String> result = boggle.boggle(dictionary, board);

    System.out.println("Words found:");
    for (String word : result) {
        System.out.println(word);
    }
}
}
        
