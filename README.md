# graphs_pdives

A small Python library of graph algorithms, featuring an implementation of **Dijkstra's shortest path algorithm** and a bonus **Prim's minimum spanning tree** implementation. The `dijkstra()` implementation and the bundled `heapq` module were provided as part of the CS 3250-002 packaging assignment; this repository packages them as an installable library following the `src` layout.

## Installation

Build and install locally with `pip`:

```bash
python -m build
python -m pip install dist/graphs_pdives-0.0.1-py3-none-any.whl
```

## Usage

```python
from graphs_pdives import sp

graph = {
    0: {1: 4, 7: 8},
    1: {0: 4, 2: 8, 7: 11},
    # ...
}

dist, path = sp.dijkstra(graph, source=0)
```

`dijkstra(graph, source)` returns:
- `dist`: a dict mapping each reachable vertex to its shortest distance from `source`
- `path`: a dict mapping each reachable vertex to the list of vertices on its shortest path from `source`

### Graph file format

Sample graphs live in `data/`. Each line is a directed, weighted edge:

```
source destination weight
```

For example, `0 1 4` is an edge from vertex `0` to vertex `1` with weight `4`.

### Command-line validation script

`test.py` at the repo root reads a graph file and prints shortest distances/paths from vertex `0`:

```bash
python test.py data/example1.txt
```

## Bonus: Prim's Minimum Spanning Tree

In addition to Dijkstra's algorithm, this library includes an implementation of **Prim's algorithm** for finding a minimum spanning tree (MST), reusing the same bundled min-heap as `sp.dijkstra()`.

```python
from graphs_pdives import mst

graph = {
    0: {1: 4, 7: 8},
    1: {0: 4, 2: 8, 7: 11},
    # ...
}

edges, total_weight = mst.prim(graph, source=0)
```

`prim(graph, source)` returns:
- `edges`: a list of `(u, v, weight)` tuples forming the minimum spanning tree
- `total_weight`: the sum of the weights of the edges in the MST

Unlike `sp.dijkstra()`, Prim's algorithm expects an **undirected** graph — every edge should appear in both directions with the same weight, as in `data/example1.txt`. Directed graphs with asymmetric edges (like `data/example2.txt`) aren't a valid input for this algorithm.

## Known limitation

`test.py` hardcodes the source vertex as `0`. `data/example4.txt` uses a different vertex numbering (`101`–`404`) with no vertex `0`, so running it raises a `KeyError`. This matches the behavior of the original reference implementation shown in the assignment materials — it isn't specific to this package's build or install.

## Credit

The `dijkstra()` algorithm and bundled `heapq.py` were provided by the course instructor for CS 3250-002 as part of this packaging assignment; this repository's contribution is the packaging and installation layer around them, plus the bonus `mst.prim()` implementation.
