# -*- coding: utf-8 -*-
from unittest import TestCase
from union_find.union_find import UnionFind

__author__ = 'goran'


class TestUnionFind(TestCase):
    def test_uf(self):
        n = 5
        uf = UnionFind(n)

        for i in range(n):
            self.assertEqual(uf.parent[i], i)
            self.assertEqual(uf.rank[i], 0)

        uf.union(0, 3)
        self.assertEqual(uf.rank[0], 1)
        self.assertEqual(uf.rank[3], 0)
        self.assertEqual(uf.find(0), 0)
        self.assertEqual(uf.find(3), 0)

        uf.union(1, 0)
        self.assertEqual(uf.rank[0], 1)
        self.assertEqual(uf.rank[1], 0)
        self.assertEqual(uf.find(0), 0)
        self.assertEqual(uf.find(1), 0)

        uf.union(2, 4)
        self.assertEqual(uf.rank[2], 1)
        self.assertEqual(uf.rank[4], 0)
        self.assertEqual(uf.find(2), 2)
        self.assertEqual(uf.find(4), 2)

        uf.union(1, 2)
        self.assertEqual(uf.rank[1], 0)
        self.assertEqual(uf.rank[0], 2)
        self.assertEqual(uf.rank[2], 1)
        self.assertEqual(uf.find(1), 0)
        self.assertEqual(uf.find(2), 0)
        self.assertEqual(uf.find(4), 0)