start = input("Enter starting node: ").strip()
end = input("Enter destination node: ").strip()
N = int(input("Enter number of edges: "))

graph = {}

for _ in range(N):
    node1, node2, weight = input().split()
    weight = int(weight)
    for u, v in [(node1, node2), (node2, node1)]:
        if u not in graph:
            graph[u] = []
        graph[u].append((int(weight), v))


for u in graph:
    graph[u].sort(key=lambda x: (x[0], x[1]))
def dfs_min_path_visual(current, destination, visited, path, total_weight, best_result):
    print(f"Exploring node: {current}, current path: {' -> '.join(path)}, total weight: {total_weight}")
    
    if current == destination:
        print(f"Reached destination! Path found: {' -> '.join(path)}, total weight: {total_weight}\n")
        if best_result is None or total_weight < best_result[1]:
            return path, total_weight
        return best_result

    if best_result is not None and total_weight >= best_result[1]:
        print(f"Pruning path: {' -> '.join(path)} (weight {total_weight}) exceeds best weight {best_result[1]}\n")
        return best_result

    visited.add(current)

    if current in graph:
        for weight, neighbor in graph[current]:
            if neighbor not in visited:
                best_result = dfs_min_path_visual(
                    neighbor,
                    destination,
                    visited.copy(),
                    path + [neighbor],
                    total_weight + weight,
                    best_result
                )
    return best_result

print("\nStarting DFS exploration...\n")
result = dfs_min_path_visual(start, end, set(), [start], 0, None)

print("--- Exploration Completed ---")
if result:
    path, total_weight = result
    print("Shortest path found:", " -> ".join(path))
    print("Total weight:", total_weight)
else:
    print(f"No path exists from {start} to {end}")
