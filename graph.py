class Graph:

    def __init__(self, vertices = 0, file_name = None):
        if file_name == None:
            self.V = vertices
            self.E = 0
        else:
            f = open(file_name)
            self.V = int(f.readline())
            self.E = int(f.readline())
            while True:
                line = f.readline()
                if line == "":
                    break
                edge = line.split()
                self.add_edge(int(edge[0]), int(edge[1]))

    def __str__(self):
        s = f"{self.V} vertices, {self.E} edges\n"
        for v in range(self.V):
            s += f"{v}: "
            for w in self.adj(v):
                s += f"{w} "
            s += "\n"
        return s

    def add_edge(self, v, w):
        pass

    def adj(self, v):
        pass

G = Graph(file_name = "tinyG.txt")
print(G)