package Part2Questions;

import java.util.*;

/**
 * Approach:
 * I treat this as a graph problem and use BFS to find the shortest path.
 * The tricky part is that edges must alternate colors, so I keep track of
 * both the current node and the last color used to reach it.
 * At each step, I only move to neighbors with a different color than before.
 * If I reach the destination, I return the distance. If not possible, return -1.
 *
 * DSA used: Graph + BFS 
 */
public class q8_AlternatingPath {
     static class Edge {
        String to;
        String color;

        Edge(String to, String color) {
            this.to = to;
            this.color = color;
        }
    }

    static class State {
        String node;
        String lastColor;
        int distance;

        State(String node, String lastColor, int distance) {
            this.node = node;
            this.lastColor = lastColor;
            this.distance = distance;
        }
    }

    public static int alternatingPath(
            List<String[]> edges,
            String origin,
            String destination
    ) {
        if (origin.equals(destination)) {
            return 0;
        }

        Map<String, List<Edge>> graph = new HashMap<>();

        // Build directed graph
        for (String[] edge : edges) {
            String from = edge[0];
            String to = edge[1];
            String color = edge[2];

            graph.putIfAbsent(from, new ArrayList<>());
            graph.putIfAbsent(to, new ArrayList<>());

            graph.get(from).add(new Edge(to, color));
        }

        Queue<State> queue = new LinkedList<>();
        Set<String> visited = new HashSet<>();

        queue.add(new State(origin, "none", 0));
        visited.add(origin + "-none");

        while (!queue.isEmpty()) {
            State current = queue.poll();

            for (Edge next : graph.getOrDefault(current.node, new ArrayList<>())) {

                // alternating colors
                if (!current.lastColor.equals("none")
                        && current.lastColor.equals(next.color)) {
                    continue;
                }

                if (next.to.equals(destination)) {
                    return current.distance + 1;
                }

                String stateKey = next.to + "-" + next.color;

                if (!visited.contains(stateKey)) {
                    visited.add(stateKey);
                    queue.add(new State(next.to, next.color, current.distance + 1));
                }
            }
        }

        return -1;
    }

    public static void main(String[] args) {
        List<String[]> edges = new ArrayList<>();

        edges.add(new String[]{"A", "B", "blue"});
        edges.add(new String[]{"A", "C", "red"});
        edges.add(new String[]{"B", "D", "blue"});
        edges.add(new String[]{"B", "E", "blue"});
        edges.add(new String[]{"C", "B", "red"});
        edges.add(new String[]{"D", "C", "blue"});
        edges.add(new String[]{"A", "D", "red"});
        edges.add(new String[]{"D", "E", "red"});
        edges.add(new String[]{"E", "C", "red"});

        System.out.println(alternatingPath(edges, "A", "E")); // 4
        System.out.println(alternatingPath(edges, "E", "D")); // -1

        // Edge case: origin == destination
        System.out.println(alternatingPath(edges, "A", "A")); // 0

        // Edge case: no path
        System.out.println(alternatingPath(edges, "C", "E")); // -1

        // Simple valid alternating path
        List<String[]> edges2 = new ArrayList<>();
        edges2.add(new String[]{"A", "B", "red"});
        edges2.add(new String[]{"B", "C", "blue"});
        System.out.println(alternatingPath(edges2, "A", "C")); // 2

        // Invalid because colors repeat
        List<String[]> edges3 = new ArrayList<>();
        edges3.add(new String[]{"A", "B", "red"});
        edges3.add(new String[]{"B", "C", "red"});
        System.out.println(alternatingPath(edges3, "A", "C")); // -1
    }
    //time O(N+M) space O(N+M)
}
