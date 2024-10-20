# Using Dijkstra's Algorithm, the distance array and the predecessor array
# and the minimum cost tree.

import heapq

# Function to implement Dijkstra's Algorithm
def dijkstra(graph, source):
    # Number of vertices
    num_vertices = len(graph)

    # Initialize distance array and predecessor array
    distances = [float('inf')] * num_vertices
    predecessors = [None] * num_vertices
    distances[source] = 0

    # Priority queue to hold (distance, vertex)
    priority_queue = [(0, source)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Skip processing if we find a longer path in the queue
        if current_distance > distances[current_vertex]:
            continue

        # Check adjacent vertices
        for neighbor, weight in enumerate(graph[current_vertex]):
            if weight != 0:  # If there is an edge
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    predecessors[neighbor] = current_vertex
                    heapq.heappush(priority_queue, (distance, neighbor))

    return distances, predecessors

# Function to build and print the minimum cost tree
def print_shortest_path_tree(predecessors, distances):
    print("Minimum Cost Tree (Shortest Path Tree):")
    for vertex, predecessor in enumerate(predecessors):
        if predecessor is not None:
            print(f"Edge: V{predecessor} -> V{vertex}, Weight: {distances[vertex] - distances[predecessor]}")

# Adjacency matrix representation of the graph
graph = [
    # V0   V1    V2    V3    V4    V5
    [0,  3.9,  5.0,  0.7,  0.0,  0.0],  # V0
    [0.0, 0.0,  0.0,  0.0,  0.3,  0.0],  # V1
    [0.0,  9.7,  0.0,  0.0,  0.7,  3.13],  # V2
    [0.0,  0.0,  0.0,  0.0,  0.0,  0.9],  # V3
    [0.0,  0.0,  0.0,  0.0,  0.0,  3.7],  # V4
    [0.0,  0.0,  0.0,  0.0,  0.0,  0.0],  # V5
]

# Running Dijkstra's algorithm from source vertex V0
source_vertex = 0
distances, predecessors = dijkstra(graph, source_vertex)

# Print the distance array and the predecessor array
print("Distance Array:", distances)
print("Predecessor Array:", predecessors)

# Print the minimum cost tree
print_shortest_path_tree(predecessors, distances)
