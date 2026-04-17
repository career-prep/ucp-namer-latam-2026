package DataStructureImplementationPart1;
import java.util.*;
public class question1AdjSet {

    
    public static void main(String[] args){
        //graph algorithm using adj set/list


        int target = 0;
        int[][] edges = {{1,2}, {2,3} ,{1,3},{3,2}, {2,0}};
        Map<Integer,Set<Integer>> graph = createGraph(edges.length,edges);
        //to check if out put is correct
        if(bfsSearch(target,graph)){
            System.out.println("bfs: True");
        }else{
            System.out.println("bfs: False");
        }
         if(dfsSearch(target,graph)){
            System.out.println("dfs: True");
        }else{
            System.out.println("dfs: False");
        }
    }
      /**
     * This fucntions creates adajency list and stores it in a map with its key and reutrns a graph to be processed.
     * @param length
     * @param edges
     * @return
     */
    static Map<Integer,Set<Integer>> createGraph(int length, int[][] edges){
        Map<Integer,Set<Integer>> graph = new HashMap<>();
        for(int i=0;i<length;i++){
            int u = edges[i][0];
            int v = edges[i][1];
            if(!graph.containsKey(u)){
                 graph.put(u,new HashSet<>());
            }
            Set<Integer> tempSet = graph.get(u);
            tempSet.add(v);
            if(!graph.containsKey(v)){
                graph.put(v,new HashSet<>());
            }
        }
        return graph;

    }



    
    /**
     * This function uses a bfs approach to go through the graph to find a target if found return true else false
     * @param target given through main.
     * @param graph created by function createGraph from main. 
     * @return boolean calcualted using bfs
     */
    static boolean bfsSearch(int target, Map<Integer,Set<Integer>> graph){
        if(graph==null){
            return false;
        }
        Queue<Integer> queue = new LinkedList<>();
        Set<Integer> visited = new HashSet<>();
        for(int key : graph.keySet()){
            if (!visited.contains(key)){
            queue.add(key);
            visited.add(key);
            while(!queue.isEmpty()){
                int currentKey = queue.remove();
                if(currentKey == target){
                    System.out.println(currentKey);// to check if the program is outputting true for the correct target variable
                    return true;
                }
                Set<Integer> neighbors = graph.get(currentKey);
                for(int num : neighbors)
                    if(!visited.contains(num)){
                        visited.add(num);
                        queue.add(num);
                }
            }
        }
        }
           return false;
           //space complexity o(n) because i have extra space when i created queues and hashSet
           // time complexity would be o(n) to be more specific its o(number of keys + number of edges)
    }




    /**
     *  This function uses a dfs approach to go through the graph to find a target if found return true else false
     * @param target
     * @param graph
     * @return
     */
    static boolean dfsSearch(int target,Map<Integer,Set<Integer>> graph){
        if(graph==null){
            return false;
        }
        Set<Integer> visited = new HashSet<>();
        for(int key: graph.keySet()){
            if(!visited.contains(key)){
                if(dfs(target,graph,visited,key)){
                    return true;
                }
            }
        }
        return false;
    }
    private static boolean dfs(int target,Map<Integer,Set<Integer>> graph,Set<Integer> visited,int key){
        Set<Integer> temp = graph.get(key);
        if(key ==target){
            return true;
        }
        visited.add(key);
        for(int neighbors : temp){
            if(!visited.contains(neighbors)){
                if(dfs(target,graph,visited,neighbors)){
                    return true;
                }
            }
         
            
        }
        return false;
    }
    //time complexity o(n+m) where n and m are keys and vlaues of map
    //space complexityo(n)  due to visited set and recursion stack
  
}
