# create class O(N)
# find O(n)
# union O(n)
# check if connected O(n)

class QuickUnion:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, x):
        while x != self.root[x]:
            x = self.root[x]
        return x
    
    def union(self, x, y):
        _x = self.find(x)
        _y = self.find(y)
        if _x != _y:
            self.root[_y] = _x
        
    def is_connected(self, x, y):
        return self.find(x) == self.find(y)
    

uf = QuickUnion(10)
uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)
assert uf.is_connected(1, 5)
assert uf.is_connected(5, 7)
assert not uf.is_connected(4, 9)
uf.union(9,4)
assert uf.is_connected(4, 9)