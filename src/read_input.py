import os

import networkx as nx


INPUT_FILE = os.path.join(os.path.dirname(__file__), '../data/wiki-vote.txt')
OUTPUT_FILE = os.path.join(os.path.dirname(__file__),
    '../data/wiki-vote.gpickle')

def main():
    with open(INPUT_FILE, 'rb') as input_file :
        graph = nx.read_edgelist(INPUT_FILE, create_using=nx.DiGraph())
    nx.write_gpickle(graph, OUTPUT_FILE)

if __name__ == '__main__':
     main()
