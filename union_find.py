class UF:
    def __init__(self, n):
        self.cnt = n
        self.id = list()
        self.sz = list()
        for i in range(n):
            self.id.append(i)
            self.sz.append(1)

    def union(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)
        if p_root == q_root:
            return
        if self.sz[p_root] < self.sz[q_root]:
            self.id[p_root] = q_root
            self.sz[q_root] += self.sz[p_root]
        else:
            self.id[q_root] = p_root
            self.sz[p_root] += self.sz[q_root]
        self.cnt -= 1

    def find(self, p):
        while p != self.id[p]:
            p = self.id[p]
        return p

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def count(self):
        return self.cnt

#f = open("tinyUF.txt")
#f = open("mediumUF.txt")
f = open("largeUF.txt")
uf = UF(int(f.readline()))
while True:
    ln = f.readline()
    if ln == '':
        break
    conn = ln.split()
    p = int(conn[0])
    q = int(conn[1])
    #if uf.connected(p, q):
    #    continue
    uf.union(p, q)
    #print(f"{p} {q}")
print(f"{uf.count()} components")

f.close()