package Part2Questions;
import  java.util.*;
public class Q6_RoadNetworks {
     /**
     * Approach:
     * I treat this as a graph problem where towns are nodes and roads are edges.
     * The goal is to find how many separate groups/road networks exist.
     * I build the graph and then run BFS from each unvisited town.
     * Every time I start a new BFS, it means I found a new road network.
     *
     * DSA used: Graph  + BFS 
     */

    public static int roadNetworks(List<String> towns, List<String[]> roads) {
        if (towns == null || towns.size() == 0) {
            return 0;
        }

        Map<String, List<String>> graph = new HashMap<>();

        for (String town : towns) {
            graph.put(town, new ArrayList<>());
        }

        for (String[] road : roads) {
            String town1 = road[0];
            String town2 = road[1];

            graph.get(town1).add(town2);
            graph.get(town2).add(town1);
        }

        Set<String> visited = new HashSet<>();
        int networks = 0;

        for (String town : towns) {
            if (!visited.contains(town) && graph.get(town).size() > 0) {
                networks++;
                bfs(town, graph, visited);
            }
        }

        return networks;
    }

    private static void bfs(String start, Map<String, List<String>> graph, Set<String> visited) {
        Queue<String> queue = new LinkedList<>();
        queue.add(start);
        visited.add(start);

        while (!queue.isEmpty()) {
            String current = queue.remove();

            for (String neighbor : graph.get(current)) {
                if (!visited.contains(neighbor)) {
                    visited.add(neighbor);
                    queue.add(neighbor);
                }
            }
        }
    }

    public static void main(String[] args) {
        List<String> towns1 = Arrays.asList(
                "Skagway", "Juneau", "Gustavus", "Homer", "Port Alsworth",
                "Glacier Bay", "Fairbanks", "McCarthy", "Copper Center",
                "Healy", "Anchorage"
        );

        List<String[]> roads1 = new ArrayList<>();
        roads1.add(new String[]{"Anchorage", "Homer"});
        roads1.add(new String[]{"Glacier Bay", "Gustavus"});
        roads1.add(new String[]{"Copper Center", "McCarthy"});
        roads1.add(new String[]{"Anchorage", "Copper Center"});
        roads1.add(new String[]{"Copper Center", "Fairbanks"});
        roads1.add(new String[]{"Healy", "Fairbanks"});
        roads1.add(new String[]{"Healy", "Anchorage"});

        System.out.println(roadNetworks(towns1, roads1)); // 4
    }
    //time spend 30 min 
    //time O(N+M) and space O(N+M)
}

