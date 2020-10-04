# Uses python3

import sys


def number_of_components(adj):
    # write your code here
    visited = [False] * len(adj)
    cc = []

    def explore(_x):
        visited[_x] = True
        cc[-1].append(_x)
        # print(visited)
        for _neighbor_of_x in adj[_x]:
            if not visited[_neighbor_of_x]:
                explore(_neighbor_of_x)

    def dfs():
        for _x in range(len(adj)):
            if not visited[_x]:
                cc.append([])
                explore(_x)

    dfs()
    # print(cc)
    return len(cc)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))
