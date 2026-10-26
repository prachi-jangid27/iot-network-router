
import heapq


def find_shortest_path(graph, start, destination):
    # Initialize distances and previous nodes
    distances = {node: float("inf") for node in graph}
    previous = {node: None for node in graph}

    distances[start] = 0

    # Min-heap stores (total_latency, node)
    min_heap = [(0, start)]

    while min_heap:
        current_distance, current_node = heapq.heappop(min_heap)

        # Ignore outdated heap entries
        if current_distance > distances[current_node]:
            continue

        # Stop when destination is reached
        if current_node == destination:
            break

        # Explore neighboring nodes
        for neighbor, latency in graph[current_node].items():
            new_distance = current_distance + latency

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current_node

                heapq.heappush(
                    min_heap,
                    (new_distance, neighbor)
                )

    # Check whether a route exists
    if distances[destination] == float("inf"):
        return [], float("inf")

    # Reconstruct the shortest path
    path = []
    current_node = destination

    while current_node is not None:
        path.append(current_node)
        current_node = previous[current_node]

    path.reverse()

    return path, distances[destination]


if __name__ == "__main__":
    # Sample IoT network with link latencies in milliseconds
    graph = {
        "A": {"B": 10, "C": 4},
        "B": {"A": 10, "D": 8},
        "C": {"A": 4, "D": 3},
        "D": {"B": 8, "C": 3, "E": 5},
        "E": {"D": 5}
    }

    start_node = "A"
    destination_node = "E"

    path, latency = find_shortest_path(
        graph,
        start_node,
        destination_node
    )

    if path:
        print("Best route:", " -> ".join(path))
        print("Total latency:", latency, "ms")
    else:
        print("No route exists between the selected nodes.")

