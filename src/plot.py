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
    total_degrees = drop_outliers(total_degrees)
    maxin = max(in_degrees)
    maxout = max(out_degrees)
    maxtot = max(total_degrees)

    pl.figure()
    pl.subplot(3, 1, 1)
    pl.hist(in_degrees, bins=scipy.arange(0, maxin + 2) - 0.5, normed=True,
            color='.5')
    pl.xlim(-0.5, maxin + 0.5)
    pl.ylim(0, 0.225)
    pl.xticks(range(maxin + 1))
    pl.yticks(scipy.arange(0, 0.3, 0.1))
    pl.xlabel('in-degree')

    pl.subplot(3, 1, 2)
    pl.hist(out_degrees, bins=scipy.arange(0, maxout + 2) - 0.5, normed=True,
            color='.5')
    pl.xlim(-0.5, maxout + 0.5)
    pl.xticks(range(maxout + 1))
    pl.xlabel('out-degree')
    pl.yticks(scipy.arange(0, 1.1, 0.2))
    pl.ylabel('fraction of nodes')

    pl.subplot(3, 1, 3)
    pl.hist(total_degrees, bins=scipy.arange(0, maxtot + 2) - 0.5, normed=True,
            color='.5')
    pl.xlim(-0.5, maxtot + 0.5)
    pl.xticks(range(maxtot + 1))
    pl.yticks(scipy.arange(0, 0.3, 0.1))
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
    ccs_sizes = drop_outliers(ccs_sizes)
    max_size = max(ccs_sizes)
    counter = collections.Counter(ccs_sizes)
    pl.figure()
    pl.hist(ccs_sizes, normed=True,
            color='.5', bins=sorted(counter.keys())[:15])
    pl.xlabel('number of nodes')
    #pl.show()
    pl.savefig(os.path.join(os.path.dirname(__file__),
        '../output/strongly_cc_dist.png'), bbox_inches='tight')


def plot_connected_comp_dist(ccs_sizes):
    print ccs_sizes
    return
    ccs_sizes = drop_outliers(ccs_sizes)
    max_size = max(ccs_sizes)
    counter = collections.Counter(ccs_sizes)
    pl.figure()
    pl.hist(ccs_sizes, normed=True,
            color='.5', bins=sorted(counter.keys()))
    pl.xlabel('number of nodes')
    #pl.show()
    pl.savefig(os.path.join(os.path.dirname(__file__),
        '../output/conn_comp_distribution.png'), bbox_inches='tight')


def plot_neigh_overlap_dist(neigh_overlaps):
    pl.figure()
    max_over = max(neigh_overlaps)
    print scipy.arange(0, max_over, .1)
    pl.hist(neigh_overlaps, bins=scipy.arange(0, max(neigh_overlaps)-.2, .1), normed=True,
            color='.5')
    pl.xticks(scipy.arange(0, max_over, .1))
    #pl.show()
    pl.savefig(os.path.join(os.path.dirname(__file__),
        '../output/neigh_overlap_distribution.png'), bbox_inches='tight')
    pl.figure()
    pl.hist(neigh_overlaps, bins=scipy.arange(0, max_over-.1, .1), normed=True,
            color='.5', cumulative=True)
    pl.xticks(scipy.arange(0, max_over-.1, .1))
    #pl.show()
    pl.savefig(os.path.join(os.path.dirname(__file__),
        '../output/neigh_overlap_acc_distribution.png'), bbox_inches='tight')


def plot_graph(graph, limit=100):
    pl.figure()
    scc = max(nx.strongly_connected_component_subgraphs())
    nx.draw(scc)
    pl.savefig(os.path.join(os.path.dirname(__file__),
        '../output/subgraph.png'), bbox_inches='tight')


def main():
    """"Main function of the module."""
    graph = \
        nx.read_gpickle('/Users/bela/UFMG/redesComplexas/cn-tp1/data/amazon0302.gpickle')
    print '----- Finished reading graph -----'
    #total_degrees, in_degrees, out_degrees = metrics.get_nodes_degrees(graph)
    #plot_degree_dist(in_degrees, out_degrees, total_degrees)
    #clus_coeffs = metrics.get_all_nodes_cluster_coeffs(graph)
    #print scipy.mean(clus_coeffs)
    #plot_clust_coeff_dist(clus_coeffs)
    #if nx.is_directed(graph):
    #    strong_ccs_sizes = metrics.get_strongly_ccs_sizes(graph)
    #    plot_strongly_ccs_dist(strong_ccs_sizes)
    #    unidrected_graph = graph.to_undirected()
    #    conn_comp_sizes = metrics.get_connected_comp_sizes(unidrected_graph)
    #else:
    #    conn_comp_sizes = metrics.get_connected_comp_sizes(graph)
    #if len(conn_com_sizes) > 1:
    #    plot_connected_comp_dist(conn_comp_sizes)
    #else:
    #    print 'There is only one connected component in the undirected graph.'
    #neigh_overlaps = metrics.get_neighborhood_overlap(graph).values()
    #plot_neigh_overlap_dist(neigh_overlaps)
    
   # plot_distance_dist()
   # plot_edges_betweeness()
   # plot_nodes_betweeness()
   # find_bridges()
    #plot_graph(graph)


if __name__ == '__main__':
     main()
