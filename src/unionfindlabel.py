from pysnit import snippet
from .unionfind import UnionFind

# @snippet(prefix="uf",
#          description="Union Find Tree with label.")
class UnionFindLabel(UnionFind):
    def __init__(self, labels):
        assert len(labels) == len(set(labels))
        self.n = len(labels)
        self.parents = [-1] * self.n
        self.d = {x: i for i, x in enumerate(labels)}
        self.d_inv = {i: x for i, x in enumerate(labels)}
    def find_label(self, x):
        return self.d_inv[super().find(self.d[x])]
    def union(self, x, y):
        super().union(self.d[x], self.d[y])
    def size(self, x):
        return super().size(self.d[x])
    def same(self, x, y):
        return super().same(self.d[x], self.d[y])
    def members(self, x):
        root = self.find(self.d[x])
        return [self.d_inv[i] for i in range(self.n) if self.find(i) == root]
    def roots(self):
        return [self.d_inv[i] for i, x in enumerate(self.parents) if x < 0]
