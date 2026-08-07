import networkx as nx


class Map:
    def __init__(self, G: nx.Graph, H: nx.Graph, func: dict):
        self.G = G
        self.H = H
        self.mapping = func
        self.isomorphism = None
    
    def is_bijection(self):
        return self.is_injection() and self.is_surjection()
    
    def is_surjection(self):
        return set(self.mapping.values()) == set(self.H.nodes())
    
    def is_injection(self):
        return len(set(self.mapping.values())) == len(self.mapping)
