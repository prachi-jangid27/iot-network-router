import heapq

# Dijkstra Algorithm
def dijkstra(graph, start, end):
    queue = [(0, start, [])]
    visited = set()
    
    while queue:
        (cost, node, path) = heapq.heappop(queue)
        if node in visited:
            continue
        visited.add(node)
        path = path + [node]
        
        if node == end:
            return cost, path
            
        for neighbor, weight in graph.get(node, {}).items():
            if neighbor not in visited:
                heapq.heappush(queue, (cost + weight, neighbor, path))
                
    return float("inf"), []

# IoT Network Topology
graph = {
    'Source': {'Router A': 5, 'Router B': 10},
    'Router A': {'Source': 5, 'Router C': 45},
    'Router B': {'Source': 10, 'Router C': 10, 'Destination': 30},
    'Router C': {'Router A': 45, 'Router B': 10, 'Destination': 5},
    'Destination': {'Router B': 30, 'Router C': 5}
}

cost, path = dijkstra(graph, 'Source', 'Destination')

print("\n" + "="*50)
print("🌐 IoT DYNAMIC NETWORK ROUTING SIMULATOR")
print("="*50)
print(f"Optimal Dynamic Path : {' ➔ '.join(path)}")
print(f"Total Network Latency: {cost} ms")
print("="*50 + "\n")
