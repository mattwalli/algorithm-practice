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
            self.vert = vertices
            self.edge = 0
        else:
            f = open(file_name)
            self.vert = int(f.readline())
            self.edge = int(f.readline())
            while True:
                ln = f.readline()
                if ln == "":
                    break
                e = ln.split()
                self.add_edge(int(e[0]), int(e[1]))
            f.close()

    def __str__(self):
        s = f"{self.V} vertices, {self.E} edges\n"
        for v in range(self.V):
            s += f"{v}: "
            for w in self.adj(v):
                s += f"{w} "
            s += "\n"
        return s
    
    def V(self):
        return self.vert
    
    def E(self):
        return self.edge

    def add_edge(self, v, w):
        pass

    def adj(self, v):
        pass

import sys
G = Graph(file_name = sys.argv[1])
print(G.V())