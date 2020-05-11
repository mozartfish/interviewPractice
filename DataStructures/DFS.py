# Implementation of DFS using python

Graph = {'A':['B', 'C'], 'B':['D', 'E'], 'C':['F'], 'D':[], 'E':['F'], 'F':[]}
visited = set()
def DFS(visited, Graph, node):
    if node not in visited:
        print(node, end="")
        visited.add(node)
        for neighbor in Graph[node]:
            DFS(visited, Graph, neighbor)

DFS(visited, Graph, 'A')
