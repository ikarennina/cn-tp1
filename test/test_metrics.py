"""A module to test the calculation of metrics in a graph."""

import unittest

import networkx as nx

import main as metrics


class TestMetricsCalculations(unittest.TestCase):
    """Test the fet_degree_dist function."""

    def setUp(self):
        """Create sample directed and undirected graphs to be used tests."""
        self.graph = nx.Graph([(0, 1), (0, 2), (0, 4), (1, 2), (1, 3), (2, 3),
            (3, 4)])
        self.digraph = nx.DiGraph([(0, 0), (0, 1), (1, 2), (2, 3), (3, 2), (3,
            4), (4, 0), (4, 2)])

    def test_shortest_paths_directed(self):
        """Test all-pairs shortest paths sizes for a directed graph."""
        result = metrics.all_shortest_paths(self.digraph)
        expected = [
            [0, 1, 2, 3, 4],
            [4, 0, 1, 2, 3],
            [3, 4, 0, 1, 2],
            [2, 3, 1, 0, 1],
            [1, 2, 1, 2, 0]]
        self.assertEqual(expected, result)

    def test_shortest_paths_undirected(self):
        """Test all-pairs shortest paths sizes for an undirected graph."""
        result = metrics.all_shortest_paths(self.graph)
        expected = [
            [0, 1, 1, 2, 1],
            [1, 0, 1, 1, 2],
            [1, 1, 0, 1, 2],
            [2, 1, 1, 0, 1],
            [1, 2, 2, 1, 0]]
        self.assertEqual(expected, result)

    def test_edge_span_directed(self):
        """Test calculation of edge span with directed graph."""
        expected_results = {(0, 1): float('Inf'), (1, 2): float('Inf'), (2, 3):
                float('Inf'), (3, 2): 2, (3, 4): float('Inf'), (4, 0):
                float('Inf'), (4, 2): 3}
        for edge in self.digraph.edges():
            src, dst = edge
            #disconsider self loops
            if src == dst:
                continue
            result = metrics.get_edge_span(self.digraph, edge)
            self.assertEqual(expected_results[edge], result, msg='Failed on'+
                    ' edge %s.\n Expected %s and got %s.' %
                    (str(edge), str(expected_results[edge]), str(result)))

    def test_edge_span_undirected(self):
        """Test calculation of edge span with undirected graph."""
        expected_results = {(0, 1): 2, (0, 2): 2, (0, 4): 3, (1, 2): 2, (1, 3):
                2, (2, 3): 2, (3, 4): 3}
        for edge in self.graph.edges():
            src, dst = edge
            #disconsider self loops
            if src == dst:
                continue
            result = metrics.get_edge_span(self.graph, edge)
            self.assertEqual(expected_results[edge], result, msg='Failed on'+
                    ' edge %s.\n Expected %s and got %s.' %
                    (str(edge), str(expected_results[edge]), str(result)))

    def test_degree_dist_directed(self):
        """Test degree distribution calculation with directed graph."""
        result = metrics.get_degree_dist(self.digraph)
        degree_dist = {2: 1, 3: 2, 4: 2}
        in_degree_dist = {1: 3, 2: 1, 3: 1}
        out_degree_dist = {1: 2, 2: 3}
        self.assertEqual((degree_dist, in_degree_dist, out_degree_dist),
                result)

    def test_degree_dist_undirected(self):
        """Test degree distribution calculation with undirected graph."""
        result = metrics.get_degree_dist(self.graph)
        degree_dist = {2: 1, 3: 4}
        self.assertEqual(degree_dist, result)

    def test_cluster_coeff_undirected(self):
        """Test calculation of local cluster coeff. with undirected graph."""
        expected_results = {0: 1.0/6, 1: 2.0/6, 2: 2.0/6, 3: 1.0/6, 4: 0}
        for node in self.graph:
            result_cc = metrics.get_local_cluster_coeff(self.graph, node)
            self.assertEqual(expected_results[node], result_cc, msg='Failed ' +
                'on node %d.\nExpected %f and got %f' % (node,
                    expected_results[node], result_cc))

    def test_cluster_coeff_directed(self):
        """Test calculation of local cluster coeff. with directed graph."""
        expected_results = {0: None, 1: None, 2: None, 3: 0.5, 4: 0}
        for node in self.digraph:
            result_cc = metrics.get_local_cluster_coeff(self.digraph, node)
            self.assertEqual(expected_results[node], result_cc, msg='Failed ' +
                'on node %d.\nExpected %s and got %s' % (node,
                    str(expected_results[node]), str(result_cc)))


if __name__ == '__main__':
    unittest.main()
