#Uses python3

import sys


def acyclic(adj):

    def toposort(adj):
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

    # print(toposort(adj))
    linear_order = [None] * len(adj)
    for i, _ in enumerate(toposort(adj)):
        linear_order[_] = i
    # print(linear_order)

    for u, v_lst in enumerate(adj):
        for v in v_lst:
            if linear_order[u] > linear_order[v]:
                return 1

    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
