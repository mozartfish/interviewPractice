"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
# DFS Solution
class Solution:
    def __init__(self):
        # dicitonary for storing nodes and their clones
        self.visited = {}
        
    def cloneGraph(self, node: 'Node') -> 'Node':
        # check if the node is null
        if node is None:
            return node
        # check if the node is already in visited
        if node in self.visited:
            return self.visited[node]
            
        # clone the node and add it to visited
        clone_node = Node(node.val, [])
        self.visited[node] = clone_node
            
        # check if there are neighbors
        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]
            
        return clone_node


# BFS Solution
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # check if the node is null
        if node is None:
            return node
        
        # set up the stuff for bfs
        visited = {}
        queue = deque([node])
        visited[node] = Node(node.val, [])
        
        # do the bfs stuff
        while queue:
            n = queue.popleft()
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
                visited[n].neighbors.append(visited[neighbor])
        
        return visited[node]
        
        
        