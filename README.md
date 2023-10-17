# Prime Annihilator Intersection Graphs

This repository is dedicated to the research and verification of whether prime annihilator intersection graphs are equivalent to bipartite graphs. Prime annihilator intersection graphs are a unique class of graphs that exhibit specific properties described below.

## Definitions

1. **Prime Annihilator Intersection Graphs**: These are graphs in which every annihilator (except for trivial ones) is the intersection of prime annihilators. An annihilator `[a, b]` in a graph `G`, where `a` and `b` are vertices of `G`, is defined as the set of all vertices `x` such that vertex `b` lies on an `a-x` geodesic. The annihilator `[a, b]` is considered prime if and only if `[a, b] = [b, a]`. These definitions are based on the following article:

    - [J. Nieminen, "Annihilators in Graphs," Results in Mathematics, Vol. 13, no. 1–2, pp. 140–146, Mar. 1988](https://link.springer.com/article/10.1007/BF03323401)

2. **Hypothesis**: The hypothesis being explored in this repository is that prime annihilator intersection graphs are exactly the same as bipartite graphs. To test this hypothesis, an efficient algorithm has been developed to check whether a given graph is a prime annihilator intersection graph.

## Algorithm

To determine if a given graph is a prime annihilator intersection graph, I use the following algorithm:

```python
Input: undirected connected graph G = (V, E)
Output: True if G is a prime annihilator intersection graph, false otherwise.

1. Find all annihilators in the graph.
2. Identify the prime annihilators.
3. Check if a given annihilator is an intersection of primes.
4. If all annihilators are intersections of prime annihilators, return True; otherwise, return False.
```
The time complexity of this algorithm is `O(n^3 * m)`, where n is the number of vertices, and m is the number of edges in the graph.

### Graph Generation

The algorithm is applied to all distinct graphs (up to isomorphism) with up to 11 vertices, demonstrating the correctness of the hypothesis for this range of graphs.

The set of all distinct graphs (up to isomorphism) with a maximum of 11 vertices is obtained from:

- [B. D. McKay and A. Piperno, "Practical Graph Isomorphism II," J. Symbolic Computation (2013) 60, 94-112](https://doi.org/10.1016/j.jsc.2013.09.003)

## Acknowledgements

I would like to express my sincere gratitude to my academic supervisor, Sergiy Kozerenko, for his valuable guidance and support throughout this research project.
