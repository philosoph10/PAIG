import networkx as nx
from tqdm import tqdm
from annihilators.paig import is_PAIG
from graph_selection.save_graphs import write_graph


def get_all_graphs_up_to_7_vertices():
    """
    get all graphs with <=7 vertices. note that they might be disconnected
    :return: a list of non-isomorphic graphs with at most 7 vertices
    """
    return nx.graph_atlas_g()


def get_all_graphs_with_7_vertices():
    """
    get all non-isomorphic connected graphs with 7 vertices
    :return: list of all graphs on 7 vertices
    """
    G_with_7_vs = []
    for G in get_all_graphs_up_to_7_vertices():
        if G.number_of_nodes() == 7 and nx.is_connected(G):
            G_with_7_vs.append(G)
    return G_with_7_vs


def get_all_graphs_with_8_vertices(G_with_7_vs):
    """
    generates all graphs on 8 vertices
    Note: it is not guaranteed that they will be distinct
    :param G_with_7_vs: list of all graphs on 7 vertices
    :return: list of all graphs on 8 vertices
    """
    G_with_8_vs = []
    for G in G_with_7_vs:
        G.add_node(7)
        for t in range(1, 128):
            G1 = G.copy()
            for i in range(8):
                if (t >> i) & 1 == 1:
                    G1.add_edge(i, 7)
            # if nx.is_connected(G1):
            G_with_8_vs.append(G1)
    return G_with_8_vs


def find_non_bipartite_paig_in_file(file):
    """
    find if a file contains a non-bipartite PAIG
    :param file: the file which contains the graphs
    :return: True, if non-bipartite PAIG is found, False otherwise
    """
    with open(file, 'r') as infile:
        lines = infile.readlines()
    i = 0
    with tqdm(total=len(lines)) as pbar:
        while i < len(lines):
            tokens = lines[i].strip().split()
            if len(tokens) == 0 or 'Graph' in lines[i]:
                i += 1
                pbar.update(1)
                continue
            n_v = int(tokens[0])
            n_e = int(tokens[1])
            G = nx.Graph()
            G.add_nodes_from(range(n_v))
            edges = lines[i + 1].strip().split()
            k = 0
            while len(edges) < 2*n_e:
                k += 1
                edges.extend(lines[i + k + 1].strip().split())
            for j in range(n_e):
                G.add_edge(int(edges[2*j]), int(edges[2*j + 1]))
            if not nx.is_bipartite(G) and is_PAIG(G):
                write_graph(G)
                return True
            i += 2 + k
            pbar.update(2 + k)
    return False
