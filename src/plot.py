import matplotlib.pyplot as pl
import os
import scipy

import networkx as nx

import metrics
import numpy as np


def drop_outliers(data):
    mean = np.mean(data)
    std_dev = np.std(data)
    filtered_list = [item for item in data if abs(item - mean) <= std_dev]
    return filtered_list

def plot_degree_dist(in_degrees, out_degrees, total_degrees):

    maxin = max(in_degrees)
    maxout = max(out_degrees)
    maxtot = max(total_degrees)

    pl.figure()
    pl.subplot(3, 1, 1)
    pl.hist(in_degrees, bins=scipy.arange(0, maxin + 2) - 0.5, normed=True)
    pl.xlim(-0.5, maxin+0.5)
    pl.ylim(0, 0.225)
    pl.xticks(range(maxin + 1))
    pl.yticks(scipy.arange(0, 0.3, 0.1))
    pl.xlabel('in-degree')

    pl.subplot(3, 1, 2)
    pl.hist(out_degrees, bins=scipy.arange(0, maxout + 2) - 0.5, normed=True)
    pl.xlim(-0.5, maxout + 0.5)
    pl.xticks(range(maxout + 1))
    pl.xlabel('out-degree')
    pl.yticks(scipy.arange(0, 1.1, 0.2))
    pl.ylabel('fraction of nodes')

    pl.subplot(3, 1, 3)
    pl.hist(total_degrees, bins=scipy.arange(0, maxtot + 2) - 0.5, normed=True)
    pl.xlim(-0.5, maxtot + 0.5)
    pl.xticks(range(maxtot + 1))
    pl.yticks(scipy.arange(0, 0.3, 0.1))
    pl.xlabel('total degree')

    pl.subplots_adjust(hspace=0.7, right=0.7)
    #pl.show()
    pl.savefig(os.path.join(os.path.dirname(__file__),
        '../output/degree_distribution.png'), bbox_inches='tight')

def plot_marginal_degree_dist(in_degrees, out_degrees, total_degrees):

    nnodes = len(in_degrees)
    maxin = max(in_degrees)
    maxout = max(out_degrees)
    maxtot = max(total_degrees)
    pdeg = scipy.zeros([maxin + 1, maxout + 1])

    for i in range(nnodes):
        din = in_degrees[i]
        dout = out_degrees[i]
        pdeg[dout][din] += 1
    pdeg = pdeg / nnodes
    
    pl.figure()
    pl.pcolor(scipy.arange(maxin + 2) - 0.5, scipy.arange(maxout + 2) - 0.5, pdeg)
    pl.xticks(range(maxin + 1))
    pl.yticks(range(maxout + 1))
    pl.xlabel('in-degree')
    pl.ylabel('out-degree')
    pl.cb = pl.colorbar()
    pl.cb.set_label('fraction of nodes')
    pl.show()
    pl.savefig('marginal_degree_distribution.png', transparent=True,
            dpi=60)


def read_input():
    pass


def main():
    """"Main function of the module."""
   # read_input()
    graph = \
        nx.read_gpickle('/Users/bela/UFMG/redesComplexas/cn-tp1/data/amazon0302.gpickle')
    total_degrees, in_degrees, out_degrees = metrics.get_nodes_degrees(graph)
    in_degrees = drop_outliers(in_degrees)
    out_degrees = drop_outliers(out_degrees)
    total_degrees = drop_outliers(total_degrees)
    plot_degree_dist(in_degrees, out_degrees, total_degrees)
    #plot_marginal_degree_dist(in_degrees, out_degrees, total_degrees)

 #  plot_degree_dist([0, 2, 0, 1, 2, 3, 3, 0, 2, 0],
  #          [2, 1, 1, 0, 0, 2, 3, 2, 1, 1],
  #          [2, 3, 1, 1, 2, 5, 6, 2, 3, 1])
  #  plot_marginal_degree_dist([0, 2, 0, 1, 2, 3, 3, 0, 2, 0],
  #          [2, 1, 1, 0, 0, 2, 3, 2, 1, 1],
  #          [2, 3, 1, 1, 2, 5, 6, 2, 3, 1])
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
