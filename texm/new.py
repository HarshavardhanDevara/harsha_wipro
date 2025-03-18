import sys
def prims_algorithm(n, graph):
    selected = [False] * n
    selected[0] = True  # Start from node 0
    edges = []
    total_distance = 0

    for _ in range(n - 1):  # MST will have (n-1) edges
        min_edge = (None, None, sys.maxsize)  # (u, v, weight)

        for u in range(n):
            if selected[u]:  # Pick only selected nodes
                for v in range(n):
                    if not selected[v] and graph[u][v] > 0:  # Pick smallest edge
                        if graph[u][v] < min_edge[2]:
                            min_edge = (u, v, graph[u][v])

        u, v, weight = min_edge
        selected[v] = True
        edges.append((u, v, weight))
        total_distance += weight
    return edges, total_distance
def main():
    # Read input
    n = int(input().strip())
    graph = [list(map(int, input().strip())) for _ in range(n)]

    # Compute MST
    mst_edges, total_distance = prims_algorithm(n, graph)

    # Print output
    print("Location\tDistance")
    for u, v, weight in mst_edges:
        print(f"{u} -> {v}\t\t{weight} km")
    print(f"Minimum total distance: {total_distance} km")
if __name__ == "__main__":
    main()
