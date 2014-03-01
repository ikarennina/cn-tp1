"""A module to perform metric calculations in a graph."""

from collections import deque
from itertools import combinations
from itertools import permutations
import matplotlib.pyplot as pl
import scipy

import networkx as nx


def get_bridges(graph, threshold=2):
    for edge in graph.edges():
        if get_edge_span(graph, edge) > threshold:
            yield edge


def get_neighborhood_overlap(graph):
    """Get the neighboorhood overlap for each edge.

    The neighboordhood overlap for the edge A and B can be defined as the ratio
    between the number of nodes which are neighbors of both A and B and the
    number of nodes which are neighbors of at least one of A and B.

    Args:
        graph: a networkx graph object

    Returns:
        overlaps: a dict indexed by an edge (a, b) of the graph (a < b)
            containing the neighboorhood overlap for that edge. Self-loops are
            disconsidered.
    """
    edges = graph.edges()
    overlaps = {}
    for n1, n2 in edges:
        neigh_n1 = set(graph.neighbors(n1))
        neigh_n2 = set(graph.neighbors(n2))
        intersection = neigh_n1.intersection(neigh_n2)
        union = neigh_n1.union(neigh_n2)
        neigh_overlap = float(len(intersection))/len(union)
        overlaps[(n1, n2)] = neigh_overlap
    return overlaps
    

def get_connected_components_sizes(graph):
    """Get the size of each connected compoent.

    Args:
        graph: a networkx undirected graph object

    Returns:
        sizes: a list in which each entry is the size of one of the connected
            components.
        None: if the graph passed is directed.
    """
    if graph.is_directed():
        return None
    nodes = set(graph.nodes())
    sizes = []
    while nodes:
        source = nodes.pop()
        size = 1
        queue = deque(graph.neighbors(source))
        while queue:
            visited = queue.popleft()
            nodes.remove(visited)
            queue.extend([node for node in graph.neighbors(visited) if node in
                nodes and node not in queue])
            size += 1
        sizes.append(size)
    return sizes


def get_all_nodes_shortest_paths_sizes(graph, unweighted=True):
    if unweighted == False:
        raise NotImplementedError
    paths = nx.all_pairs_shortest_path(graph)
    return [len(x.values()[0]) for x in paths.values()]

def get_edges_betweenness(graph):
    betweenness = nx.edge_betweenness_centrality(graph)
    return betweenness.values()

def get_nodes_betweenness(graph):
    betweenness = nx.betweenness_centrality(graph)
    return betweenness.values()


def get_edge_span(graph, edge):
    """Get the span of an edge.

    The span of an edge (u,v) is the size of the shortest path between u and v,
    when (u,v) is removed from the graph.

    This calculatin can be done with a breadth-first search, since we are
    dealing with non-weighted graphs.

    Args:
        graph: a networkx graph object
        edge: a tuple (u,v)

    Returns:
        span: size of shortest alternate path
        Inf: if there is no alternate path
    """
    source, target = edge
    queue = deque([source])
    distances = {source: 0}
    while queue:
        node = queue.popleft()
        if node == target:
            return distances[node]
        for neigh in graph.neighbors(node):
            #disconsider the edge being evaluated
            if node == source and neigh == target:
                continue
            if neigh not in distances:
                distances[neigh] = distances[node] + 1
                queue.append(neigh)
    return float('Inf')


def get_all_nodes_cluster_coeffs(graph):
    return [cc for cc in (get_cluster_coeff(graph, node) for node in graph) if
            cc]

def get_cluster_coeff(graph, node_id):
    """Calculate local cluster coefficient.

    Args:
        graph: a networkx graph object
        node_id: the id of a node in the graph

    Returns:
        cluster_coeff: The cluster coefficient of the node, calculated as the
            probability of two random neighbors of the node being connected.
        None: if the node has only one neighbor, the clustering coefficient is
            undefined and the function returns None.
    """
    neighbors = graph.neighbors(node_id)
    #disconsider self loops
    if node_id in neighbors:
        neighbors.remove(node_id)
    if len(neighbors) < 2:
        return None
    count = 0
    candidates = permutations(neighbors, 2) if graph.is_directed() else \
        combinations(neighbors, 2)
    for edge in candidates:
        if graph.has_edge(*edge):
            count += 1
    return float(count)/(len(neighbors) * (len(neighbors) - 1))

def get_strongly_ccs_sizes(graph):
    ccs = nx.strongly_connected_components(graph)
    return [len(cc) for cc in ccs]


def get_connected_comp_sizes(graph):
    ccs = nx.connected_components(graph)
    return [len(cc) for cc in ccs]


def get_nodes_degrees(graph):
    """Plot degree distribution of graph.

    Args:
        graph: a networkx graph object

    Returns:
        degrees: a list of the degrees of the nodes
        total_degrees, in_degrees, out_degrees: in the case of a directed network,
            three lists are returned: one with the total degree of each node, one
            with the in-degree of each node and another with the out-degree of
            each node
    """
    total_degrees = graph.degree().values()
    if not graph.is_directed():
        return total_degrees
    in_degrees = graph.in_degree().values()
    out_degrees = graph.out_degree().values()
    return total_degrees, in_degrees, out_degrees

