# -*- coding: utf-8 -*-
from blist import sorteddict

__author__ = 'goran'


class Graph:
    INF = 100000000000

    def __init__(self, N, directed=False):
        self.N = N
        self.directed = directed
        self.adj = {}
        for i in range(1, N + 1):
            self.adj[i] = sorteddict()

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



