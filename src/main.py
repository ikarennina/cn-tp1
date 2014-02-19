"""A module to perform metric calculations in a graph."""

from itertools import combinations
from itertools import permutations

import networkx as nx

def get_local_cluster_coeff(graph, node_id):
    """Calculate local cluster coefficient.
    
    Args:
        graph: a networkx graph object
        node_id: the id of a node in the graph

    Returns:
        cluster_coeff: The cluster coefficient of the node, calculated as the
            probability of two random neighbors of the node being connected.
    """
    neighbors = graph.neighbors(node_id)
    #disconsider self loops
    if node_id in neighbors:
        neighbors.remove(node_id)
    count = 0
    candidates = permutations(neighbors, 2) if graph.is_directed() else \
        combinations(neighbors, 2)
    for edge in candidates:
        if graph.has_edge(x, y)
            count += 1
    cc = count/(len(neighbors) * (len(neighbors) - 1))
    return cc if graph.is_directed() else 2 * cc


def get_degree_dist(graph):
    """Plot degree distribution of graph.

    Args:
        graph: a networkx graph object

    Returns:
        degree_dist: A dictionary with degree as keys and count(degree) as
            value, if graph is undirected.
        degree_dist, in_degree_dist, out_degree_dist: A tuple of dicts containing
            the cummulative degree distribution, the in-degree distribution and the
            out-degree distribution, if graph is directed.
    """
    degrees_list = graph.degree().values()
    degree_dist = {v: degrees_list.count(v) for v in degrees_list}
    if not graph.is_directed():
        return degree_dist
    in_degrees_list = graph.in_degree().values()
    in_degree_dist = {v: in_degrees_list.count(v) for v in in_degrees_list}
    out_degrees_list = graph.out_degree().values()
    out_degree_dist = {v: out_degrees_list.count(v) for v in out_degrees_list}
    return degree_dist, in_degree_dist, out_degree_dist


def main():
    """"Main function of the module."""
   # read_input()
   # plot_degree_dist(graph)
   # plot_clust_coeff()
   # plot_connected_comp_dist()
   # plot_neigh_overlap_dist()
   # plot_distance_dist()
   # plot_edges_betweeness()
   # plot_nodes_betweeness()
   # find_bridges()
   # plot_graph()




if __name__ == '__main__':
    # main()
