#Uses python3

import sys
import queue
import copy


def shortet_paths(adj, cost, s):
    #write your code here
    # distance = [10**19] * n
    # reachable = [0] * n
    # shortest = [1] * n
    MAX_DIST = 10**19
    dist = [MAX_DIST + 1] * len(adj)
    prev = [None] * len(adj)
    dist[s] = 0
    negative_cycle_nodes = set()
    for _ in range(len(adj)):
        for u in range(len(adj)):
            for v, w in zip(adj[u], cost[u]):
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    prev[v] = u
                    if _ == len(adj) - 1:
                        negative_cycle_nodes.add(v)

    q = list(negative_cycle_nodes)
    while len(q):
        u = q.pop(0)
        for v in adj[u]:
            if v not in negative_cycle_nodes:
                negative_cycle_nodes.add(v)
                q.append(v)

    reachable = [1 if dist[_] < MAX_DIST else 0 for _ in range(len(adj))]
    shortest = [1 if reachable[_] and _ not in negative_cycle_nodes else 0 for _ in range(len(adj))]
    return dist, reachable, shortest


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
    s = data[0]
    s -= 1
    # distance = [10**19] * n
    # reachable = [0] * n
    # shortest = [1] * n
    distance, reachable, shortest = shortet_paths(adj, cost, s)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])

