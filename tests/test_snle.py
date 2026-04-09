import os
import sys
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from graph import Graph
from hashmap import HashMap
from trie import Trie
from utils import DispatchQueue


class TestSNLE(unittest.TestCase):
    def test_graph_add_nodes_edges(self):
        g = Graph()
        g.add_edge('A', 'B', 3)
        self.assertEqual(g.num_nodes(), 2)
        self.assertEqual(g.num_edges(), 1)

    def test_dijkstra_path(self):
        g = Graph()
        g.add_edge('A', 'B', 1)
        g.add_edge('B', 'C', 2)
        g.add_edge('A', 'C', 10)
        path, cost = g.dijkstra('A', 'C')
        self.assertEqual(path, ['A', 'B', 'C'])
        self.assertEqual(cost, 3)

    def test_dijkstra_disconnected(self):
        g = Graph()
        g.add_node('A')
        g.add_node('B')
        path, cost = g.dijkstra('A', 'B')
        self.assertIsNone(path)
        self.assertEqual(cost, float('inf'))

    def test_cycle_detection_true(self):
        g = Graph()
        g.add_edge('A', 'B', 1)
        g.add_edge('B', 'C', 1)
        g.add_edge('C', 'A', 1)
        has_cycle, cycle = g.detect_cycle()
        self.assertTrue(has_cycle)
        self.assertTrue(len(cycle) >= 3)

    def test_cycle_detection_false(self):
        g = Graph()
        g.add_edge('A', 'B', 1)
        g.add_edge('B', 'C', 1)
        has_cycle, cycle = g.detect_cycle()
        self.assertFalse(has_cycle)
        self.assertEqual(cycle, [])

    def test_connected_components(self):
        g = Graph()
        g.add_edge('A', 'B', 1)
        g.add_edge('C', 'D', 1)
        self.assertEqual(g.connected_components(), 2)

    def test_hashmap_insert_search(self):
        hm = HashMap()
        hm.insert('DepotA', {'active': True})
        self.assertEqual(hm.search('DepotA'), {'active': True})

    def test_hashmap_delete(self):
        hm = HashMap()
        hm.insert('DepotA', 1)
        removed = hm.delete('DepotA')
        self.assertEqual(removed, 1)
        self.assertIsNone(hm.search('DepotA'))

    def test_trie_autocomplete(self):
        trie = Trie()
        trie.insert('DepotA')
        trie.insert('DepotB')
        trie.insert('ZoneNorth')
        self.assertEqual(trie.autocomplete('Dep'), ['DepotA', 'DepotB'])

    def test_dispatch_queue_order(self):
        q = DispatchQueue()
        q.enqueue(q.make_package('PKG1', 3, 'A', 1.0))
        q.enqueue(q.make_package('PKG2', 9, 'B', 2.0))
        q.enqueue(q.make_package('PKG3', 6, 'C', 3.0))
        top = q.dequeue()
        self.assertEqual(top.package_id, 'PKG2')


if __name__ == '__main__':
    unittest.main()
