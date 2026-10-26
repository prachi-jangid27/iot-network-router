
import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import random
import heapq

st.set_page_config(
    page_title="IoT Network Routing Simulator",
    page_icon="🌐",
    layout="wide"
)

# Find the shortest path using Dijkstra's algorithm
def find_shortest_path(graph, start, destination):
    distances = {node: float("inf") for node in graph}
    distances[start] = 0

    previous = {}
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        if current_node == destination:
            break

        for neighbor, latency in graph[current_node].items():
            new_distance = current_distance + latency

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current_node

                heapq.heappush(
                    priority_queue,
                    (new_distance, neighbor)
                )

    if distances[destination] == float("inf"):
        return [], float("inf")

    path = []
    current = destination

    while current != start:
        path.append(current)
        current = previous[current]

    path.append(start)
    path.reverse()

    return path, distances[destination]


# Create the IoT network
def create_network():
    return {
        "A": {"B": 10, "C": 4},
        "B": {"A": 10, "D": 8, "E": 7},
        "C": {"A": 4, "D": 3, "F": 9},
        "D": {"B": 8, "C": 3, "E": 5, "F": 6},
        "E": {"B": 7, "D": 5, "F": 2},
        "F": {"C": 9, "D": 6, "E": 2}
    }


# Convert the network into a graph for visualization
def build_graph(network):
    graph = nx.Graph()

    for node in network:
        for neighbor, latency in network[node].items():
            graph.add_edge(node, neighbor, latency=latency)

    return graph


# Dashboard title
st.title("🌐 Dynamic IoT Network Routing Simulator")

st.write(
    "Simulate an IoT network and find the shortest route "
    "using Dijkstra's algorithm."
)

# Initialize the network
if "network" not in st.session_state:
    st.session_state.network = create_network()

network = st.session_state.network

# Select source and destination
source = st.sidebar.selectbox(
    "Source Node",
    list(network.keys()),
    index=0
)

destination = st.sidebar.selectbox(
    "Destination Node",
    list(network.keys()),
    index=5
)

# Simulate changing network latency
if st.sidebar.button("Simulate Network Traffic"):
    updated_network = create_network()

    for node in updated_network:
        for neighbor in list(updated_network[node]):
            if node < neighbor:
                latency = random.randint(2, 20)

                updated_network[node][neighbor] = latency
                updated_network[neighbor][node] = latency

    st.session_state.network = updated_network
    st.rerun()

# Find the shortest route
path, total_latency = find_shortest_path(
    network,
    source,
    destination
)

# Display the network
st.subheader("IoT Network Topology")

graph = build_graph(network)
positions = nx.spring_layout(graph, seed=42)

fig, ax = plt.subplots(figsize=(9, 5))

# Highlight the shortest route
path_edges = list(zip(path, path[1:])) if path else []

edge_colors = [
    "green" if (u, v) in path_edges or (v, u) in path_edges
    else "gray"
    for u, v in graph.edges()
]

nx.draw_networkx(
    graph,
    positions,
    ax=ax,
    node_color="skyblue",
    node_size=1500,
    font_size=12
)

nx.draw_networkx_edges(
    graph,
    positions,
    ax=ax,
    edge_color=edge_colors,
    width=2
)

edge_labels = nx.get_edge_attributes(graph, "latency")

nx.draw_networkx_edge_labels(
    graph,
    positions,
    edge_labels=edge_labels,
    ax=ax
)

ax.axis("off")
st.pyplot(fig)
plt.close(fig)

# Display routing results
st.subheader("Routing Results")

if path:
    st.success("Optimal Route: " + " → ".join(path))
    st.write(f"**Total Latency:** {total_latency} ms")
else:
    st.error("No route exists between these nodes.")

