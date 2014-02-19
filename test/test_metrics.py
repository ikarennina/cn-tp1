"""A module to test the calculation of metrics in a graph."""

import unittest

import networkx as nx

import main as metrics


class testDegreeDistribution(unittest.TestCase):
    """Test the fet_degree_dist function."""
    
    def test_directed(self):
        """Test with directed graph."""
        graph = nx.DiGraph([(0, 0), (0, 1), (1, 2), (2, 3), (3, 2), (3, 4), (4,
            0), (4, 2)])
        result = metrics.get_degree_dist(graph)
        degree_dist = {2: 1, 3: 2, 4: 2}
        in_degree_dist = {1: 3, 2: 1, 3: 1}
        out_degree_dist = {1: 2, 2: 3}
        self.assertEqual((degree_dist, in_degree_dist, out_degree_dist),
                result)
    
    def test_undirected(self):
        """Test with undirected graph."""
        graph = nx.Graph([(0, 1), (0, 2), (0, 4), (1, 2), (1, 3), (2, 3), (3,
            4), (4, 0)])
        result = metrics.get_degree_dist(graph)
        degree_dist = {2: 1, 3: 4}
        self.assertEqual(degree_dist, result)


if __name__ == '__main__':
    unittest.main()
