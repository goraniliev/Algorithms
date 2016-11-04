# -*- coding: utf-8 -*-
'''
https://www.hackerrank.com/contests/data-structure-tasks-binary-tree-union-find/challenges/connected-component
'''

import sys
__author__ = 'goran'

class UnionFind:
    def __init__(self, n: int):
        self.parent = [0] * n
        self.rank = [0] * n
        # self.elements = [0] * n

        for i in range(n):
            self.make_set(i)

    def make_set(self, i: int):
        self.parent[i] = i
        self.rank[i] = 0
        # self.elements[i] = 1

    def union(self, x: int, y: int):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return

        # x and y are not already in the same set -> Merge them
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
            # self.elements[y_root] += self.elements[x_root]
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
            # self.elements[x_root] += self.elements[y_root]
        else:
            self.parent[y_root] = x_root
            # self.elements[x_root] += self.elements[y_root]
            self.rank[x_root] += 1

    def find(self, x: int):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

n = int(sys.stdin.readline())

uf = UnionFind(n)

components = n

for line in sys.stdin:
    (u, v) = tuple([int(i) - 1 for i in line.split()])
    if uf.find(u) == uf.find(v):
        cycle = ' CYCLE FORMED!'
    else:
        cycle = ''
        components -= 1
    print('{}{}'.format(components, cycle))
    uf.union(u, v)
