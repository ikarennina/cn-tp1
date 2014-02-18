"""A module to perform metric calculations in a graph."""

import networkx as nx

def get_degree_dist(graph, undirected=True):
    """Plot degree distribution of graph.

    Args:
        graph: a networkx graph object
        undirected: boolean indicating if graph is undirected or not (True by
            default)

    Returns:
        degree_dist: A dictionary with degree as keys and count(degree) as
            value, if graph is undirected.
        degree_dist, in_degree_dist, out_degree_dist: A tuple containing the
            cummulative degree distribution, the in-degree distribution and the
            out-degree distribution, if graph is directed.
    """
    degrees_list = graph.degree().values()
    degree_dist = {v: degrees_list.count(v) for v in degrees_list}
    if undirected:
        return degree_dist
    in_degrees_list = graph.in_degree().values()
    in_degree_dist = {v: in_degrees_list.count(v) for v in in_degrees_list}
    out_degree_dist = graph.out_degree()
    return degree_dist, in_degree_dist, out_degree_dist


def main():
    """"Main function of the module."""
    #read_input()
    graph = nx.fast_gnp_random_graph(5, .3)
    print graph.nodes()
    get_degree_dist(graph)
   # return
   # plot_clust_coeff()
   # plot_connected_comp_dist()
   # plot_neigh_overlap_dist()
   # plot_distance_dist()
   # plot_edges_betweeness()
   # plot_nodes_betweeness()
   # find_bridges()
   # plot_graph()




if __name__ == '__main__':
    main()
