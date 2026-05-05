from collections import deque

# Data Structure: Graph (Adjacency List)
# Algorithm: BFS / Connected Components
# Time Complexity: O(cities + roads)
# Space Complexity: O(cities + roads)


def count_road_networks(cities: list[str], roads: list[tuple[str, str]]) -> int:
    if not cities:
        return 0

    road_map = {city: [] for city in cities}

    for first_city, second_city in roads:
        road_map[first_city].append(second_city)
        road_map[second_city].append(first_city)

    visited_cities = set()
    network_count = 0

    for city in cities:
        if city not in visited_cities:
            network_count += 1
            explore_network(city, road_map, visited_cities)

    return network_count


def explore_network(
    starting_city: str,
    road_map: dict[str, list[str]],
    visited_cities: set[str],
) -> None:
    city_queue = deque([starting_city])
    visited_cities.add(starting_city)

    while city_queue:
        current_city = city_queue.popleft()

        for neighboring_city in road_map[current_city]:
            if neighboring_city not in visited_cities:
                visited_cities.add(neighboring_city)
                city_queue.append(neighboring_city)


def run_tests() -> None:
    assert count_road_networks(
        ["A", "B", "C", "D", "E"],
        [("A", "B"), ("B", "C"), ("D", "E")]
    ) == 2

    assert count_road_networks(
        ["A", "B", "C"],
        [("A", "B"), ("B", "C")]
    ) == 1

    assert count_road_networks(
        ["A", "B", "C"],
        []
    ) == 3

    assert count_road_networks([], []) == 0

    assert count_road_networks(
        ["A"],
        []
    ) == 1

    assert count_road_networks(
        ["A", "B", "C", "D"],
        [("A", "B")]
    ) == 3

    print("All tests passed")


if __name__ == "__main__":
    run_tests()
