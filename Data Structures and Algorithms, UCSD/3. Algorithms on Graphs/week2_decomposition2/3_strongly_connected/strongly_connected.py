#Uses python3

import sys

sys.setrecursionlimit(200000)


def toposort(adj):
    # print(adj)
    visited = [False] * len(adj)
    post_order = []

    def explore(_x):
        visited[_x] = True
        for _neighbor_of_x in adj[_x]:
            if not visited[_neighbor_of_x]:
                explore(_neighbor_of_x)
        post_order.append(_x)

    def dfs():
        for _x in range(len(adj)):
            if not visited[_x]:
                explore(_x)

    dfs()
    post_order.reverse()
    return post_order


def reverse_graph(adj):
    ret_adj = [[] for _ in range(len(adj))]
    for u, adj_u in enumerate(adj):
        for v in adj_u:
            ret_adj[v].append(u)
    return ret_adj


def number_of_strongly_connected_components(adj):
    #write your code here
    rev_adj = reverse_graph(adj)
    topo_order = toposort(rev_adj)
    # print(topo_order)

    visited = [False] * len(adj)
    scc = []

    def explore(_x):
        visited[_x] = True
        scc[-1].append(_x)
        for _neighbor_of_x in adj[_x]:
            if not visited[_neighbor_of_x]:
                explore(_neighbor_of_x)

    for _x in topo_order:
        if not visited[_x]:
            scc.append([])
            explore(_x)

    # print(scc)
    return len(scc)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))
