import networkx as nx
from graph_selection.load_graphs import get_all_graphs_up_to_7_vertices
from graph_selection.save_graphs import write_graph
from annihilators.paig import is_PAIG
from tqdm import tqdm

graphs = get_all_graphs_up_to_7_vertices()
paig_found = False
for graph in tqdm(graphs):
    if not nx.is_bipartite(graph) and is_PAIG(graph):
        write_graph(graph, 'graphs7')
        paig_found = True
        break
print(f"Non-bipartite PAIG found -> {paig_found}")
