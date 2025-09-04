import networkx as nx
import random

def generate_k_regular_graph(N, k):
    """
    Generate a k-regular undirected graph with N nodes.
    """
    if (N * k) % 2 != 0:
        raise ValueError("N * k must be even for a k-regular graph.")
    return nx.random_regular_graph(d=k, n=N)

def bfs_receptive_field(graph, start_node, L):
    """
    Perform BFS up to depth L from the start_node.
    Return the set of nodes in the receptive field.
    """
    visited = set([start_node])
    current_level = set([start_node])

    for _ in range(L):
        next_level = set()
        for node in current_level:
            neighbors = set(graph.neighbors(node))
            next_level.update(neighbors - visited)
        visited.update(next_level)
        current_level = next_level
        if not current_level:
            break  # No more new nodes to visit
    return visited

# Parameters
N = 1000000    # Number of nodes
k = 200      # Neighbors per node
L = 3       # Number of GCN layers (i.e., BFS depth)

# Generate graph and run BFS
G = generate_k_regular_graph(N, k)
start_node = random.choice(list(G.nodes()))
rf_nodes = bfs_receptive_field(G, start_node, L)

print(f"Receptive field size after {L} layers: {len(rf_nodes)} nodes")