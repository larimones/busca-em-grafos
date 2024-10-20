class BellmanFord:
    def __init__(self, vertices, edges):
        self.vertices = vertices  # Number of vertices
        self.edges = edges        # List of edges in the format (u, v, weight)
        self.INF = float('inf')

    def run(self, source):
        # Initialize distances and predecessors
        distance = [self.INF] * self.vertices
        predecessor = [None] * self.vertices
        distance[source] = 0

        # Relax all edges (vertices-1) times
        for _ in range(self.vertices - 1):
            for u, v, weight in self.edges:
                if distance[u] != self.INF and distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight
                    predecessor[v] = u

        # Check for negative weight cycles
        for u, v, weight in self.edges:
            if distance[u] != self.INF and distance[u] + weight < distance[v]:
                raise ValueError("Graph contains a negative weight cycle")

        return distance, predecessor

    def print_minimum_cost_tree(self, distance, predecessor):
        print("Minimum Cost Tree (Shortest Path Tree):")
        for v in range(1, self.vertices):
            if predecessor[v] is not None:
                u = predecessor[v]
                # Find the weight of the edge between u and v
                for edge in self.edges:
                    if edge[0] == u and edge[1] == v:
                        weight = edge[2]
                        print(f"Edge: V{u} -> V{v}, Weight: {weight}")

# Graph edges (u, v, weight)
edges = [
    (0, 1, 3.9), (0, 2, 5.0), (0, 3, 0.7),  # V0 to V1, V2, V3
    (1, 4, 0.3),                            # V1 to V4
    (2, 1, 9.7), (2, 4, 0.7), (2, 5, 3.13), # V2 to V1, V4, V5
    (3, 5, 0.9),                            # V3 to V5
    (4, 5, 3.7)                             # V4 to V5
]

# Number of vertices
vertices = 6

# Run Bellman-Ford Algorithm
bf = BellmanFord(vertices, edges)
source_vertex = 0

try:
    distance, predecessor = bf.run(source_vertex)

    # Output distances and predecessors
    print("Distance Array:", distance)
    print("Predecessor Array:", predecessor)

    # Print the minimum cost tree
    bf.print_minimum_cost_tree(distance, predecessor)

except ValueError as ve:
    print(ve)
