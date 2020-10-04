#Uses python3

import sys
import queue


def bipartite(adj):
    #write your code here
    # MAX_DIST = 100000
    dist = [None] * len(adj)
    part_labels = [None] * len(adj)  # bipartite labels, takes None, True or False

    s = 0  # starting node
    dist[s] = 0
    part_labels[s] = True
    Q = [s]

    while len(Q):
        u = Q.pop(0)
        for v in adj[u]:
            if dist[v] is None:
                Q.append(v)
                dist[v] = dist[u] + 1
                part_labels[v] = not part_labels[u]
            else:
                if part_labels[v] == part_labels[u]:
                    return 0
    return 1


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
    print(bipartite(adj))
