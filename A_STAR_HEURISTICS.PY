import heapq

def input_weighted_tree():
    tree = {}
    n = int(input("Enter number of nodes in the tree: "))
    print("For each node, enter children in format: child:cost (comma-separated), or leave blank if none.")
    for _ in range(n):
        node = input("Node: ")
        children_input = input(f"Children of {node}: ")
        children = []
        if children_input:
            for child_pair in children_input.split(','):
                child, cost = child_pair.strip().split(':')
                children.append((child.strip(), int(cost)))
        tree[node] = children
    return tree

def input_heuristics(tree):
    heuristics = {}
    all_nodes = set(tree.keys())
    for children in tree.values():
        for child, _ in children:
            all_nodes.add(child)

    print("\nEnter heuristic value for each node (estimated cost to goal):")
    for node in all_nodes:
        heuristics[node] = int(input(f"Heuristic for node '{node}': "))
    return heuristics

def a_star(tree, heuristics, start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start))

    g_scores = {node: float('inf') for node in heuristics}
    g_scores[start] = 0

    f_scores = {node: float('inf') for node in heuristics}
    f_scores[start] = heuristics[start]

    came_from = {}

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for neighbor, cost in tree.get(current, []):
            tentative_g_score = g_scores[current] + cost

            if tentative_g_score < g_scores[neighbor]:
                came_from[neighbor] = current
                g_scores[neighbor] = tentative_g_score
                f_scores[neighbor] = tentative_g_score + heuristics[neighbor]
                heapq.heappush(open_list, (f_scores[neighbor], neighbor))

    return None

# Run the code
if __name__ == "__main__":
    tree = input_weighted_tree()
    heuristics = input_heuristics(tree)
    start = input("\nEnter start node: ")
    goal = input("Enter goal node: ")

    path = a_star(tree, heuristics, start, goal)
    if path:
        print("\nA* Path:", " -> ".join(path))
    else:
        print("No path found.")
