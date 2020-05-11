from collections import deque
# adjacency list representation of a graph
G = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}

def BFS(graph, root):
    visited, q = set(), deque([root])
    visited.add(root)

    # while the queue is not empty
    while q:
        vertex = q.popleft()
        print(str(vertex) + " ", end="")

        # if not visited mark it as visited and enqueue it
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)


BFS(G, 0)





