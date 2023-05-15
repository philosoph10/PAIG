from annihilators.Annihilator import Annihilator
import networkx as nx


def get_all_annihilators_of_graph(G):
    """
    yields all non-trivial annihilators of graph G
    :param G: the graph
    :return: list of all annihilators
    """
    dists = dict(nx.all_pairs_shortest_path_length(G))
    annihs = []
    for a in G.nodes():
        for b in G.nodes():
            if a != b:
                annihs.append(Annihilator(G, a, b, dists))
    return annihs


def is_intersection_of_primes(primes, annih):
    """
    checks if an annihilator is an intersection of prime annihilators in a graph
    :param primes: all prime annihilators of the graph
    :param annih: the annihilator
    :return: True, if annih is intersection of elements of primes
    """
    if annih.is_prime:
        return True
    primes_containing_annih = []
    for prime in primes:
        if annih.is_subset(prime):
            primes_containing_annih.append(prime.nodes)
    if len(primes_containing_annih) == 0:
        return False
    intersection_of_primes_containing_annih = set.intersection(*tuple(primes_containing_annih))
    return intersection_of_primes_containing_annih == annih.nodes


def is_PAIG(G):
    """
    checks if a graph is a prime annihilator intersection graph
    :param G: the graph
    :return: True, if G is PAIG, otherwise returns False
    """
    annihs = get_all_annihilators_of_graph(G)
    primes = []
    for annih in annihs:
        if annih.is_prime:
            primes.append(annih)

    for annih in annihs:
        if annih.is_prime:
            continue
        if not is_intersection_of_primes(primes, annih):
            return False
    return True
