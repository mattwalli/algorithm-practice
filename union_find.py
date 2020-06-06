class UF:
    def __init__(self, n):
        self.cnt = n
        self.id = list()
        for i in range(n):
            self.id.append(i)

    def union(self, p, q):
        p_id = self.find(p)
        q_id = self.find(q)
        if p_id == q_id:
            return
        self.id[p_id] = q_id
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
f = open("mediumUF.txt")
#f = open("largeUF.txt")
uf = UF(int(f.readline()))
while True:
    ln = f.readline()
    if ln == '':
        break
    conn = ln.split()
    p = int(conn[0])
    q = int(conn[1])
    if uf.connected(p, q):
        continue
    uf.union(p, q)
    #print(f"{p} {q}")
print(f"{uf.count()} components")

f.close()