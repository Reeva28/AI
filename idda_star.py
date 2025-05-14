def input_tree_with_heuristics():
    tree = {}
    heuristics = {}
    
    n = int(input("Enter number of nodes: "))
    
    for _ in range(n):
        node = input("Node: ")
        children_input = input(f"Children of {node} (format: child:cost, comma-separated): ")
        tree[node] = []
        if children_input:
            for pair in children_input.split(','):
                child, cost = pair.strip().split(':')
                tree[node].append((child.strip(), int(cost)))
        heuristics[node] = int(input(f"Heuristic for node {node}: "))
    
    return tree, heuristics

def ida_star(start, goal, tree, heuristics):
    threshold = heuristics[start]
    path = [start]

    while True:
        print(f"\nCurrent Threshold: {threshold}")
        temp = search(path, 0, threshold, goal, tree, heuristics)
        print("Path in this iteration:", " -> ".join(path))
        if temp == "FOUND":
            return path
        if temp == float('inf'):
            return None
        threshold = temp

def search(path, g, threshold, goal, tree, heuristics):
    current = path[-1]
    f = g + heuristics[current]

    if f > threshold:
        return f
    if current == goal:
        return "FOUND"

    min_threshold = float('inf')
    for neighbor, cost in tree.get(current, []):
        if neighbor not in path:
            path.append(neighbor)
            temp = search(path, g + cost, threshold, goal, tree, heuristics)
            if temp == "FOUND":
                return "FOUND"
            if temp < min_threshold:
                min_threshold = temp
            path.pop()
    return min_threshold

if __name__ == "__main__":
    tree, heuristics = input_tree_with_heuristics()
    start = input("\nEnter start node: ")
    goal = input("Enter goal node: ")

    result_path = ida_star(start, goal, tree, heuristics)

    if result_path:
        print("\nFinal path found:", " -> ".join(result_path))
    else:
        print("No path found.")