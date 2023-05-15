import networkx as nx


def write_graph(G, filename='graphs'):
    """
    write a graph to a file in format:
    n_vertices
    u_1 v_1 u_2 v_2 ... u_n_edges v_n_edges
    :param G: the graph
    :param n_vertices: number of vertices
    :param filename: the name of the output file
    """
    n_vertices = G.number_of_nodes()
    with open(filename + '.txt', 'a') as outfile:
        outfile.write(str(n_vertices) + ' ')
        for u, v in G.edges():
            outfile.write(str(u) + ' ' + str(v) + ' ')
        outfile.write('\n')


def read_graphs(filename='graphs'):
    """
    read graph from file
    :param filename: file to read from
    :param n: number of vertices
    :return: a list og graphs
    """
    graphs = []
    with open(filename + '.txt', 'r') as infile:
        lines = infile.readlines()
        for line in lines:
            G = nx.Graph()
            numbers = line.split(' ')
            n = int(numbers[0])
            G.add_nodes_from(range(n))
            edges = []
            edges_str = numbers[1:]
            for i in range(1, len(edges_str), 2):
                edges.append((int(edges_str[i-1].strip()), int(edges_str[i].strip())))
            G.add_edges_from(edges)
            graphs.append(G)
    return graphs
