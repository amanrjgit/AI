from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSutil(self,s,visited):
        visited[s]=True
        print(s,end=" ")

        for i in self.graph[s]:
            if not visited[i]:
                self.DFSutil(i, visited)

    def DFS(self,s):

        visited= [False]*(len(self.graph)+1)

        self.DFSutil(s,visited)

g=Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

g.DFS(2)
