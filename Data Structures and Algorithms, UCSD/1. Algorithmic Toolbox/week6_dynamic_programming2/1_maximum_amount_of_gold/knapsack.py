# Uses python3
import sys

# def optimal_weight(W, w):
#     # write your code here
#     result = 0
#     for x in w:
#         if result + x <= W:
#             result = result + x
#     return result


def optimal_weight(W, w, cache):
    # write your code here
    n = len(w)
    if W == 0 or n == 0:
        return 0

    if (W, n) in cache:
        return cache[(W, n)]

    v2 = optimal_weight(W, w[:n - 1], cache)
    if W - w[n - 1] >= 0:
        v1 = optimal_weight(W - w[n - 1], w[:n - 1], cache) + w[n - 1]
        result = max(v1, v2)
    else:
        result = v2

    cache[(W, n)] = result

    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    T = dict()
    print(optimal_weight(W, w, T))
    # print(T)
