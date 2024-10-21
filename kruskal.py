class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            # Union by rank
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

class Kruskal:
    def __init__(self, vertices, edges):
        self.vertices = vertices  # Number of vertices
        self.edges = edges        # List of edges in the format (u, v, weight)

    def run(self):
        # Sort edges by their weight
        self.edges.sort(key=lambda edge: edge[2])

        uf = UnionFind(self.vertices)
        mst = []  # List to store the Minimum Spanning Tree edges
        total_cost = 0  # Total cost of the Minimum Spanning Tree

        for u, v, weight in self.edges:
            # Check if including this edge forms a cycle
            if uf.find(u) != uf.find(v):
                uf.union(u, v)
                mst.append((u, v, weight))
                total_cost += weight

        return mst, total_cost

    def print_minimum_spanning_tree(self, mst, total_cost):
        print("Minimum Spanning Tree (MST):")
        for u, v, weight in mst:
            print(f"Edge: V{u} -> V{v}, Weight: {weight}")
        print(f"Total cost of MST: {total_cost}")

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

# Run Kruskal's Algorithm
kruskal = Kruskal(vertices, edges)
mst, total_cost = kruskal.run()

# Print the Minimum Spanning Tree and its total cost
kruskal.print_minimum_spanning_tree(mst, total_cost)
