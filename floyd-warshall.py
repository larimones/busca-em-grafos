import numpy as np

# Number of vertices
V = 6
inf = float('inf')

# Graph representation with weights, using 0.0 for no edges and positive values for edge weights
graph = [
    # V0   V1    V2    V3    V4    V5
    [0,   3.9,  5.0,  0.7,  0.0,  0.0],  # V0
    [0.0, 0.0,  0.0,  0.0,  0.3,  0.0],  # V1
    [0.0,  9.7,  0.0,  0.0,  0.7,  3.13], # V2
    [0.0,  0.0,  0.0,  0.0,  0.0,  0.9],  # V3
    [0.0,  0.0,  0.0,  0.0,  0.0,  3.7],  # V4
    [0.0,  0.0,  0.0,  0.0,  0.0,  0.0],  # V5
]

# Initialize distance matrix with weights from the graph
# If the weight is 0 (and not on the diagonal), we treat it as 'inf' (no direct path)
dist = np.array([[inf if graph[i][j] == 0 and i != j else graph[i][j] for j in range(V)] for i in range(V)])

# Initialize the predecessor matrix
# Set the predecessor to None if no edge, otherwise the vertex index
pred = np.array([[None if i == j or graph[i][j] == 0 else i for j in range(V)] for i in range(V)])

# Floyd-Warshall Algorithm
for k in range(V):
    for i in range(V):
        for j in range(V):
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                pred[i][j] = pred[k][j]

# Function to print matrices
def print_matrices(dist, pred):
    print("Distance Matrix:")
    for row in dist:
        print(["inf" if x == inf else round(x, 2) for x in row])

    print("\nPredecessor Matrix:")
    for row in pred:
        print(row)

# Display the distance and predecessor matrices
print_matrices(dist, pred)
