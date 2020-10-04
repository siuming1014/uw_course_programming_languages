#Uses python3

import sys


def negative_cycle(adj, cost):
    #write your code here
    MAX_DIST = 1000
    dist = [MAX_DIST + 1] * len(adj)
    prev = [None] * len(adj)
    s = 0
    dist[s] = 0
    negative_cycle_exists = False
    for _ in range(len(adj)):
        for u in range(len(adj)):
            for v, w in zip(adj[u], cost[u]):
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    prev[v] = u
                    if _ == len(adj) - 1:
                        negative_cycle_exists = True
    return 1 if negative_cycle_exists else 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
