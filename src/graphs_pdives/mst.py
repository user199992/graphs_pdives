from .heapq import heappush, heappop

def prim(graph, source):
    visited = {source}
    edges = []
    total_weight = 0
    heap = []

    def push_edges(u):
        for v, w in graph[u].items():
            if v not in visited:
                heappush(heap, (w, u, v))

    push_edges(source)

    while heap and len(visited) < len(graph):
        w, u, v = heappop(heap)
        if v in visited:
            continue
        visited.add(v)
        edges.append((u, v, w))
        total_weight += w
        push_edges(v)

    return edges, total_weight
