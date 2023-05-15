import networkx as nx


# noinspection SpellCheckingInspection
class Annihilator(object):

    """
    object that defines an annihilator
    an annihilator ⌈a,b⌉ is a set of vertices x such b lies on some a-x geodesic
    """

    def __init__(self, G, a, b, distances=None):
        self.a = a
        self.b = b
        self.G = G
        dists = distances
        if distances is None:
            dists = dict(nx.all_pairs_shortest_path_length(G))
        ab = dists[a][b]
        self.nodes = set()
        self.is_prime = True
        for node in G.nodes():
            if ab + dists[b][node] == dists[a][node]:
                self.nodes.add(node)
            else:
                if ab + dists[a][node] != dists[b][node]:
                    self.is_prime = False

    def __eq__(self, annih):
        return self.a == annih.a and self.b == annih.b and self.G == annih.G

    def __str__(self):
        return str(self.nodes)

    def __hash__(self):
        return hash(G) + self.a * G.number_of_nodes() + self.b

    def is_subset(self, annih):
        """
        check if the annihilator is a subset of another annihilator
        :param annih: another annihilator
        :return: True, if annih is a supset of this annihilator, False otherwise
        """
        return self.nodes.issubset(annih.nodes)
