import collections
import matplotlib.pyplot as pl
import os
import random
import scipy

import networkx as nx

import metrics
import numpy as np


def drop_outliers(data):
    mean = np.mean(data)
    std_dev = np.std(data)
    return [item for item in data if abs(item - mean) <=
        std_dev]


def plot_degree_dist(in_degrees, out_degrees, total_degrees):
    in_degrees = drop_outliers(in_degrees)
    out_degrees = drop_outliers(out_degrees)
    total_degrees = drop_outliers(total_degrees)
    maxin = max(in_degrees)
    maxout = max(out_degrees)
    maxtot = max(total_degrees)

    pl.figure()
    pl.subplot(3, 1, 1)
    pl.hist(in_degrees, bins=scipy.arange(0, maxin + 2, 1) - 0.5, normed=True,
            color='.5')
    pl.xlim(-0.5, 14)
    pl.xticks(range(0, 15, 2))
    pl.yticks(scipy.arange(0, 1, 0.2))
    pl.xlabel('in-degree')

    pl.subplot(3, 1, 2)
    pl.hist(out_degrees, bins=scipy.arange(0, maxout + 2, 1) - 0.5, normed=True,
            color='.5')
    pl.xlim(-0.5, 20)
    pl.xticks(range(0, 21, 2))
    pl.xlabel('out-degree')
    pl.yticks(scipy.arange(0, .6, 0.2))
    pl.ylabel('fraction of nodes')

    pl.subplot(3, 1, 3)
    pl.hist(total_degrees, bins=scipy.arange(0, maxtot + 2, 1) - 0.5, normed=True,
            color='.5')
    pl.xlim(-0.5, 20)
    pl.xticks(range(0, 21, 2))
    pl.yticks(scipy.arange(0, .6, 0.2))
    pl.xlabel('total degree')

    pl.subplots_adjust(hspace=0.7, right=0.7)
    #pl.show()
    pl.savefig(os.path.join(os.path.dirname(__file__),
        '../output/degree_distribution.png'), bbox_inches='tight')


def plot_clust_coeff_dist(clus_coeffs):
    pl.figure()
    pl.hist(clus_coeffs, bins=scipy.arange(0, 1.1, .1), normed=True,
            color='.5')
    pl.xticks(scipy.arange(0, 1.1, .1))
    #pl.xlabel('in-degree')
    #pl.show()
    pl.savefig(os.path.join(os.path.dirname(__file__),
        '../output/cc_distribution.png'), bbox_inches='tight')


def plot_strongly_ccs_dist(ccs_sizes):
    max_size = max(ccs_sizes)
    counter = collections.Counter(ccs_sizes)
    if len(counter.keys()) < 5:
        print 'Data distribution not suitable for plotting.'
        print counter
        return
    pl.figure()
    pl.hist(ccs_sizes, normed=True,
            color='.5')
    pl.xlabel('number of nodes')
    #pl.show()
    pl.savefig(os.path.join(os.path.dirname(__file__),
        '../output/strongly_cc_dist.png'), bbox_inches='tight')


def plot_connected_comp_dist(ccs_sizes):
    max_size = max(ccs_sizes)
    counter = collections.Counter(ccs_sizes)
    if len(counter.keys()) < 5:
        print 'Data distribution not suitable for plotting.'
        print counter
        return
    pl.figure()
    pl.hist(ccs_sizes, normed=True,
            color='.5', bins=sorted(counter.keys()))
    pl.xlabel('number of nodes')
    pl.show()
    #pl.savefig(os.path.join(os.path.dirname(__file__),
    #    '../output/conn_comp_distribution.png'), bbox_inches='tight')


def plot_neigh_overlap_dist(neigh_overlaps):
    pl.figure()
    max_over = max(neigh_overlaps)
    pl.hist(neigh_overlaps, bins=scipy.arange(0, max_over + .1, .1), normed=True,
            color='.5')
    pl.xticks(scipy.arange(0, max_over, .1))
    #pl.show()
    pl.savefig(os.path.join(os.path.dirname(__file__),
        '../output/neigh_overlap_distribution.png'), bbox_inches='tight')
    pl.figure()
    pl.hist(neigh_overlaps, bins=scipy.arange(0, max_over + .1, .1), normed=True,
            color='.5', cumulative=True)
    pl.xticks(scipy.arange(0, max_over + .1, .1))
    #pl.show()
    pl.savefig(os.path.join(os.path.dirname(__file__),
        '../output/neigh_overlap_acc_distribution.png'), bbox_inches='tight')


