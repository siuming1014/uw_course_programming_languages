# Uses python3

import sys


def reach(adj, x, y):
    # write your code here
    # print(adj, x, y)
    visited = [False] * len(adj)

    def explore(_x):
        visited[_x] = True
        # print(visited)
        for _neighbor_of_x in adj[_x]:
            if not visited[_neighbor_of_x]:
                explore(_neighbor_of_x)

    explore(x)
    return int(visited[y])


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))
