# -*- coding: utf-8 -*-
# https://www.hackerrank.com/challenges/kruskalmstrsub
__author__ = 'goran'


class Edge:
    def __init__(self, v1, v2, weight):
        self.v1 = v1
        self.v2 = v2
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight


class UnionFind:
    def __init__(self, n: int):
        self.parent = [0] * n
        self.rank = [0] * n

        for i in range(n):
            self.make_set(i)

    def make_set(self, i: int):
        self.parent[i] = i
        self.rank[i] = 0

    def union(self, x: int, y: int):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return

        # x and y are not already in the same set -> Merge them
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1

    def find(self, x: int):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]


class Graph:
    INF = 100000000000

    def __init__(self, N, directed=False):
        self.N = N
        self.directed = directed
        self.adj = {}
        for i in range(0, N):
            self.adj[i] = dict()

    def add_edge(self, from_, to, weight):
        self.adj[from_][to] = weight
        if not self.directed:
            self.adj[to][from_] = weight

    def prim(self, start):
        min_span_tree = Graph(self.N, directed=self.directed)

        included_nodes = set([start])

        while len(included_nodes) < self.N:
            best_node = 0
            best_weight = Graph.INF
            from_node = 0
            for node in included_nodes:
                for next_node, weight in self.adj[node].items():
                    if next_node not in included_nodes and weight < best_weight:
                        from_node = node
                        best_node = next_node
                        best_weight = weight
                        break
            included_nodes.add(best_node)
            min_span_tree.add_edge(from_node, best_node, best_weight)

        return min_span_tree

    @property
    def get_all_edges(self):
        result = []
        for node, neighbors in self.adj.items():
            for neighbor, weight in neighbors.items():
                result.append(Edge(node, neighbor, weight))
        return result

    def kruskal(self):
        all_edges = sorted(self.get_all_edges)

        uf = UnionFind(self.N)

        kruskal_edges = []

        for edge in all_edges:
            if uf.find(edge.v1) != uf.find(edge.v2):
                kruskal_edges.append(edge)
                uf.union(edge.v1, edge.v2)

            if len(kruskal_edges) == self.N - 1:
                break

        return kruskal_edges


(N, M) = tuple([int(i) for i in input().split()])
g = Graph(N)
for i in range(M):
    x, y, r = tuple([int(i) for i in input().split()])
    g.add_edge(x - 1, y - 1, r)
kruskal_edges = g.kruskal()
print(sum([edge.weight for edge in kruskal_edges]))