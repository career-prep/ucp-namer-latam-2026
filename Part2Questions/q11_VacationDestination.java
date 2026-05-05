package Part2Questions;

import java.util.*;

public class q11_VacationDestination {
    /**
     * Algorithm used: Dijkstras Dsa used Graph
     * 
     * so my plan is to think of cities as graph wehre each connectoin has a travel time meaning weighted greaph
     * I will start from origin and explore other cities while choosing the path that takes the least time so far.
     * i will keep track of the least time so far. then count how many cities i can reach within the time limit given
     */

    static class Edge {
        String city;
        double time;

        Edge(String city, double time) {
            this.city = city;
            this.time = time;
        }
    }

    static class State {
        String city;
        double totalTime;

        State(String city, double totalTime) {
            this.city = city;
            this.totalTime = totalTime;
        }
    }

    public static int vacationDestination(List<String[]> routes, String origin, double timeLimit) {
        Map<String, List<Edge>> graph = new HashMap<>();

        
        for (String[] route : routes) {
            String from = route[0];
            String to = route[1];
            double time = Double.parseDouble(route[2]);

            graph.putIfAbsent(from, new ArrayList<>());
            graph.putIfAbsent(to, new ArrayList<>());

            graph.get(from).add(new Edge(to, time));
            graph.get(to).add(new Edge(from, time));
        }

        if (!graph.containsKey(origin)) {
            return 0;
        }

        Map<String, Double> shortestTime = new HashMap<>();

        PriorityQueue<State> pq = new PriorityQueue<>(
            (a, b) -> Double.compare(a.totalTime, b.totalTime)
        );

        shortestTime.put(origin, 0.0);
        pq.add(new State(origin, 0.0));

        while (!pq.isEmpty()) {
            State current = pq.poll();

            if (current.totalTime > shortestTime.get(current.city)) {
                continue;
            }

            for (Edge edge : graph.get(current.city)) {
                double newTime = current.totalTime + edge.time;

                // Add stopover cost only when current city is not the origin
                if (!current.city.equals(origin)) {
                    newTime += 1;
                }

                if (!shortestTime.containsKey(edge.city) || newTime < shortestTime.get(edge.city)) {
                    shortestTime.put(edge.city, newTime);
                    pq.add(new State(edge.city, newTime));
                }
            }
        }

        int count = 0;

        for (String city : shortestTime.keySet()) {
            if (!city.equals(origin) && shortestTime.get(city) <= timeLimit) {
                count++;
            }
        }

        return count;
    }

    public static void main(String[] args) {
        List<String[]> routes = new ArrayList<>();

        routes.add(new String[]{"Boston", "New York", "4"});
        routes.add(new String[]{"New York", "Philadelphia", "2"});
        routes.add(new String[]{"Boston", "Newport", "1.5"});
        routes.add(new String[]{"Washington, D.C.", "Harper's Ferry", "1"});
        routes.add(new String[]{"Boston", "Portland", "2.5"});
        routes.add(new String[]{"Philadelphia", "Washington, D.C.", "2.5"});

        System.out.println(vacationDestination(routes, "New York", 5));  // 2
        System.out.println(vacationDestination(routes, "New York", 7));  // 4
        System.out.println(vacationDestination(routes, "New York", 8));  // 6
    }
}
// Time is O(M log N) space is O(N+M)
//  N = number of cities M = number of routes
