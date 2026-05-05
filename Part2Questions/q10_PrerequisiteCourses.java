package Part2Questions;

import java.util.*;
/**
 * Approach:
 * I treat courses as a graph and use topological sort (BFS).
 * I track how many prerequisites each course has (inDegree).
 * I start with courses that have 0 prerequisites, then gradually
 * reduce dependencies of other courses as I process them.
 * If I can process all courses, I return the order; otherwise,
 * a cycle exists so I return an empty list.
 *
 * DSA used: Graph  + BFS 
 *
 * 
 */
public class q10_PrerequisiteCourses {

    public static List<String> prerequisiteCourses(
            List<String> courses,
            Map<String, List<String>> prerequisites
    ) {
        if (courses == null || courses.size() == 0) {
            return new ArrayList<>();
        }

        Map<String, List<String>> graph = new HashMap<>();
        Map<String, Integer> inDegree = new HashMap<>();
        Queue<String> queue = new LinkedList<>();
        List<String> result = new ArrayList<>();

        for (String course : courses) {
            graph.put(course, new ArrayList<>());
            inDegree.put(course, 0);
        }

        for (String course : prerequisites.keySet()) {
            for (String prereq : prerequisites.get(course)) {
                graph.get(prereq).add(course);
                inDegree.put(course, inDegree.get(course) + 1);
            }
        }

        for (String course : courses) {
            if (inDegree.get(course) == 0) {
                queue.add(course);
            }
        }

        while (!queue.isEmpty()) {
            String current = queue.remove();
            result.add(current);

            for (String nextCourse : graph.get(current)) {
                inDegree.put(nextCourse, inDegree.get(nextCourse) - 1);

                if (inDegree.get(nextCourse) == 0) {
                    queue.add(nextCourse);
                }
            }
        }

        if (result.size() != courses.size()) {
            return new ArrayList<>();
        }

        return result;
    }

    public static void main(String[] args) {
        List<String> courses1 = Arrays.asList(
                "Intro to Programming",
                "Data Structures",
                "Algorithms",
                "Operating Systems"
        );

        Map<String, List<String>> prereqs1 = new HashMap<>();
        prereqs1.put("Data Structures", Arrays.asList("Intro to Programming"));
        prereqs1.put("Algorithms", Arrays.asList("Data Structures"));
        prereqs1.put("Operating Systems", Arrays.asList("Data Structures"));

        System.out.println(prerequisiteCourses(courses1, prereqs1));


        List<String> courses2 = Arrays.asList(
                "A", "B", "C"
        );

        Map<String, List<String>> prereqs2 = new HashMap<>();
        prereqs2.put("A", Arrays.asList("B"));
        prereqs2.put("B", Arrays.asList("C"));
        prereqs2.put("C", Arrays.asList("A"));

        System.out.println(prerequisiteCourses(courses2, prereqs2)); // cycle → []
    }
    //time taken 35min 
    //time O(N + M) sapce O(N + M) // n is number of courses and m is number of prerequisite realtionships
}