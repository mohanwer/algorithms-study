# constructor O(n)
# find O(@n)
# union O(@n)
# connected O(@n)

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        _x, _y = self.find(x), self.find(y)
        if _x != _y:
            if self.rank[_x] > self.rank[_y]:
                self.root[_y] = _x
            elif self.rank[_x] < self.rank[_y]:
                self.root[_x] = _y
            else:
                self.root[_y] = _x
                self.rank[_x] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)

uf = UnionFind(10)
# 1-2-5-6-7 3-8-9 4
uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)
assert uf.connected(1, 5)
assert uf.connected(5, 7)
assert not uf.connected(4, 9)
# 1-2-5-6-7 3-8-9-4
uf.union(9, 4)
assert uf.connected(4, 9)