def plot_graph(graph):
    pl.figure()
    nx.draw_networkx(graph, with_labels=False, node_size=20, width=.2,
            style='dotted', edge_color='0.2')
    pl.savefig(os.path.join(os.path.dirname(__file__),
        '../output/subgraph.png'), bbox_inches='tight')


def plot_distances_dist(distances):
    max_size = max(distances)
    pl.figure()
    pl.hist(distances, normed=True,
            color='.5', bins=scipy.arange(0, max_size + .5))
    pl.xlabel('hops')
    #pl.show()
    pl.savefig(os.path.join(os.path.dirname(__file__),
        '../output/distances_dist.png'), bbox_inches='tight')


def plot_edges_betweenness_dist(betweenness):
    betweenness = drop_outliers(betweenness)
    pl.figure()
    pl.hist(betweenness, normed=True, color='.5')
    #pl.show()
    pl.savefig(os.path.join(os.path.dirname(__file__),
        '../output/edges_betweenness_dist.png'), bbox_inches='tight')


def plot_nodes_betweenness_dist(betweenness):
    betweenness = drop_outliers(betweenness)
    pl.figure()
    pl.hist(betweenness, normed=True, color='.5')
    #pl.show()
    pl.savefig(os.path.join(os.path.dirname(__file__),
        '../output/nodes_betweenness_dist.png'), bbox_inches='tight')


def main():
    """"Main function of the module."""
    graph = \
        nx.read_gpickle(os.path.join(os.path.dirname(__file__),
            '../data/wiki-vote.gpickle'))
    print '----- Finished reading graph -----'
    total_degrees, in_degrees, out_degrees = metrics.get_nodes_degrees(graph)
    plot_degree_dist(in_degrees, out_degrees, total_degrees)
    clus_coeffs = metrics.get_all_nodes_cluster_coeffs(graph)
    print scipy.mean(clus_coeffs)
    plot_clust_coeff_dist(clus_coeffs)
    if nx.is_directed(graph):
       #strong_ccs_sizes = metrics.get_strongly_ccs_sizes(graph)
       #plot_strongly_ccs_dist(strong_ccs_sizes)
       #undirected_graph = graph.to_undirected()
       #conn_comp_sizes = metrics.get_connected_comp_sizes(undirected_graph)
    else:
       #conn_comp_sizes = metrics.get_connected_comp_sizes(graph)
    if len(conn_comp_sizes) > 1:
       #plot_connected_comp_dist(conn_comp_sizes)
    else:
       #print 'There is only one connected component in the undirected graph.'
    neigh_overlaps = metrics.get_neighborhood_overlap(graph).values()
    plot_neigh_overlap_dist(neigh_overlaps)
    distances = metrics.get_all_nodes_shortest_paths_sizes(graph)
    print max(distances)
    plot_distances_dist(distances)
    edges_betweenness = metrics.get_edges_betweenness(graph)
    #nx.write_gpickle(edges_betweenness, os.path.join(os.path.dirname(__file__),
    #        '../data/betweenness.gpickle'))
    #edges_betweenness = nx.read_gpickle(os.path.join(os.path.dirname(__file__),
    #        '../data/betweenness.gpickle'))
    plot_edges_betweenness_dist(edges_betweenness) 
    nodes_betweenness = metrics.get_nodes_betweenness(graph)
    #nx.write_gpickle(nodes_betweenness, os.path.join(os.path.dirname(__file__),
    #        '../data/nodes_betweenness.gpickle'))
    #nodes_betweenness = nx.read_gpickle(os.path.join(os.path.dirname(__file__),
    #        '../data/nodes_betweenness.gpickle'))
    plot_nodes_betweenness_dist(nodes_betweenness)
    bridges2 = [bridge for bridge in metrics.get_bridges(graph)]
    print len(bridges2)
    nx.write_gpickle(bridges2, os.path.join(os.path.dirname(__file__),
            '../data/bridges2.gpickle'))
    plot_graph(graph)


if __name__ == '__main__':
     main()
