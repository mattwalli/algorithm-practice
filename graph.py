class Bag:
    class Node:
        def __init__(self, value, next):
            self.value = value
            self.next = next
    
    def __init__(self):
        self.head = None
    
    def add(self, value):
        self.head = self.Node(value, self.head)
    
    def __iter__(self):
        point = self.head
        while point != None:
            yield point.value
            point = point.next

class Graph:
    def __init__(self, vertices = 0, file_name = None):
        if file_name == None:
            self.V = vertices
            self.E = 0
            self.adj_list = [Bag() for _ in range(self.V)]
        else:
            f = open(file_name)
            self.V = int(f.readline())
            self.E = int(f.readline())
            self.adj_list = [Bag() for _ in range(self.V)]
            for _ in range(self.E):
                edge = f.readline().split()
                self.add_edge(int(edge[0]), int(edge[1]))
            f.close()

    def __str__(self):
        s = f"{self.V} vertices, {self.E} edges\n"
        for v in range(self.V):
            s += f"{v}: "
            for w in self.adj(v):
                s += f"{w} "
            s += "\n"
        return s

    def add_edge(self, v, w):
        self.adj_list[v].add(w)
        self.adj_list[w].add(v)
        self.E += 1

    def adj(self, v):
        return self.adj_list[v]

class DepthFirstSearch:
    def __init__(self, graph, start):
        def dfs(v):
            self.marks[v] = True
            self.cnt += 1
            for w in graph.adj(v):
                if not self.marks[w]:
                    dfs(w)
        
        self.marks = [False for _ in range(graph.V)]
        self.cnt = 0
        dfs(start)
        
    def marked(self, v):
        return self.marks[v]
    
    def count(self):
        return self.cnt

import sys
G = Graph(file_name = sys.argv[1])
s = int(sys.argv[2])
search = DepthFirstSearch(G, s)
for v in range(G.V):
    if search.marked(v):
        print(v)
print(f"count: {search.count()}")