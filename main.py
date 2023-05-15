"""
This is a test script.
Run it to check that everything works correctly.
"""

import networkx as nx
from graph_selection.load_graphs import get_all_graphs_up_to_7_vertices
from annihilators.paig import is_PAIG
from tqdm import tqdm

graphs = get_all_graphs_up_to_7_vertices()
paig_found = False
for graph in tqdm(graphs):
    assert not nx.is_bipartite(graph) or is_PAIG(graph), "A bipartite graph must be PAIG!"
print(f"Non-bipartite PAIG found -> {paig_found}")
print('Expected output: "Non-bipartite PAIG found -> False"')