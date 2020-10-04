#Uses python3

import sys
import math
import copy


class PriorityQueue:
    def __init__(self, input_lst=None):
        if input_lst is None:
            input_lst = []

        self.__data = input_lst
        self.__idx_map = {k: i for i, k in enumerate(input_lst)}
        for i in range(math.floor(len(self) / 2), 0, -1):
            self.__shift_down(i)

    def __repr__(self):
        return str(self.__data)

    def __len__(self):
        return len(self.__data)

    def check_idx_map(self):
        is_valid = True
        for i, k in enumerate(self.__data):
            if self.__idx_map[k] != i:
                is_valid = False
        return is_valid

    def push(self, k):
        self.__data.append(k)
        self.__idx_map[k] = len(self) - 1
        self.__shift_up(len(self))

    def pop_min(self):
        if not len(self):
            raise ValueError
        self.__swap(1, len(self))
        ret = copy.deepcopy(self.__data[-1])
        del self.__data[-1]
        del self.__idx_map[ret]
        self.__shift_down(1)
        return ret

    def get_min(self):
        return self.__data[0]

    def change_key(self, k_before, k_after):
        if k_before not in self.__idx_map:
            raise ValueError

        idx = self.__idx_map[k_before]
        self.__data[idx] = k_after
        del self.__idx_map[k_before]
        self.__idx_map[k_after] = idx

        if k_after > k_before:
            self.__shift_down(idx + 1)
        if k_before > k_after:
            self.__shift_up(idx + 1)

    @staticmethod
    def __left(i):
        return 2 * i

    @staticmethod
    def __right(i):
        return 2 * i + 1

    @staticmethod
    def __parent(i):
        return math.floor(i / 2)

    def __swap(self, i, j):
        self.__idx_map[self.__data[i - 1]], self.__idx_map[self.__data[j - 1]] = j - 1, i - 1
        self.__data[i - 1], self.__data[j - 1] = self.__data[j - 1], self.__data[i - 1]

    def __shift_up(self, i):
        while i > 1 and self.__data[self.__parent(i) - 1] > self.__data[i - 1]:
            self.__swap(self.__parent(i), i)
            i = self.__parent(i)

    def __shift_down(self, i):
        min_idx = i
        l = self.__left(i)
        r = self.__right(i)
        if l <= len(self) and self.__data[l - 1] < self.__data[min_idx - 1]:
            min_idx = l
        if r <= len(self) and self.__data[r - 1] < self.__data[min_idx - 1]:
            min_idx = r
        if i != min_idx:
            self.__swap(i, min_idx)
            self.__shift_down(min_idx)


def distance(adj, cost, s, t):
    #write your code here
    # print(adj)
    # print(cost)
    MAX_DIST = 1000 * 100000
    dist = [MAX_DIST + 1] * len(adj)
    prev = [None] * len(adj)
    dist[s] = 0
    q = PriorityQueue(list(zip(dist, range(len(adj)))))
    while len(q):
        _, u = q.pop_min()
        for v, w in zip(adj[u], cost[u]):
            if dist[v] > dist[u] + w:
                old_dist_v = dist[v]
                dist[v] = dist[u] + w
                prev[v] = u
                q.change_key((old_dist_v, v), (dist[v], v))

    return -1 if dist[t] > MAX_DIST else dist[t]


# def distance(adj, cost, s, t):
#     #write your code here
#     # print(adj)
#     # print(cost)
#     MAX_DIST = 1000
#     dist = [MAX_DIST + 1] * len(adj)
#     prev = [None] * len(adj)
#     dist[s] = 0
#     q = list(zip(dist, range(len(adj))))
#     while len(q):
#         _, u = min(q)
#         for v, w in zip(adj[u], cost[u]):
#             if dist[v] > dist[u] + w:
#                 v_idx = q.index((dist[v], v))
#                 dist[v] = dist[u] + w
#                 prev[v] = u
#                 q[v_idx] = (dist[v], v)
#
#     return -1 if dist[t] > MAX_DIST else dist[t]


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
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
